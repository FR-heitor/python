# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:15:54 2020

@author: franc
"""

"Exercícios para módulo de entrada/saída de variáveis"

def main():
    'variável = tipo(inserir(exibir("argumento opcional")'
    print('Por favor, informe quais números você quer calcular:')
    a = float(input(print('Digite o número 1:')))
    b = float(input(print('Digite o número 2:')))
    c = float(input(print('Digite o número 3:')))
    d = float(input(print('Digite o número 4:')))
    tupla = (a,b,c,d)
    
    print('Quais números você quer que interajam:', a,',',b,',',c,'ou',d,'?')
    aa = float(input(print('Escolha um número: ')))
    bb = float(input(print('Escolha outro número: ')))
    if aa not in tupla:
        aa = float(input(print('Escolha um número: ')))
    if bb not in tupla:
        bb = float(input(print('Escolha outro número: ')))
    
    def calculo():
        soma = aa+bb
        produto  = aa*bb
        divi = aa/bb
        print('Soma: ', soma)
        print('Produto: ', produto)
        print('Divisão: ', divi)
            
        Subtra = a - b - c - d                                
        print('Subtração entre os quatro números', Subtra)
    
   
    calculo() 
'Chamar função'            
main()