def valida_login(usuario, senha):
    if usuario == 'admin' and senha == '123':
        print("login bem sucedido")
        
    else:
        print("Falha no login")
        
user = input("Informe o nome do usuario: ")
password = input("Informe a senha: ")
valida_login(user, password)



    

