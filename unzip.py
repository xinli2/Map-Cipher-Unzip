"""
    File: unzip.py
    Author: Xin Li
    Purpose: This program deals with decoding a compressed data
    stream.
"""

def unzip(new_lst):
    compress_lst = []
    ans=''
    index = 0
    for i in range(len(new_lst)):
        if len(new_lst[i]) > 1:
            for k in range(int(new_lst[i][1])):
                compress_lst.append(compress_lst[index-int(new_lst[i][0])+k])
            index +=k

        else:
            compress_lst.append(new_lst[i])
        index +=1
    for k in compress_lst:
        ans += str(k)
    return ans
