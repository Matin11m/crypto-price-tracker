import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd


def plot_with_matplotlib(coin_name, historical_data):
    """
    Plot chart with matplotlib.
    """
    if historical_data is None or not historical_data:
        print('No Historical Data Found')
        return
    df = pd.DataFrame(historical_data, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['price'])
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title(f'{coin_name.capitalize()} Price Chart')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_with_plotly(coin_name, historical_data):
    """
    Plot chart with Plotly.
    """
    if historical_data is None or not historical_data:
        print('No Historical Data Found')
        return
    df = pd.DataFrame(historical_data, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    fig = go.Figure(data=[go.Scatter(x=df['timestamp'], y=df['price'])])
    fig.update_layout(title=f'{coin_name.capitalize()} Price Chart',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)')
    fig.show()
