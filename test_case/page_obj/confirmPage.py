# _*_ coding: utf-8 _*_
#!/usr/bin/python2.7
#Filename: loginPage.py

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from loginPage import Login
from homePage import homePage
from bookPage import bookPage
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class confirmPage(Page):

    url = '/PreActivity/PreActivityInfo'

    carinfo_loc = (By.XPATH, "//section[@id='divcarinfo']/div[@class='con-box clearfix']/div[@class='img-box']/p")

    def get_car_info(self):
        return self.find_element(self.carinfo_loc).text

    storeinfo_loc = (By.XPATH, "//section[@id='divcarinfo']/div[@class='con-box clearfix']/div[@class='order-inf clearfix']/div[@class='inf'/p]")

    def get_store_info(self):
        info_list = self.find_elements(self.storeinfo_loc)
        list = []
        for info in info_list:
            text = info.text
            list.append(text)
        return list

    basic_insurance_loc = (By.XPATH, "//section[@id='divcarinfo']/section[@class='list-con fjfwf']/div/dl/dd[1]/div[@class='price-box']/p/span")

    def get_basic_insurance_price(self):
        return self.find_element(self.basic_insurance_loc).text

    fee_loc = (By.XPATH, "//section[@id='divcarinfo']/section[@class='list-con fjfwf']/div/dl/dd[2]/div[@class='price-box']/p/span")

    def get_fee(self):
        return self.find_element(self.fee_loc).text

    advance_insurance_price_loc = (By.ID, 'serviceprice')
    advance_insurance_checkbox_loc = (By.XPATH, "//dd[@id='divrice3']/div[@class='value clearfix']")

    def select_advance_insurance(self):
        self.find_element(self.advance_insurance_checkbox_loc).click()

    def get_advance_insurance_price(self):
        return self.find_element(self.advance_insurance_price_loc).text

    total_price_loc = (By.ID, 'totalprice')
    def get_total_price(self):
        return self.find_element(self.total_price_loc).text

    submit_button_loc = (By.ID, 'createOrder')

    def submit_order(self):
        if EC.element_to_be_clickable(self.submit_button_loc):
            print 'submit order'
        else:
            raise NoSuchElementException()



if __name__ == '__main__':
    driver = webdriver.Firefox()
    loginPage = Login(driver)
    loginPage.user_login()
    sleep(5)
    homePage = homePage(driver)
    homePage.link_navigator('在线预订')
    sleep(5)
    bookPage = bookPage(driver)
    bookPage.select_car('别克凯越',100)
    confirmPage = confirmPage(driver)

