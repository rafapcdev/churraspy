from py_scripts.SQL import carnes_bovinas, aves, churrasco_e_cia, frios, refrigerante, cervejas
from pandas import DataFrame,concat
from pandas.errors import SettingWithCopyWarning
from warnings import filterwarnings
from re import search
from json import loads
from py_scripts import members_path

# Silenciar todos os avisos do pandas

def filtrar_lt_ml(row) -> bool:
    pattern = r"\d+\s?(lt|ml)"
    val = search(pattern, row.lower())
    if val:
        return True
    else: 
        return False



def get_and_clean_df(preco_Final_str:bool = False) -> dict:
    filterwarnings('ignore', category=SettingWithCopyWarning)


    df_carnes = concat([carnes_bovinas(),aves()], axis=0)
    df_guarnicoes = concat([ churrasco_e_cia() , frios()], axis=0)

    df_dict = {key.replace(" ", "-"):df_carnes.loc[df_carnes["tipo"] == key] for key in df_carnes["tipo"].unique().tolist()}
    df_dict["Guarnições"] = df_guarnicoes
    df_dict["Refrigerantes"] = refrigerante()
    df_dict["Cervejas"] = cervejas()

    if preco_Final_str:
        for key in df_dict.keys():
        # Ensure the values are strings and apply the replacement
            df_dict[key]["preco_final"] = df_dict[key]["preco_final"].apply(lambda row: str(row).replace(".", ","))


    df_dict["Refrigerantes"] = df_dict["Refrigerantes"][df_dict["Refrigerantes"]["nome"].apply(filtrar_lt_ml)]
    df_dict["Cervejas"] = df_dict["Cervejas"][df_dict["Cervejas"]["nome"].apply(filtrar_lt_ml)]


    return df_dict


def get_members() -> DataFrame:

    with open(members_path, "r") as file:
        members = loads(file.read())

    df = DataFrame(members)

    front = df[df["department"].apply(lambda department: True  if search("Front-End", department) else False)].sort_values("name")
    back = df[df["department"].apply(lambda department: True  if search("Back-End", department) else False)].sort_values("name")
    webscrapping = df[df["department"] == "WebScrapping"].sort_values("name")
    manager = df[df["department"] == "Product Manager"].sort_values("name")
    leader = df[df["department"] == "Tech Leader"].sort_values("name")
    final_df = concat([front, back, webscrapping, manager, leader], axis=0 ,ignore_index=True)
    return final_df