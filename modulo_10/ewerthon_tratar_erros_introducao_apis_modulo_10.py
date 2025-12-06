import requests

def buscar_previsao():
    cidade = input("Digite o nome da cidade: ")
    api_key = "c6b00ef98ca4e93e99dfe883fa0f1540"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    try:
        print("Buscando dados da API...")

        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()  # força erro se status não for 200

        dados = resposta.json()

        # Exibindo informações
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']

        print("\n✅ Dados do clima:")
        print(f"Cidade: {cidade}")
        print(f"Temperatura: {temperatura}ºC")
        print(f"Clima: {descricao}")

    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão. Verifique sua internet.")

    except requests.exceptions.Timeout:
        print("❌ A requisição demorou demais (timeout).")

    except requests.exceptions.HTTPError:
        print("❌ Erro HTTP. Cidade não encontrada ou API com problema.")

    except Exception as erro:
        print(f"❌ Ocorreu um erro inesperado: {erro}")

# Chamando a função
buscar_previsao()
