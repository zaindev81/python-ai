import yfinance as yf
import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Fetch historical market data (multi-ticker)")
    parser.add_argument(
        "--tickers",
        nargs="+",
        help="Ticker symbols (space or comma separated). Example: AAPL MSFT TSLA  or  AAPL,MSFT,TSLA",
    )
    parser.add_argument("--period", type=str, default="1mo", help="Period (e.g. 1mo, 3mo, 1y)")
    parser.add_argument("--interval", type=str, default="1d", help="Data interval (e.g. 1m, 5m, 1d)")

    args = parser.parse_args()
    tickers = args.tickers
    period = args.period
    interval = args.interval

    data = yf.download(tickers, period=period, interval=interval)

    if data is None or (isinstance(data, pd.DataFrame) and data.empty):
        print("No data returned.")
        return


    per_ticker = {}

    # print("data.columns", data.columns)
    # data.columns MultiIndex([( 'Close', 'AAPL'),
    #         ( 'Close', 'MSFT'),
    #         ( 'Close', 'TSLA'),
    #         (  'High', 'AAPL'),
    #         (  'High', 'MSFT'),
    #         (  'High', 'TSLA'),
    #         (   'Low', 'AAPL'),
    #         (   'Low', 'MSFT'),
    #         (   'Low', 'TSLA'),
    #         (  'Open', 'AAPL'),
    #         (  'Open', 'MSFT'),
    #         (  'Open', 'TSLA'),
    #         ('Volume', 'AAPL'),
    #         ('Volume', 'MSFT'),
    #         ('Volume', 'TSLA')],
    #        names=['Price', 'Ticker'])

    print("data.loc", data.loc)

    for c in data.columns:
        print(f"Column: {c}")



    if isinstance(data.columns, pd.MultiIndex):
        if set(tickers).issubset(set(data.columns.get_level_values(0))):
            for t in tickers:
                per_ticker[t] = data[t].dropna(how="all")
        else:
            for t in tickers:
                cols = [c for c in data.columns if c[1] == t]
                # print(f"Ticker: {t}, Columns: {cols}")

                if cols:
                    df = data.loc[:, cols]
                    df.columns = [c[0] for c in cols]
                    per_ticker[t] = df.dropna(how="all")
    else:
        per_ticker[tickers[0]] = data.dropna(how="all")

    print("Close prices (latest):\n")
    for t in tickers:
        df = per_ticker.get(t)
        if df is None or df.empty or "Close" not in df.columns:
            print(f"{t}: (no data)\n")
            continue

        latest_close = df["Close"].iloc[-1]
        print(f"Latest Close Price for {t}: {latest_close}\n")
        print(df["Close"], "\n")

if __name__ == "__main__":
    main()