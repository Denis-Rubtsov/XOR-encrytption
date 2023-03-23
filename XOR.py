from random import *

def generate_key(l):
    key = ''
    english_alphabet_lower = "abcdefghijklmnopqrstuvwxyz" #Creating strings with symbols
    english_alphabet_upper = english_alphabet_lower.upper()
    russian_alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_alphabet_upper = russian_alphabet_lower.upper()
    special_symbols = "!@#$%^&*()_-+=/?.>,<';:[]{}\\|"
    all_symbols = english_alphabet_lower + english_alphabet_upper + russian_alphabet_lower + russian_alphabet_upper + special_symbols
    
    for i in range(l):
        key += all_symbols[randrange(0,len(all_symbols))] #Creating random key
    return key

def xor(text,key):
    encypted = ''
    for i in range(len(text)):
        encypted += chr(ord(text[i])^ord(key[i])) #Xor encryption
    return encypted
