from py_scripts.utilidade import get_and_clean_df

def calculo():
    pedidos = {'geral': {'n_pessoas': 10}, 'Bovinos': ['Alcatra com Maminha Peça Inteira kg', 'Picanha Bovina Maturatta Peca Inteira kg'], 'Aves': [], 'Guarnições': ['Linguiça de Frango Seara kg', 'Linguiça Lombo c/Alho e Ervas Premium Aurora 500g'], 'Bebidas': ['Refrigerante Flexa Pet 2Lt Uva', 'Refrigerante Flexa Pet 2Lt Laranja', 'Água Mineral Natural Minalba 510ml'], 'Cervejas': ['Cerveja Orange Sunshine Hocus Pocus 500ml', 'Cerveja Caymmi Pilsner BackBone Grf 600ml']}
    n_pessoas = pedidos.pop("geral")["n_pessoas"]
    consumo_medio = {
        'Bovinos':0.3, # kg
        'Aves':0.3, # kg
        'Guarnições': 0.3, # kg
        'Bebidas': 300, # ml
        'Cervejas': 300 #ml
    }


    df_dict = get_and_clean_df(preco_Final_str=False)


    def calcular_item(tipo):
        """
        O consumo médio
        """
        df_tmp = df_dict[tipo][df_dict[tipo]["nome"].isin(pedidos[tipo])]
        df_tmp.rename(columns={"preco_final":"preco"}, inplace=True)
        print(df_tmp[tipo])
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
        f_dict[key] = calcular_item(tipo=key)

    return f_dict