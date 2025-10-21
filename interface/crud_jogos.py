import customtkinter as ctk
from conexao import get_connection

# ---------------- Configuração inicial ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def menu_jogos():
    con = get_connection()

    janela = ctk.CTkToplevel()
    janela.title("Gerenciar Jogos")
    janela.geometry("600x500")

    titulo = ctk.CTkLabel(janela, text="🎮 Gerenciar Jogos", font=("Arial", 20, "bold"))
    titulo.pack(pady=15)

    # ---------------- FRAME DE CAMPOS ----------------
    frame_campos = ctk.CTkFrame(janela)
    frame_campos.pack(pady=10)

    label_titulo = ctk.CTkLabel(frame_campos, text="Título:")
    label_titulo.grid(row=0, column=0, padx=10, pady=5)
    entry_titulo = ctk.CTkEntry(frame_campos, width=250)
    entry_titulo.grid(row=0, column=1, pady=5)

    label_data = ctk.CTkLabel(frame_campos, text="Data (YYYY-MM-DD):")
    label_data.grid(row=1, column=0, padx=10, pady=5)
    entry_data = ctk.CTkEntry(frame_campos, width=250)
    entry_data.grid(row=1, column=1, pady=5)

    label_desenvolvedor = ctk.CTkLabel(frame_campos, text="Desenvolvedor:")
    label_desenvolvedor.grid(row=2, column=0, padx=10, pady=5)
    entry_desenvolvedor = ctk.CTkEntry(frame_campos, width=250)
    entry_desenvolvedor.grid(row=2, column=1, pady=5)

    label_imagem = ctk.CTkLabel(frame_campos, text="Imagem/Capa:")
    label_imagem.grid(row=3, column=0, padx=10, pady=5)
    entry_imagem = ctk.CTkEntry(frame_campos, width=250)
    entry_imagem.grid(row=3, column=1, pady=5)

    # ---------------- FUNÇÕES CRUD ----------------
    def cadastrar_jogo():
        titulo = entry_titulo.get()
        data = entry_data.get()
        dev = entry_desenvolvedor.get()
        img = entry_imagem.get()

        cur = con.cursor()
        sql = """
            INSERT INTO jogo (titulo, data_lancamento, desenvolvedor, imagem_capa)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(sql, (titulo, data, dev, img))
        con.commit()
        atualizar_lista()
        ctk.CTkLabel(janela, text="✅ Jogo cadastrado com sucesso!").pack(pady=5)

        # limpa os campos
        entry_titulo.delete(0, "end")
        entry_data.delete(0, "end")
        entry_desenvolvedor.delete(0, "end")
        entry_imagem.delete(0, "end")

    def excluir_jogo():
        selecionado = lista_jogos.get()
        if not selecionado:
            return

        id_jogo = selecionado.split(" | ")[0].replace("ID: ", "")
        cur = con.cursor()
        sql = "DELETE FROM jogo WHERE idjogo=%s"
        cur.execute(sql, (id_jogo,))
        con.commit()
        atualizar_lista()

    def atualizar_lista():
        cur = con.cursor()
        cur.execute("SELECT idjogo, titulo, desenvolvedor FROM jogo ORDER BY idjogo")
        jogos = cur.fetchall()
        lista_jogos.delete(0, "end")
        for jogo in jogos:
            lista_jogos.insert("end", f"ID: {jogo[0]} | {jogo[1]} ({jogo[2]})")

    # ---------------- BOTÕES ----------------
    frame_botoes = ctk.CTkFrame(janela)
    frame_botoes.pack(pady=10)

    ctk.CTkButton(frame_botoes, text="Cadastrar", command=cadastrar_jogo).grid(row=0, column=0, padx=10)
    ctk.CTkButton(frame_botoes, text="Excluir", command=excluir_jogo).grid(row=0, column=1, padx=10)
    ctk.CTkButton(frame_botoes, text="Atualizar Lista", command=atualizar_lista).grid(row=0, column=2, padx=10)

    # ---------------- LISTA DE JOGOS ----------------
    lista_jogos = ctk.CTkTextbox(janela, width=500, height=200)
    lista_jogos.pack(pady=15)

    # Primeira atualização da lista
    atualizar_lista()

    # ---------------- FECHAR ----------------
    ctk.CTkButton(janela, text="Voltar", command=janela.destroy).pack(pady=10)

    janela.mainloop()


