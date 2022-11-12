# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:18:58 2022

@author: fariz
"""

def pangkat(a,b,c=1):
    if b>0:
        c=c*a
        b=b-1
        pangkat(a, b, c)
    else:
        print(c)
        

angka=int(input('angka: '))
x=int(input('pangkat: '))
pangkat(angka, x)