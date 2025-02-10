from SQL import carnes_bovinas, aves, tabela_hoje
from py_scripts.utilidade import carnes_bovinas, aves, churrasco_e_cia, frios
from pandas import concat



df = concat([carnes_bovinas(),aves(),churrasco_e_cia(), frios()], axis=0)
df["nome"] = df["nome"].apply(lambda row: row.replace("kg","").strip())
df_hoje = tabela_hoje()
