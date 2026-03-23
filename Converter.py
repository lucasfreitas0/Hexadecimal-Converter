import sysconfig
from os import system


def limpar_tela():
    platform_id = sysconfig.get_platform()
    system('cls') if platform_id == 'win-amd64' else system('clear')
    
def mostrar_menu(): 
    print("Escolha a base:") 
    print("1. Binário")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")


opcoes_menu = [1, 2, 3, 4]
bases_para_conversao = [2, 8, 10, 16]


print("Bem-vindo ao conversor de bases!\n")

while True:
    
    

    try:

        mostrar_menu()
        base_origem = int(input("Digite o número correspondente à base de origem: "))

        limpar_tela()
        mostrar_menu()
        base_destino = int(input("Digite o número correspondente à base de destino: "))
        
        if base_origem or base_destino not in opcoes_menu:
            limpar_tela()
            print("Base de origem ou base de destino inválida, Tente novamente.")
            continue

        limpar_tela()
        numero_digitado = input("Digite o número a ser convertido: ")
        numero_decimal = int(numero_digitado, bases_para_conversao[base_origem - 1])
         
    except ValueError:
        limpar_tela()
        print("Número inválido para a base de origem.\n") # tirar esse except e por no case da base_origem se possivel (n sei se da)
        continue
    except Exception:
        limpar_tela()
        print('Erro desconhecido.\n')
        continue
    
    match(base_origem):
        case 1:
            numero_decimal = int(numero_digitado, 2)
        case 2:
            numero_decimal = int(numero_digitado, 8)
        case 3:
            numero_decimal = int(numero_digitado, 10)
        case 4:
            numero_decimal = int(numero_digitado, 16)
        
    match(base_destino):
        case 1:                              
            numero_convertido = bin(numero_decimal) # ok
        case 2:
            numero_convertido = oct(numero_decimal) # ok
        case 3:
            numero_convertido = numero_decimal # ok
        case 4:
            numero_convertido = hex(numero_decimal).upper() # ok


    if isinstance(numero_convertido, str):
        print(f"O número {numero_digitado} na base de destino é {numero_convertido[2:]}.")
    else:
        print(f"O número {numero_digitado} na base de destino é {numero_convertido}.")


    continuar_convertendo = input("Deseja realizar outra conversão? (s/n): ").lower()
    limpar_tela()
    validacao_true = continuar_convertendo == 'n' or continuar_convertendo == 'nao'
    if validacao_true:
        break
