"""2º Objetivo: Com o Release de Resultados já separado página por página,
 queremos incluir apenas as Páginas de Destaque (Página 1), DRE (Página 14) e 
 Balanço (Página 16).

    - Juntar vários pdfs em 1"""
import PyPDF2 as pyf
from pathlib import Path

num_paginas = [1, 14, 16] #Define uma lista com os números das págs que deseja combinar

novo_arquivo = pyf.PdfWriter() #cria um novo arquivo pdf para colocar as 3 págs adicionadas
for num in num_paginas:
    pagina_pdf = pyf.PdfReader(f"paginas/Arquivo Pagina {num}.pdf") #Lê o arquivo PDF correspondente à página desejada
    novo_arquivo.add_page(pagina_pdf.pages[0]) #add pág no novo arquivo pdf

    
with Path(f"Consolidado.pdf").open(mode="wb") as arquivo:
    novo_arquivo.write(arquivo) #salva

#Extra: Para adicionar todas as páginas de 2 pdfs
"""pdf_mesclado = pyf.PdfMerger()

pdf_mesclado.append("MGLU_ER_3T20_POR.pdf")
pdf_mesclado.append("MGLU_ER_4T20_POR.pdf")

with Path(f"Mesclado.pdf").open(mode="wb") as arquivo:
    pdf_mesclado.write(arquivo)"""