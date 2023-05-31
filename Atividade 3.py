def ordenar_por_ultima_letra(nome):
    return nome[-1]

def organizar_nomes(lista):
    # Ordenar em ordem alfabética padrão
    lista_alfabetica = sorted(lista)

    # Ordenar em ordem alfabética da última letra do nome "Inácio"
    lista_inacio = sorted(lista, key=ordenar_por_ultima_letra)

    return lista_alfabetica, lista_inacio

# Exemplo de uso
nomes = ["Inácio", "Lucas", "Maria", "Rafaela", "Ana"]
nomes_alfabetica, nomes_inacio = organizar_nomes(nomes)

print("Ordem alfabética padrão:", nomes_alfabetica)
print("Ordem alfabética da última letra do nome 'Inácio':", nomes_inacio)
