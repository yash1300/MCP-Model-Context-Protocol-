import asyncio
from json import load

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def run_chat():
    load_dotenv()
    config_file = "mcpdemo/browser_mcp.json"

    print("Intializing....")

    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="llama-3.3-70b-versatile")

    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steeps = 15,
        memory_enabled = True
    )

    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("==================================\n")

    try: 
        while True:
            user_input = input("\nYou: ")
            if user_input.lower in ["exit", 'quit']:
                print("Ending....")
                break

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            print("\nAssistant: ", end="", flush=True)

            try:
                # Run the agent with the user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally: #clean up
        if client and client.session:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_chat())