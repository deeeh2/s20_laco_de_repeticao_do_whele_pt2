"""
CONTAR VOGAIS
"""
while True:
    palavra = input("Digite uma palavra (ou pressione Enter para sair): ")
    if palavra == "": # se não tiver palavras, por isso ENTER direto
        break # Se não conter nunhuma palavra então para.

    vogais = "aeiouAEIOU" # Estou ensinado o algorito a reconhecemos
    contagem_vogais = sum(1 for letra in palavra if letra in vogais)
    """ A variavel contagem_vogais contém uma função de soma (sum) que atribui o número 1 
    para cada vogal prente na variável vogais para depois somar."""
    print(f"A palavra '{palavra}' tem {contagem_vogais} vogais.")                                   