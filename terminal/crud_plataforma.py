from conexao import get_connection

# === INSERIR ===
def adicionar_plataforma(con):
    nome = input("Digite o nome: ")
    fabricante = input("Digite a fabricante: ")
    descricao = input("Digite a descrição: ")

    cur = con.cursor()
    sql = """
        INSERT INTO plataforma (nome, fabricante, descricao)
        VALUES (%s, %s, %s)
    """
    cur.execute(sql, (nome, fabricante, descricao))
    con.commit()
    print("\n✅ Plataforma cadastrada com sucesso!")

# === LISTAR ===
def listar_plataforma(con):
    cur = con.cursor()
    sql = """
        SELECT idplataforma, nome, fabricante, descricao
        FROM plataforma
        ORDER BY idplataforma
    """
    cur.execute(sql)
    plataformas = cur.fetchall()

    print("\n🎮 Lista de plataformas:")
    print("-" * 60)
    for p in plataformas:
        print(f"ID: {p[0]} | Nome: {p[1]} | Fabricante: {p[2]} | Descrição: {p[3]}")
    print("-" * 60)

# === EDITAR ===
def editar_plataforma(con):
    listar_plataforma(con)
    idplataforma = input("\nDigite o ID da plataforma que deseja editar: ")

    novo_nome = input("Novo nome: ")
    novo_fabricante = input("Novo fabricante: ")
    nova_descricao = input("Nova descrição: ")

    cur = con.cursor()
    sql = """
        UPDATE plataforma
        SET nome=%s, fabricante=%s, descricao=%s
        WHERE idplataforma=%s
    """
    cur.execute(sql, (novo_nome, novo_fabricante, nova_descricao, idplataforma))
    con.commit()
    print("\n✅ Plataforma atualizada com sucesso!")

# === EXCLUIR ===
def excluir_plataforma(con):
    listar_plataforma(con)
    idplataforma = input("\nDigite o ID da plataforma que deseja excluir: ")

    cur = con.cursor()
    sql = "DELETE FROM plataforma WHERE idplataforma=%s"
    cur.execute(sql, (idplataforma,))
    con.commit()
    print("\n🗑️ Plataforma excluída com sucesso!")

# === MENU ===
def menu_plataformas(con):
    while True:
        print("\n===== GERENCIAR PLATAFORMAS =====")
        print("1. Cadastrar plataforma")
        print("2. Listar plataformas")
        print("3. Editar plataforma")
        print("4. Excluir plataforma")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_plataforma(con)
        elif opcao == "2":
            listar_plataforma(con)
        elif opcao == "3":
            editar_plataforma(con)
        elif opcao == "4":
            excluir_plataforma(con)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")

# === EXECUÇÃO DIRETA ===
if __name__ == "__main__":
    con = get_connection()
    try:
        menu_plataformas(con)
    finally:
        con.close()
