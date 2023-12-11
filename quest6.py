#faça um programa que leia 5 valores inteiros. Conte quantos desses numeros digitados sao pares e mostre essa informacao.
# Pequena explicação
print("Descubra a média de valores positivos.")
# Criação da lista "numeros" e da variável "positivo"
numeros = []
positivo = 0
# Repete uma ação 5 vezes
for i in range(0, 5):
    # Pede um valor para ser armazenado na variável "numero"
    numero = float(input(f'Digite o {i + 1}° número: '))
    
    # Se o número for maior que 0, adicionar 1 na variável positivo, colocar ele na lista "numeros"
    if numero > 0:
        positivo += 1
        numeros.append(numero)
# Soma todos os números da lista "numeros"
soma = sum(numeros)
int(f"{positivo} {'valor' if positivo == 1 else 'valores'} positivos")
# Mostra a média da lista "numeros"
if positivo > 0:
    media = soma / positivo
    print(f"Média dos valores positivos: {media}")
else:
    print("Não há valores positivos para calcular a média.")