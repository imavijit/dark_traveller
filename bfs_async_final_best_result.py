import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import re
from urllib.parse import urlparse, urljoin
import time
from collections import deque



async def extract_link(link, url, depth, visited, semaphore):
    async with semaphore:
        href = await link.get_attribute("href")
        if href:
            if not href.startswith("http"):
                href = urljoin(url, href)

            if href.endswith(".pdf"):
                name = await link.inner_text()
                return [], [{"Sublink": url, "Depth": depth, "Name": name, "PDF Link": href}]

            if href.startswith("http") and urlparse(href).netloc == urlparse(url).netloc and href not in visited:
                if not re.search(r'\.\w+$', href):
                    return [href], []
        return [], []

async def navigate_and_extract(browser, start_url, depth, visited, semaphore=None):
    queue = deque([(start_url, 1)])
    sublink_data = []
    pdf_data = []
    total_sublinks = 0
    skipped_sublinks = 0

    while queue:
        url, current_depth = queue.popleft()
        if current_depth > depth:
            continue

        async with semaphore:
            context = await browser.new_context()
            page = await context.new_page()
            try:
                await page.goto(url)
            except Exception as e:
                print(f"Error while navigating to {url}: {e}")
                await context.close()
                continue

            parsed_url = urlparse(url)
            domain = f"{parsed_url.scheme}://{parsed_url.netloc}"

            links = await page.query_selector_all("a[href]")
            link_tasks = [asyncio.create_task(extract_link(link, url, depth, visited, semaphore)) for link in links]
            result = await asyncio.gather(*link_tasks)

            sublinks = [item for sublist in [result[0] for result in result] for item in sublist]
            pdf_links = [item for sublist in [result[1] for result in result] for item in sublist]

            sublink_data.extend([{"Sublink": url, "Depth": current_depth, "Link": link} for link in sublinks])
            pdf_data.extend(pdf_links)

            total_sublinks += len(sublinks)

            for sublink in sublinks:
                actual_link = sublink.rsplit("#", 1)[0]
                if "#" in sublink and actual_link in visited:
                    print('Skipping-link: ', sublink)
                    print('Actual-link: ', actual_link)
                    skipped_sublinks += 1
                    continue
                if domain in sublink and sublink not in visited:
                    print('Running Sublink: ', sublink)
                    visited.add(sublink)
                    queue.append((sublink, current_depth + 1))

            await context.close()

    return sublink_data, pdf_data, total_sublinks, skipped_sublinks


async def main():
    start_time = time.time()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        start_url = 'https://www.tanla.com/investor-relations'
        # start_url = "https://www.tanla.com/"
        max_depth = 2
        visited = set()

        semaphore = asyncio.Semaphore(50)

        sublink_data, pdf_data, total_sublinks, skipped_sublinks = await navigate_and_extract(browser, start_url, max_depth, visited, semaphore=semaphore)

        start_time1 = time.time()

        await browser.close()

    with pd.ExcelWriter("extracted_data.xlsx") as writer:
        df_sublinks = pd.DataFrame(sublink_data)
        df_sublinks.to_excel(writer, sheet_name="Sublinks", index=False)

        df_pdfs = pd.DataFrame(pdf_data)
        df_pdfs.to_excel(writer, sheet_name="PDF Links", index=False)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"Total time taken to combine data: {elapsed_time1} seconds")

    print("Data extraction and export completed successfully!")
    print(f"Total sublinks extracted: {total_sublinks}")
    print(f"Skipped sublinks: {skipped_sublinks}")
    print(f"Visited Links: {len(visited)}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())



