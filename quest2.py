#leia o salario do funcionario calcule e mostre o novo salario, bem como o valor de reajuste ganho e indice reajustado em percentual
salatu=float(input("Digite o valor do seu salario atual: "))
#pedir o valor da variavel
if salatu >= 0 and salatu<=400:
    v1=(salatu*15)/100
    v2= salatu+v1
    v3= "15%"
    print (f"seu novo salario é de: {v2}")
    print (f"seu aumento foi de: {v1}")
    print (f"a porcentagem aumentada é de: {v3}")
#nessa condiçao, pegasse a variavel e a soma com o valor calculado do seu aumento
elif salatu > 400 and salatu <=800:
    v4=(salatu*12)/100
    v5= salatu+v4
    v6="12%"
    print (f"seu novo salario é de: {v5}")
    print (f"seu aumento foi de: {v4}")
    print (f"a porcentagem aumentada é de: {v6}")
#nessa condiçao, pegasse a variavel e a soma com o valor calculado do seu aumento, mas dessa vez com uma porcentagem de aumento menor
elif salatu > 800 and salatu <=1200:
    v7=(salatu*10)/100
    v8=salatu+v7
    v9="10%"
    print (f"seu novo salario é de: {v8}")
    print (f"seu aumento foi de: {v7}")
    print (f"a porcentagem aumentada é de: {v9}")
#nessa condiçao, pegasse a variavel e a soma com o valor calculado do seu aumento, mas dessa vez com uma porcentagem de aumento ainda menor
elif salatu > 1200 and salatu <=2000:
    v10=(salatu*7)/100
    v11=salatu+v10
    v12="7%"
    print (f"seu novo salario é de: {v11}")
    print (f"seu aumento foi de: {v10}")
    print (f"a porcentagem aumentada é de: {v12}")
#nessa condiçao, pegasse a variavel e a soma com o valor calculado do seu aumento, mas dessa vez com uma porcentagem de aumento reduzida
else :
   v13=(salatu*4)/100
   v14=salatu+v13
   v15="4%"
   print (f"seu novo salario é de: {v14}")
   print (f"seu aumento foi de: {v13}")
   print (f"a porcentagem aumentada é de: {v15}")
#quando a variavel nao atendeu as expectativas anteriores, ela passara por essa condicao.