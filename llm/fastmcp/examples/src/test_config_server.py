import asyncio
from fastmcp import Client

async def test_server():
    try:
        async with Client("src/config_server.py") as client:
            print("=== Testing Config Server ===")

            # List available tools
            print("Available tools:")
            tools = await client.list_tools()
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")
            print()

            # List available resources (if any)
            print("Available resources:")
            resources = await client.list_resources()
            for resource in resources:
                print(f"  - {resource.uri}: {resource.description}")
            print()

            # Test get_status tool
            print("Testing get_status tool:")
            status_result = await client.call_tool("get_status", {})
            print(f"  get_status() = {status_result.content[0].text}")
            print()

            # Test echo_message tool
            print("Testing echo_message tool:")
            echo_result = await client.call_tool("echo_message", {"message": "Hello, FastMCP!"})
            print(f"  echo_message('Hello, FastMCP!') = {echo_result.content[0].text}")
            print()

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_server())