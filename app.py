import asyncio

import aiohttp
from flask import Flask, json

URL1 = 'http://localhost:5000/static/data1.json'
URL2 = 'http://localhost:5000/static/data2.json'
URL3 = 'http://localhost:5000/static/data3.json'
# URL3 = 'http://www.google.com:81/'                              # URL with timeout for test


async def getjson(session, url) -> list:
    response_json = []
    try:
        response = await session.get(url)
        response_json = await response.json()
    except asyncio.TimeoutError:
        print('A timeout occurred.')
        pass
    except Exception as e:
        print(e)
        pass
    return response_json


async def aiohttp_main():
    data = []
    timeout = aiohttp.ClientTimeout(total=2)    # Overriding default timeout with 2 seconds
    async with aiohttp.ClientSession(timeout=timeout) as session:
        data.extend(await getjson(session, URL1))
        data.extend(await getjson(session, URL2))
        data.extend(await getjson(session, URL3))
    return data


app = Flask(__name__,  static_url_path='/static')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/get-data')
def get_data():
    data = asyncio.run(aiohttp_main())
    data = sorted(data, key=lambda d: d['id'])
    return json.jsonify(data)


if __name__ == '__main__':
    app.run()
