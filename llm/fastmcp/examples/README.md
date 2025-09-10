# examples

## Setup

```sh
uv init
uv venv
source .venv/bin/activate
uv pip install fastmcp aiohttp
```

## Install

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Development

```sh
# basic
uv run python src/basic.py
uv run python src/test_basic.py

# echo
uv run python src/echo.py
uv run python src/test_echo.py

# file
uv run python src/file.py
uv run python src/test_file.py

# config
uv run src/config_server.py
uv run src/config_server.py --name MyServer --debug
```