# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:26:59 2020

@author: franc
"""
#forma 1
#contador numérico para cálculo
a = 0 
#condicional
while a <= 20:
    a += 1
    #divisão para número inteiro
    b = a % 2
    if a == 15:
        break
    if b == 0:
        print('Valor par:',a, 'resto da divisão: ',b)
        
#forma 2

#condicional
for a in range(1,20):
    #divisão para número inteiro
    b = a % 2
    if a == 15:
        break
    if b == 0:
        print('Valor par:',a, 'resto da divisão: ',b)
        
#forma 3

#condicional
for a in range(0,20,2):
    #divisão para número inteiro
    b = a % 2
    if a == 16:
        break
    print('Valor par:',a, 'resto da divisão: ',b)