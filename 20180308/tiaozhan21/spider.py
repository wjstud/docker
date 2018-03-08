import csv
import asyncio
import aiohttp
import async_timeout
from scrapy.http import HtmlResponse

results = []

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            print('response: ', response)
            return await response.text()

def parse(url, body):
    print('body: ', body)
    response = HtmlResponse(url=url, body=body, encoding='utf-8') # 必须设置encoding为utf-8
    print('response: ', response)
    for rep in response.css('li.public'):
        name = rep.xpath('.//h3/a/text()').extract_first().strip()
        update_time = rep.xpath('.//relative-time/@datetime').extract_first().strip()
        results.append((name, update_time))

async def task(url):
    async with aiohttp.ClientSession() as session:
        print('url: ', url)
        html = await fetch(session, url) # 必须设置await关键字
        print('html: ', html)
        parse(url, html)

def main():
    loop = asyncio.get_event_loop()
    url_template = 'https://github.com/shiyanlou?page={}&tab=repositories'
    tasks = [task(url_template.format(i)) for i in range(1, 5)]
    print('tasks: ', tasks)
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/home/shiyanlou/shiyanlou-repos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == '__main__':
    main()
