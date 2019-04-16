salario = int(input('Salario? '))
imposto = input('Imposto em % (ex: 27.5)? ')
if imposto == '':
    imposto = 27.5
else:
    imposto =  float(imposto)
print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

imposto = float(input("Imposto: "))
if imposto < 10:
    print("Medio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito Alto")

imposto = float(input("Imposto: "))
if imposto < 10.:
    print("Baixo")
elif imposto >=10. and imposto <= 27.:
    print("Médio")
elif imposto > 27. and imposto < 100:
    print("Alto")
else:
    print("Imposto inválido")

salario = int(input('Salario? '))
imposto = 27.
while imposto > 0.:
    imposto = input('Imposto ou (0) para sair: ')
    if not imposto:
        imposto = 27.
    else:
        imposto = float(imposto)
    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
