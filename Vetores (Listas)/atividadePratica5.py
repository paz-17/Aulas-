lista = []

while True:
    addItem = input("Adicione um item: ")
    lista.append(addItem)

    if addItem == 'fim':
        break
    lista.append(addItem)

    print(f"o tamanho da minha lista é: {len(lista)} ")
