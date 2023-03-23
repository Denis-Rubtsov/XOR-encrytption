from XOR import *
from transfer import *

crypt = True

choice = int(input('Encrypt or decrypt? (1,2) '))

if choice == 2:
    message = input('Input message:')
    text, key = disconnection(message)
    print(xor(text, key))
    crypt = False
else:
    text = input('Input text: ')
    result = '\n'
    while '\n' in result:
        key = generate_key(len(text))
        result = combine(key,xor(text,key))
    print(result)