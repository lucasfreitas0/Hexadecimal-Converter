import json

caminho_arquivo = 'Conversion-table.json'
tabela_conversao = {}

# inicio do codigo
print("Bem-vindo ao conversor de bases!")
#loop para o menu de conversão
while True:
    print("Escolha a base de origem:")
    print("1. Binário\n2. Octal\n3. Decimal\n4. Hexadecimal")
    base_origem = int(input("Digite o número correspondente à base de origem: "))
    if base_origem not in [1, 2, 3, 4]:
        print("Base de origem inválida. Tente novamente.")
        break
    print("Escolha a base de destino:")
    print("1. Binário\n2. Octal\n3. Decimal\n4. Hexadecimal")
    base_destino = int(input("Digite o número correspondente à base de destino: "))
    if base_destino not in [1, 2, 3, 4]:
        print("Base de destino inválida. Tente novamente.")
        break
    numero = input("Digite o número a ser convertido: ")
#checagem se o numero escolhido está na base de origem correta
    if base_origem in [1, 2, 3, 4]:
        try:
            numero_decimal = int(numero, [2, 8, 10, 16][base_origem - 1])
        except ValueError:
            print("Número inválido para a base de origem.")
            break
    else:
        print("Base de origem inválida.")
    if base_destino == 1:
        numero_convertido = bin(numero_decimal)[2:]
    elif base_destino == 2:
        numero_convertido = oct(numero_decimal)[2:]
    elif base_destino == 3:
        numero_convertido = str(numero_decimal)
    elif base_destino == 4:
        numero_convertido = hex(numero_decimal)[2:].upper()
    else:
        print("Base de destino inválida.")
    print(f"O número {numero} na base de origem é {numero_convertido} na base de {base_destino}.")
    
    continuar = input("Deseja realizar outra conversão? (s/n): ")
    if continuar.lower() != 's':
        break
