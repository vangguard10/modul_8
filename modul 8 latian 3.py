# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 08:49:01 2022

@author: fariz
"""

import math as m

hexa={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
deci={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
def htod (a,b=0,c=-1,d=0):
    if c>=-(len(a)):
        e=a[c]
        if e.upper() in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
            d=d+(deci[e.upper()]*pow(16,b))
            c=c-1
            b=b+1
            htod(a,b,c,d)
            if c < -(len(a)):
                print(d)
        else:
            print('Invalid input!')

        
def dtoh (a,c=[]):
    b=a%16
    a=m.floor(a/16)
    d=hexa[b]
    c.insert(0, d)
    if a>0:
        dtoh(a)
    else:
        print(*c)
        c.clear()
i=0
while i == 0:
    print('')
    print('''program konversi hexadecimal <==> decimal
input:
hexadecimal ==> decimal: 1
decimal ==> hexadecimal: 2
keluar/exit            : 3''')
    awal=(input('program mana yang ingin di lakukan? '))
    if awal=='':
        i=1
    elif int(awal)==1:
        o=1
        print('tekan <ENTER> untuk selesai')
        while o==1:
            angka_h=str(input('masukan data hexadecimal: '))
            if angka_h=='':
                o=0
            else:
                list(angka_h)
                htod(angka_h)
    elif int(awal)==2:
        o=1
        print('tekan <ENTER> untuk selesai')
        while o==1:
            angka_h=str(input('masukan data decimal: '))
            x=list(angka_h)
            if angka_h=='':
                o=0
                i=0
            else:
                f=1
                for i in range(-(len(x)),0):
                    if x[i]in('1','2','3','4','5','6','7','8','9','0'):
                        f=f*1
                    else:
                        f=f*0
                if f==1:
                    int(angka_h)
                    dtoh(int(angka_h))
                elif f==0:
                    print('Invalid input!')
                
    elif int(awal) == 3:
        i=1
        break
    else:
        i=1
        break
print('''
terima kasih telah menggunakan program saya
ig: alfarizqiwira''')