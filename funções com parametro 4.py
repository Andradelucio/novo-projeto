def calcula_média(qtd_notas):
    total = 0
    contador = 0
    
    while(contador < qtd_notas):
        total == float(input("digite a nota: "))
        contador += 1
        
        return total/qtd_notas
    
    
def verifica_aprovação(média, faltas, nome):
    print("Média: ", média, "Faltas: ", faltas)
    if (média >= 5 and faltas <= 4):

       print("estudante ", nome, "APROVADO(A)")
    elif(média < 5 and faltas  <= 4):
       print("Estudante ", nome, " em RECUPERAÇÃO") 
    else:
       print("Estudante ", nome, "REPROVADO(A)")
             
e = input("Digite o mome do(a) estudante:")
f = int(input("Qantas faltas o(a) estudante teve? "))
n = int(input("Quantas notas dejeja inserir? "))
m = calcula_média(n)

verifica_aprovação(m, f, e)