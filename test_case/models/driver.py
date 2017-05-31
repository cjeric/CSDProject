from selenium import webdriver
from selenium.webdriver import Remote

def browser(host='http://172.16.250.129:4444/wd/hub', browserName='firefox'):
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browserName,
                                          'version': '',
                                          'javascriptEnabled': True})
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.chesudi.com")
    dr.quit()

