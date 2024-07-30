def le_notas():
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    return[nota1, nota2, nota3]

def calcula_média():
    n1, n2, n3 = le_notas()
    media = (n1 + n2 + n3)/3
    return media


resultado = calcula_média()
print("Media: " ,resultado)


