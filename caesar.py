#!/usr/bin/env python3

# Caesar Cipher

from nltk import word_tokenize

f = open('words.txt', 'r', errors='ignore')
whole_list = f.readline().split()
f.close()

def encrypt(msg, key):

    if msg is None:
        return None

    encrypted_msg = ''
    
    for character in msg:

        if 'a' <= character <= 'z':
            encrypted_msg += chr(97 + (ord(character) - 97 + key)%26)
        elif 'A' <= character <= 'Z':
            encrypted_msg += chr(65 + (ord(character) - 65 + key)%26)
        else:
            encrypted_msg += character

    return encrypted_msg


def decrypt(msg):

    if msg is None:
        return None

    case_string = ''
    for letter in msg:
        if 'A' <= letter <= 'Z':
            case_string += '1'
        else:
            case_string += '0'
            
    msg = msg.lower()

    final_key = 0
    length = len(word_tokenize(msg))    

    for key in range(26):
        count = 0
        
        for word in word_tokenize(msg):
            if whole_list.__contains__(encrypt(word, key)) is True:
                count = count + 1
        if count == length:
            final_key = key
            break

    decrypted_msg = encrypt(msg, final_key)
    
    orginal_cased_decrypted_msg = ''

    for i in range(len(decrypted_msg)):
        orginal_cased_decrypted_msg += chr(ord(decrypted_msg[i]) - int(case_string[i])*(97-65))

    return orginal_cased_decrypted_msg


if __name__ == '__main__':
    print('Enter 1 to encrypt')
    print('Enter 2 to decrypt with key')
    print('Enter 3 to decrypt without key')
    n = int(input())

    if n == 1:
        string = input('Enter sentence to encrypt ')
        key = int(input('Enter key to encrypt with '))
        print('Encrypted string is - {0}'.format(encrypt(string, key526)))

    elif n == 2:
        string = input('Enter sentence to decrypt ')
        key = int(input('Enter key to decrypt with '))
        print('Decrypted string is - {0}'.format(encrypt(string, -key%26)))

    elif n == 3:
        string = input('Enter sentence to decrypt ')
        print('Decrypted string is - {0}'.format(decrypt(string)))

    else:
        print('Wrong input')
