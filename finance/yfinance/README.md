# yfinance

## Setup

```sh
source .venv/bin/activate
uv add yfinance pandas
```

## Activate

```sh
source .venv/bin/activate
uv sync
```

## Examples

```sh
# 0.
python examples/00_basic_fetch.py --tickers AAPL MSFT TSLA

# 1.
python -m examples.01_basic_history --ticker AAPL --period 3mo
python -m examples.01_basic_history --ticker MSFT --period 3mo

# 2.
uv run python examples/02_multiple_history.py --tickers AAPL MSFT TSLA --period 3mo

# 3.
uv run python examples/03_specify_date_range.py
```

## Jupyter Notebook

```sh
pip install yfinance mplfinance matplotlib
```