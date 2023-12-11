#leia um valor com duas casas decimais, equivalente ao salario
#de uma pessoa em lisarb. Em seguida, calcule e mostre o valor
#que essa pessoa deve pagar no imposto de renda.
sal:float(input("Digite o valor do seu salario: "))
#pedir o salario da pessoa
if sal <=2000.00:
    print("Insento")
#variavel nao valida para adicionar impostos
elif sal > 2000.00 and sal <= 3000.00:
    n1: (sal * 8.0)/100.00
    print(f"o imposto a pagar é: ${n1}")
#a variavel vai passar pelo processo para descobrir o imposto que devera ser pago
elif sal > 3000.00 and sal<= 4500.00:
    n2: (sal * 18.00) / 100.00
    print(f"O imposto a pagar é: ${n2}") 
#a variavel maior que 2000 vai passar por o mesmo processo, mas com uma porcentagem de imposto maior
else:
    print (f"Seu imposto e de: ${(sal * 28)/100}")
#a variavel sendo maior que as espectativas devera passar pelo mesmo processo, mas comuma porcentagemde imposto ainda maior
