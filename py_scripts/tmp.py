from py_scripts.SQL import carnes_bovinas, aves, tabela_hoje
from py_scripts.utilidade import get_and_clean_df
from pandas import concat, DataFrame


conn = connect("churrasquin.db")
cursor = conn.cursor()
cursor.execute("select * from Produtos").fetchall()

df = get_and_clean_df()



for i, row in DataFrame(df).iterrows():
    print(row["nome"], row["url_imagem"])