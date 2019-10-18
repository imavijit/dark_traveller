#!/bin/python3
alphabet= 'abcdefghijklmnopqrstuvwxyz'
special_characters = " ,.-;:_?!="

def encrypt(message,key):
  cipher_message=" "
  for character in message:
      if character in alphabet:
        pos=alphabet.find(character)
        newpos=(pos+key)%26
        cipher_message+=alphabet[newpos]
      else:
        cipher_message+=character
  return cipher_message

def decrypt(cipher_message,key=None):
  for key in range(len(alphabet)):
    message=" "
    for character in cipher_message:
      if character in alphabet:
       pos=alphabet.find(character)
       new_pos=(pos-key)%26
       message+=alphabet[new_pos]

      else:
        message+=character

    print('Key #%s: %s' % (key,message))


if __name__ == "__main__":
  while(True):
    while(True):
      print("Do you want to encrypt or decrypt?: ")
      ans=input().lower()
      if ans in 'encrypt e decrypt d'.split():
        ans=ans
        break
      else:
        print('Enter either "encrypt" or "e" or "decrypt" or "d"')

    if(ans=="encrypt" or ans=="e"):
        message=input("Please enter a message: ")
        key=int(input("Enter a Key between (1-26) : "))
        print("The encrypted message is: ", encrypt(message,key))



    elif(ans=="decrypt" or ans=="d"):
       #cipher = encrypt("This sentence is encrypted. Encryption is broken     by using awesome encryption algorithms!",5)
        cipher=input("Enter the cipher_text")
        if(cipher.isupper()==True):
          cipher=cipher.lower()
        print(decrypt(cipher))

    if input('Do You Want To Continue? [y/n]') != 'y':
        break
