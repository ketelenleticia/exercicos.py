contador=1
def novo_perdido(cardapio):
     pedido={
     "id": contador,
     "itens": [],
     "total": 0, 
     }
     contador+=1
     print("adicione o item ao seu pedido")

     while True:
          pedido=[]
          id_item=int(input("digite um id: "))
          qtd=int(input("digite a quantidade: "))
          for c in cardapio:
               if c["id"]==id_item:
                    pedido["itens"].append({
                         'id':id_item,
                         'quantidade':qtd
                    })
                    pedido["total"]+=item["preço"]* qtd
                    return pedido
def calcular_total(pedido,cardapio):
     total=pedido["total"]
     if total> 50:
          total*=0.9
          print("a desconto")
     else:
          print("nao a desconto")

quantidade_total=sum(item["quantidd"])               

     
               
                    
                    




        
