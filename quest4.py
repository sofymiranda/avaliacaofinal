#leia um numero inteiro que represente um codigo de ddd para discagem interurbana. Em seguida informe a qual cidade o ddd pertence, considerando a tabela abaixo.
print("Descubra de onde é seu DDD\n")
# Solicita ao usuário que digite o número de telefone brasileiro
numero = int(input("Digite seu número de telefone (brasileiro). \nObs: Não utilize espaços ou sinais: "))
# Obtém os dois primeiros dígitos do número, que representam o DDD
ddd = int(str(numero)[:2])
# Dicionário de mapeamento de DDD para região
mapeamento_ddds = {
    61: "Brasília",
    71: "Salvador",
    11: "São Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitória",
    31: "Belo Horizonte"
}
# Verifica se o DDD está cadastrado e imprime a região correspondente
if ddd in mapeamento_ddds:
    print(mapeamento_ddds[ddd])
else:
    print("DDD não cadastrado")
