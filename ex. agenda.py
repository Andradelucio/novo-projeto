def cadastrar_evento():
    agenda = open('C:/Users/luciojulia/desktop/agenda.txt', 'a')
    evento = input("Informe o evento: \n")
    evento += "\n"
    agenda.write(evento)
    agenda.close()
    
def apagar_agenda():
    agenda = open("C:/Users/luciojulia/desktop/agenda.txt", 'w')
    agenda.write("")
    agenda.close()
    
def visualizar_agenda():
    agenda = open("C:/Users/luciojulia/desktop/agenda.txt", 'r')
    for evento in agenda.readlines():
        print(evento)
    agenda.close()
    
while True:
    mensagem = "O que deseja fazer?\n[C]adastrar evento\n[A]pagar Agenda\n[V]isualizar agenda\n[s]air\n"
    opção = input(mensagem)
    if opção == 'c':
        cadastrar_evento()
    elif opção == 'a':
        apagar_agenda()
    elif opção == 'v':
        visualizar_agenda()
    elif opção == 's':
        break
    else:
        print("Opção invalida")
    

