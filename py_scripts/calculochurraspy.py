
# Função para mostrar as carnes disponíveis
#def mostrar_carnes_disponiveis():
 #   return ['Alcatra', 'Picanha', 'Patinho', 'Lagarto', 'Fígado']

import SQL

# Função para calcular a quantidade média de carne por pessoa
def calcular_quantidade_carnes(carnes_escolhidas, num_pessoas):
    media_por_pessoa = 0.3

    quantidade_carne = {}
    for carne in carnes_escolhidas:
        quantidade_carne[carne] = media_por_pessoa[carne] * num_pessoas

    return quantidade_carne

#def mostrar_bebidas_disponiveis():
    #return ['Coca-cola', 'Pepsi', 'Cerveja', 'Uisque', 'Agua de coco']

def calcular_quantidade_bebida(bebida_escolhidas, num_pessoas):
    media_por_pessoa = 0.4

    quantidade_bebida = {}
    for bebida in bebida_escolhidas:
        quantidade_bebida[bebida] = media_por_pessoa[bebida] * num_pessoas

    return quantidade_bebida

# Função para calcular e exibir os resultados na interface
def calcular_churrasco():
    try:
        num_pessoas = int(entry_pessoas.get())
        if num_pessoas <= 0:
            raise ValueError("O número de pessoas deve ser maior que 0.")

        carnes_escolhidas = []
        for i, carne in enumerate(carnes_disponiveis):
            if carne_vars[i].get():
                carnes_escolhidas.append(carne)

        if not carnes_escolhidas:
            raise ValueError("Você precisa selecionar pelo menos uma carne.")

        # Calculando a quantidade de carne necessária
        quantidades = calcular_quantidade_carnes(carnes_escolhidas, num_pessoas)

        resultado_texto = "Resumo do seu churrasco:\n\n"
        for carne, quantidade in quantidades.items():
            preco, mercado = buscar_preco(carne)
            resultado_texto += f"{carne}:\n"
            resultado_texto += f"  Quantidade necessária: {quantidade:.2f} kg\n"
            resultado_texto += f"  Preço por kg: R${preco:.2f}\n"
            resultado_texto += f"  Melhor preço encontrado no: {mercado}\n"
            resultado_texto += f"  Total para {carne}: R${preco * quantidade:.2f}\n\n"

        resultado_label.config(text=resultado_texto)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))






