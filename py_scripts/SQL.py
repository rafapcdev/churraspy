import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from web_scrapping import webscrapping_princesa
from pandas import read_sql, concat
from sqlite3 import connect
from datetime import date

def historico():
    conn = connect('Churrasquin.db')
    histo = read_sql('''SELECT nome, tipo, preco_final, data_extracao 
                     FROM Produtos ;''', conn)
    return histo

def tabela_hoje():
    conn = connect('Churrasquin.db')
    df = read_sql("select * from Produtos where data_extracao = strftime('%d/%m/%Y', DATE('now')) ", conn)
    return df

def atualizar():
    conn = connect('Churrasquin.db')
    df_sql = read_sql("select * from Produtos", conn)
    hoje = date.today().strftime("%d/%m/%Y")
    if df_sql["data_extracao"].max() == hoje:
        print("Banco Atualizado")
        pass
    if df_sql["data_extracao"].max() != hoje: 
        print("precisa atualizar")
        df_hoje = webscrapping_princesa()
        df_total = concat([df_hoje, df_sql], axis=0 ,ignore_index=True)
        df_total.to_sql("Produtos", conn, index= False, if_exists="replace")
        print("Banco Atualizado")

def carnes_bovinas():
    conn = connect('Churrasquin.db')
    carnes_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Bovinos' AND data_extracao = strftime('%d/%m/%Y', DATE('now')) ;", conn)
    carnes = carnes_df
    return carnes

def aves():
    conn = connect('Churrasquin.db')
    aves_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Aves' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    aves = aves_df
    return aves

def bitters():
    conn = connect('Churrasquin.db')
    bitters_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Bitters' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    bitters = bitters_df
    return bitters

def cervejas():
    conn = connect('Churrasquin.db')
    cervejas_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Cervejas' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    cervejas = cervejas_df
    return cervejas

def cervejas_puro_malte():
    conn = connect('Churrasquin.db')
    cervejas_Malte_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Cervejas Puro Malte' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    cervejas_m = cervejas_Malte_df
    return cervejas_m

def churrasco_e_cia():
    conn = connect('Churrasquin.db')
    churrasco_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Churrasco e Cia' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    churrass = churrasco_df
    return churrass

def cha_mate():
    conn = connect('Churrasquin.db')
    mate_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Chá / Mates' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    chazin = mate_df
    return chazin

def coca():
    conn = connect('Churrasquin.db')
    coca_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Coca Cola' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    coca_c = coca_df
    return coca_c

def destilados():
    conn = connect('Churrasquin.db')
    dest_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Destilados' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    destil = dest_df
    return destil

def frios():
    conn = connect('Churrasquin.db')
    frio_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Frios e outros' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    friozin = frio_df
    return friozin

def gin():
    conn = connect('Churrasquin.db')
    ginx_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Gin' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    ginzin = ginx_df
    return ginzin

def ice_drink():
    conn = connect('Churrasquin.db')
    ice_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Ice e Drinks' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    icezin = ice_df
    return icezin

def Isotonico():
    conn = connect('Churrasquin.db')
    Isoto_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Isotônicos e Energéticos' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    tonico = Isoto_df
    return tonico

def ofertas():
    conn = connect('Churrasquin.db')
    of_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Ofertas Sadia' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    ofertinhas = of_df
    return ofertinhas

def refrescos():
    conn = connect('Churrasquin.db')
    ref_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Refresco e sucos' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    sucos = ref_df
    return sucos

def refrigerante():
    conn = connect('Churrasquin.db')
    refri_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Refrigerante' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    gerante = refri_df
    return gerante

def utilidades():
    conn = connect('Churrasquin.db')
    uti_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Utilidades' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    lidades = uti_df
    return lidades

def vinho():
    conn = connect('Churrasquin.db')
    vin_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Vinhos Importados' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    vinhozin = vin_df
    return vinhozin

def vinho_espuma():
    conn = connect('Churrasquin.db')
    vinho_esp_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Vinhos e Espumantes' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    espuma = vinho_esp_df
    return espuma

def agua():
    conn = connect('Churrasquin.db')
    agu_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Águas' AND data_extracao = strftime('%d/%m/%Y', DATE('now'));", conn)
    aguinha = agu_df
    return aguinha