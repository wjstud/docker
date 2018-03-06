import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse

results = []

def parse(response):
    for comment in response.xpath('//div[contains(@class, "comment-list-item")]'):
        result = {}
        result['username'] = comment.xpath('.//a[@class="username"]/text()').extract_first().strip()
        result['content'] = comment.xpath('.//p/text()').extract_first()
        results.append(result)

def has_next_page(response):
    if response.xpath('//li[@class="disabled next-page"]'):
        return False
    return True

def goto_next_page(driver):
    button = driver.find_element_by_xpath('//li[@class="next-page"]')
    button.click()

def wait_page_return(driver, page):
    WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//ul[@class="pagination"]/li[@class="active"]'),
                str(page)
                )
            )

def spider():
    driver = webdriver.PhantomJS()
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)
    page = 1
    while True:
        wait_page_return(driver, page)
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode('utf8'))
        parse(response)
        if not has_next_page(response):
            break
        page += 1
        goto_next_page(driver)
    with open('/home/shiyanlou/comments.json', 'w') as f:
        f.write(json.dumps(results))

if __name__ == '__main__':
    spider()
