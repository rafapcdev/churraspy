from requests import get
from bs4 import BeautifulSoup
from json import loads
from pandas import DataFrame
from datetime import date


def carne(page:int):
    global items

    url = f"https://www.princesasupermercados.com.br/marica-1/destaque/churrasco?page={str(page)}"
    res = get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    script = soup.find("script", {"id": "__NEXT_DATA__"})
    json_data = loads(script.text)
    lista_produtos = json_data["props"]["pageProps"]["products"]
    if lista_produtos == []:
        return None
    else:
        for produto in lista_produtos:
            items["nome"].append(produto["name"])
            items["preco"].append(produto["price"])
            items["preco_desconto"].append(produto["priceWithDiscount"])
            items["tipo"].append(produto["department"])
            items["url_imagem"].append(produto["image"])

        return 1

def bebidas(page: int):
    global items

    url2 = f"https://www.princesasupermercados.com.br/marica-1/bebidas-1572?page={str(page)}"
    res = get(url2)
    soup = BeautifulSoup(res.text, 'html.parser')
    script = soup.find("script", {"id": "__NEXT_DATA__"})
    json_data = loads(script.text)
    lista_produtos = json_data["props"]["pageProps"]["products"]
    if lista_produtos == []:
        return None
    else:
        for produto in lista_produtos:
            items["nome"].append(produto["name"])
            items["preco"].append(produto["price"])
            items["preco_desconto"].append(produto["priceWithDiscount"])
            items["tipo"].append(produto["department"])
            items["url_imagem"].append(produto["image"])

        return 1

def webscrapping_princesa():
    global items

    items = {
        "nome": [],
        "preco": [],
        "preco_desconto": [],
        "tipo":[],
        "url_imagem": []
    }

    for c in range(1,100):
        res = carne(c)
        if res == None:
            break

    for c in range(1, 100):
        res = bebidas(c)
        if res == None:
            break

    df = DataFrame(items)
    df["preco_final"] = df.apply(lambda row: row["preco_desconto"] if row["preco_desconto"] > 0 else row["preco"], axis=1)
    df.drop(["preco", "preco_desconto"], axis=1, inplace=True)
    df["data_extracao"] = date.today().strftime("%d/%m/%Y")
    #df.to_excel("saidas/test2.xlsx", index=False)

    return df



