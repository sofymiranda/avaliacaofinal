#variavel com a denominação media e outra variavel com a denominaçao
media=0
quantidade=0
#repete uma acao 6 vezes
for i in range(6):
    #pedir para o usuario colocar o valor para ser armazenado na variavel 
    num=float(input(f"digite o {i+1} numero: "))
    #nessa parte o programa pegara a media e somara ao num
    if num > 0:
        #se o num fot maior que 0 adicionar 1 na variavel positiva
        quantidade=quantidade + 1
#mostra a quantidade de valores positivos
print(f"{quantidade} valores positivos")
#mostra a media da lista numeros:
print(f"{media/quantidade :0.1f}")
