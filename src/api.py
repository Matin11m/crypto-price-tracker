import requests
import json

def get_crypto_price(coin):
    """دریافت قیمت لحظه‌ای یک ارز دیجیتال."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # بررسی وضعیت کد HTTP (خطاها)
        data = response.json()
        price = data[coin]['usd']
        return price
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    except (KeyError, TypeError): # مدیریت خطای وقتی که کوین پیدا نشه یا داده به فرمت مورد انتظار نباشه
        return "Coin not found"

def get_historical_price(coin, days=30):
    """دریافت داده‌های تاریخی قیمت یک ارز دیجیتال."""
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