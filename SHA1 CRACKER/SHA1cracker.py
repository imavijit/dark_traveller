from urllib.request import urlopen, hashlib

#take get the hasjh from user
sha1hash=input("Please input hash to crack.\n")

#open a file full with password guesses
COMMON_PASSWORD_LIST = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

#guess from the list of password
for guess in COMMON_PASSWORD_LIST.split('\n'):

    # make hash of guess password annd then compare it with our user input hash
    hash_guess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()

    if( sha1hash == hash_guess):
        print("The password is : ", str(guess))
        quit()
    elif(hash_guess != sha1hash):
        print("Password guess" + str(guess)+ "does not match, trying next")

print("Password not in database, we will get them next time")
