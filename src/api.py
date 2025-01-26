import requests
import json


def get_crypto_price(coin):
    """
    Get the real-time price of a cryptocurrency.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data[coin]['usd']
        return price
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    except (KeyError, TypeError):  # Handle error when coin is not found or data is not in expected format
        return "Coin not found"


def get_historical_price(coin, days=30):
    """
    Get historical price data of a cryptocurrency.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days={days}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        prices = data['prices']
        return prices
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error parsing data: {e}")
        return None
