from banco import conexao

class Produto:
    def __init__(self, nome, valor, quantidade, id=None):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

    @staticmethod
    def listar_todos():
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos;")
        produtos = cursor.fetchall()
        cursor.close()
        return produtos

    def salvar(self):
        cursor = conexao.cursor()
        comando = "INSERT INTO produtos (nome, valor, quantidade) VALUES (%s, %s, %s);"
        cursor.execute(comando, (self.nome, self.valor, self.quantidade))
        conexao.commit()
        cursor.close()

    @staticmethod
    def buscar_por_id(produto_id):
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos WHERE id = %s;", (produto_id,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            return Produto(resultado[1], resultado[2], resultado[3], resultado[0])
        return None

    def atualizar(self):
        cursor = conexao.cursor()
        comando = "UPDATE produtos SET nome = %s, valor = %s, quantidade = %s WHERE id = %s;"
        cursor.execute(comando, (self.nome, self.valor, self.quantidade, self.id))
        conexao.commit()
        cursor.close()

    @staticmethod
    def deletar_por_id(produto_id):
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s;", (produto_id,))
        conexao.commit()
        cursor.close()
