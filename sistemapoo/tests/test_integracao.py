import unittest
from produto import Produto

class TestProdutoIntegracao(unittest.TestCase):

    def test_deletar_produto_por_id(self):
        print("Executando: teste integracao")

        
        produto = Produto("teste integracao", "22.22", "222")
        produto.salvar()

        
        produtos = Produto.listar_todos()
        self.assertGreaterEqual(len(produtos), 1)
        produto_id = produtos[-1][0] 

        
        Produto.deletar_por_id(produto_id)

       
        produtos_restantes = Produto.listar_todos()
        ids_restantes = [p[0] for p in produtos_restantes]
        self.assertNotIn(produto_id, ids_restantes)

       
        produto_apagado = Produto.buscar_por_id(produto_id)
        self.assertIsNone(produto_apagado)
