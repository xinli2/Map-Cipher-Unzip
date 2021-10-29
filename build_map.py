"""
    File: build_map.py
    Author: Xin Li
    Purpose: This program deals with building and checking maps
    for the substitution cipher.
"""
def build_map(filename):
    map = {}
    filename.strip(filename)
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        if line[0]!= '':
            if line[0][0] != '#':
                assert len(line) == 2
                assert len(line[0])==1 and len(line[1])==1
                assert line[0] not in map
                map[line[0]] = line[1]
    return map

def is_valid_map(map):
    lst = ['', ' ', '\n', '\t']
    test = True
    value_lst = []
    key_lst = []
    for key, value in map.items():
        if isinstance(key,str) == False:
            test = False
        if isinstance(value,str) == False:
            test = False
        if len(key) !=1:
            test = False
        if len(value) !=1:
            test = False
        if key in lst:
            test = False
        key_lst.append(key)
        if value in lst:
            test = False
        if value in value_lst:
            test = False
        if value not in value_lst:
            value_lst.append(value)

    return test
