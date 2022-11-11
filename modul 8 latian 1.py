# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:06:13 2022

@author: fariz
"""

def penjumlahan(a,b=1,d=0):
    if a>0:
        a=a-1
        c=int(input(f'masukan angka ke-{b}:'))
        d=d+c
        b+=1
        penjumlahan(a, b, d)
        
    else:
        print(f'Jumlah: {d}')
        print('''
terima kasih telah menggunakan program saya
ig: alfarizqiwira''')
    
a=int(input('banyak angka yang ingin di jumlah kan: '))
penjumlahan(a)