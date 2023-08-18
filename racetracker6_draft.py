import concurrent.futures
import multiprocessing
import threading
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import gspread
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import bs4
import sqlite3
import requests as r

# Set up Chrome Webdriver service using webdriver_manager
chrome_driver_path = ChromeDriverManager().install()

# Set up Chrome Webdriver using webdriver_manager
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")
options.add_argument("--disable-features=NetworkService")

# Initialize ChromeDriver service
service = Service(executable_path=chrome_driver_path)

# Initialize the driver using the obtained service and options
driver = webdriver.Chrome(service=service, options=options)


def crawl(horsedata):
    modrow = []
    horsecounter = 1
    newhorse = horsedata.strip().replace(' ', '+')
    modrow.append(newhorse)
    for i in range(15):
        modrow.append(f'{newhorse}{horsecounter}')
        horsecounter += 1

    errorchecker = 0
    for j in modrow:
        fulldata = []
        mainhorse = j.replace("+", " ").strip()
        mainhorse2 = re.sub(r'\d+$', '', mainhorse)
        fulldata.append(mainhorse2)

        try:
            req = r.get(f'https://www.pedigreequery.com/{j}')

            soup = BeautifulSoup(req.text, "html.parser")
            tab = soup.find('table', class_="pedigreetable")
            # bod = tab.find('tbody')
            tro = tab.find_all('tr')

            tcol = tro[0].find_all('a')
            try:
                name = tcol[0].text.strip().title()
                country = tcol[0].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            try:
                name = tcol[1].text.strip().title()
                country = tcol[1].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[8].find_all('a')
            try:
                name = tcol[0].text.strip().title()
                country = tcol[0].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[0].find_all('a')
            try:
                name = tcol[2].text.strip().title()
                country = tcol[2].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[4].find_all('a')
            try:
                name = tcol[0].text.strip().title()
                country = tcol[0].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[8].find_all('a')
            try:
                name = tcol[1].text.strip().title()
                country = tcol[1].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[12].find_all('a')
            try:
                name = tcol[0].text.strip().title()
                country = tcol[0].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[16].find_all('a')
            try:
                name = tcol[0].text.strip().title()
                country = tcol[0].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            try:
                name = tcol[1].text.strip().title()
                country = tcol[1].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[24].find_all('a')
            try:
                name = tcol[0].text.strip().title()
                country = tcol[0].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[16].find_all('a')
            try:
                name = tcol[2].text.strip().title()
                country = tcol[2].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[20].find_all('a')
            try:
                name = tcol[0].text.strip().title()
                country = tcol[0].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[24].find_all('a')
            try:
                name = tcol[1].text.strip().title()
                country = tcol[1].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)
            tcol = tro[28].find_all('a')
            try:
                name = tcol[0].text.strip().title()
                country = tcol[0].next_sibling
                if isinstance(country, bs4.element.NavigableString):
                    if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                        full = name
                    else:
                        full = name + country
                else:
                    full = name + ""
            except:
                full = "No Horse Listed"
            fulldata.append(full)

            cursor.execute(
                "INSERT INTO horse_data (horse, sire, cola, colb, colc, cold, cole, colf, dam, colg, colh, coli, colj, colk, coll) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", fulldata)
            connection.commit()

            fulldata.clear()
            errorchecker = 0

        except AttributeError:
            # this means the horse does not exist on the db
            fulldata.clear()
            errorchecker += 1
            if errorchecker > 2:
                break
            continue


def firsturl(url):
    cola.clear()
    colb.clear()
    colc.clear()
    cold.clear()
    raceurls = []
    coln.clear()
    colr.clear()
    colv.clear()
    colz.clear()
    colad.clear()
    colah.clear()
    colal.clear()
    horselist = []
    sirelist = []
    horselist.clear()
    sirelist.clear()

    driver.get(url)
    time.sleep(10)

    try:
        # wait for the "purse" element to be present on the page
        menu = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.ID, "purse")))
    except NoSuchElementException:
        print('Page Load took too long, there might be something wrong with your net')
        driver.quit()
        quit()

    time.sleep(10)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # racename - make a tab name
    track = soup.find('span', class_="track-name").text.strip()
    wks = database.add_worksheet(
        title=track.upper(), rows=1000, cols=42)  # uncomment this later

    while True:
        prev = driver.find_element(By.ID, "race-nav-previous")
        prev2 = prev.find_element(By.CLASS_NAME, "race-number").text.strip()
        if prev2.find("R0") > -1:
            break
        else:
            prev.click()
            time.sleep(10)

    while True:
        nex = driver.find_element(By.ID, "race-nav-next")
        nex2 = nex.find_element(By.CLASS_NAME, "race-number").text.strip()
        if nex2.find("R0") > -1:
            raceurls.append(driver.current_url)
            break
        else:
            raceurls.append(driver.current_url)
            nex.click()
            time.sleep(10)

    time.sleep(3)

    # start of driver2
    for ur in raceurls:
        driver.get(ur)
        time.sleep(10)

        try:
            # wait for the element to be present on the page
            menu = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, "purse")))
        except NoSuchElementException:
            print('Page Load took too long, there might be something wrong with your net')
            driver.quit()
            quit()

        time.sleep(10)

        # driver2.minimize_window()

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        while True:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            mtp_element = soup.find('div', class_="mtp-label")

            if mtp_element:
                mtp = mtp_element.text
                if mtp != "OFF":
                    print("MTP:", mtp)
                    break  # Exit the loop if valid MTP is found
            else:
                print("MTP not found. Waiting...")

            time.sleep(5)  # Wait for a few seconds before checking again

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # racenum + purse on row 1
        racenum = soup.find('span', id="race_dropdown_identifier").text.strip()
        purse = soup.find('div', id="purse").text.strip()
        # Include MTP in racenumpurse
        racenumpurse = f"{racenum}-{purse} (MTP: {mtp})"

        cola.append(list([racenumpurse]))
        cola.append(list(["P#"]))
        colb.append(list())
        colb.append(list(["PP#"]))
        colc.append(list())
        colc.append(list(["Horse"]))
        cold.append(list())
        cold.append(list(["Odds"]))

        runs = soup.find_all('div', class_="entry")

        for run in runs:
            # shirtnumber
            shirtnum = run.find('div', class_="saddle-cloth").text.strip()
            try:
                cola.append(list([int(shirtnum)]))
            except:
                cola.append(list([shirtnum]))
            # PP number
            ppnum = run.find(
                'div', class_="program-post-position ng-star-inserted").text.strip().replace("PP ", "")
            try:
                colb.append(list([int(ppnum)]))
            except:
                colb.append(list([ppnum]))
            # entryrunnername
            horse = run.find('span', class_="entry-runner-name").text.strip()
            horselist.append(horse)
            colc.append(list([horse]))
            # sirename for my reference only
            sire = run.find('span', class_="entry-sire-name").text.strip()
            sirelist.append(sire)

            # Scrape and append odds
            odds_element = run.find(
                'span', class_='main-detail odds-main-detail')
            if odds_element:
                horse_odds = odds_element.text.strip()
                cold.append(list([horse_odds]))
            else:
                # If odds not found, append "N/A" or any other suitable placeholder
                cold.append(list(["N/A"]))

            # wks.update_cell(row, 7, sire)

        horselist.append("Dummydata123456789")
        sirelist.append("Dummydata123456789")

    check = "1sturl"
    printer(wks, check)

    # compare horses and sire
    coln.append(list())
    colr.append(list())
    colv.append(list())
    colz.append(list())
    colad.append(list())
    colah.append(list())
    colal.append(list())
    coln.append(list())
    colr.append(list())
    colv.append(list())
    colz.append(list())
    colad.append(list())
    colah.append(list())
    colal.append(list())
    for horses in range(len(horselist)):
        if horselist[horses] == "Dummydata123456789":
            coln.append(list())
            colr.append(list())
            colv.append(list())
            colz.append(list())
            colad.append(list())
            colah.append(list())
            colal.append(list())
            coln.append(list())
            colr.append(list())
            colv.append(list())
            colz.append(list())
            colad.append(list())
            colah.append(list())
            colal.append(list())
            continue

        cursor.execute("SELECT sire, cola, colc, cole, colg, coli, colk FROM horse_data WHERE UPPER(horse) = UPPER(?) AND UPPER(sire) = UPPER(?)",
                       (horselist[horses], sirelist[horses],))
        result = cursor.fetchall()

        if result:
            print(
                f'{horselist[horses]} with {sirelist[horses]} sire is found from local db.')
            coln.append(list([result[0][0]]))
            colr.append(list([result[0][1]]))
            colv.append(list([result[0][2]]))
            colz.append(list([result[0][3]]))
            colad.append(list([result[0][4]]))
            colah.append(list([result[0][5]]))
            colal.append(list([result[0][6]]))
            continue

        print(
            f'{horselist[horses]} with {sirelist[horses]} sire is not found from the local db. Pulling data from web instead...')

        driver.get(url2)

        time.sleep(2)

        try:
            # wait for the element to be present on the page
            menu = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
        except NoSuchElementException:
            print('Page Load took too long, there might be something wrong with your net')
            driver.quit()
            quit()

        menu.send_keys(horselist[horses])
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@value="Horse Search"]').click()
        # print(horselist[horses])
        # print(sirelist[horses])
        time.sleep(2)

        for ihap in range(5):
            try:
                time.sleep(1)
                checker = driver.find_element(By.TAG_NAME, "legend")
                break
            except:
                continue

        try:
            time.sleep(2)
            na = driver.find_element(By.TAG_NAME, "legend").text.strip()
            if na.find("Horse Not Found") > -1:
                coln.append(list(["Horse Not found in web DB"]))
                colr.append(list())
                colv.append(list())
                colz.append(list())
                colad.append(list())
                colah.append(list())
                colal.append(list())
                continue

            soup = BeautifulSoup(driver.page_source, "html.parser")
            table = soup.find('table', class_="tablesorter")
            body = table.find('tbody')
            tr = body.find_all('tr')

            checker2 = 0

            for t in tr:
                ttd = t.find_all('td')
                horsename = re.sub('[^A-Za-z0-9]+', '', ttd[0].text.lower())
                sirename = re.sub('[^A-Za-z0-9]+', '', ttd[4].text.lower())
                if horsename.find(re.sub('[^A-Za-z0-9]+', '', horselist[horses].lower())) > -1 or re.sub('[^A-Za-z0-9]+', '', horselist[horses].lower()).find(horsename) > -1:
                    if sirename.find(re.sub('[^A-Za-z0-9]+', '', sirelist[horses].lower())) > -1 or re.sub('[^A-Za-z0-9]+', '', sirelist[horses].lower()).find(sirename) > -1:
                        if sirename != "":
                            checker2 = 0
                            newurl = ttd[0].find('a').get('href')
                            break
                checker2 += 1

            if checker2 > 0:
                coln.append(
                    list(["Horse with exact Sire not found from database"]))
                colr.append(list())
                colv.append(list())
                colz.append(list())
                colad.append(list())
                colah.append(list())
                colal.append(list())
                continue

            driver.get(url2 + newurl)
        except:
            pass

        time.sleep(3)

        # code to fetch report
        try:
            # wait for the element to be present on the page
            menu = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pedigreetable")))
        except NoSuchElementException:
            print('Page Load took too long, there might be something wrong with your net')
            driver.quit()
            quit()

        time.sleep(2)

        tcol1 = []
        tcol2 = []
        tcol3 = []
        tcol4 = []

        tcol1.clear()
        tcol2.clear()
        tcol3.clear()
        tcol4.clear()

        soup = BeautifulSoup(driver.page_source, "html.parser")
        tab = soup.find('table', class_="pedigreetable")
        bod = tab.find('tbody')
        tro = bod.find_all('tr')

        tcol = tro[0].find_all('a')
        try:
            name = tcol[0].text.strip().title()
            country = tcol[0].next_sibling
            if isinstance(country, bs4.element.NavigableString):
                if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                    full = name
                else:
                    full = name + country
            else:
                full = name + ""
        except:
            full = "No Horse Listed"
        coln.append(list([full]))
        try:
            name = tcol[1].text.strip().title()
            country = tcol[1].next_sibling
            if isinstance(country, bs4.element.NavigableString):
                if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                    full = name
                else:
                    full = name + country
            else:
                full = name + ""
        except:
            full = "No Horse Listed"
        colr.append(list([full]))
        try:
            name = tcol[2].text.strip().title()
            country = tcol[2].next_sibling
            if isinstance(country, bs4.element.NavigableString):
                if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                    full = name
                else:
                    full = name + country
            else:
                full = name + ""
        except:
            full = "No Horse Listed"
        colv.append(list([full]))
        tcol = tro[8].find_all('a')
        try:
            name = tcol[1].text.strip().title()
            country = tcol[1].next_sibling
            if isinstance(country, bs4.element.NavigableString):
                if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                    full = name
                else:
                    full = name + country
            else:
                full = name + ""
        except:
            full = "No Horse Listed"
        colz.append(list([full]))
        tcol = tro[16].find_all('a')
        try:
            name = tcol[1].text.strip().title()
            country = tcol[1].next_sibling
            if isinstance(country, bs4.element.NavigableString):
                if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                    full = name
                else:
                    full = name + country
            else:
                full = name + ""
        except:
            full = "No Horse Listed"
        colad.append(list([full]))
        try:
            name = tcol[2].text.strip().title()
            country = tcol[2].next_sibling
            if isinstance(country, bs4.element.NavigableString):
                if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                    full = name
                else:
                    full = name + country
            else:
                full = name + ""
        except:
            full = "No Horse Listed"
        colah.append(list([full]))
        tcol = tro[24].find_all('a')
        try:
            name = tcol[1].text.strip().title()
            country = tcol[1].next_sibling
            if isinstance(country, bs4.element.NavigableString):
                if country.find('(USA)') > -1 or country.find('(CAN)') > -1:
                    full = name
                else:
                    full = name + country
            else:
                full = name + ""
        except:
            full = "No Horse Listed"
        colal.append(list([full]))

        print(
            f'Adding {horselist[horses]} to the local db for future references..')
        crawl(horselist[horses])

    check = "2ndurl"
    printer(wks, check)

    wks.format("A1:AP1000", {
        "backgroundColor": {
            "red": 0.0,
            "green": 0.0,
            "blue": 0.0
        },
        "horizontalAlignment": "LEFT",
        "textFormat": {
            "foregroundColor": {
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
            },
            "fontSize": 18,
            "bold": False,
            "fontFamily": "Montserrat",
            "italic": True
        }
    })

    wks.columns_auto_resize(start_column_index=0, end_column_index=42)
    wks.format("A1:AP", {"horizontalAlignment": "CENTER"})
    wks.columns_auto_resize(start_column_index=0, end_column_index=42)
    wks.columns_auto_resize(start_column_index=0, end_column_index=42)
    wks.columns_auto_resize(start_column_index=0, end_column_index=42)


def printer(wks, check):

    if check == "1sturl":
        wks.update('A1:A', cola)
        wks.update('B1:B', colb)
        wks.update('C1:C', colc)
        wks.update('D1:D', cold)
    else:
        wks.update('N1:N', coln)
        wks.update('R1:R', colr)
        wks.update('V1:V', colv)
        wks.update('Z1:Z', colz)
        wks.update('AD1:AD', colad)
        wks.update('AH1:AH', colah)
        wks.update('AL1:AL', colal)


def updatedb():  # removed function because this is scary
    horsename = input(
        "Please enter the name of the horse you want to update: ")

    cursor.execute("""
    SELECT * from horse_data WHERE
    UPPER(horse) = UPPER(?)
    OR UPPER(sire) = UPPER(?)
    OR UPPER(dam) = UPPER(?)
    OR UPPER(cola) = UPPER(?)
    OR UPPER(colb) = UPPER(?)
    OR UPPER(colc) = UPPER(?)
    OR UPPER(cold) = UPPER(?)
    OR UPPER(cole) = UPPER(?)
    OR UPPER(colf) = UPPER(?)
    OR UPPER(colg) = UPPER(?)
    OR UPPER(colh) = UPPER(?)
    OR UPPER(coli) = UPPER(?)
    OR UPPER(colj) = UPPER(?)
    OR UPPER(colk) = UPPER(?)
    OR UPPER(coll) = UPPER(?)
    """, (horsename, horsename, horsename, horsename, horsename, horsename, horsename, horsename, horsename, horsename, horsename, horsename, horsename, horsename, horsename,))

    rows = cursor.fetchall()

    if not rows:
        print("Horse does not appear anywhere in the local DB.")
        while True:
            ask = input("Do you want to exit? (y/n): ")
            if ask != 'y' and ask != 'n':
                print("Please select 'y' or 'n' only.")
                continue
            else:
                break

        if ask == 'y':
            return
        else:
            updatedb()

    else:
        total_count = 0
        for row in rows:
            for col in row:
                if isinstance(col, str):
                    total_count += col.lower().count(horsename.lower())

        print(
            f'\nThere are a total of {total_count} horses with the name {horsename} in the local DB.\n')
        updatehorse = input("Please input the New Name of the horse: ")
        print(f"Updating {horsename} into {updatehorse}...")

        # Update horse here:
        columns = ['horse', 'sire', 'dam', 'cola', 'colb', 'colc', 'cold',
                   'cole', 'colf', 'colg', 'colh', 'coli', 'colj', 'colk', 'coll']
        for column in columns:
            cursor.execute(f"""
                UPDATE horse_data
                SET {column} = ?
                WHERE UPPER({column}) = UPPER(?)
            """, (updatehorse, horsename))

        connection.commit()
        print(f"Horse Name updated!")

    while True:
        ask = input("Update more horses? (y/n): ")
        if ask != 'y' and ask != 'n':
            print("Please select 'y' or 'n' only.")
            continue
        else:
            break

    if ask == 'y':
        updatedb()


cola = []
colb = []
colc = []
cold = []
coln = []
colr = []
colv = []
colz = []
colad = []
colah = []
colal = []


# philip's cred
cred_file = 'racescraper-bac97e3a512c.json'
# my cred
# cred_file = 'racescraper-395115-74fff1a1d581.json'
gc = gspread.service_account(cred_file)
database = sheet = gc.open("SampleRaceTracker")

connection = sqlite3.connect("horsedatabase.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS horse_data (
        horse_id INTEGER PRIMARY KEY AUTOINCREMENT,
        horse TEXT,
        sire TEXT,
        cola TEXT,
        colb TEXT,
        colc TEXT,
        cold TEXT,
        cole TEXT,
        colf TEXT,
        dam TEXT,
        colg TEXT,
        colh TEXT,
        coli TEXT,
        colj TEXT,
        colk TEXT,
        coll TEXT,
        date_added TEXT DEFAULT (datetime('now','localtime'))
    )
""")


print("Starting RaceTracker...")

numofrace = input("Number of Races: ")
url1 = []
for i in range(int(numofrace)):
    tempurl = input("Please input Race URL(s): ")
    url1.append(tempurl)

print("Running..")


# url1 = "https://www.twinspires.com/bet/todays-races/time"
url2 = "https://www.pedigreequery.com"

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver2 = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
except Exception as e:
    print("Something wrong with the Chrome WebDriver. There's probably an issue with compatibility")
    print("Please check your current Chrome Browser version and access this page: 'https://chromedriver.chromium.org/downloads' to download the compatible version.")
    print("As soon as done, move the chromedriver.exe file into the folder where this app is located and just click 'Replace'.")

# driver = uc.Chrome()

for numms in url1:
    print("\n\n\n\n\nNow working on: " + str(numms) + " URL..")
    print("-----------------\n\n\n\n\n")
    firsturl(numms)

driver.quit()
# driver2.quit()
print("Scraping Complete!")


#########    Realtime value extraction part goes here   ##########


race_links = url1
### Real-time MTP & ODD capturing PART ###
# start monitoring loop
previous_mtp_value = None
race = url1


# initialize empty lists
# odds_list = []
pp_list = []
runner_list = []

sheet = database
spreadsheet_lock = {i + 1: threading.Lock() for i in range(len(race_links))}

# Global lock to ensure sequential processing
selenium_lock = threading.Lock()


def new_function(link_num, url):
    link = url
    worksheet1 = sheet.get_worksheet(link_num)
    existing_data = worksheet1.get_all_values()

    # opening and reading that corresponding excel sheet only

    num_races = len([i for i in range(0, len(existing_data)) if existing_data[i]
                     [0].__contains__('RACE') and existing_data[i]
                     [0].__contains__('-Purse')])

    links = []

    # Use regex to find the race number in the link
    match = re.search(r'/(\d+)/advanced$', link)
    if match:
        base_link = link[:match.start(1)]
        for i in range(1, num_races + 1):
            new_link = f'{base_link}{i}/advanced'
            links.append(new_link)
    else:
        print("Race number not found in the link.")

    driver = webdriver.Chrome(service=service, options=options)
    for l in range(len(links)):
        mtp_value = 0
        odds_list = []  # Create a new odds_list for each thread

        while True:

            # This line is present at the beginning of the while loop, which ensures that the odds_list is cleared before each iteration of the loop.
            odds_list.clear()
            # navigate to the webpage
            with selenium_lock:
                driver.get(
                    links[l])
                time.sleep(5)

            race_num = r = l+1
            p = [i for i in range(0, len(existing_data)) if existing_data[i]
                 [0].__contains__(f'RACE {race_num}-Purse')][0]
            q = [i for i in range(0, len(existing_data)) if existing_data[i]
                 [0].__contains__(f'RACE {race_num+1}-Purse')][0]

            try:
                # Locate the element
                element = driver.find_element(By.CLASS_NAME, 'mtp-value')

                # Extract the value
                mtp_value = element.text
                print("mtp_value: ", mtp_value)
                # Check for changes
                if mtp_value != previous_mtp_value:
                    print("MTP Value changed:", mtp_value)
                    previous_mtp_value = mtp_value

                    # Update the cell with the new value
                    # worksheet1.update('A2', mtp_value)
                    cell = f"C{p + 1}"
                    # with spreadsheet_lock:
                    with spreadsheet_lock[link_num]:
                        worksheet1.update(cell, f'{mtp_value} MTP')

            except:
                pass

            try:
                # Find the elements
                entries = driver.find_elements(
                    By.CLASS_NAME, 'odds-main-detail')
                odds_list.clear()

                for i in range(len(entries)):
                    odds_value = entries[i].text.strip()
                    odds_list.append(odds_value)

                c = 2
                # for i in range(p+2, q+1):
                for i in range(p+2, p+2+len(odds_list)):

                    # update the odds value in column D (column index 4)
                    # subtract 2 to match index with list

                    if existing_data[i][3] != odds_list[c - 2]:

                        # update the cell in column D (Odds column)
                        # adding 1 to match 1-based indexing of Google Sheets
                        cell_range = f"D{i + 1}"
                        # updating as a 2D list
                        # with spreadsheet_lock:
                        if existing_data[i][3] != 'Odds':
                            with spreadsheet_lock[link_num]:
                                worksheet1.update(
                                    cell_range, [[odds_list[c - 2]]])

                    # sleep for a while before moving to the next update
                    time.sleep(1)  # adjust the sleep duration as needed

                    c += 1

            except:
                pass

            cell = f"C{p + 1}"
            # with spreadsheet_lock:
            with spreadsheet_lock[link_num]:
                worksheet1.update(cell, f'{mtp_value} MTP')

            time.sleep(3)  # Delay for 5 seconds before checking again

            if (mtp_value == 'OFFICIAL'):
                # update results here
                break

    driver.quit()


# new_function(
#     1, 'https://www.twinspires.com/bet/program/classic/belterra-park/btp/Thoroughbred/1/advanced')


threads = []


args_list = [(i + 1, race_links[i])
             for i in range(len(race_links))]  # list of argument tuples


max_threads = len(race_links)  # Adjust this based on your needs
with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
    for args in args_list:
        executor.submit(new_function, *args)
        time.sleep(5)
