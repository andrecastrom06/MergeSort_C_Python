import random

def gerar_lista(tamanho):
    return [random.randint(0, 100000) for _ in range(tamanho)]

def salvar_lista_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        for numero in lista:
            f.write(f"{numero}\n")

def menu():
    print("Escolha o tamanho da lista:")
    print("1 - Pequena")
    print("2 - Média")
    print("3 - Grande")

    opcao = input("Opção: ")

    tamanhos = {
        "1": 1000,
        "2": 10000,
        "3": 20000
    }

    tamanho = tamanhos.get(opcao)
    if not tamanho:
        print("Opção inválida.")
        return

    lista = gerar_lista(tamanho)
    salvar_lista_em_arquivo(lista, "lista.txt")
    print(f"Lista com {tamanho} números gerada em 'lista.txt'.")

if __name__ == "__main__":
    menu()