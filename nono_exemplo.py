"""
LOGIN SIMPLES
"""

usuario_correto = "admin" # O usuário deverá ser este.
senha_correta = "1234" # A senha deverá ser esta.

while True: # enquanto estiver na lista (enquanto for verdadeiro)
    usuario = input("Nome de usuário: ") # recebe o usuário
    senha = input("Senha: ") # recebe a senha
    
    if usuario == usuario_correto and senha == senha_correta: # se o usúario E asenha estiver correta
     print ("Login bem-sucedido!") # Se estiver correto
    break# se estiver correto o sistema para.
else: # então, caso contrátrio, por outro lado... 
         print("Usuário ou senha incorretos! Tente novamente.")
      