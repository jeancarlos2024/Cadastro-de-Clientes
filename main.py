def mostrar_menu():
    print("\n=== MENU ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("0 - Sair")


def telefone_valido(telefone):
    telefone = telefone.strip()
    return telefone.isdigit() and len(telefone) >= 8


def telefone_existe(clientes, telefone):
    return any(c["telefone"] == telefone for c in clientes)


def cadastrar_cliente(clientes):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()

    if not nome:
        print("Erro: nome não pode ser vazio.")
        return

    if not telefone_valido(telefone):
        print("Erro: telefone inválido (mínimo 8 números).")
        return

    if telefone_existe(clientes, telefone):
        print("Erro: telefone já cadastrado.")
        return

    cliente = {
        "nome": nome,
        "telefone": telefone
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    print("\n--- CLIENTES ---")
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. Nome: {cliente['nome']} | Telefone: {cliente['telefone']}")


def buscar_cliente(clientes):
    termo = input("Digite o nome para buscar: ").strip().lower()

    if not termo:
        print("Digite algo para buscar.")
        return

    encontrados = [
        c for c in clientes
        if termo in c["nome"].lower()
    ]

    if not encontrados:
        print("Nenhum cliente encontrado.")
        return

    print("\n--- RESULTADOS ---")
    for cliente in encontrados:
        print(f"Nome: {cliente['nome']} | Telefone: {cliente['telefone']}")


def main() -> None:
    clientes = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            cadastrar_cliente(clientes)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            buscar_cliente(clientes)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()