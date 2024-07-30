idade = int(input("Digite a idade do paciente"))

if( idade >= 60):
    print("Paciente é idoso")
elif (idade >= 18 and idade < 60):
    print("Paciente é adulto")
elif (idade >= 13 and idade < 60):
    print("paciente é adolecente ")
else:
    print("paciente é criança")
    


