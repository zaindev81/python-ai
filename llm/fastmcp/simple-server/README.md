# simple-server

## Setup

```sh
uv init

uv venv
source .venv/bin/activate

# install
uv pip install fastmcp
```

## Install

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Run

```sh
fastmcp dev simple_server.py
uv run python simple_server.py

# claude
fastmcp install simple_server.py --name "SimpleServer"
```

## Test

```sh
uv run python test_client.py

python test_client.py
```