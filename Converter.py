import json
import os

def limparTela():
    os.system('cls')

def mostrarMenu(): 
    print("Escolha a base de origem:")
    print("1. Binário")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")



caminho_arquivo = 'Conversion-table.json'
tabela_conversao = {}
opcoes_bases = [1, 2, 3, 4]


print("Bem-vindo ao conversor de bases!\n")

while True:
    
    
    mostrarMenu()

    try:

        base_origem = int(input("Digite o número correspondente à base de origem: "))
        if base_origem not in opcoes_bases:
            print("Base de origem inválida. Tente novamente.")
            continue

        limparTela()
        mostrarMenu()

        base_destino = int(input("Digite o número correspondente à base de destino: "))
        if base_destino not in opcoes_bases:
            print("Base de destino inválida. Tente novamente.")
            continue

        limparTela()
        numero = int(input("Digite o número a ser convertido: "))
        if base_origem in opcoes_bases:
            numero_decimal = numero, [2, 8, 10, 16][base_origem - 1]
        else:
            print("Base de origem inválida.")
            
    except ValueError:
        limparTela()
        print("Número inválido para a base de origem.\n")
        continue
    except TypeError:
        limparTela()
        print('Erro: Entrada inválida.\n')
        continue
    except Exception:
        limparTela()
        print('Erro desconhecido.\n')
        continue
    
    match(base_destino):
        case 1:
            numero_convertido = bin(numero_decimal)
        case 2:
            numero_convertido = oct(numero_decimal)
        case 3:
            numero_convertido = str(numero_decimal)
        case 4:
            numero_convertido = hex(numero_decimal).upper()
        case _:
            print("Base de destino inválida")
            continue 

    print(f"O número {numero} na base de origem é {numero_convertido} na base de {base_destino}.")

    continuarConvertendo = input("Deseja realizar outra conversão? (s/n): ").lower()
    validacaoTrue = continuarConvertendo == 'n' or continuarConvertendo == 'nao'
    if validacaoTrue:
        break
