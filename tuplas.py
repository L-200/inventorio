pão = ("pão", 2, 20)
sabonete = ("sabonete", 5, 10)
chocolate = ("chocolate", 6, 6)
lista = [pão, sabonete, chocolate]
novo_pro_nome = input()
novo_pro_preco = float(input())
novo_pro_quant = int(input())
novo_pro = (novo_pro_nome, novo_pro_preco, novo_pro_quant)
lista.append(novo_pro)
print("Lista com o produto adicionado: ", lista)
print("Qual dos 4 itens deseja remover? ")
removido = int(input())
del(lista[removido])
print("Lista com um produto removido: ", lista)
valor = pão[2] + chocolate[2] + novo_pro[2]
print("Valor do inventário: ", valor)