#escreva um programa que repita a leitura de uma senha ate que ela seja valida. Para cada leitura de senha incorreta informada, escrevera mensagem: "senha invalida"
#quando a senha for informada corretamente, exiba a mensagem "acesso permitido". A senha correta é o valor 2002

# Exibe uma mensagem indicando que é um cofre
print("Cofre")
# Define a senha correta que permite o acesso
senha_correta = 2002
# Define o número máximo de tentativas permitidas
max_tentativas = 3
# Loop que controla as tentativas do usuário
for tentativa_atual in range(1, max_tentativas + 1):
    # Obtém a tentativa de senha do usuário e converte para um número inteiro
    tentativa = int(input("Digite a senha: "))
    
    # Verifica se a senha fornecida está correta
    if tentativa == senha_correta:
        # Se a senha está correta, exibe uma mensagem e encerra o loop
        print("Acesso permitido")
        break
    else:
        # Se a senha está incorreta, exibe uma mensagem com o número da tentativa atual
        print("Senha incorreta. Tentativa {} de {}".format(tentativa_atual, max_tentativas))
else:
    # Se o loop termina sem atingir o break, exibe uma mensagem indicando que o limite de tentativas foi atingido
    print("Limite de tentativas atingido. Acesso negado.")