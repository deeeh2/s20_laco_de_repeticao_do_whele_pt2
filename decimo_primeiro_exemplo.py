"""
TABUADA
"""

while True:
    numero = int(input("Digite um número para ver a tabuada (0 para sair): "))
    if numero == 0: # Se o número digitado for 0
        break # o programa para quando digitados 0
    for i in range(1, 11):  
        """
        A variável i significa o intervalo númerico do range que ínicia de  zero até o último número corresponde ao intervalo do range.
        """
        print(f"{numero} x {i} = {numero * i}")
        """
        Será mostrada a tubuada na tela 
        """