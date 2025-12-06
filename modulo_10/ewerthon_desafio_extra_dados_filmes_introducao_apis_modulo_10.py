import requests

def buscar_filme():
    api_key = "c6b00ef98ca4e93e99dfe883fa0f1540"
    filme = input("Digite o nome do filme: ")

    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "language": "pt-BR",
        "query": filme
    }

    try:
        resposta = requests.get(url, params=params)
        resposta.raise_for_status()

        dados = resposta.json()

        if dados['results']:
            filme_encontrado = dados['results'][0]

            titulo = filme_encontrado['title']
            sinopse = filme_encontrado['overview']
            generos_ids = filme_encontrado['genre_ids']

            # Traduzindo os IDs dos gêneros
            generos_url = "https://api.themoviedb.org/3/genre/movie/list"
            generos_resp = requests.get(generos_url, params={
                "api_key": api_key,
                "language": "pt-BR"
            }).json()

            mapa_generos = {
                g['id']: g['name'] for g in generos_resp['genres']
            }

            generos_nomes = [mapa_generos.get(gid, "Desconhecido") for gid in generos_ids]

            print("\n🎬 Filme encontrado:")
            print(f"Título: {titulo}")
            print(f"Gêneros: {', '.join(generos_nomes)}")
            print(f"Sinopse: {sinopse}")

        else:
            print("❌ Nenhum filme encontrado.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a API: {e}")

# Chamando a função
buscar_filme()
