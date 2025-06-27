



🧠 MCP Agent Demo (Beginner-Friendly)
This project is a small experiment I built to explore how AI models can interact with real-world tools using something called MCP – Model Context Protocol.

📌 What Is MCP?
MCP (Model Context Protocol) is a system that allows AI models (like ChatGPT or LangChain agents) to connect with external tools or services — like opening a browser, searching something online, or interacting with a website — all through a structured interface.

Think of MCP like giving an AI a "remote control" to tools on your computer. Each tool (like a browser or search engine) is made available through something called an MCP server.

🧰 What I Built
This project connects a LangChain agent to a few different MCP servers, such as:

🧪 Playwright MCP Server – lets the AI use a headless browser (navigate, click, take screenshots, etc.)

🔍 DuckDuckGo Search MCP Server – lets the AI perform live searches

🏠 Airbnb MCP Server – automates and interacts with Airbnb-like websites

These servers expose real-world actions the AI agent can use to complete tasks.

⚙️ How It Works
A JSON config (browser_mcp.json) defines which MCP servers to run

The Python app loads this config and starts the agent

The agent can then use any available tools (like "navigate to a page", "search", or "click a button")

Everything runs asynchronously using Python's asyncio

🛠 Project Structure
bash
Copy
Edit
mcpdemo/
├── app.py                  # Main file to run the agent
├── browser_mcp.json        # Config file listing all MCP servers
└── .venv/                  # Python virtual environment (optional)
