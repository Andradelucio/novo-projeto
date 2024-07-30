lado = float(input("Digite o lado do quadrado em metros: "))

def calcula_area():
    area = lado*lado
    return area
    
resultado = calcula_area()
print("A area do quadrado de lado ", lado, "m é ", resultado, "m²")

