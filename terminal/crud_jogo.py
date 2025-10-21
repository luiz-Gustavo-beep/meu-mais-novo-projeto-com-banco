from conexao import get_connection

# === Cadastrar um novo jogo ===
def cadastrar_jogo(con):
    titulo = input("Título: ")
    data_lancamento = input("Data de lançamento (YYYY-MM-DD): ")
    desenvolvedor = input("Desenvolvedor: ")
    imagem_capa = input("Imagem da capa (nome ou URL): ")

    cur = con.cursor()
    sql = """
        INSERT INTO jogo (titulo, data_lancamento, desenvolvedor, imagem_capa)
        VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (titulo, data_lancamento, desenvolvedor, imagem_capa))
    con.commit()
    print("\n✅ Jogo cadastrado com sucesso!")


# === Listar todos os jogos ===
def listar_jogos(con):
    cur = con.cursor()
    sql = """
        SELECT idjogo, titulo, data_lancamento, desenvolvedor, imagem_capa
        FROM jogo
        ORDER BY idjogo
    """
    cur.execute(sql)
    jogos = cur.fetchall()

    print("\n🎮 Lista de Jogos:")
    print("-" * 60)
    for jogo in jogos:
        print(f"ID: {jogo[0]} | Título: {jogo[1]} | Lançamento: {jogo[2]} | "
              f"Desenvolvedor: {jogo[3]} | Capa: {jogo[4]}")
    print("-" * 60)


# === Editar jogo existente ===
def editar_jogo(con):
    listar_jogos(con)
    idjogo = input("\nDigite o ID do jogo que deseja editar: ")

    novo_titulo = input("Novo título: ")
    nova_data = input("Nova data (YYYY-MM-DD): ")
    novo_desenvolvedor = input("Novo desenvolvedor: ")
    nova_imagem = input("Nova imagem: ")

    cur = con.cursor()
    sql = """
        UPDATE jogo
        SET titulo=%s, data_lancamento=%s, desenvolvedor=%s, imagem_capa=%s
        WHERE idjogo=%s
    """
    cur.execute(sql, (novo_titulo, nova_data, novo_desenvolvedor, nova_imagem, idjogo))
    con.commit()
    print("\n✅ Jogo atualizado com sucesso!")


# === Excluir jogo ===
def excluir_jogo(con):
    listar_jogos(con)
    idjogo = input("\nDigite o ID do jogo que deseja excluir: ")

    cur = con.cursor()
    sql = "DELETE FROM jogo WHERE idjogo=%s"
    cur.execute(sql, (idjogo,))
    con.commit()
    print("\n🗑️ Jogo excluído com sucesso!")


# === Menu de gerenciamento ===
def menu_jogos(con):
    while True:
        print("\n===== GERENCIAR JOGOS =====")
        print("1. Cadastrar jogo")
        print("2. Listar jogos")
        print("3. Editar jogo")
        print("4. Excluir jogo")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_jogo(con)
        elif opcao == "2":
            listar_jogos(con)
        elif opcao == "3":
            editar_jogo(con)
        elif opcao == "4":
            excluir_jogo(con)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")


# === Execução direta (teste rápido) ===
if __name__ == "__main__":
    con = get_connection()
    try:
        menu_jogos(con)
    finally:
        con.close()