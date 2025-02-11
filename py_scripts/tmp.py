from py_scripts.utilidade import get_and_clean_df


df_dict = get_and_clean_df()

for key in df_dict.keys():
   df_dict[key]["preco_final"] = df_dict[key]["preco_final"].apply(lambda row: str(row).replace(".",","))