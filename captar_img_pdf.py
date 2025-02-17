"""Captar imagem em um pdf
from pikepdf import Pdf, PdfImage

arquivo = Pdf.open("MGLU_ER_3T20_POR.pdf")

for pagina in arquivo.pages:
    for nome, imagem in pagina.images.items():
        imagem_salvar = PdfImage(imagem)
        imagem_salvar.extract_to(fileprefix=f"imagens/{nome}")"""
