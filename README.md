LLM with MCP: Multi-Tool Agent with LangChain & Groq LLM
This project demonstrates how to build a multi-tool LLM agent using LangChain, Groq LLM, and LangGraph with MCP (Multi-Client Protocol) servers for Math and Weather tasks.

The agent intelligently routes user queries to the right tool, allowing seamless integration of external APIs and local Python functions in an LLM workflow.

🚀 Features
Multi-Tool Agent

Handles Math operations and Weather queries in a single agent.

Automatically decides which tool to invoke based on user input.

Weather API Integration

Fetches real-time weather from OpenWeather API.

Returns temperature, feels-like, and conditions in a friendly message.

Math Server

Performs Addition and Multiplication using MCP over stdio transport.

LangChain + LangGraph

Uses create_react_agent for a reasoning-based LLM workflow.

Executes tool calls sequentially with strict type control.

Groq LLM Integration

Powered by LLaMA3-8B-8192 via ChatGroq.

Handles natural language understanding and tool orchestration efficiently.

| Component           | Technology Used                          |
| ------------------- | ---------------------------------------- |
| **LLM**             | Groq LLaMA3-8B-8192 via `langchain_groq` |
| **Agent Framework** | LangChain + LangGraph (ReAct pattern)    |
| **Tools Protocol**  | MCP (Multi-Client Protocol)              |
| **Servers**         | FastMCP for Weather & Math               |
| **API**             | OpenWeatherMap API                       |
| **Environment**     | Python 3.10+, AsyncIO, dotenv            |

 How It Works
User Query → LLM Agent

The query is sent to LangGraph ReAct Agent.

Tool Selection

If the query is Math-related, the Math MCP Server handles it.

If the query is Weather-related, the Weather MCP Server fetches real data.

Sequential Tool Execution

Tools are executed one at a time as per the system prompt rules.

Output is returned to the LLM for final formatting.

Response

The agent returns calculated results or weather details in natural language.
