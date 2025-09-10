from typing import List, Optional
import yfinance as yf
import pandas as pd

def fetch_history(
    ticker: str,
    period: str = "1mo",
    interval: str = "1d",
    auto_adjust: bool = True,
) -> pd.DataFrame:
    return yf.Ticker(ticker).history(period=period, interval=interval, auto_adjust=auto_adjust)

def fetch_multi_history(
    tickers: List[str],
    period: str = "1mo",
    interval: str = "1d",
    auto_adjust: bool = True,
) -> pd.DataFrame:
    df = yf.download(tickers=tickers, period=period, interval=interval, auto_adjust=auto_adjust, group_by="ticker")
    return df
