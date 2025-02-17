#Trabalhando com textos e informações dentro de um pdf

"""1º Objetivo: Quero identificar como foram as Despesas com Vendas da MGLU
    - Pegar texto da página e identificar onde está essa informação"""
import PyPDF2 as pyf
from pathlib import Path

arquivo = pyf.PdfReader("MGLU_ER_3T20_POR.pdf")

qtde_paginas = len(arquivo.pages)
print(qtde_paginas)

metadados_arquivo = arquivo.metadata
print(metadados_arquivo)

texto_referencia = "| Despesas com Vendas"

for i, pagina in enumerate(arquivo.pages):
    texto_pagina = pagina.extract_text()
    if texto_referencia in texto_pagina:
        print("Numero Pagina: ", i+1)
        texto_analisar = texto_pagina
        print(texto_analisar)

posicao_inicial = texto_analisar.find(texto_referencia)
posicao_final = texto_analisar.find("|", posicao_inicial + 1)

texto_final = texto_analisar[posicao_inicial:posicao_final]
print(texto_final)