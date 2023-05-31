def multiplicar_por_2(lista):
    nova_lista = []
    for numero in lista:
        print(numero)  # Imprime o número original
        multiplicado = numero * 2
        nova_lista.append(multiplicado)  # Adiciona o número multiplicado à nova lista
    return nova_lista

# Exemplo de uso
lista = [2, 3, 7, 12, 2]
lista_multiplicada = multiplicar_por_2(lista)

print("Lista original:", lista)
print("Lista multiplicada por 2:", lista_multiplicada)
