from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from django.contrib import admin
from .models import Produto

class ProdutoModelTest(TestCase):
    def test_str_representation(self):
        p = Produto.objects.create(
            nome="Caneca Teste",
            descricao="Uma caneca para testes",
            preco=Decimal("19.90"),
            quantidade=5
        )
        self.assertIn("Caneca Teste", str(p))  # __str__ deve conter o nome

    def test_create_product_values(self):
        p = Produto.objects.create(
            nome="Bola",
            descricao="Bola de futebol",
            preco=Decimal("49.99"),
            quantidade=10
        )
        self.assertEqual(Produto.objects.count(), 1)
        self.assertEqual(p.preco, Decimal("49.99"))
        self.assertEqual(p.quantidade, 10)


class ProdutoViewsTest(TestCase):
    def setUp(self):
        # cria um produto inicial
        self.produto = Produto.objects.create(
            nome="Camiseta",
            descricao="Camiseta branca",
            preco=Decimal("39.90"),
            quantidade=3
        )

    def test_lista_produtos_status_e_template(self):
        url = reverse('lista_produtos')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # verifica se template contém o nome do produto
        self.assertContains(resp, "Camiseta")

    def test_criar_produto_via_post(self):
        url = reverse('criar_produto')
        data = {
            'nome': 'Shorts',
            'descricao': 'Shorts azul',
            'preco': '29.50',
            'quantidade': '7'
        }
        resp = self.client.post(url, data, follow=True)
        # deve redirecionar para a lista de produtos e criar o registro
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Produto.objects.filter(nome='Shorts').exists())
        self.assertContains(resp, 'Shorts')

    def test_editar_produto_via_post(self):
        url = reverse('editar_produto', args=[self.produto.id])
        data = {
            'nome': 'Camiseta EDITADA',
            'descricao': 'Descrição editada',
            'preco': '49.99',
            'quantidade': '6'
        }
        resp = self.client.post(url, data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, 'Camiseta EDITADA')
        self.assertEqual(self.produto.quantidade, 6)
        self.assertContains(resp, 'Camiseta EDITADA')

    def test_excluir_produto(self):
        url = reverse('excluir_produto', args=[self.produto.id])
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Produto.objects.filter(id=self.produto.id).exists())


class ProdutoAdminRegistrationTest(TestCase):
    def test_produto_is_registered_in_admin(self):
        # Verifica se Produto está registrado no admin
        self.assertIn(Produto, admin.site._registry)
