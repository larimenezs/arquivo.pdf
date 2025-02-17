"""2º Objetivo: Quero analisar o DRE (sem ajuste - Página 5)
    - Para ler tabelas em pdf, use o tabula (é ninja)"""
    

import tabula

tabelas = tabula.read_pdf("MGLU_ER_3T20_POR.pdf", pages=5)
df_resultado = tabelas[0]
# excluir linhas totalmente vazias
df_resultado = df_resultado.dropna(how="all", axis=0)
# excluir colunas totalmente vazias
df_resultado = df_resultado.dropna(how="all", axis=1)
df_resultado.columns = df_resultado.iloc[0]
df_resultado = df_resultado.iloc[1:]
df_resultado = df_resultado.reset_index(drop=True)
print(df_resultado)

print("----------------------------------------------------------------")
"""3º Objetivo: Quero analisar o Capital de Giro e os Investimentos (ambas as tabelas na página 12)
    - Páginas com mais de 1 tabela"""
tabelas = tabula.read_pdf("MGLU_ER_3T20_POR.pdf", pages=12)
for tabela in tabelas:
    tabela = tabela.dropna(how="all", axis=0)
    tabela = tabela.reset_index(drop=True)
    print(tabela)