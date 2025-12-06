# weather.py
import os
import requests
from datetime import datetime, timedelta
from datetime import timezone

from dotenv import load_dotenv
load_dotenv()


OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not OPENWEATHER_API_KEY:
    raise SystemExit("Defina a variável de ambiente OPENWEATHER_API_KEY com sua chave da OpenWeatherMap.")

def get_current_weather(city: str, api_key: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "pt_br"}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Erro ao conectar com OpenWeatherMap: {e}")
    try:
        data = resp.json()
    except ValueError:
        raise ValueError("Resposta da API não é um JSON válido.")
    return data

def get_forecast(city: str, api_key: str, days=3):
    # endpoint 5 day / 3 hour forecast
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "pt_br"}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Erro ao buscar previsão: {e}")
    try:
        data = resp.json()
    except ValueError:
        raise ValueError("Resposta da API (forecast) não é um JSON válido.")
    # 'list' tem previsões a cada 3 horas; vamos agregar por dia (próximos N dias)
    now = datetime.now(timezone.utc)
    end = now + timedelta(days=days)
    daily = {}
    for item in data.get("list", []):
        dt = datetime.fromtimestamp(item["dt"], timezone.utc)
        if dt < now or dt > end:
            continue
        date_key = dt.date().isoformat()
        temps = daily.setdefault(date_key, [])
        temps.append(item["main"]["temp"])
    # reduzir para média por dia
    summary = []
    for date_key, temps in sorted(daily.items()):
        avg_temp = sum(temps) / len(temps)
        summary.append({"date": date_key, "avg_temp": round(avg_temp, 1)})
    return summary

def pretty_print_weather(city: str):
    try:
        current = get_current_weather(city, OPENWEATHER_API_KEY)
    except Exception as e:
        print("Erro:", e)
        return

    # Extrair campos relevantes com cuidado (verificando keys)
    name = current.get("name", city)
    sys = current.get("sys", {})
    country = sys.get("country", "")
    main = current.get("main", {})
    weather_arr = current.get("weather", [])
    weather_desc = weather_arr[0]["description"] if weather_arr else "N/D"
    temp = main.get("temp")
    feels_like = main.get("feels_like")
    humidity = main.get("humidity")
    wind = current.get("wind", {}).get("speed")

    print(f"\nClima atual em {name}{' - ' + country if country else ''}:")
    if temp is not None:
        print(f"  Temperatura: {temp} °C (sensação: {feels_like} °C)")
    else:
        print("  Temperatura: N/D")
    print(f"  Condição: {weather_desc}")
    print(f"  Umidade: {humidity}%")
    print(f"  Vento: {wind} m/s")

    # previsão
    try:
        forecast = get_forecast(city, OPENWEATHER_API_KEY, days=3)
    except Exception as e:
        print("Não foi possível obter previsão:", e)
        return

    if forecast:
        print("\nPrevisão (resumo dos próximos 3 dias):")
        for day in forecast:
            print(f"  {day['date']}: temperatura média ~ {day['avg_temp']} °C")
    else:
        print("\nPrevisão: dados não disponíveis.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        city = " ".join(sys.argv[1:])
    else:
        city = input("Digite a cidade (ex: São Paulo,BR ou London,UK): ").strip()
    if not city:
        print("Cidade vazia. Encerrando.")
    else:
        pretty_print_weather(city)
