import asyncio
from fastmcp import Client

async def test_server():
    try:
        async with Client("simple_server.py") as client:
            tools = await client.list_tools()
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")
            print()

            resources = await client.list_resources()
            for resource in resources:
                print(f"  - {resource.uri}: {resource.description}")
            print()

            result = await client.call_tool("add", {"a": 10, "b": 5})
            print(f"  add(10, 5) = {result.content[0].text}")

            result = await client.call_tool("subtract", {"a": 10, "b": 5})
            print(f"  subtract(10, 5) = {result.content[0].text}")

            result = await client.call_tool("multiply", {"a": 3, "b": 7})
            print(f"  multiply(3, 7) = {result.content[0].text}")
            print()

            result = await client.call_tool("divide", {"a": 7, "b": 2})
            print(f"  divide(7, 2) = {result.content[0].text}")
            print()

            result = await client.call_tool("floor_divide", {"a": 7, "b": 2})
            print(f"  floor_divide(7, 2) = {result.content[0].text}")
            print()

            version = await client.read_resource("config://version")
            print(f"  version: {version[0].text}")

            greeting = await client.read_resource("greeting://john")
            print(f"  greeting: {greeting[0].text}")
            print()

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_server())