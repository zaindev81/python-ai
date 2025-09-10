import asyncio
from fastmcp import Client

async def test_server():
    try:
        async with Client("src/echo.py") as client:
            # Test tools listing
            print("Available tools:")
            tools = await client.list_tools()
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")
            print()

            # Test resources listing
            print("Available resources:")
            resources = await client.list_resources()
            for resource in resources:
                print(f"  - {resource.uri}: {resource.description}")
            print()

            # Test prompts listing
            print("Available prompts:")
            prompts = await client.list_prompts()
            for prompt in prompts:
                print(f"  - {prompt.name}: {prompt.description}")
            print()

            # Test echo tool
            print("Testing echo tool:")
            result = await client.call_tool("echo_tool", {"text": "Hello, World!"})
            print(f"  echo_tool('Hello, World!') = {result.content[0].text}")
            print()

            # Test static resource
            print("Testing static resource:")
            resource_result = await client.read_resource("echo://static")
            print(f"  echo://static = {resource_result[0].text}")
            print()

            # Test template resource
            print("Testing template resource:")
            template_result = await client.read_resource("echo://template-text")
            print(f"  echo://template-text = {template_result[0].text}")
            print()

            # Test prompt
            print("Testing echo prompt:")
            prompt_result = await client.get_prompt("echo", {"text": "Hello from prompt!"})
            print(f"  echo prompt = {prompt_result.messages[0].content.text}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_server())