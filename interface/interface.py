import customtkinter as ctk
from crud_jogos import menu_jogos
from curd_categoria import menu_categorias
from crud_plataforma import menu_plataformas

# ---------------- Configuração ----------------
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

# ---------------- Janela Principal ----------------
app = ctk.CTk()
app.title('Sistema de Gerenciamento')
app.geometry('400x400')

# ---------------- Título ----------------
titulo = ctk.CTkLabel(app, text='🎮 SISTEMA DE GERENCIAMENTO', font=('Arial', 16, 'bold'))
titulo.pack(pady=20)

# ---------------- Funções dos Botões ----------------
def abrir_jogos():
    app.withdraw()  # Esconde o menu principal
    menu_jogos()    # Abre o CRUD de jogos
    app.deiconify() # Mostra o menu novamente quando fechar o CRUD

def abrir_categorias():
    app.withdraw()
    menu_categorias()
    app.deiconify()

def abrir_plataformas():
    app.withdraw()
    menu_plataformas()
    app.deiconify()

def sair():
    app.destroy()

# ---------------- Botões ----------------
ctk.CTkButton(app, text='Gerenciar Jogos', command=abrir_jogos, width=200).pack(pady=10)
ctk.CTkButton(app, text='Gerenciar Categorias', command=abrir_categorias, width=200).pack(pady=10)
ctk.CTkButton(app, text='Gerenciar Plataformas', command=abrir_plataformas, width=200).pack(pady=10)
ctk.CTkButton(app, text='Sair', command=sair, fg_color='red', hover_color='#a83232', width=200).pack(pady=20)

# ---------------- Rodapé ----------------
rodape = ctk.CTkLabel(app, text='Escolha uma opção para gerenciar', font=('Arial', 12))
rodape.pack(pady=10)

# ---------------- Iniciar App ----------------
app.mainloop()
