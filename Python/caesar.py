#!/usr/bin/env python3

# Caesar Cipher

from nltk import word_tokenize

f = open('words.txt', 'r', errors='ignore')
whole_list = f.readline().split()
f.close()

whole_list_small = [x.lower() for x in whole_list]
whole_list_big = [x.upper() for x in whole_list]

def encrypt(msg, key):

    if msg is None:
        return None

    size = len(msg)
    encrypted_msg = ''

    if key > 26:
        key = key % 26
        key = key - 26

    for i in range(size):

        if msg[i].isalpha() is False:
            encrypted_msg = encrypted_msg + msg[i]
            continue

        character = ord(msg[i])

        # Check for capital letters
        if character <= 90 and (character + key > 90):
            letter = chr(character + key - 26)
        elif character >= 65 and character <= 90 and (character + key < 65):
            letter = chr(character + key + 26)
        # Check for small letters
        elif character >= 97 and character <= 122 and (character + key > 122):
            letter = chr(character + key - 26)
        elif character >= 97 and character <= 122 and (character + key < 97):
            letter = chr(character + key + 26)
        else:
            letter = chr(character + key)

        encrypted_msg = encrypted_msg + letter

    return encrypted_msg


def decrypt(msg):

    if msg is None:
        return None

    final_key = 0
    length = len(word_tokenize(msg))
    count = 0

    for key in range(26):
        for word in word_tokenize(msg):
            if whole_list.__contains__(encrypt(word, key)) is True:
                count = count + 1
            elif whole_list_big.__contains__(encrypt(word, key)) is True:
                count = count + 1
            elif whole_list_small.__contains__(encrypt(word, key)) is True:
                count = count + 1

        if count == length:
            final_key = key
            break
        count = 0

    return encrypt(msg, final_key)


if __name__ == '__main__':
    print('Enter 1 to encrypt')
    print('Enter 2 to decrypt with key')
    print('Enter 3 to decrypt without key')
    n = int(input())

    if n == 1:
        string = input('Enter sentence to encrypt ')
        key = int(input('Enter key to encrypt with '))
        print('Encrypted string is - {0}'.format(encrypt(string, key)))

    elif n == 2:
        string = input('Enter sentence to decrypt ')
        key = int(input('Enter key to decrypt with '))
        print('Decrypted string is - {0}'.format(encrypt(string, -key)))

    elif n == 3:
        string = input('Enter sentence to decrypt ')
        print('Decrypted string is - {0}'.format(decrypt(string)))

    else:
        print('Wrong input')
