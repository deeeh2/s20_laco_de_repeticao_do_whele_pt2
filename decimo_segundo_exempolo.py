"""
CONTAGEM REGRESSIVA
"""
while True:
    numero = int(input("Digite um número para iniciar a contagem regressiva: ")) 
    
    while numero >= 0: # enquanto for maior que zero  
        print(numero) # mostre o número
        numero -= 1 # na ordem decrecente
    
    continuar = input("Quer fazer outra contagem regressiva? (s/n): ")
    if continuar.lower() == 'n': # se digitar a letra
        break