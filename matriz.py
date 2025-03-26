matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o múmero para a posição [{i}][{j}]: "))
        linha.append(numero)
    matriz.append(linha)
    
    
print("A matriz que você digitou foi: ")

for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]:4}", end=" ")
    print()
    
soma_primeira_coluna = 0

for i in range(3):
    soma_primeira_coluna += matriz[i][0]
print(f"A soma da primeira coluna é: {soma_primeira_coluna}")

produto_primeira_linha = 1 

for j in range(3):
    produto_primeira_linha *= matriz[0][j]
print(f"O produto dos elementos da primeira linha é: {produto_primeira_linha}")

soma_total = 0

for i in range(3):
    for j in range(3):
        soma_total += matriz[i][j]
print(f"A soma de todos os elementos da matriz é: {soma_total}")

soma_diagonal_principal = 0

for i in range(3):
    soma_diagonal_principal += matriz[i][i]
print(f"A soma da diagonal principal é: {soma_diagonal_principal}")