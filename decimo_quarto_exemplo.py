"""
SOMANDO OS DÍGITOS
"""

while True:
    numero = input("Digite um número inteiro (ou 0 para sair): ")
    if numero == "0":
        break
    
    soma_digitos = sum(int(digito) for digito in numero)
    """
    A variável soma de digitos recebe uma função que soma cada digito esta contido em um número é somado com outro.
    """
    print(f"A soma dos dígitos de {numero} é {soma_digitos}")
    """
    Existe o número digitado e a soma de todos os dígitos  deste mesmo número
    """