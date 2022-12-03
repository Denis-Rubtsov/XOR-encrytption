from random import *

def to_hex(text):
    text_hex = ''
    for i in text:
        text_hex += hex(ord(i))[2:] + ' '
    return text_hex

def to_str(text):
    text_str = ''
    text_list = text.split()
    for i in text_list:
        text_str += chr(int(i,16))
    return text_str

def generate_key(l):
    global key
    english_alphabet_lower = "abcdefghijklmnopqrstuvwxyz" #Creating strings with symbols
    english_alphabet_upper = english_alphabet_lower.upper()
    russian_alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_alphabet_upper = russian_alphabet_lower.upper()
    special_symbols = "!@#$%^&*()_-+=/?.>,<';:[]{}\\|"
    all_symbols = english_alphabet_lower + english_alphabet_upper + russian_alphabet_lower + russian_alphabet_upper + special_symbols
    
    for i in range(l):
        key += all_symbols[randrange(0,len(all_symbols))] #Creating random key

def xor():
    encypted = ''
    for i in range(len(text)):
        encypted += chr(ord(text[i])^ord(key[i])) #Xor encryption
    return encypted

key = ''
text = input('Input text: ')
crypt = True

choice = int(input('Encrypt or decrypt? (1,2) '))

if choice == 2:
    text = to_str(text)
    key = input('Input key: ')
    key = to_str(key)
    crypt = False
else:
    generate_key(len(text))

text_encrypted = xor()
if choice == 1:
    print(to_hex(text_encrypted))
elif choice == 2:
    print(text_encrypted)
if crypt:
    print(to_hex(key))
input()