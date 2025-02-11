from py_scripts.SQL import carnes_bovinas, aves, churrasco_e_cia, frios
from pandas import concat
from py_scripts.SQL import refrigerante, cervejas


def get_and_clean_df():
    df_carnes = concat([carnes_bovinas(),aves()], axis=0)
    df_bebidas = concat([ refrigerante() ,cervejas()], axis=0)
    df_guarnicoes = concat([ churrasco_e_cia() , frios()], axis=0)
    df_carnes['nome'] = df_carnes['nome'].str.replace('kg|peça inteira', '', regex=True).str.strip()

    df_dict = {key.replace(" ", "-"):df_carnes.loc[df_carnes["tipo"] == key] for key in df_carnes["tipo"].unique().tolist()}
    df_dict["Guarnições"] = df_guarnicoes
    df_dict["Bebidas"] = df_bebidas

    return df_dict

