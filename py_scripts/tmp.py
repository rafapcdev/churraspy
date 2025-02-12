from py_scripts.utilidade import get_and_clean_df
from re import search, match, findall

pedidos = {'geral': {'n_pessoas': 10}, 'Bovinos': ['Alcatra com Maminha Peça Inteira kg', 'Picanha Bovina Maturatta Peca Inteira kg'], 'Aves': [], 'Guarnições': ['Linguiça de Frango Seara kg', 'Linguiça Lombo c/Alho e Ervas Premium Aurora 500g'], 'Refrigerantes': ['Refrigerante Flexa Pet 2Lt Uva', 'Refrigerante Flexa Pet 2Lt Laranja', 'Água Mineral Natural Minalba 510ml'], 'Cervejas': ['Cerveja Orange Sunshine Hocus Pocus 500ml', 'Cerveja Caymmi Pilsner BackBone Grf 600ml']}
n_pessoas = pedidos.pop("geral")["n_pessoas"]
consumo_medio = {
    'Bovinos':0.3, # kg
    'Aves':0.3, # kg
    'Guarnições': 0.3, # kg
    'Bebidas': 0.3, # l
    'Cervejas': 0.3 # l
}


df_dict = get_and_clean_df(preco_Final_str=False)


def calcular_item(tipo):
    """
    O consumo médio
    """
    if not pedidos[tipo]:
        return None
    
    df_tmp = df_dict[tipo][df_dict[tipo]["nome"].isin(pedidos[tipo])]
    df_tmp.rename(columns={"preco_final":"preco"}, inplace=True)
    
    if tipo in ("Refrigerantes", "Cervejas"):
       pass 

    
    qtd_comprar = consumo_medio[tipo] * n_pessoas / df_tmp.shape[0]
    df_tmp = df_tmp.assign(preco_final= lambda row: row["preco"] * qtd_comprar)
    preco_total = sum(df_tmp["preco_final"])

    return {
                "df": df_tmp,
                "qtd_comprar": qtd_comprar,
                "preco_total": preco_total
    }   


f_dict = {}
for key in pedidos.keys():
    f_dict[key] = calcular_item(key)

print(f_dict)


"""
from py_scripts.utilidade import get_and_clean_df
from re import search, match, findall


pedidos = {'geral': {'n_pessoas': 10}, 'Bovinos': ['Alcatra com Maminha Peça Inteira kg', 'Picanha Bovina Maturatta Peca Inteira kg'], 'Aves': [], 'Guarnições': ['Linguiça de Frango Seara kg', 'Linguiça Lombo c/Alho e Ervas Premium Aurora 500g'], 'Refrigerantes': ['Refrigerante Flexa Pet 2Lt Uva', 'Refrigerante Flexa Pet 2Lt Laranja', 'Água Mineral Natural Minalba 510ml'], 'Cervejas': ['Cerveja Orange Sunshine Hocus Pocus 500ml', 'Cerveja Caymmi Pilsner BackBone Grf 600ml']}
n_pessoas = pedidos.pop("geral")["n_pessoas"]
consumo_medio = {
    'Bovinos':0.3, # kg
    'Aves':0.3, # kg
    'Guarnições': 0.3, # kg
    'Bebidas': 0.3, # l
    'Cervejas': 0.3 # l
}

df_dict = get_and_clean_df(preco_Final_str=False)


tipo = "Refrigerantes"
df_tmp = df_dict[tipo][df_dict[tipo]["nome"].isin(pedidos[tipo])]
df_tmp.rename(columns={"preco_final":"preco"}, inplace=True)


search(r"(\d+\s?(lt|ml))", df_tmp["nome"].to_list()[2].lower())

def capturar_volume(row):
    val = search(r"(\d+\s?(lt|ml))", row.lower()).group()
    return int(search(r"(\d+)", val).group())  if val.__contains__("lt") else int(search(r"(\d+)", val).group() ) / 1000

df_tmp["nome"].apply(capturar_volume)
df_tmp[df_tmp["nome"].str.contains(r"(\d+\s?(lt|ml))")]
"""
