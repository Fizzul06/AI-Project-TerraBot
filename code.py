import time
import os
import asyncio
import python_weather

os.environ['TZ'] = 'Asia/Kuala_Lumpur'

time.tzset()

async def get_weather():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get('Bangi')
        
        print(f"Current Temperature: {weather.temperature}°C")
        print(f"Weather Condition:   {weather.description}")

weather = ["cuaca", "weather"]
times = ['time', 'masa', 'waktu']
bye = ['bye', 'exit', 'quit']

while True:
  user = input("Hi! How can I help you? ")
  user = user.lower()
  if any(word in user for word in weather):
    print("Here is the current weather situation:")
    await get_weather()
  elif any(word in user for word in times):
    print("It's %s." % time.strftime("%H:%M", time.localtime()))
  elif any(word in user for word in bye):
    print("See you later.")
    break
  else:
    print("Sorry, I don't understand, can you rephrase your questions?")
