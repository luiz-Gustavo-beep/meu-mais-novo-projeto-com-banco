import customtkinter as ctk
from tkinter import messagebox
from conexao import get_connection

# === CONFIGURAÇÃO INICIAL ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def menu_plataformas():
    con = get_connection()

    # === JANELA PRINCIPAL ===
    janela = ctk.CTk()
    janela.title("🎮 Gerenciar Plataformas")
    janela.geometry("650x500")

    titulo = ctk.CTkLabel(
        janela,
        text="📁 Gerenciar Plataformas",
        font=("Arial", 20, "bold")
    )
    titulo.pack(pady=15)

    # === FRAME DE CAMPOS ===
    frame_campos = ctk.CTkFrame(janela)
    frame_campos.pack(pady=10)

    label_nome = ctk.CTkLabel(frame_campos, text="Nome:")
    label_nome.grid(row=0, column=0, padx=10, pady=5)
    entry_nome = ctk.CTkEntry(frame_campos, width=300)
    entry_nome.grid(row=0, column=1, pady=5)

    label_desc = ctk.CTkLabel(frame_campos, text="Descrição:")
    label_desc.grid(row=1, column=0, padx=10, pady=5)
    entry_desc = ctk.CTkEntry(frame_campos, width=300)
    entry_desc.grid(row=1, column=1, pady=5)

    # === LISTA DE PLATAFORMAS ===
    lista_plataformas = ctk.CTkTextbox(janela, width=580, height=230)
    lista_plataformas.pack(pady=10)

    # === FUNÇÕES CRUD ===
    def atualizar_lista():
        cur = con.cursor()
        cur.execute("SELECT idplataforma, nome, descricao FROM plataforma ORDER BY idplataforma")
        plataformas = cur.fetchall()
        lista_plataformas.delete("1.0", "end")
        for plat in plataformas:
            lista_plataformas.insert("end", f"ID: {plat[0]} | {plat[1]} - {plat[2]}\n")

    def cadastrar_plataforma():
        nome = entry_nome.get().strip()
        desc = entry_desc.get().strip()

        if not nome:
            messagebox.showwarning("Aviso", "O campo 'Nome' é obrigatório.")
            return

        cur = con.cursor()
        sql = "INSERT INTO plataforma (nome, descricao) VALUES (%s, %s)"
        cur.execute(sql, (nome, desc))
        con.commit()

        atualizar_lista()
        entry_nome.delete(0, "end")
        entry_desc.delete(0, "end")
        messagebox.showinfo("Sucesso", "✅ Plataforma cadastrada com sucesso!")

    def editar_plataforma():
        selecionado = lista_plataformas.get("insert linestart", "insert lineend")
        if not selecionado.strip():
            messagebox.showwarning("Aviso", "Selecione uma plataforma na lista para editar.")
            return

        idplataforma = selecionado.split(" | ")[0].replace("ID: ", "")
        novo_nome = entry_nome.get().strip()
        nova_desc = entry_desc.get().strip()

        if not novo_nome:
            messagebox.showwarning("Aviso", "Preencha o novo nome antes de editar.")
            return

        cur = con.cursor()
        sql = "UPDATE plataforma SET nome=%s, descricao=%s WHERE idplataforma=%s"
        cur.execute(sql, (novo_nome, nova_desc, idplataforma))
        con.commit()

        atualizar_lista()
        entry_nome.delete(0, "end")
        entry_desc.delete(0, "end")
        messagebox.showinfo("Sucesso", "✅ Plataforma atualizada com sucesso!")

    def excluir_plataforma():
        selecionado = lista_plataformas.get("insert linestart", "insert lineend")
        if not selecionado.strip():
            messagebox.showwarning("Aviso", "Selecione uma plataforma na lista para excluir.")
            return

        idplataforma = selecionado.split(" | ")[0].replace("ID: ", "")

        confirmar = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir esta plataforma?")
        if not confirmar:
            return

        cur = con.cursor()
        cur.execute("DELETE FROM plataforma WHERE idplataforma=%s", (idplataforma,))
        con.commit()

        atualizar_lista()
        messagebox.showinfo("Sucesso", "🗑️ Plataforma excluída com sucesso!")

    # === BOTÕES ===
    frame_botoes = ctk.CTkFrame(janela)
    frame_botoes.pack(pady=10)

    ctk.CTkButton(frame_botoes, text="Cadastrar", command=cadastrar_plataforma).grid(row=0, column=0, padx=10)
    ctk.CTkButton(frame_botoes, text="Editar", command=editar_plataforma).grid(row=0, column=1, padx=10)
    ctk.CTkButton(frame_botoes, text="Excluir", command=excluir_plataforma).grid(row=0, column=2, padx=10)
    ctk.CTkButton(frame_botoes, text="Atualizar Lista", command=atualizar_lista).grid(row=0, column=3, padx=10)

    # === BOTÃO VOLTAR ===
    ctk.CTkButton(janela, text="Voltar", command=janela.destroy).pack(pady=10)

    # === PRIMEIRA ATUALIZAÇÃO ===
    atualizar_lista()

    janela.mainloop()


# === EXECUÇÃO DIRETA ===
if __name__ == "__main__":
    menu_plataformas()
