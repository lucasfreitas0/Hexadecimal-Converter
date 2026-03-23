import json
from os import system
import sysconfig

def limparTela():
    platform_id = sysconfig.get_platform();
    system('cls') if platform_id == 'win' else system('clear')

def mostrarMenu(): 
    print("Escolha a base de origem:") 
    print("1. Binário")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")



caminho_arquivo = 'Conversion-table.json'
tabela_conversao = {}
opcoes_menu = [1, 2, 3, 4]
bases_para_conversao = [2, 8, 10, 16]


print("Bem-vindo ao conversor de bases!\n")

while True:
    
    mostrarMenu()

    try:


        base_origem = int(input("Digite o número correspondente à base de origem: "))
        limparTela()
        mostrarMenu()
        base_destino = int(input("Digite o número correspondente à base de destino: "))
        
        if base_origem  not in opcoes_menu or base_destino not in opcoes_menu:
            print("Base de origem ou base de destino inválida, Tente novamente.")
            continue

        limparTela()
        numero = input("Digite o número a ser convertido: ")
        if base_origem in opcoes_menu:
            numero_decimal = int(numero, bases_para_conversao[base_origem - 1]) # O número decimal ta recebendo mais de um valor. Aqui tem que passar um valor só.
        else:
            print("Base de origem inválida.")
            
    except ValueError:
        limparTela()
        print("Número inválido para a base de origem.\n")
        continue
    except Exception:
        limparTela()
        print('Erro desconhecido.\n')
        continue
    
    #match para base origem
    match(base_destino):
        case 1:                              
            numero_convertido = bin(numero_decimal) # ok
        case 2:
            numero_convertido = oct(numero_decimal) # ok
        case 3:
            numero_convertido = numero_decimal # ok
        case 4:
            numero_convertido = hex(numero_decimal).upper() # ok
        case _:
            print("Base de destino inválida")
            continue 
    if isinstance(numero_convertido, str):
        print(f"O número {numero} na base de destino é {numero_convertido[2:]}.")
    else:
        print(f"O número {numero} na base de destino é {numero_convertido}.")


    continuarConvertendo = input("Deseja realizar outra conversão? (s/n): ").lower()
    limparTela()
    validacaoTrue = continuarConvertendo == 'n' or continuarConvertendo == 'nao'
    if validacaoTrue:
        break
