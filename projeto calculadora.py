arquivo = open('C:/users/luciojulia/desktop/calculadora.txt', 'r')
conta = arquivo.readline()
arquivo.close()
conta = conta.split()

resultado = ""
if conta[1] == '+':
    resultado = int(conta[0]) + int(conta[2])
elif conta[1] == '-':
    resultado = int(conta[0]) - int(conta[2])
elif conta[1] == 'x':
    resultado = int(conta[0]) * int(conta[2]) 
elif conta[1] == '/' and int(conta[2]) !=0:
    resultado = int(conta[0]) / int(conta[2]) 
    
resultado = " = " + str(resultado)
print(resultado)
arquivo = open("C:/users/luciojulia/desktop/calculadora.txt", 'a')
arquivo.write(resultado)
arquivo.close()
        
    
