# test_api.py
import pytest
import json
from app import app # Importe a instância do seu aplicativo Flask

# 1. FIXTURE para o cliente de teste
@pytest.fixture
def client():
    """Cria um cliente de teste para simular requisições."""
    # Configura o Flask para modo de teste
    app.config['TESTING'] = True
    
    # Cria e retorna o cliente de teste
    with app.test_client() as client:
        yield client 

# 2. TESTE DE SUCESSO (Status 200)
def test_somar_sucesso(client):
    """Verifica se o endpoint de soma retorna o resultado correto e status 200."""
    # Simula o corpo da requisição POST
    dados_requisicao = {"a": 5, "b": 3}
    
    # Faz a requisição POST para a rota /calculadora/somar
    resposta = client.post(
        '/calculadora/somar',
        data=json.dumps(dados_requisicao),
        content_type='application/json'
    )
    
    # Verifica o código de status HTTP
    assert resposta.status_code == 200
    
    # Analisa o JSON da resposta
    dados_resposta = json.loads(resposta.data)
    
    # Verifica o resultado
    assert dados_resposta['resultado'] == 8.0


# 3. TESTE PARA ENTRADAS INVÁLIDAS (Status 400) - Similares ao Exercício 3
def test_somar_entrada_nao_numerica(client):
    """Verifica se entradas não numéricas retornam erro 400."""
    dados_requisicao = {"a": "dez", "b": 5}
    
    resposta = client.post(
        '/calculadora/somar',
        data=json.dumps(dados_requisicao),
        content_type='application/json'
    )
    
    # O teste DEVE falhar e retornar 400 (Bad Request)
    assert resposta.status_code == 400
    
    dados_resposta = json.loads(resposta.data)
    
    # Verifica se a mensagem de erro está correta
    assert "Ambos os inputs devem ser números." in dados_resposta['erro']

# 4. TESTE PARA REQUISIÇÃO MAL FORMADA (Status 400)
def test_somar_parametros_faltando(client):
    """Verifica se a ausência de um parâmetro ('b') retorna erro 400."""
    dados_requisicao = {"a": 5} # 'b' está faltando
    
    resposta = client.post(
        '/calculadora/somar',
        data=json.dumps(dados_requisicao),
        content_type='application/json'
    )
    
    assert resposta.status_code == 400
    
    dados_resposta = json.loads(resposta.data)
    assert "Requisição inválida. É necessário fornecer 'a' e 'b'." in dados_resposta['erro']