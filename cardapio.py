def carregar_cardapio():
   cardapio=[
     {"id": 1, "nome": "Hambúrguer", "preco": 12.50},
     {"id": 2, "nome": "Batata Frita", "preco": 7.00},
     {"id": 3, "nome": "Refrigerante", "preco": 5.00}
    ]
   return cardapio

def exibir_cardapio():
   print(carregar_cardapio)
   return

def buscar_item(cardapio,id_item):
   