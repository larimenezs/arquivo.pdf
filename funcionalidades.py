"""Funcionalidades que podem ser úteis:

- Inserir arquivo no meio do outro
- Quero colocar dentro do Resultado do 4T20 os destaques do 3T20 para poder comparar 
os 2 dentro do mesmo relatório."""
import PyPDF2 as pyf
from pathlib import Path

pdf_mesclado = pyf.PdfMerger()

pdf_mesclado.append("MGLU_ER_4T20_POR.pdf")
pdf_mesclado.merge(1, "paginas/Arquivo Pagina 1.pdf")

with Path(f"Relatório 2 Trimestres.pdf").open(mode="wb") as arquivo:
    pdf_mesclado.write(arquivo)


"""Rodar página do PDF
import PyPDF2 as pyf
from pathlib import Path

arquivo_pdf_original = pyf.PdfReader("MGLU_ER_3T20_POR.pdf")

novo_arquivo = pyf.PdfWriter()

for pagina in arquivo_pdf_original.pages:
    pagina.rotate(90)
    novo_arquivo.add_page(pagina)

with Path(f"Paginas Rotacionadas.pdf").open(mode="wb") as arquivo:
    novo_arquivo.write(arquivo)"""