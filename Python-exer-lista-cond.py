# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 23:07:59 2020

@author: franc
"""
# Exercício para uso do laço de repetição

def main():
    print('Insira notas para das médias e mostrar aprovações:')
    
    listanome = ['Carlos', 'Heitor', 'João', 'Abraão', 'Rodolfo', 'Thiago']
    listanota = [8,9,10,3,5,7]
    #contador responsável pela localização de aluno e nota exata
    n = 0
    for lista in listanome:
        
        
        
        print(' ')
        #função para adicionar novo aluno e nota correspondente.
        a = str('Sim')
        b = str(input('Digite sua resposta: Sim ou Não: '))
        if b == a:
                aluno = str(input(print('Digite nome do aluno: ')))
                nota = float(input(print('Digite nota do aluno: ')))
                #adição do aluno e nota nas listas correspondentes.   
                listanome.append(aluno)
                listanota.append(nota)
                
        elif b != a:
                print('Nome do aluno:',lista, 'nota do aluno', listanota[n])
                if listanota[n] >= 6:
                    print("Aluno aprovado!")
                elif listanota[n] < 6:
                    print('Nos vemos na próxima!')
                else:
                    pass
        
        
        n = 1 + n
        
main()
        