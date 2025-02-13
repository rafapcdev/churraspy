from py_scripts.web_scrapping import webscrapping_princesa
from pandas import read_sql, concat
from sqlite3 import connect
from datetime import date
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(base_dir, 'Churrasquin.db')

def historico():
    conn = connect(db_path)
    histo = read_sql('''SELECT nome, tipo, preco_final, data_extracao 
                     FROM Produtos ;''', conn)
    return histo

def tabela_hoje():
    conn = connect(db_path)
    df = read_sql("select * from Produtos where data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime')) ", conn)
    return df

def deletar_hoje():
    conn = connect(db_path)
    df_sql = read_sql("select * from Produtos", conn)

def atualizar():
    conn = connect(db_path)
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
    conn = connect(db_path)
    carnes_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Bovinos' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime')) ;", conn)
    carnes = carnes_df
    return carnes

def aves():
    conn = connect(db_path)
    aves_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Aves' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    aves = aves_df
    return aves

def bitters():
    conn = connect(db_path)
    bitters_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Bitters' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    bitters = bitters_df
    return bitters

def cervejas():
    conn = connect(db_path)
    cervejas_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Cervejas' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    cervejas = cervejas_df
    return cervejas

def cervejas_puro_malte():
    conn = connect(db_path)
    cervejas_Malte_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Cervejas Puro Malte' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    cervejas_m = cervejas_Malte_df
    return cervejas_m

def churrasco_e_cia():
    conn = connect(db_path)
    churrasco_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Churrasco e Cia' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    churrass = churrasco_df
    return churrass

def cha_mate():
    conn = connect(db_path)
    mate_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Chá / Mates' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    chazin = mate_df
    return chazin

def coca():
    conn = connect(db_path)
    coca_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Coca Cola' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    coca_c = coca_df
    return coca_c

def destilados():
    conn = connect(db_path)
    dest_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Destilados' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    destil = dest_df
    return destil

def frios():
    conn = connect(db_path)
    frio_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Frios e outros' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    friozin = frio_df
    return friozin

def gin():
    conn = connect(db_path)
    ginx_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Gin' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    ginzin = ginx_df
    return ginzin

def ice_drink():
    conn = connect(db_path)
    ice_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Ice e Drinks' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    icezin = ice_df
    return icezin

def Isotonico():
    conn = connect(db_path)
    Isoto_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Isotônicos e Energéticos' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    tonico = Isoto_df
    return tonico

def ofertas():
    conn = connect(db_path)
    of_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Ofertas Sadia' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    ofertinhas = of_df
    return ofertinhas

def refrescos():
    conn = connect(db_path)
    ref_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Refresco e sucos' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    sucos = ref_df
    return sucos

def refrigerante():
    conn = connect(db_path)
    refri_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Refrigerante' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    gerante = refri_df
    return gerante

def utilidades():
    conn = connect(db_path)
    uti_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Utilidades' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    lidades = uti_df
    return lidades

def vinho():
    conn = connect(db_path)
    vin_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Vinhos Importados' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    vinhozin = vin_df
    return vinhozin

def vinho_espuma():
    conn = connect(db_path)
    vinho_esp_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Vinhos e Espumantes' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    espuma = vinho_esp_df
    return espuma

def agua():
    conn = connect(db_path)
    agu_df = read_sql("SELECT * FROM Produtos WHERE tipo = 'Águas' AND data_extracao = strftime('%d/%m/%Y', DATE('now', 'localtime'));", conn)
    aguinha = agu_df
    return aguinha

