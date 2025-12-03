pedido=[]
def novo_pedido(cardapio):
    id=int(input("digite ID do item: "))
    qtd=int(input("digite a quantidade: "))
    item=cardapio[id]

    for item in cardapio:
        if item["id"]==id:
            total=item["preço"] * qtd 

        pedido.append({
            "item":item["nome"],
            "qtd": qtd,
            "total": total
        })
    print("Seu pedido foi adicionado!")

    print("ID nao foi encontrado")
    return

def calcular_total(pedido,cardapio):
    total_geral=sum([item["total"] for item in pedido])
    if total_geral > 50:
        divisao=total_geral/10
        total=total_geral-divisao
        