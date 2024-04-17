estoque = {"maçã": 10, "banana": 15, "laranja": 20, "uva": 12}
venda1_nome = (input("qual o produto vendido? "))
venda1_quant = int(input("quantas foram vendidas? "))
estoque[venda1_nome] -= venda1_quant
print("Venda de ", venda1_quant, venda1_nome+"s", " realizada com sucesso")
venda2_nome = (input("qual o produto vendido? "))
venda2_quant = int(input("quantas foram vendidas? "))
estoque[venda2_nome] -= venda2_quant
print("Venda de",venda2_quant, venda2_nome"s", realizada com sucesso")
venda3_nome = (input("qual o produto vendido? "))
venda3_quant = int(input("quantas foram vendidas? "))
estoque[venda3_nome] -= venda3_quant
print("Venda de ", venda3_quant, venda3_nome+"s", "realizada com sucesso")
venda4_nome = (input("qual o produto vendido? "))
venda4_quant = int(input("quantas foram vendidas? "))
estoque[venda4_nome] -= venda4_quant
print("Venda de ", venda4_quant, venda4_nome+"a", " realizada com sucesso")
print("Estoque atualizado: maçã: ", estoque["maçã"])
print("banana ", estoque["banana"])
print("laranja: ", estoque["laranja"])
print("uva: ", estoque["uva"])