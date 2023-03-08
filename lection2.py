a = 1 #input()
print(type(a))
print(id(a))
print(hash(a))

#help()

text = input('введи что-нибудь ')
print(text)
if str.isdecimal(text):
    text = int(text)
    print(bin(text))
    print(oct(text))
    print(hex(text))
else:
    print(str.isascii(text))




