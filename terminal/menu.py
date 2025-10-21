from conexao import get_connection
from crud_jogo import menu_jogos
from crud_categoria import menu_categorias
from crud_plataforma import menu_plataformas

def menu_principal():
    con = get_connection()
    try:
        while True:
            print("\n===== SISTEMA DE GERENCIAMENTO =====")
            print("1. Gerenciar Jogos")
            print("2. Gerenciar Categorias")
            print("3. Gerenciar Plataformas")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                menu_jogos(con)
            elif opcao == "2":
                menu_categorias(con)
            elif opcao == "3":
                menu_plataformas(con)
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    finally:
        con.close()

# === EXECUÇÃO ===
if __name__ == "__main__":
    menu_principal()
