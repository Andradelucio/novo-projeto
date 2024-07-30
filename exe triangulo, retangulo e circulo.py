def calcula_area_retangulo(base, altura):
    return base*altura

def calcula_area_retangulo(base, altura):
    return (base*altura)/2

def calcula_area_circulo(raio):
    return 3.14*(raio**2)


while True:
    
    forma = input("Qual a forma geometrica desja calculara a area?\n[r]etangulo\n[t]riangulo\n[c]irculo\n[s]air\n")
    if forma =='r':
        b = float(input("Informe a base do retangulo"))
        a = float(input("Informe a altura do retangulo"))
        print("Area do retangulo: ", calcula_area_retangulo(b,a) )
    elif forma == 't':
        b = float(input("Informe a base do triangulo "))
        a = float(input("Informe a altura do triangulo "))
        print("Area do triangulo: ", calcula_area_triangulo(b,a) )
        
    elif forma == 'c':
        r = float(input("Informe o raio de um circulo "))
      
        print("Area do retangulo: ", calcula_area_circulo(r) )
    elif forma == 's':
        break
    else:
        print("Opção invalida")
        
              
                      
    
        
    

