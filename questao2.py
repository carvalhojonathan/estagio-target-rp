'''
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.'''

def verifica_a(string):
    cont = 0
    for i in string:
        if i == 'a' or i == 'A':
            cont += 1
    return cont

string = input('Digite uma string: ')

if verifica_a(string):
    print(f'A letra "a" ocorre {verifica_a(string)} vezes na string informada.')
else:
    print('A letra "a" não ocorre na string informada.')