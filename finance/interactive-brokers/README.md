# Interactive Brokers

## Setup

```sh
uv init
uv venv
source .venv/bin/activate
uv pip install yfinance pandas
uv pip install ib-insync
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
uv run python examples/basic.py
```