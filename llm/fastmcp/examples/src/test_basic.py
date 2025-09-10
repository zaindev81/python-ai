import asyncio
from fastmcp import Client

async def test_server():
    try:
        async with Client("src/basic.py") as client:
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


    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_server())