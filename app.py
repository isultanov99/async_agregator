import asyncio

import aiohttp
from flask import Flask, json, redirect, url_for

URLS = [
    'http://localhost:5000/static/data1.json',
    'http://localhost:5000/static/data2.json',
    'http://localhost:5000/static/data3.json',
]
# 'http://www.google.com:81/'                              # URL with timeout for test


async def getjson(session, url) -> list:
    response_json = []
    try:
        async with session.get(url) as resp:
            response_json = await resp.json()
    except asyncio.TimeoutError:
        print('A timeout occurred.')
        pass
    except Exception as e:
        print(e)
        pass
    return response_json


async def aiohttp_main():
    timeout = aiohttp.ClientTimeout(total=2)    # Overriding default timeout with 2 seconds
    async with aiohttp.ClientSession(timeout=timeout) as session:
        data = []
        for url in URLS:
            data.append(asyncio.ensure_future(getjson(session, url)))

        all_data = await asyncio.gather(*data)
    return all_data


app = Flask(__name__,  static_url_path='/static')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/get-data')
def get_data():
    data = asyncio.run(aiohttp_main())
    data = [item for sublist in data for item in sublist]
    data = sorted(data, key=lambda d: d['id'])
    return json.jsonify(data)

@app.route('/')
def home():
    return redirect(url_for('get_data'))

if __name__ == '__main__':
    app.run()
