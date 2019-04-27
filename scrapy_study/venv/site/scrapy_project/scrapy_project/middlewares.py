from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse


class SeleniumMiddleware():
    def __init__(self, timeout=30, service_args=[]):
        self.timeout = timeout
        self.browser = webdriver.Chrome(executable_path="F:/brower_driver/chromedriver", service_args=service_args)
        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        try:
            self.browser.get(request.url)
            self.wait.until(
                EC.presence_of_element_located((By.ID, 'pageList-4-relate')))
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)


