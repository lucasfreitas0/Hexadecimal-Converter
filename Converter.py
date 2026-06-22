import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def mostrar_menu():
    print("Escolha a base:")
    print("1. Binário")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")

#converte o texto pra base de destino letra por letra
def texto_para_base(texto, base_destino):
    
    resultado = []

    for letra in texto:

        codigo = ord(letra)

        match base_destino:
            case 1:
                resultado.append(bin(codigo)[2:])
            case 2: 
                resultado.append(oct(codigo)[2:])
            case 4:
                resultado.append(hex(codigo)[2:].upper())

    return " ".join(resultado)

#converte o texto, letra por letra 
def base_para_texto(codigo, base_origem):
    resultado = ""

    for pedaco in codigo.split():

        match base_origem:
            case 1:
                decimal = int(pedaco, 2)
            case 2:
                decimal = int(pedaco, 8)
            case 4:
                decimal = int(pedaco, 16)

        resultado += chr(decimal)
    return resultado


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
            print("Base inválida")
            continue

        if base_origem == base_destino:
            print("As bases devem ser diferentes.")
            continue

        limpar_tela()
        valor = input("Digite o valor a ser convertido: ")

        try:
            decimal = int(
                valor,
                bases_para_conversao[base_origem -1]
            )
            match base_destino:
                case 1:
                    resultado = bin(decimal)[2:]
                case 2:
                    resultado = oct(decimal)[2:]
                case 3:
                    resultado = str(decimal)
                case 4:
                    resultado = hex(decimal)[2:].upper()

        except ValueError:
            #testa se tem texto para converter
            if base_origem == 3 and base_destino in [1, 2, 4]:
               resultado = texto_para_base(
                   valor,
                   base_destino
               )


            elif base_destino == 3 and base_origem in [1, 2, 4]:
                resultado = base_para_texto(
                    valor,
                    base_origem
                )
            
            else:
                print(
                    "Conversão de texto permitida apenas entre "
                    "Decimal e Binário/Octal/Hexadecimal."
                )
                continue
        
        print(
            f"\nValor de Origem: {valor}"
            f"\nResultado: {resultado}"
        )

        continuar = input(
            "\nDeseja realizar outra conversão? (s/n):"
            ).lower()
        
        limpar_tela()

        if continuar != "s":
            break

    except Exception as erro:
        limpar_tela()
        print(f"Erro: {erro}")