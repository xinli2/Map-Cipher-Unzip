"""
    File: subs_cipher.py
    Author: Xin Li
    Purpose: This program actually dose the encoding and
    decoding of the substitution sipher.
"""
'''from build_map import build_map
map = build_map(filename)
test = is_valid_map(map)
assert test == True
'''
def encode(map,msg):
    lst=[]
    new_string =''
    string = msg
    for i in range (len(string)):
        if string[i] in map:
            lst.append(map[string[i]])
        else:
            lst.append(string[i])
    for j in lst:
        new_string += j
    return new_string
def decode(map,msg):
    decode_map= {}
    value_lst= []
    key_lst = []
    lst=[]
    new_string= ''
    for key in map:
        value_lst.append(key)
        key_lst.append(map[key])
    for index in range(len(key_lst)):
        decode_map[key_lst[index]] =value_lst[index]
    for i in range (len(msg)):
        if msg[i] in decode_map:
            lst.append(decode_map[msg[i]])
        else:
            lst.append(msg[i])
    for j in lst:
        new_string += j
    return new_string
