arquivo = open("C:/Users/luciojulia/desktop/calculadora.txt", 'r')

contas = []

for linha in arquivo.readlines():
    contas.append(linha)
arquivo.close()

operacoes = []
for conta in contas:
    operacoes.append(conta.split())
    
print(operacoes)
texto_final = ""
resultado = ""
for lista in operacoes:
    if lista[1]  == "+":
        resultado = int(lista[0]) + int(lista[2])
    elif lista[1] == "-":
        resultado = int(lista[0]) - int(lista[2])
    elif lista[1] == "x":
        resultado = int(lista[0]) * int(lista[2])
    elif lista[1] == "/" and int(lista[2]) != 0:
        resultado = int(lista[0]) / int(lista[2])
    texto_final += lista[0] + " " + lista[1] + " " + lista[2] + " = " + str(resultado) + "\n"
    
arquivo = open("C:/Users/luciojulia/desktop/calculadora.txt", 'w')
arquivo.write(texto_final)
arquivo.close()
        
    
      
      
