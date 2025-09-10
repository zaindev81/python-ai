from fastmcp import FastMCP

mcp = FastMCP("SimpleServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    return a / b

@mcp.tool()
def floor_divide(a: int, b: int) -> int:
    return a // b

@mcp.resource("config://version")
def get_version() -> str:
    return "v1.0.0"

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"hello, {name}"

if __name__ == "__main__":
    mcp.run()