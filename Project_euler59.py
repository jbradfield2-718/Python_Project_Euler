''' Project Euler Problem 59--XOR Cryptography
    Each character on a computer is assigned a unique code and the preferred standard is ASCII
    (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
    The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
    then 107 XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the
    encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than
    the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password
    key for security, but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
    a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
    decrypt the message and find the sum of the ASCII values in the original text. '''

import csv
import time
import Functions

start = time.clock()
ls = []
file = []

def str_to_int(str):
    num = 0
    for i in range(0, len(str)):
        if i != (len(str) -1):
            num +=  (ord(str[i]) - 48)*(10**(len(str) - i -1))
        else:
            num += ((ord(str[i]) - 48))
    return num

def find_all(search, string):
    ls = []
    start = 0
    end = len(string)
    test = 0
    while(test != -1):
        test = string.find(search, start, end)
        if (test != -1):
            ls.append( test )
            start = ls[-1] +1
            print(start)
    return ls

def increment_pass(key_a, key_b, key_c):
    key_a += 1

    if(key_a == 123):
        key_a = 97
        key_b += 1
    if(key_b == 123):
        key_c += 1
        key_b = 97

    return (key_a, key_b, key_c)
       
with open('cipher1.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        ls.append(row)

file = ls[0]                        # this is the file of strings --- need function to take each string, convert to equivalent integer.

for i in range(0, len(file)):       # for loop converts all strings to equivalent ints
    file[i] = str_to_int(file[i])


''' Lower case ASCII characters range 97 (a) --> 122 (z)
    Brute force-cylce through the entire range of possiblites and test against common words
    26**3 == 17676 possible combinations of password '''
''' Common words, the be to of and that have '''

common_word1 = 'the'
common_word2 = 'be'
common_word3 = 'and'
common_word4 = 'all'

test_file = file
test_str = ''
list_of_possibles = []
correct_str = ''

key_a = 97
key_b = 97
key_c = 97

while (True):
    counter = 0
    current_password = chr(key_a) + chr(key_b) + chr(key_c)
    for i in range(0, len(test_file)):              # This loop cycles over the test file and applies the XOR cipher to attempt decryption
        if (counter == 0):
            test_str += chr( test_file[i] ^ key_a )
            counter += 1
        elif (counter == 1):
            test_str += chr( test_file[i] ^ key_b )
            counter += 1
        else:
            test_str += chr( test_file[i] ^ key_c )
            counter = 0

    if (common_word1 in test_str and common_word2 in test_str and common_word3 in test_str and common_word4 in test_str):
        list_of_possibles.append(current_password)
        correct_str = test_str
        break
        
        

    (key_a, key_b, key_c) = increment_pass(key_a, key_b, key_c)

    test_str = ''
    
    if(key_c == 123):
        break

answer_sum = 0
for i in range(0, len(correct_str)):
    answer_sum += ord( correct_str[i] )        

print("The possible passwords are: ",list_of_possibles,'\n')
print('The decoded text is: \n',correct_str,'\n')
print('\nThe sum of the ASCII characters in the decoded string is ', answer_sum,'\n')
Functions.runtime(start)   
    
