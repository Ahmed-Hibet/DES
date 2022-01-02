
initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2, 
                       60, 52, 44, 36, 28, 20, 12, 4, 
                       62, 54, 46, 38, 30, 22, 14, 6, 
                       64, 56, 48, 40, 32, 24, 16, 8, 
                       57, 49, 41, 33, 25, 17, 9, 1, 
                       59, 51, 43, 35, 27, 19, 11, 3, 
                       61, 53, 45, 37, 29, 21, 13, 5, 
                       63, 55, 47, 39, 31, 23, 15, 7]

pc1 = [57, 49, 41, 33, 25, 17, 9, 
       1, 58, 50, 42, 34, 26, 18, 
       10, 2, 59, 51, 43, 35, 27, 
       19, 11, 3, 60, 52, 44, 36, 
       63, 55, 47, 39, 31, 23, 15, 
       7, 62, 54, 46, 38, 30, 22, 
       14, 6, 61, 53, 45, 37, 29, 
       21, 13, 5, 28, 20, 12, 4]

pc2 = [14, 17, 11, 24, 1, 5, 
       3, 28, 15, 6, 21, 10, 
       23, 19, 12, 4, 26, 8, 
       16, 7, 27, 20, 13, 2, 
       41, 52, 31, 37, 47, 55, 
       30, 40, 51, 45, 33, 48, 
       44, 49, 39, 56, 34, 53, 
       46, 42, 50, 36, 29, 32]

SBox = [
    [
        (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
        (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
        (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
        (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13)
    ],

    [
        (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10),
        (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5),
        (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15),
        (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9)
    ],

    [
        (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8),
        (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1),
        (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7),
        (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12) 
    ],

    [
        (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15),
        (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9),
        (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4),
        (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14)
    ],

    [
        (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9),
        (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6),
        (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14),
        (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3)
    ],

    [
        (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11),
        (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8),
        (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6),
        (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13)
    ],

    [
        (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1),
        (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6),
        (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2),
        (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12)
    ],

    [
        (13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7),
        (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2),
        (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8),
        (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11)
    ]
]

expansion = [32, 1, 2, 3, 4, 5, 
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]

No_of_left_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

p = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

final_permutation = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]


key = "0001001100110100010101110111100110011011101111001101111111110001"

subKey = []

### representing the plaintext in the form of hexadecimal digites of their ASCII code ###

def convert_plaintext_to_hexadecimal(plaintext):
    converted_plaintext = ""
    for i in plaintext:
        single_character = hex( ord(i) )[2:]
        if len(single_character) == 1:
            single_character = '0' + single_character
        converted_plaintext += single_character
    return converted_plaintext

def convert_binary_to_hexadecimal(text):
    hexForm = hex(int(text,2))[2:]
    lenOfHex = len(hexForm)
    for i in range(lenOfHex,16):
        hexForm = '0' + hexForm
    return hexForm

def convert_hexa_to_binary(text):
    binForm = bin( int(text,16) )[2:]
    lenOfBin = len(binForm)
    for i in range(lenOfBin,64):
        binForm = '0' + binForm
    return binForm

def perform_reverse_initial_permutation(text):
    new_text = ['0' for i in range(64)]
    for i in range(64):
        new_text[ initial_permutation[i] - 1 ] = text[i]
    reverse_IP = ''.join(new_text)
    return reverse_IP

def XOR(text1, text2):
    new_text = ""
    for i in range(len(text1)):
        if text1[i] == text2[i]:
            new_text += '0'
        else:
            new_text += '1'
    return new_text

def left_shift(text):
    temp = text[1:]
    temp += text[0]
    return temp

def apply_pc1():
    new_text = ""
    for i in pc1:
        new_text += key[i-1]
    return new_text

def apply_pc2(text):
    new_text = ""
    for i in pc2:
        new_text += text[i-1]
    return new_text

def subkey_generation():
    pc1_result = apply_pc1()
    Co = pc1_result[:28]
    Do = pc1_result[28:]
    for i in range(16):
        for j in range(No_of_left_shift[i]):
            Co = left_shift(Co)
            Do = left_shift(Do)
        newSubKey = apply_pc2(Co+Do)
        subKey.append(newSubKey)

def expand_32_to_48(text):
    new_text = ""
    for i in expansion:
        new_text += text[i-1]
    return new_text

def apply_sbox(text):
    new_text = ""
    for i in range(0,48,6):
        row = text[i] + text[i+5]
        row = int(row,2)
        column = text[i+1:i+5]
        column = int(column,2)
        sbox = i//6
        sbox_value = SBox[sbox][row][column]
        sbox_value = bin(sbox_value)[2:]
        lenOfBinary = len(sbox_value)
        for _ in range(lenOfBinary,4):
            sbox_value = '0' + sbox_value
        new_text += sbox_value
    return new_text

def apply_p(text):
    new_text = ""
    for i in p:
        new_text += text[i-1]
    return new_text

def f_function(text, keyi):
    expanded_text = expand_32_to_48(text)
    text_XOR_Key = XOR(expanded_text, keyi)
    after_sbox = apply_sbox(text_XOR_Key)
    after_p = apply_p(after_sbox)
    return after_p

def apply_reverse_final_permutation(text):
    new_text = ['0' for i in range(64)]
    for i in range(64):
        new_text[ final_permutation[i] - 1 ] = text[i]
    reverse_FP = ''.join(new_text)
    return reverse_FP



#plaintext = input() # accepting the plaintext from the user

#hex_plaintext = convert_plaintext_to_hexadecimal(plaintext)

#plain = hex(int("0000000100100011010001010110011110001001101010111100110111101111",2))[2:]

print("Enter the ciphertext:")
ciphertext = input()
len_of_ciphertext = len(ciphertext)

subkey_generation()
plaintext = ""
for j in range(0,len_of_ciphertext,16):
    cipher = ciphertext[j:j+16]
    cipher = convert_hexa_to_binary(cipher)
    after_FP = apply_reverse_final_permutation(cipher)
    L16 = after_FP[32:]
    R16 = after_FP[:32]
    for k in range(15,-1,-1):
        perform_f_function = f_function(L16,subKey[k])
        temp = L16
        L16 = XOR(perform_f_function,R16)
        R16 = temp
    round_plaintext = perform_reverse_initial_permutation(L16+R16)
    plaintext += convert_binary_to_hexadecimal(round_plaintext)
print(plaintext)

lenOfPlaintext = len(plaintext)
original_plaintext = ""
for j in range(0,lenOfPlaintext,2):
    singleChar = plaintext[j:j+2]
    if singleChar != '00':
        original_plaintext += chr(int(singleChar,16))
print(original_plaintext)

#f_function("11110000101010101111000010101010","000110110000001011101111111111000111000001110010")
#subkey_generation()
#print(len(apply_sbox("011000010001011110111010100001100110010100100111")))
#print(plaintext)
#print()

