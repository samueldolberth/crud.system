from PyQt5 import uic, QtWidgets
from produto import Produto
from banco import conexao
from utils import gerar_pdf

numero_id = 0

# terminal: python -m unittest test_unitario test_integracao

def funcao_principal():
    nome = tela_cadastro.txtProduto.text()
    valor = tela_cadastro.txtValor.text()
    quantidade = tela_cadastro.txtQuantidade.text()

    produto = Produto(nome, valor, quantidade)
    produto.salvar()

    tela_cadastro.txtProduto.setText('')
    tela_cadastro.txtValor.setText('')
    tela_cadastro.txtQuantidade.setText('')

def chama_tela_listarDados():
    tela_listar.show()
    produtos = Produto.listar_todos()
    tela_listar.tableWidget.setRowCount(len(produtos))
    tela_listar.tableWidget.setColumnCount(4)

    for i, prod in enumerate(produtos):
        for j in range(4):
            tela_listar.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(prod[j])))

def excluir_dados():
    linha = tela_listar.tableWidget.currentRow()
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM produtos;")
    ids = cursor.fetchall()
    cursor.close()
    Produto.deletar_por_id(ids[linha][0])
    tela_listar.tableWidget.removeRow(linha)

def editar_dados():
    global numero_id
    linha = tela_listar.tableWidget.currentRow()
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM produtos;")
    ids = cursor.fetchall()
    cursor.close()

    numero_id = ids[linha][0]
    produto = Produto.buscar_por_id(numero_id)

    if produto:
        tela_editar.show()
        tela_editar.txtId.setText(str(produto.id))
        tela_editar.txtNome.setText(produto.nome)
        tela_editar.txtValor.setText(str(produto.valor))
        tela_editar.txtQuantidade.setText(str(produto.quantidade))

def salvar_dados_editados():
    global numero_id
    nome = tela_editar.txtNome.text()
    valor = tela_editar.txtValor.text()
    quantidade = tela_editar.txtQuantidade.text()

    produto = Produto(nome, valor, quantidade, numero_id)
    produto.atualizar()

    tela_editar.close()
    tela_listar.close()
    chama_tela_listarDados()

# PyQt5
app = QtWidgets.QApplication([])

tela_cadastro = uic.loadUi("ui/tela_cadastro.ui")
tela_listar = uic.loadUi("ui/tela_listarDados.ui")
tela_editar = uic.loadUi("ui/tela_editarDados.ui")

# Conexões de botões
tela_cadastro.btnEnviar.clicked.connect(funcao_principal)
tela_cadastro.btnListar.clicked.connect(chama_tela_listarDados)

tela_listar.btnPdf.clicked.connect(gerar_pdf)
tela_listar.btnExcluir.clicked.connect(excluir_dados)
tela_listar.btnEditar.clicked.connect(editar_dados)

tela_editar.btnSalvar.clicked.connect(salvar_dados_editados)

tela_cadastro.show()
app.exec()

conexao.close()
