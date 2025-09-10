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

    if not tickers:
        print("Please provide at least one ticker symbol using --tickers")
        return

    if not period:
        print("Please provide a valid period using --period")
        return

    if not interval:
        print("Please provide a valid interval using --interval")
        return


    data = yf.download(tickers, period=period, interval=interval)
    # print("Fetched data:", data)


    # Stops the program if no data is fetched (e.g., wrong ticker or bad period).
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


    # before
    # | Date       | Close (AAPL) | Close (MSFT) | High (AAPL) | High (MSFT) | ... |
    # | ---------- | ------------ | ------------ | ----------- | ----------- | --- |
    # | 2025-09-01 | 200.1        | 400.2        | 201.0       | 401.5       | ... |
    # | 2025-09-02 | 201.2        | 401.3        | 202.3       | 402.8       | ... |

    # after
    # | Date       | Open  | High  | Low   | Close | Volume  |
    # | ---------- | ----- | ----- | ----- | ----- | ------- |
    # | 2025-09-01 | 198.5 | 201.0 | 197.8 | 200.1 | 5000000 |
    # | 2025-09-02 | 199.0 | 202.3 | 198.2 | 201.2 | 4800000 |


    print("data.loc", data.loc)
    print("=" * 60)

    for c in data.columns:
        print(f"Column: {c}")

    print("=" * 60)


    # Convert the combined DataFrame into one DataFrame per ticker.
    # We need to extract data for each ticker separately, like this:
    # For AAPL
    # Date	Open	High	Low	Close	Volume
    # 2025-09-01	198.5	201.0	197.8	200.1	5000000
    # 2025-09-02	199.0	202.3	198.2	201.2	4800000

    # For MSFT
    # Date	Open	High	Low	Close	Volume
    # 2025-09-01	398.8	401.5	397.2	400.2	3000000
    # 2025-09-02	399.1	402.8	398.0	401.3	3100000
    if isinstance(data.columns, pd.MultiIndex): # Checks if the DataFrame uses MultiIndex columns.

        if set(tickers).issubset(set(data.columns.get_level_values(0))):
            for t in tickers:
                print("Handling single-level columns")
                per_ticker[t] = data[t].dropna(how="all")
        else:
            # normally here
            print("Handling MultiIndex columns")
            for t in tickers:
                # print("data.columns[1]", data.columns[1])
                # print("data.columns[1][1]", data.columns[1][1])

                # filter columns for this ticker
                cols = [c for c in data.columns if c[1] == t]
                # c is a tuple like ('Close', 'AAPL').


                # ┌────────────┬───────────────┬───────────────┐
                # │   Date     │ ('Close','AAPL') │ ('Close','MSFT') │
                # ├────────────┼───────────────┼───────────────┤
                # │ 2025-09-01 │      200.1       │      400.2       │
                # │ 2025-09-02 │      201.2       │      401.3       │
                # └────────────┴───────────────┴───────────────┘

                # ↓  .loc[:, cols]

                # ┌────────────┬───────────────┐
                # │   Date     │ ('Close','AAPL') │
                # ├────────────┼───────────────┤
                # │ 2025-09-01 │      200.1       │
                # │ 2025-09-02 │      201.2       │
                # └────────────┴───────────────┘


                if cols:
                    print("cols", data.loc)
                    # .loc[:, cols] means
                    #   : → select all rows
                    #   cols → select only the specified columns

                    # Extracts data for the specific ticker and renames columns to remove the ticker suffix.
                    df = data.loc[:, cols] # all of the rows, only cols
                    # print("df", df)

                    # [
                    #     ('Close', 'AAPL'),
                    #     ('High', 'AAPL'),
                    #     ('Low', 'AAPL'),
                    #     ('Open', 'AAPL'),
                    #     ('Volume', 'AAPL')
                    # ]
                    # =>
                    # ['Close', 'High', 'Low', 'Open', 'Volume']

                    df.columns = [c[0] for c in cols]
                    print(f"Data for {t}:\n", df.head(), "\n")

                    # remove rows where all elements are NaN
                    per_ticker[t] = df.dropna(how="all")

    else:
        per_ticker[tickers[0]] = data.dropna(how="all")


    # Print Latest Close Price
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