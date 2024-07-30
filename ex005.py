dia = input("Digite a letra referente ao dia da semana\n{s} sabado\n{d} domingo")

clima = input("digite a letra referente ao clima\n{e} ensolarado\n{n} nublado\n{c} chuvoso")

print("Menu promociona do dia: ")

if (dia == "s"):
    if (clima == "e"):
         print("Frango greshado com legumes")
    elif(clima == "n" or clima == "c"):
         print('Feijoada')
         
        
    else:
        print("Clima informado incorretamente")
elif (dia == "d"):
    if(clima == "e"):
        print('Espetinho de carnes')
    elif(clima == "n" or clima == "c"):
        print('Sopa de vegetais')
    else:
        print("Clima informado corretamente")
else:
    print("Dia informado incorretamente")
        
        
        
              
        
    
        