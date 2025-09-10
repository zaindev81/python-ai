import asyncio
import os
from fastmcp import Client

async def test_file_server():
    try:
        async with Client("src/file.py") as client:
            print("=== File Demo Server Test ===\n")

            # Test tools listing
            print("Available tools:")
            tools = await client.list_tools()
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")
            print()

            # Test 1: Get test file from server (default path)
            print("Test 1: Getting default file (requirements.txt)")
            try:
                result = await client.call_tool("get_test_file_from_server", {})
                print(f"  Result type: {type(result)}")
                if hasattr(result, 'content') and result.content:
                    content = result.content[0]
                    print(f"  Content type: {type(content)}")
                    if hasattr(content, 'text'):
                        print(f"  File content preview: {content.text[:200]}...")
                    elif hasattr(content, 'data'):
                        print(f"  File data length: {len(content.data)} bytes")
                print("  ✓ Default file test completed")
            except Exception as e:
                print(f"  ✗ Default file test failed: {e}")
            print()

            # Test 2: Get test file from server (custom path)
            print("Test 2: Getting custom file (setup.py or pyproject.toml)")
            custom_paths = ["setup.py", "pyproject.toml", "README.md", "__init__.py"]

            for path in custom_paths:
                try:
                    if os.path.exists(path):
                        print(f"  Testing with existing file: {path}")
                        result = await client.call_tool("get_test_file_from_server", {"path": path})
                        if hasattr(result, 'content') and result.content:
                            content = result.content[0]
                            if hasattr(content, 'text'):
                                print(f"    File content preview: {content.text[:100]}...")
                            print(f"    ✓ Custom file test with {path} completed")
                        break
                except Exception as e:
                    print(f"    ✗ Custom file test with {path} failed: {e}")
            else:
                print("  No suitable test files found, trying with non-existent file")
                try:
                    result = await client.call_tool("get_test_file_from_server", {"path": "non_existent.txt"})
                    print("  ✓ Non-existent file test completed (may return empty or error)")
                except Exception as e:
                    print(f"  ✗ Non-existent file test failed: {e}")
            print()

            # Test 3: Get PDF from URL (default URL)
            print("Test 3: Getting PDF from default URL")
            try:
                result = await client.call_tool("get_test_pdf_from_url", {})
                print(f"  Result type: {type(result)}")
                if hasattr(result, 'content') and result.content:
                    content = result.content[0]
                    print(f"  Content type: {type(content)}")
                    if hasattr(content, 'data'):
                        print(f"  PDF data length: {len(content.data)} bytes")
                    elif hasattr(content, 'text'):
                        print(f"  Content (text): {len(content.text)} characters")
                print("  ✓ Default PDF test completed")
            except Exception as e:
                print(f"  ✗ Default PDF test failed: {e}")
            print()

            # Test 4: Get PDF from custom URL
            print("Test 4: Getting PDF from custom URL")
            custom_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
            try:
                result = await client.call_tool("get_test_pdf_from_url", {"url": custom_url})
                if hasattr(result, 'content') and result.content:
                    content = result.content[0]
                    if hasattr(content, 'data'):
                        print(f"  Custom PDF data length: {len(content.data)} bytes")
                    elif hasattr(content, 'text'):
                        print(f"  Content (text): {len(content.text)} characters")
                print("  ✓ Custom PDF test completed")
            except Exception as e:
                print(f"  ✗ Custom PDF test failed: {e}")
            print()

            # Test 5: Error handling - invalid URL
            print("Test 5: Error handling with invalid URL")
            try:
                result = await client.call_tool("get_test_pdf_from_url", {"url": "https://invalid-url-that-does-not-exist.com/file.pdf"})
                print("  ✗ Expected error but got result")
            except Exception as e:
                print(f"  ✓ Expected error occurred: {type(e).__name__}")
            print()

            print("=== All tests completed ===")

    except Exception as e:
        print(f"Connection Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_file_server())