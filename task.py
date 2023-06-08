import aiohttp
import asyncio
import random
import time
import requests

# async def f1():
#     n = random.randrange(0, 5)
#     print(n)
#     await asyncio.sleep(n)
#     print('end')
#
#
# async def main():
#     tasks = []
#     for i in range(101):
#         task = asyncio.create_task(f1())
#         tasks.append(task)
#     for i in tasks:
#         await i


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']




# async def main():
#     for city in cities:
#         url = 'https://api.openweathermap.org/data/2.5/weather' \
#               f'?appid=2a4ff86f9aaa70041ec8e82db64abf56&q={city}&units=metric'
#         responce = requests.get(url)
#         print(city)
#         print(responce.json()['main']['temp'])
#
#
#
#
#
# start_time = time.time()
# asyncio.run(main())
# end_time = time.time()
# print("Total time", end_time - start_time)




async def get_weather():
   url = 'https://api.openweathermap.org/data/2.5/weather' \
         '?appid=2a4ff86f9aaa70041ec8e82db64abf56&q=Minsk&units=metric'
   async with aiohttp.ClientSession() as session:
       async with session.get(url) as response:
           text = await response.text()
           print(text)
           json = await response.json()
           print(json)


asyncio.run(get_weather())
