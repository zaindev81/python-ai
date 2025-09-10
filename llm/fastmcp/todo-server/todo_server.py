import datetime
from typing import List, Dict, Any
from pydantic import BaseModel
from fastmcp import FastMCP, Context

# Define a complex input with Pydantic model
class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False
    created_at: str = None

# Create an instance of the MCP server
mcp = FastMCP("ToDo Management Server")

# Simple in-memory storage
todos: List[TodoItem] = [
    TodoItem(id=1, title="Learn FastMCP", completed=False, created_at="2024-01-01"),
    TodoItem(id=2, title="Build sample app", completed=True, created_at="2024-01-02")
]
counter = 3

@mcp.tool()
async def add_todo(title: str, ctx: Context) -> Dict[str, Any]:
    """Add a new ToDo item"""
    global counter

    # Log using the context
    await ctx.info(f"Adding new ToDo: {title}")

    new_todo = TodoItem(
        id=counter,
        title=title,
        created_at=datetime.datetime.now().strftime("%Y-%m-%d")
    )
    todos.append(new_todo)
    counter += 1

    await ctx.info(f"ToDo added: ID {new_todo.id}")

    return {
        "success": True,
        "todo": new_todo.model_dump(),
        "message": f"ToDo '{title}' has been added"
    }

@mcp.tool()
async def un_complete_todo(todo_id: int, ctx: Context) -> Dict[str, Any]:
    """Mark a ToDo item as incomplete"""
    await ctx.info(f"Marking ToDo as incomplete: ID {todo_id}")

    for todo in todos:
        if todo.id == todo_id:
            todo.completed = False
            await ctx.info(f"ToDo marked as incomplete: {todo.title}")
            return {
                "success": True,
                "todo": todo.model_dump(),
                "message": f"ToDo '{todo.title}' marked as incomplete"
            }

    await ctx.warning(f"ToDo not found for ID: {todo_id}")
    return {
        "success": False,
        "message": f"ToDo with ID {todo_id} not found"
    }

@mcp.tool()
async def complete_todo(todo_id: int, ctx: Context) -> Dict[str, Any]:
    """Mark a ToDo item as completed"""
    await ctx.info(f"Marking ToDo as complete: ID {todo_id}")

    for todo in todos:
        if todo.id == todo_id:
            todo.completed = True
            await ctx.info(f"ToDo completed: {todo.title}")
            return {
                "success": True,
                "todo": todo.model_dump(),
                "message": f"ToDo '{todo.title}' marked as completed"
            }

    await ctx.warning(f"ToDo not found for ID: {todo_id}")
    return {
        "success": False,
        "message": f"ToDo with ID {todo_id} not found"
    }

@mcp.tool()
def delete_todo(todo_id: int) -> Dict[str, Any]:
    """Delete a ToDo item"""
    global todos

    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(i)
            return {
                "success": True,
                "deleted_todo": deleted_todo.model_dump(),
                "message": f"ToDo '{deleted_todo.title}' has been deleted"
            }

    return {
        "success": False,
        "message": f"ToDo with ID {todo_id} not found"
    }

@mcp.resource("todos://all")
def get_all_todos() -> List[Dict[str, Any]]:
    """Get all ToDo items"""
    return [todo.model_dump() for todo in todos]

@mcp.resource("todos://completed")
def get_completed_todos() -> List[Dict[str, Any]]:
    """Get completed ToDo items"""
    return [todo.model_dump() for todo in todos if todo.completed]

@mcp.resource("todos://pending")
def get_pending_todos() -> List[Dict[str, Any]]:
    """Get pending (incomplete) ToDo items"""
    return [todo.model_dump() for todo in todos if not todo.completed]

@mcp.resource("todos://{todo_id}")
def get_todo_by_id(todo_id: str) -> Dict[str, Any]:
    """Get a specific ToDo item by its ID"""
    try:
        id_int = int(todo_id)
        for todo in todos:
            if todo.id == id_int:
                return todo.model_dump()
        return {"error": f"ToDo with ID {todo_id} not found"}
    except ValueError:
        return {"error": "Invalid ID format"}

@mcp.resource("stats://summary")
def get_stats() -> Dict[str, Any]:
    """Get summary statistics of ToDos"""
    total = len(todos)
    completed = len([t for t in todos if t.completed])
    pending = total - completed

    return {
        "total_todos": total,
        "completed_todos": completed,
        "pending_todos": pending,
        "completion_rate": round((completed / total * 100) if total > 0 else 0, 1)
    }

@mcp.prompt()
def todo_summary_prompt() -> str:
    """Prompt for generating a summary of ToDos"""
    return """
Analyze the following ToDo data and create a concise summary:

- Overall progress
- Tasks to prioritize
- Completion rate
- Recommended actions

Use the resources 'todos://all' and 'stats://summary'.
"""

if __name__ == "__main__":
    mcp.run()
