"""2º Objetivo: Com o Release de Resultados já separado página por página,
 queremos incluir apenas as Páginas de Destaque (Página 1), DRE (Página 14) e 
 Balanço (Página 16).

    - Juntar vários pdfs em 1"""
import PyPDF2 as pyf
from pathlib import Path

num_paginas = [1, 14, 16]

novo_arquivo = pyf.PdfWriter()
for num in num_paginas:
    pagina_pdf = pyf.PdfReader(f"paginas/Arquivo Pagina {num}.pdf") #cria um novo pdf
    novo_arquivo.add_page(pagina_pdf.pages[0]) #add esta pág em outro arquivo pdf

    
with Path(f"Consolidado.pdf").open(mode="wb") as arquivo:
    novo_arquivo.write(arquivo) #salva