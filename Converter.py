import json

caminho_arquivo = 'Conversion-table.json'
tabela_conversao = {}

try:
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        conteudo = json.load(f)
        
        if isinstance(conteudo, list) and len(conteudo) > 0:
            tabela_conversao = conteudo[0]
        else:
            tabela_conversao = conteudo
            
        print("Sucesso! O arquivo foi carregado.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro: O JSON está corrompido.")

# inicio do codigo
print("Bem-vindo ao conversor de bases!")

while True:
    print("Escolha a base de origem:")
    print("1. Binário\n2. Octal\n3. Decimal\n4. Hexadecimal")
    base_origem = int(input("Digite o número correspondente à base de origem: "))
    print("Escolha a base de destino:")
    print("1. Binário\n2. Octal\n3. Decimal\n4. Hexadecimal")
    base_destino = int(input("Digite o número correspondente à base de destino: "))
    numero = input("Digite o número a ser convertido: ")

    if base_origem == 1:
        try:
            numero_decimal = int(numero, 2)
        except ValueError:
            print("Número inválido para a base de origem.")
            continue
    elif base_origem == 2:
        try:
            numero_decimal = int(numero, 8)
        except ValueError:
            print("Número inválido para a base de origem.")
            continue
    elif base_origem == 3:
        try:
            numero_decimal = int(numero)
        except ValueError:
            print("Número inválido para a base de origem.")
            continue
    elif base_origem == 4:
        try:
            numero_decimal = int(numero, 16)
        except ValueError:
            print("Número inválido para a base de origem.")
            continue
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
    print(f"O número {numero} na base de origem é {numero_convertido} na base de destino.")
    continuar = input("Deseja realizar outra conversão? (s/n): ")
    if continuar.lower() != 's':
        break
