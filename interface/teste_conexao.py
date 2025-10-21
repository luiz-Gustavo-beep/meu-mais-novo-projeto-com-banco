from conexao import get_connection

try:
    conexao = get_connection()
    if conexao.is_connected():
        print("✅ Conexão com o MySQL bem-sucedida!")
        print("Banco de dados conectado:", conexao.database)
    conexao.close()
except Exception as e:
    print("❌ Erro ao conectar ao MySQL:", e)
