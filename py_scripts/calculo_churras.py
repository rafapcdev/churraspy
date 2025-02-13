from py_scripts.utilidade import get_and_clean_df
from re import search
from math import ceil

def calculo_churrasco(pedidos):
    n_pessoas = int(pedidos.pop("geral")["n_pessoas"])
    consumo_medio = {
        'Bovinos':0.3, # kg
        'Aves':0.3, # kg
        'Guarnições': 0.3, # kg
        'Refrigerantes': 0.3, # l
        'Cervejas': 0.3 # l
    }


    df_dict = get_and_clean_df(preco_Final_str=False)

    def capturar_volume(row):
                val = search(r"(\d+\s?(lt|ml))", row.lower()).group()
                return int(search(r"(\d+)", val).group())  if val.__contains__("lt") else int(search(r"(\d+)", val).group() ) / 1000



    def calcular_item(tipo):
        """
        O consumo médio
        """
        if not pedidos[tipo]:
            return None
        
        df_tmp = df_dict[tipo][df_dict[tipo]["nome"].isin(pedidos[tipo])]
        df_tmp.rename(columns={"preco_final":"preco"}, inplace=True)
        
        if tipo in ("Refrigerantes", "Cervejas"):
            df_tmp["litros"] = df_tmp["nome"].apply(capturar_volume)

        
        qtd_comprar = consumo_medio[tipo] * n_pessoas / df_tmp.shape[0]
        qtd_comprar = qtd_comprar if qtd_comprar >= 1 else 1
        df_tmp = df_tmp.assign(preco_final= lambda row: round(row["preco"] * qtd_comprar,2))
        df_tmp["qtd_comprar"] = round(qtd_comprar,2)
        preco_total = sum(df_tmp["preco_final"])

        return {
                    "df": df_tmp,
                    "qtd_comprar": qtd_comprar,
                    "preco_total": preco_total
        }   


    f_dict = {}
    f_dict["preco_final"] = 0.0    
    for key in pedidos.keys():
        f_dict[key] = calcular_item(key)
        if f_dict[key]:
            f_dict["preco_final"] +=  f_dict[key]["preco_total"]

    f_dict["qtd_carvao"] = ceil(n_pessoas/20 )# 12 é o preço do saco de carvao
    f_dict["preco_carvao"] = 12 * f_dict["qtd_carvao"]  # 12 é o preço do saco de carvao
    f_dict['preco_final'] += f_dict["preco_carvao"]
    f_dict['preco_final'] = round(f_dict['preco_final'], 2)
    return f_dict

