# _*_ coding: utf-8 _*_
#!/usr/bin/python2.7
#Filename: loginPage.py

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from homePage import homePage
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class bookPage(homePage):

    url = '/OnlineBooking/index'

    def get_store_info_map(self):
        address = self.find_element(By.ID, 'spTradareaAD').text#.encode('utf8')
        phone = self.find_element(By.ID, 'spTradareaPhone').text
        hours = self.find_element(By.ID, 'spTradareaTime').text
        return address, phone, hours

    def get_car_info_row(self, car_name):
        self.car_name = car_name
        WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located((By.ID, "ulcarlist")))
        li_list = self.find_elements(By.XPATH, "//ul[@id='ulcarlist']/li")
        i = 1
        for li_item in li_list:
            if li_item.get_attribute('class') == 'other-box':
                i += 1
                continue;
            else:
                carname_loc = "//ul[@id='ulcarlist']/li[" + str(i) + "]/div[@class='relative-box']/div[@class='information-box']/h4/a"
                if self.find_element(By.XPATH, carname_loc).text == car_name.decode('utf8'):
                    car_info_row_loc = "//ul[@id='ulcarlist']/li[" + str(i) + "]/div[@class='relative-box']/"
                    return car_info_row_loc
                else:
                    i += 1

    def get_car_price(self, car_info_row_loc):
        car_price_loc = car_info_row_loc + "div[@class='price-box']/p[@class='price']/b"
        return self.find_element(By.XPATH, car_price_loc).text

    def get_car_total_price(self, car_info_row_loc):
        car_total_price_loc = car_info_row_loc + "div[@class='price-box']/p[@class='yhl']/span"
        return self.find_element(By.XPATH, car_total_price_loc).text

    def click_car_button(self, car_info_row_loc, scroll_x):
        car_button_loc = car_info_row_loc + "div[@class='op-box clearfix']/a"
        car_button = self.find_element(By.XPATH,car_button_loc)
        js = 'window.scrollTo(0,' + str(scroll_x) + ')'
        self.driver.execute_script(js)
        car_button.click()

    backup_store_row = "//ul[@id='ulcarlist']/li[@class='other-box' and @style='height: 139px;']/ul/li/div[@class='relative-box']"

    def select_car(self, car_name, scroll_x):
        car_info_row = self.get_car_info_row(car_name)
        self.click_car_button(car_info_row, scroll_x)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    book_page = bookPage(driver)
    book_page.open()
    address = book_page.get_store_info_map()
    print address
    #driver.quit()