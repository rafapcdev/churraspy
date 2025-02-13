from requests import get
from bs4 import BeautifulSoup
from json import loads
from pandas import DataFrame
from datetime import date
from re import search

def get_data_script_with_id(url):
    global items 
    soup = BeautifulSoup(url, "html.parser")
    script = soup.find("script", {"id": "__NEXT_DATA__"})
    json_data = loads(script.text)

    lista_produtos = json_data["props"]["pageProps"]["products"]
    if lista_produtos == []:
        return 0
    
    for produto in lista_produtos:
        items["nome"].append(produto["name"])
        items["preco"].append(produto["price"])
        items["preco_desconto"].append(produto["priceWithDiscount"])
        items["tipo"].append(produto["department"])
        items["url_imagem"].append(produto["image"])

    return 1

def get_data_script_without_id(url):
    global items
    soup = BeautifulSoup(url, "html.parser")
    scripts = soup.find_all("script")
    script = scripts[-2]

    text = script.text
    text = text[text.find("(") + 1 : len(text) - 1]
    json_data = loads(text)

    tmp = json_data[1]
    text = search(r"(\[.*)", tmp)
    if not text:
        return 0
    
    json_data = loads(text.group())
    
    products_item = json_data[1][3]["children"]

    for list_items in products_item:
        items["nome"].append(list_items[3]["product"]["name"])
        items["preco"].append(list_items[3]["product"]["price"])
        items["preco_desconto"].append(list_items[3]["product"]["priceWithDiscount"])
        items["tipo"].append(list_items[3]["product"]["department"])
        items["url_imagem"].append(list_items[3]["product"]["image"])
        
    return 1



def carnes():
    global items
    for i in range(1,20):
        print(i)
        
        url = f"https://www.princesasupermercados.com.br/marica-1/destaque/churrasco?page={str(i)}"
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
            break

def bebidas():
    global items
    for i in range(1,20):
        print(i)
        
        url = f"https://www.princesasupermercados.com.br/marica-1/bebidas-1572?page={str(i)}"
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
            break

def web_scrapping_items(url):
    global items
    for i in range(1,100):
        url = url + str(i)
        val = get_data_script_without_id(url)
        if val == 0:
            break
        
        
def webscrapping_princesa():
    global items

    items = {
        "nome": [],
        "preco": [],
        "preco_desconto": [],
        "tipo":[],
        "url_imagem": []
    }

    #web_scrapping_items("https://www.princesasupermercados.com.br/marica-1/destaque/churrasco?page=")
    #web_scrapping_items("https://www.princesasupermercados.com.br/marica-1/bebidas-1572?page=")
    carnes()
    bebidas()


    df = DataFrame(items)
    df["preco_final"] = df.apply(lambda row: row["preco_desconto"] if row["preco_desconto"] > 0 else row["preco"], axis=1)
    df.drop(["preco", "preco_desconto"], axis=1, inplace=True)
    df["data_extracao"] = date.today().strftime("%d/%m/%Y")
    #df.to_excel("saidas/test2.xlsx", index=False)

    return df