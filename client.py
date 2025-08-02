from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], ## Ensure correct absolute path
                "transport":"stdio",
            
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  # Ensure server is running here
                "transport": "streamable_http",
            }

        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    
    system_prompt = """
    You are a multi-tool agent handling math and weather.
- For math questions: always use math tools (add, multiple) and return numbers.
- For weather questions: always use the weather tool and return text directly.
- Never try to convert weather output into math or vice versa.
-Always resolve one tool call completely before the next.
- Never pass objects or tool IDs as parameters, only raw literal values.

    """
    
    tools=await client.get_tools()
    model=ChatGroq(model="llama3-8b-8192")
    agent = create_react_agent(model, tools,prompt=system_prompt)

    # math_response = await agent.ainvoke(
    #     {"messages": [{"role": "user", "content": "What is 6+6 * 45 ?"}]}
    # )

    # # 
    # print("Math response:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
    {"messages": [{"role": "user", "content": "what is the weather in Chennai?"}]}
    )
    print("Weather response:", weather_response['messages'][-1].content)
asyncio.run(main())