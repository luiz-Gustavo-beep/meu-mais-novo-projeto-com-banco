from conexao import get_connection

# === INSERIR ===
def adicionar_categoria(con):
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    
    cur = con.cursor()
    sql = """
        INSERT INTO categoria (nome, descricao)
        VALUES (%s, %s)
    """
    cur.execute(sql, (nome, descricao))
    con.commit()
    print("\n✅ Categoria cadastrada com sucesso!")

# === LISTAR ===
def listar_categoria(con):
    cur = con.cursor()
    sql = """
        SELECT idcategoria, nome, descricao
        FROM categoria
        ORDER BY idcategoria
    """
    cur.execute(sql)
    categorias = cur.fetchall()

    print("\n🎮 Lista de categorias:")
    print("-" * 60)
    for categoria in categorias:
        print(f"ID: {categoria[0]} | Nome: {categoria[1]} | Descrição: {categoria[2]}")
    print("-" * 60)

# === EDITAR ===
def editar_categoria(con):
    listar_categoria(con)
    idcategoria = input("\nDigite o ID da categoria que deseja editar: ")

    novo_nome = input("Novo nome: ")
    nova_descricao = input("Nova descrição: ")

    cur = con.cursor()
    sql = """
        UPDATE categoria
        SET nome=%s, descricao=%s
        WHERE idcategoria=%s
    """
    cur.execute(sql, (novo_nome, nova_descricao, idcategoria))
    con.commit()
    print("\n✅ Categoria atualizada com sucesso!")

# === EXCLUIR ===
def excluir_categoria(con):
    listar_categoria(con)
    idcategoria = input("\nDigite o ID da categoria que deseja excluir: ")

    cur = con.cursor()
    sql = "DELETE FROM categoria WHERE idcategoria=%s"
    cur.execute(sql, (idcategoria,))
    con.commit()
    print("\n🗑️ Categoria excluída com sucesso!")

# === MENU ===
def menu_categorias(con):
    while True:
        print("\n===== GERENCIAR CATEGORIAS =====")
        print("1. Cadastrar categorias")
        print("2. Listar categorias")
        print("3. Editar categorias")
        print("4. Excluir categorias")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_categoria(con)
        elif opcao == "2":
            listar_categoria(con)
        elif opcao == "3":
            editar_categoria(con)
        elif opcao == "4":
            excluir_categoria(con)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")

# === EXECUÇÃO DIRETA ===
if __name__ == "__main__":
    con = get_connection()
    try:
        menu_categorias(con)
    finally:
        con.close()
