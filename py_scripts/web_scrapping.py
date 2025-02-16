from requests import get
from bs4 import BeautifulSoup
from json import loads
from pandas import DataFrame
from datetime import date
from re import search
from typing import List

def request_data(product:str = ["carnes", "bebidas"], keys = List[str]) -> dict | None:
    items = {key:[] for key in keys}

    if product == "carnes":
        url_base = "https://www.princesasupermercados.com.br/marica-1/destaque/churrasco?page="
    else:
        url_base = "https://www.princesasupermercados.com.br/marica-1/bebidas-1572?page="

    for i in range(1,20):
        print(f"capturando dados da seção {product}, pagina: {i}")
        
        url = url_base + str(i)
        res = get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        scripts = soup.find_all("script")
        script = scripts[-2]

        text = script.text
        text = text[text.find("(") + 1 : len(text) - 1]
        json_data = loads(text)

        try:
            tmp = json_data[1]
            text = search(r"(\[.*)", tmp)
            json_data = loads(text.group())
        
            products_item = json_data[1][3]["children"]
            for list_items in products_item:
                items["nome"].append(list_items[3]["product"]["name"])
                items["preco"].append(list_items[3]["product"]["price"])
                items["preco_desconto"].append(list_items[3]["product"]["priceWithDiscount"])
                items["tipo"].append(list_items[3]["product"]["department"])
                items["url_imagem"].append(list_items[3]["product"]["image"])

        except:
            print(f"\tNão há dados na seção {product}, pagina: {i}.\n\tFinalizando a captura de dados para seçao {product}")
            break   
    
    return items if items[keys[0]] else None

def webscrapping_princesa() -> DataFrame:

    items = {
        "nome": [],
        "preco": [],
        "preco_desconto": [],
        "tipo":[],
        "url_imagem": []
    }

    keys = list(items.keys())

    items_tmp = request_data("carnes", keys)

    if items_tmp:
        [items[key].extend(items_tmp[key]) for key in keys]
    
    items_tmp = request_data("bebidas", keys)

    if items_tmp:
        [items[key].extend(items_tmp[key]) for key in keys]

    df = DataFrame(items)
    df["preco_final"] = df.apply(lambda row: row["preco_desconto"] if row["preco_desconto"] > 0 else row["preco"], axis=1)
    df.drop(["preco", "preco_desconto"], axis=1, inplace=True)
    df["data_extracao"] = date.today().strftime("%d/%m/%Y")

    return df