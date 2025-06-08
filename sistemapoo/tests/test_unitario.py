import unittest
from unittest.mock import MagicMock, patch
from produto import Produto

class TestProduto(unittest.TestCase):
    
    @patch('produto.conexao')
    def test_salvar_produto(self, mock_conexao):

        print("Executando: teste unitario")
        
        mock_cursor = MagicMock()
        mock_conexao.cursor.return_value = mock_cursor

        produto = Produto(nome="unitario", valor="11.11", quantidade="111")

       
        produto.salvar()

        
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO produtos (nome, valor, quantidade) VALUES (%s, %s, %s);",
            ("unitario", "11.11", "111")
        )
        mock_conexao.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
