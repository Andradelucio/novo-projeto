def calcula_delta(a, b, c):
    return(b**2) - 4*a*c

def calcula_x(a, b, c):
    if a == 0:
        return -c/b
    else:
        delta = calcula_delta(a, b, c)
        if delta == 0:
            return -b/(2*a)
        else:
            x1 = (-b + delta**0.5)/(2*a)
            x2 = (-b - delta**0.5)/(2*a)
            return[x1, x2]
        
a = float(input("Digite o valor de a "))
b = float(input("Digite o valor de b "))
c = float(input("Digite o valor de c "))

print("Resultado ", calcula_x(a,b,c))
            
        
    
    

