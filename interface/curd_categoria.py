import customtkinter as ctk
from conexao import get_connection
from tkinter import messagebox

# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def menu_categorias():
    con = get_connection()

    # === JANELA PRINCIPAL ===
    janela = ctk.CTk()
    janela.title("🎮 Gerenciar Categorias")
    janela.geometry("650x500")

    titulo = ctk.CTkLabel(
        janela,
        text="📁 Gerenciar Categorias",
        font=("Arial", 20, "bold")
    )
    titulo.pack(pady=15)

    # === FRAME CAMPOS ===
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

    # === FUNÇÕES CRUD ===
    def atualizar_lista():
        cur = con.cursor()
        cur.execute("SELECT idcategoria, nome, descricao FROM categoria ORDER BY idcategoria")
        categorias = cur.fetchall()
        lista_categorias.delete("1.0", "end")
        for cat in categorias:
            lista_categorias.insert("end", f"ID: {cat[0]} | {cat[1]} - {cat[2]}\n")

    def cadastrar_categoria():
        nome = entry_nome.get()
        desc = entry_desc.get()

        if not nome:
            messagebox.showwarning("Aviso", "O campo 'Nome' é obrigatório.")
            return

        cur = con.cursor()
        sql = "INSERT INTO categoria (nome, descricao) VALUES (%s, %s)"
        cur.execute(sql, (nome, desc))
        con.commit()

        atualizar_lista()
        entry_nome.delete(0, "end")
        entry_desc.delete(0, "end")
        messagebox.showinfo("Sucesso", "✅ Categoria cadastrada com sucesso!")

    def excluir_categoria():
        selecionado = lista_categorias.get("insert linestart", "insert lineend")
        if not selecionado.strip():
            messagebox.showwarning("Aviso", "Selecione uma categoria na lista para excluir.")
            return

        idcategoria = selecionado.split(" | ")[0].replace("ID: ", "")
        cur = con.cursor()
        cur.execute("DELETE FROM categoria WHERE idcategoria=%s", (idcategoria,))
        con.commit()

        atualizar_lista()
        messagebox.showinfo("Sucesso", "🗑️ Categoria excluída com sucesso!")

    def editar_categoria():
        selecionado = lista_categorias.get("insert linestart", "insert lineend")
        if not selecionado.strip():
            messagebox.showwarning("Aviso", "Selecione uma categoria na lista para editar.")
            return

        idcategoria = selecionado.split(" | ")[0].replace("ID: ", "")
        novo_nome = entry_nome.get()
        nova_desc = entry_desc.get()

        if not novo_nome:
            messagebox.showwarning("Aviso", "Preencha o novo nome antes de editar.")
            return

        cur = con.cursor()
        sql = "UPDATE categoria SET nome=%s, descricao=%s WHERE idcategoria=%s"
        cur.execute(sql, (novo_nome, nova_desc, idcategoria))
        con.commit()

        atualizar_lista()
        entry_nome.delete(0, "end")
        entry_desc.delete(0, "end")
        messagebox.showinfo("Sucesso", "✅ Categoria atualizada com sucesso!")

    # === BOTÕES ===
    frame_botoes = ctk.CTkFrame(janela)
    frame_botoes.pack(pady=10)

    ctk.CTkButton(frame_botoes, text="Cadastrar", command=cadastrar_categoria).grid(row=0, column=0, padx=10)
    ctk.CTkButton(frame_botoes, text="Editar", command=editar_categoria).grid(row=0, column=1, padx=10)
    ctk.CTkButton(frame_botoes, text="Excluir", command=excluir_categoria).grid(row=0, column=2, padx=10)
    ctk.CTkButton(frame_botoes, text="Atualizar Lista", command=atualizar_lista).grid(row=0, column=3, padx=10)

    # === LISTA DE CATEGORIAS ===
    lista_categorias = ctk.CTkTextbox(janela, width=580, height=230)
    lista_categorias.pack(pady=10)

    # Primeira atualização
    atualizar_lista()

    # === BOTÃO VOLTAR ===
    ctk.CTkButton(janela, text="Voltar", command=janela.destroy).pack(pady=10)

    janela.mainloop()


# === EXECUÇÃO DIRETA ===
if __name__ == "__main__":
    menu_categorias()
