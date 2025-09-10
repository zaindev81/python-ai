import argparse
from src.data import fetch_history

def main():
    parser = argparse.ArgumentParser(description="Fetch historical stock data")
    parser.add_argument("--ticker", type=str, default="AAPL", help="Stock ticker symbol")
    parser.add_argument("--period", type=str, default="1mo", help="Time period for historical data")

    args = parser.parse_args()
    ticker_symbol = args.ticker
    period = args.period

    if not ticker_symbol:
        print("Please provide a valid ticker symbol using --ticker")
        return

    if not period:
        print("Please provide a valid period using --period")
        return

    print("Fetching data for:", ticker_symbol, "Period:", period)

    # Creates a Ticker object for the given stock symbol.
    # ticker = yf.Ticker(ticker_symbol)
    # print("Ticker Info:", ticker.info)

    # Fetches historical market data for the specified period.
    # data = ticker.history(period)
    # print(data)

    history = fetch_history(ticker_symbol, period=args.period)
    print("history", history)

    # .iloc is a Pandas feature that lets you select rows and columns
    # in a DataFrame by position (index numbers), not by labels.
    print("Latest Close Price:", history["Close"].iloc[-1])
    print("Latest High Price:", history["High"].iloc[-1])
    print("Latest Low Price:", history["Low"].iloc[-1])


if __name__ == "__main__":
    main()