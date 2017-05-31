# _*_ coding: utf-8 _*_
#!/usr/bin/python2.7
#Filename: base.py
from selenium import webdriver

class Page(object):
    '''base page object'''

    home_page = 'http://www.chesudi.com'

    def __init__(self, driver, base_url = home_page, parent = None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not access to %s' % url

    def find_element(self, *locators):
        return self.driver.find_element(*locators)

    def find_elements(self, *locators):
        return self.driver.find_elements(*locators)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    page = Page(driver)
