arquivo = open('C:/Users/luciojulia/desktop/teste.txt', 'a')#append

frase = "\nterei muito sucesso na minha jornada!"

arquivo.write(frase)
arquivo.close()

arquivo = open('C:/Users/luciojulia/desktop/teste.txt', 'r')#reader
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
              

