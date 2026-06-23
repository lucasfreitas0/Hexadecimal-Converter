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


def converter(base_origem, base_destino, valor): #função pra usar os valores

    bases_para_conversao = [2, 8, 10, 16]

    try:

        decimal = int(
            valor,
            bases_para_conversao[base_origem - 1]
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

    except ValueError: #checa se algum valor foi colocado indevidamente

        if base_origem == 1:
          raise ValueError(
            "Binário aceita apenas 0 e 1."
        )

        elif base_origem == 2:
            raise ValueError(
            "Octal aceita apenas números de 0 a 7."
        )

        elif base_origem == 4:
            raise ValueError(
            "Hexadecimal aceita 0-9 e A-F."
            )
        elif base_origem == base_destino:
            raise ValueError(
                "São as mesmas bases"
        )
