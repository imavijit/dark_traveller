## Hex -> decimal -> ASCII CHAR

"""
Below is a the flag encoded as a hex string. Decode this back into bytes.

63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d

"""


#Solution:1
s = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

s_final = ' '.join(s[i:i + 2] for i in range(0, len(s), 2)) #inserting a space after every 2 character

##int(i, 16) => converts hexadecimal number 'i' to decimal number.
l = list(map(lambda i: int(i, 16), s_final.split())) ##convert all hex to decimal and store in a list

res = ''.join(map(chr, l))  ##convert to ASCII using chr()
print(res)


#Solution:2
x = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
print(bytes.fromhex(x))
