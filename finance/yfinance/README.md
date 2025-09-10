# yfinance

## Setup

```sh
uv init
uv venv
source .venv/bin/activate
uv pip install yfinance pandas
```

## Activate

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Examples

```sh
# 1.
uv run python examples/01_basic_history.py --ticker AAPL --period 3mo
uv run python examples/01_basic_history.py --ticker MSFT --period 3mo
uv run python examples/01_basic_history.py --ticker AMZN --period 3mo
uv run python examples/01_basic_history.py --ticker GOOGL --period 3mo
uv run python examples/01_basic_history.py --ticker META --period 3mo
uv run python examples/01_basic_history.py --ticker NVDA --period 3mo
uv run python examples/01_basic_history.py --ticker TSLA --period 3mo
uv run python examples/01_basic_history.py --ticker NFLX --period 3mo

uv run python examples/01_basic_history.py --ticker ^GSPC --period 3mo
uv run python examples/01_basic_history.py --ticker ^DJI --period 3mo
uv run python examples/01_basic_history.py --ticker ^IXIC --period 3mo

# 2.
uv run python examples/02_multiple_history.py --tickers AAPL MSFT TSLA --period 3mo

# 3.
uv run python examples/03_specify_date_range.py
```

## Jupyter Notebook

```sh
pip install yfinance mplfinance matplotlib
```