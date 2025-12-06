import requests

def clima():
    cidade = input("Digite o nome da cidade: ")
    api_key = "c6b00ef98ca4e93e99dfe883fa0f1540"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    resposta = requests.get(url)
    dados = resposta.json()

    # Filtrando e exibindo dados específicos
    temperatura = dados['main']['temp']
    sensacao = dados['main']['feels_like']
    umidade = dados['main']['humidity']
    clima = dados['weather'][0]['description']

    print("\n🌤️  Informações do Clima:")
    print(f"Cidade: {cidade}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Sensação térmica: {sensacao}°C")
    print(f"Umidade do ar: {umidade}%")
    print(f"Condição climática: {clima}")

# Chamando a função
clima()
