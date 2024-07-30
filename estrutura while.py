num1 = 0
num2 = 0

def ler_numeros():
    global num1
    global num2
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
                 
                 
operação = input("Digite a operação que deseja fazer: ")
ler_numeros()

if operação == '+':
    print(num1 + num2)
elif operação == '-':
    print(num1 - num2)
elif operação == '*':
    print(num1 * num2)
elif operação == '/':
    while num2 == 0:
        print("O valor da segunda variavel não pode ser zero")
        ler_numeros()
    print(num1 / num2)
    

    
    
