import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
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
        
        if base_origem not in opcoes_menu or base_destino not in opcoes_menu:
            limpar_tela()
            print("Base de origem ou base de destino inválida, Tente novamente.")
            continue

        if base_origem == base_destino:
            print("A base de destino deve ser diferente da base de origem, Tente novamente.")
            continue

        limpar_tela()
        numero_digitado = input("Digite o número a ser convertido: ").upper()
        numero_decimal_base_destino = int(numero_digitado, bases_para_conversao[base_origem - 1])
        
    except ValueError:
        limpar_tela()
        print("Número inválido para a base de origem.\n")
        continue
    except Exception:
        limpar_tela()
        print('Erro desconhecido.\n')
        continue
    
        
    match(base_destino):
        case 1:                              
            numero_convertido_base_destino = bin(numero_decimal_base_destino)
        case 2:
            numero_convertido_base_destino = oct(numero_decimal_base_destino)
        case 3:
            numero_convertido_base_destino = numero_decimal_base_destino
        case 4:
            numero_convertido_base_destino = hex(numero_decimal_base_destino).upper()

    

    if isinstance(numero_convertido_base_destino, str):
        print(f"O número digitado na base de origem é: {numero_digitado} na base de destino é: {numero_convertido_base_destino[2:]}.")
    else:
        print(f"O número digitado na base de origem é: {numero_digitado} na base de destino é: {numero_convertido_base_destino}.")


    continuar_convertendo = input("Deseja realizar outra conversão? (s/n): ").lower()
    limpar_tela()
    validacao_true = continuar_convertendo == 'n' or continuar_convertendo == 'nao'
    if validacao_true:
        break
