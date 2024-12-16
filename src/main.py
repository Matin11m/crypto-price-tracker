from src.api import get_crypto_price, get_historical_price
from src.plotting import plot_with_matplotlib, plot_with_plotly
#from src.utils import format_price (اگر فایل utils.py را داشتید)

def main():
    coin_name = input("Enter the cryptocurrency name (e.g., bitcoin): ").lower()
    price = get_crypto_price(coin_name)

    if isinstance(price, float):
      print(f"The current price of {coin_name.capitalize()} is: ${price}")
      #formatted_price = format_price(price) # مثال استفاده از تابع format_price
      #print(f"Formatted price: {formatted_price}")
    elif isinstance(price, str):
        print(price)
        return #اگر کوین پیدا نشد از تابع خارج شود

    historical_data = get_historical_price(coin_name, 30)

    if historical_data:
        plot_choice = input("Choose plot library (matplotlib/plotly): ").lower()
        if plot_choice == "matplotlib":
            plot_with_matplotlib(coin_name, historical_data)
        elif plot_choice == "plotly":
            plot_with_plotly(coin_name, historical_data)
        else:
            print("Invalid plot library choice.")

if __name__ == "__main__":
    main()