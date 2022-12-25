import functools
import sys
import math
import time


def result(letter):
    if letter == '2':
        return 2
    if letter == '1':
        return 1
    if letter == '0':
        return 0
    if letter == '-':
        return -1
    if letter == '=':
        return -2

def getNum(string):
    dgt = 1
    ans = 0
    for i in range(len(string)-1, -1, -1):
        if string[i] == '\n':
            continue
        ans += result(string[i]) * dgt
        dgt *= 5
    return ans

def toSNAFU(num):
    dgts = []
    i = 0
    carry = 0
    while num != 0:
        dgt = num % 5 + carry
        if dgt > 2:
            dgt -= 5
            carry = 1
        else:
            carry = 0
        dgts.append(dgt)
        i += 1
        num = num // 5
    rstr = ''
    for i in range(len(dgts)-1,-1,-1):
        dgt = dgts[i]
        if dgt in (0,1,2):
            rstr += str(dgt)
        if dgt == -1:
            rstr += '-'
        if dgt == -2:
            rstr += '='
    return rstr

def main():
    with open('25.in','r') as fin:
        lns = fin.readlines()

    s = 0
    for ln in lns:
        s += getNum(ln)
    print(s)
  
if __name__ == '__main__':
    main()
    
