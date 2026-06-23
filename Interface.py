import tkinter as tk
from tkinter import ttk
import Converter


def centralizar(janela, largura, altura): #ele calcula o tamanho da tela pra abrir o conversor centralizado

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    janela.geometry(
        f"{largura}x{altura}+{x}+{y}"
    )

janela = tk.Tk()
janela.title("Conversor de Bases")
centralizar(janela, 600, 400)

# Título
titulo = tk.Label(
    janela,
    text="Conversor de Bases",
    font=(16)
)
titulo.pack(pady=10)

# Entrada
tk.Label(
    janela,
    text="Digite o valor:"
).pack()

entrada = tk.Entry(
    janela,
    width=25
)
entrada.pack(pady=5)

# Base de origem
tk.Label(
    janela,
    text="Base de origem:"
).pack()

base_origem = ttk.Combobox(
    janela,
    values=[
        "Binário",
        "Octal",
        "Decimal",
        "Hexadecimal"
    ],
    state="readonly"
)

base_origem.pack(pady=5)

# Base de destino
tk.Label(
    janela,
    text="Base de destino:"
).pack()

base_destino = ttk.Combobox(
    janela,
    values=[
        "Binário",
        "Octal",
        "Decimal",
        "Hexadecimal"
    ],
    state="readonly"
)

base_destino.pack(pady=5)

# Resultado
label_resultado = tk.Label(
    janela,
    text="Resultado aparecerá aqui"
)

label_resultado.pack(pady=20)

bases = {
    "Binário": 1,
    "Octal": 2,
    "Decimal": 3,
    "Hexadecimal": 4
}


def converter_click(): #ele pega os valores e converte tudo no .py e só manda os resultados pra ca
    origem = bases[base_origem.get()]
    destino = bases[base_destino.get()]
    valor = entrada.get()

    try:

        valor = entrada.get()

        origem = bases[base_origem.get()]
        destino = bases[base_destino.get()]

        resultado = Converter.converter(
            origem,
            destino,
            valor
        )

        label_resultado.config(
            text=f"Resultado: {resultado}"
        )

    except Exception as erro:

        label_resultado.config(
            text=f"Erro: {erro}"
        )

# Botão
botao = tk.Button(
    janela,
    text="Converter",
    command=converter_click
)

botao.pack(pady=10)

janela.mainloop()