lista = []
nentradas = 0
nsaidas = 0
while True:
    livro = input()
    if livro == "pare":
        break
    else:
        nentradas += 1
        autor = input()
        ano = int(input())
        entrada = [livro, autor, ano]
        lista.append(entrada)
while nentradas != nsaidas:
    print("Titulo:", lista[nsaidas][0])
    print("Autor:", lista[nsaidas][1])
    print("Ano de Publicacao:", lista[nsaidas][2])
    nsaidas += 1