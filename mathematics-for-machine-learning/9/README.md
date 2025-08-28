# 9

## Setup

```sh
uv init
uv venv
source .venv/bin/activate
uv pip install scikit-learn numpy matplotlib pandas yfinance
```

## Install

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Examples

```sh
python3 examples/housing-predict.py
python3 examples/capm_apple_sp500.py
```