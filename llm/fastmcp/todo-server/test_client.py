import asyncio
import json
from fastmcp import Client

async def test_advanced_server():
    """Test the advanced ToDo server"""

    async with Client("todo_server.py") as client:
        print("=== ToDo Management Server Test ===\n")

        # 1. Check initial state
        print("1. Initial ToDo list:")
        todos = await client.read_resource("todos://all")
        initial_todos = json.loads(todos[0].text)
        for todo in initial_todos:
            status = "✅" if todo["completed"] else "⏳"
            print(f"  {status} [{todo['id']}] {todo['title']}")
        print()

        # 2. Check initial statistics
        print("2. Initial statistics:")
        stats = await client.read_resource("stats://summary")
        stats_data = json.loads(stats[0].text)
        print(f"  Total: {stats_data['total_todos']}")
        print(f"  Completed: {stats_data['completed_todos']}")
        print(f"  Pending: {stats_data['pending_todos']}")
        print(f"  Completion rate: {stats_data['completion_rate']}%")
        print()

        # 3. Add a new ToDo
        print("3. Adding a new ToDo:")
        result = await client.call_tool("add_todo", {
            "title": "Read the FastMCP documentation"
        })
        add_result = json.loads(result.content[0].text)
        print(f"  ✅ {add_result['message']}")
        print()

        # 4. Get specific ToDo
        print("4. Check newly added ToDo:")
        new_todo_id = add_result['todo']['id']
        todo_detail = await client.read_resource(f"todos://{new_todo_id}")
        todo_data = json.loads(todo_detail[0].text)
        print(f"  ID: {todo_data['id']}")
        print(f"  Title: {todo_data['title']}")
        print(f"  Completed: {todo_data['completed']}")
        print(f"  Created at: {todo_data['created_at']}")
        print()

        # 5.1 Mark ToDo as completed
        print("5.1 Marking ToDo as completed:")
        complete_result = await client.call_tool("complete_todo", {
            "todo_id": new_todo_id
        })
        complete_data = json.loads(complete_result.content[0].text)
        print(f"  ✅ {complete_data['message']}")
        print()

        # 5.2 Mark ToDo as incomplete
        print("5.2 Marking ToDo as incomplete:")
        un_complete_result = await client.call_tool("un_complete_todo", {
            "todo_id": new_todo_id
        })
        un_complete_data = json.loads(un_complete_result.content[0].text)
        print(f"  ✅ {un_complete_data['message']}")
        print()

        # 6. List completed ToDos
        print("6. Completed ToDos:")
        completed_todos = await client.read_resource("todos://completed")
        completed_data = json.loads(completed_todos[0].text)
        for todo in completed_data:
            print(f"  ✅ [{todo['id']}] {todo['title']} ({todo['created_at']})")
        print()

        # 7. List pending ToDos
        print("7. Pending ToDos:")
        pending_todos = await client.read_resource("todos://pending")
        pending_data = json.loads(pending_todos[0].text)
        for todo in pending_data:
            print(f"  ⏳ [{todo['id']}] {todo['title']} ({todo['created_at']})")
        print()

        # 8. Check updated statistics
        print("8. Updated statistics:")
        updated_stats = await client.read_resource("stats://summary")
        updated_stats_data = json.loads(updated_stats[0].text)
        print(f"  Total: {updated_stats_data['total_todos']}")
        print(f"  Completed: {updated_stats_data['completed_todos']}")
        print(f"  Pending: {updated_stats_data['pending_todos']}")
        print(f"  Completion rate: {updated_stats_data['completion_rate']}%")
        print()

        # 9. Get summary prompt
        print("9. Checking ToDo summary prompt:")
        prompt = await client.get_prompt("todo_summary_prompt", {})
        print("  Prompt content:")
        print(prompt.messages[0].content.text)
        print()

        print("=== Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_advanced_server())
