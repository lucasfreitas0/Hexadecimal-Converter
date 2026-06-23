import os

def texto_para_base(texto, base_destino): # ele lê letra por letra pra transformar em numero

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


def base_para_texto(codigo, base_origem): # aqui faz o processo inverso

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


def converter(base_origem, base_destino, valor):

    bases_para_conversao = [2, 8, 10, 16]

    # SE AS BASES FOREM IGUAIS
    if base_origem == base_destino:
        raise ValueError("A base de origem e destino são as mesmas.")

    try:
        # 1. Tenta converter como NÚMERO PURO primeiro
        decimal = int(
            valor,
            bases_para_conversao[base_origem -1]
        )

        match base_destino:
            case 1:
                return bin(decimal)[2:]
            case 2:
                return oct(decimal)[2:]
            case 3:
                return str(decimal)
            case 4:
                return hex(decimal)[2:].upper()

    except ValueError:
        # 2. Se falhar como número, significa que pode ser TEXTO/ASCII
        
        # Se a origem for Decimal (3), significa que é um texto normal (Ex: "Ola")
        # que quer ser transformado nos códigos das outras bases
        if base_origem == 3:
            return texto_para_base(valor, base_destino)
            
        # Se a origem for outra base (1, 2 ou 4), significa que é uma sequência 
        # de códigos (Ex: "01000001 01000010") querendo voltar a ser texto
        elif base_destino == 3:
            try:
                return base_para_texto(valor, base_origem)
            except Exception:
                raise ValueError("Formato de código inválido para conversão em texto.")
                
        # 3. Se não cair em nenhum dos casos de texto, aí sim valida os erros de digitação
        else:
            if base_origem == 1:
                raise ValueError("Binário aceita apenas 0, 1 e espaços.")
            elif base_origem == 2:
                raise ValueError("Octal aceita apenas números de 0 a 7 e espaços.")
            elif base_origem == 4:
                raise ValueError("Hexadecimal aceita 0-9, A-F e espaços.")