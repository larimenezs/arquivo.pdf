""" O que fazer quando o tabula não consegue ler alguma linha da tabela? 
Como o cabeçalho, no nosso caso?"""

import tabula
tabelas = tabula.read_pdf("MGLU_ER_3T20_POR.pdf", pages=12)

df_capitalgiro = tabelas[0]
df_capitalgiro = df_capitalgiro.dropna(how="all", axis=0)
df_capitalgiro = df_capitalgiro.reset_index(drop=True)
# display(df_capitalgiro)
tabelas2 = tabula.read_pdf("MGLU_ER_3T20_POR.pdf", pages=12, lattice=True)
df_capitalgiro2 = tabelas2[0]
df_capitalgiro2 = df_capitalgiro2.dropna(how="all", axis=0)
df_capitalgiro2 = df_capitalgiro2.dropna(how="all", axis=1)
df_capitalgiro2 = df_capitalgiro2.reset_index(drop=True)
colunas = df_capitalgiro2.iloc[0]
colunas = colunas.dropna()
df_capitalgiro.columns = colunas
print(df_capitalgiro)