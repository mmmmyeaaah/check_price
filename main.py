import requests
import asyncio

from config import config


token=config.token.get_secret_value()
url = 'https://api.binance.com/'
params = {'symbol': 'ETHUSDT'}
response = requests.get(f'{url}api/v3/ticker', params=params)

async def check_price():
    price = float(response.json()['lastPrice'])
    new_price = float(response.json()['lastPrice'])
    if abs(price - new_price) > price / 100:
        print(f'{int(price)}')


async def schedule():
    while True:
        await check_price()
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(schedule())