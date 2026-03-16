import json

caminho_arquivo = 'Conversion-table.json'
tabela_conversao = {}

try:
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        # 1. Carregamos o arquivo
        conteudo = json.load(f)
        
        # 2. Se o seu JSON for uma lista de um único dicionário:
        if isinstance(conteudo, list) and len(conteudo) > 0:
            tabela_conversao = conteudo[0]
        else:
            tabela_conversao = conteudo
            
        print("Sucesso! O arquivo foi carregado.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro: O JSON está corrompido.")

simbolo_procurado = " "
encontrado = False

# 3. Agora tabela_conversao tem os dados reais
for id_chave, valores in tabela_conversao.items():
    if id_chave == "_comentario":
        continue
    
    # Verifique se 'valores' é realmente um dicionário antes de acessar ["simbolo"]
    if isinstance(valores, dict) and valores.get("simbolo") == simbolo_procurado:
        print(f"Símbolo '{simbolo_procurado}' achado no ID: {id_chave}")
        print(f"Detalhes: {valores}")
        encontrado = True
        break

if not encontrado:
    print(f"Símbolo '{simbolo_procurado}' não encontrado na tabela.")