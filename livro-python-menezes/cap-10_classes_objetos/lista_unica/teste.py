from listaunica import ListaUnica

lu = ListaUnica(int)
lu.adiciona(5)
lu.adiciona(3)
# lu.adiciona(2.5)
print(f"Tamanho original: {len(lu)} itens")

for elem in lu:
    print(elem)

lu.adiciona(5)
print(f"Tamanho depois de tentar add o 5: {len(lu)} itens")
print(f"Primeiro elemento: {lu[0]}")
print(f"Segundo elemento: {lu[1]}")
