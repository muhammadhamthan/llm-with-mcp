from mcp.server.fastmcp import FastMCP
import asyncio
import requests
import os

from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("Weather")

API_KEY = os.getenv("WEATHER_API_KEY")
print(API_KEY)

def fetch_weather(location:str) ->str:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":location,
        "appid":API_KEY,
        "units":"metric"
    }
    
    response = requests.get(base_url,params=params)
    print("Status:", response.status_code)
    print("Raw Response:", response.text)  # Debugging

    data = response.json()
    
    if data.get("cod") != 200:
        return f"Sorry, I coundn't fetch the weather for {location}"
    
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feel_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"].capitalize()
    
    return (
        f"The weather in {city}, {country} is currently {description} 🌤.\n"
        f"Temperature: {temp}°C (feels like {feel_like}°C).\n"
        f"It's a great day to enjoy your time outdoors if possible!"
    )

@mcp.tool()
async def get_weather(location:str) ->str:
    """Get the weather location"""
    return fetch_weather(location)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
