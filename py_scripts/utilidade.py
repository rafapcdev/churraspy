from py_scripts.SQL import carnes_bovinas, aves, churrasco_e_cia, frios
from pandas import concat

def get_and_clean_df():
    df = concat([carnes_bovinas(),aves(),churrasco_e_cia(), frios()], axis=0)
    #df["nome"] = df["nome"].apply(lambda row: row.replace("kg","").strip())
    df['nome'] = df['nome'].str.replace('kg|peça inteira', '', regex=True).str.strip()

    df_dict = {key.replace(" ", "-"):df.loc[df["tipo"] == key] for key in df["tipo"].unique().tolist()}
    return df_dict

