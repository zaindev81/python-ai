# todo-server

## Setup

```sh
uv init

uv venv
source .venv/bin/activate

# install
uv pip install fastmcp pydantic typing asyncio
uv pip install .
```

## Install

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Run

```sh
fastmcp dev todo_server.py
uv run python todo_server.py

# claude
fastmcp install todo_server.py --name "TodoServer"
```

## Test

```sh
uv run python test_client.py

python test_client.py
```

## Claude Desktop

1. Setup Claude MCP configuration in Claude Desktop
2. Restart Claude Desktop

```sh
vim ~/Library/Application\ Support/Claude/claude_desktop_config.json

# /Users/Username/Library/Logs/Claude/xxx.log

{
  "mcpServers": {
    "simple-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/python-llms/fastmcp/simple-server",
        "run",
        "simple-server"
      ]
    }
    "todo-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/python-llms/fastmcp/todo-server",
        "run",
        "todo-server"
      ]
    }
  }
}
```

# Order

**Complete TODO Commands in English:**

## 1. Adding Tasks
```
Add a new task "Prepare presentation slides"
Create a todo item "Call the client"
Add "Review quarterly report" to my todo list
```

## 2. Completing Tasks
```
Mark task ID 1 as completed
Complete todo item 2
Finish task number 3
```

## 3. Uncompleting Tasks
```
Mark task ID 1 as incomplete
Set todo item 2 back to pending
Uncheck task number 3
```

## 4. Deleting Tasks
```
Delete task ID 1
Remove todo item 2
Delete task number 3
```

## 5. Viewing All Tasks
```
Show me all todo items
Display my complete task list
What are all my todos?
```

## 6. Viewing Completed Tasks
```
Show me completed tasks
What tasks have I finished?
Display all done items
```

## 7. Viewing Pending Tasks
```
Show me pending tasks
What tasks are still incomplete?
Display unfinished items
```

## 8. Getting Statistics
```
Show me todo statistics
What's my completion rate?
Give me a progress summary
```

## 9. Getting Detailed Reports
```
Generate a todo summary report
Analyze my task progress
Create a comprehensive todo overview
```

## Quick Examples to Try:
```
Add a new task "Buy groceries"
Show me all my tasks
Mark task 1 as completed
What's my completion rate?
```

Try any of these commands and I'll use your todo-server tools to help you manage your tasks!