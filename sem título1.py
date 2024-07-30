x = 17
erros = 0

palpite = int(input("Digite seu palpite"))

while(palpite != x):
    erros = erros + 1
    palpite = int(input("Voce errou. Digite novamente: "))

print("Parabéns voce acertou o numero ", x)
print("Tentativas erradas: ", erros)