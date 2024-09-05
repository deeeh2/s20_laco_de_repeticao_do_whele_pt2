"""
ESCOLHENDO A OPÇÃO
"""

while True: # enquanto for VERDADEIRO (Se estiver nesta lista)
    print("\nMenu:")
    print("1. pizza")
    print("2. esfira")
    print("3. kibe")
    print("4. coxinha")
    print("0. sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '0': # Se a escolha for igual a 0
        print("Saindo...")
        break # O progrema foi interrompido de acordo com a condição
    elif escolha == '1':
        print("Você escolheu a pizza!")
    elif escolha == '2':
        print("Você escolheu a esfira!")
    elif escolha == '3': 
         print(" você escolheu a kibe !" )
    elif escolha == '4': 
        print(" você escolheu a coxinha !" )
    else:
        print("Opção inválida! Tente novamente.")