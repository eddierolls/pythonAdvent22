# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:55:09 2022

@author: edwar
"""
snafMap = {'=':-2,'-':-1,'0':0,'1':1,'2':2}

def snafu2dec(num):
    N = len(num)
    return sum([snafMap[num[x]]*(5**(N-1-x)) for x in range(N)])

def dec2quin(num):
    N = 0
    while num>=5**(N+1):
        N+=1
    out = []
    for n in range(N,-1,-1):
        out.append(num//(5**n))
        num-=(5**n)*out[-1]
    return out

def quin2snafu(num):
    num = [0] + num
    for x in range(len(num)-1,-1,-1):
        if num[x]==3:
            num[x-1]+=1
            num[x]='='
        elif num[x]==4:
            num[x-1]+=1
            num[x]='-'
        elif num[x]==5:
            num[x-1]+=1
            num[x]='0'
        else:
            num[x] = str(num[x])
    if num[0]=='0':
        num = num[1:]
    return ''.join(num)

def dec2snafu(num):
    return quin2snafu(dec2quin(num))

f = open("inputs/Day25.txt")
out = 0
for line in f:
    num = line.strip()
    assert num==dec2snafu(snafu2dec(num))
    out += snafu2dec(num)
print(dec2snafu(out))