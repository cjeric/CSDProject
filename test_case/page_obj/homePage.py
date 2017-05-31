# _*_ coding: utf-8 _*_
#!/usr/bin/python2.7
#Filename: loginPage.py

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from base import Page
from time import sleep
from selenium import webdriver

class homePage(Page):

    url = '/'
    #Go to the specific page
    def link_navigator(self, link_text):
        link = self.find_element(By.LINK_TEXT, link_text)
        link.click()

    start_city_loc = (By.ID, "cityGet")

    def start_city_input(self):
        self.find_element(*self.start_city_loc).click()

    def select_city(self, start_city = '上海'):
        ''' select the city to get the car
        :param start_city:
        :return:
        '''
        self.start_city_input()
        self.find_element(By.LINK_TEXT, start_city).click()

    start_store_loc = (By.ID,"storeGet")

    def start_store_input(self):
        self.find_element(*self.start_store_loc).click()

    def select_store(self, district = '长宁区', start_store = '天山店'):
        '''select the store to get the car
        :param district: the district the store belonged to
        :param start_store: the store name
        :return:
        '''
        self.start_store_input()
        self.find_element(By.LINK_TEXT,district).click()
        self.find_element(By.LINK_TEXT, start_store).click()

    def get_store_info(self, district, start_store):
        self.start_store_input()
        self.find_element(By.LINK_TEXT, district).click()
        store_link = self.find_element(By.LINK_TEXT, start_store)
        ActionChains(self.driver).move_to_element(store_link).perform()
        addres = self.find_element(By.ID, 'divmaddress').text
        phone = self.find_element(By.ID, 'divphone').text
        hours = self.find_element(By.ID, 'divtime').text
        return addres, phone, hours

    end_city_loc = (By.ID, "cityBack")

    def end_city_input(self):
        self.find_element(*self.end_city_loc).click()

    end_store_loc = (By.ID, "storeBack")

    def end_store_input(self):
        self.find_element(*self.end_store_loc).click()

    prev_month_loc = (By.CLASS_NAME, "cal-prev")

    def prev_month(self):
        self.find_element(*self.prev_month_loc).click()

    next_month_loc = (By.CLASS_NAME, "cal-nex")

    def next_month(self):
        self.find_element(*self.prev_month_loc).click()

    start_date_input_loc = (By.ID, "Tdate")
    end_date_input_loc = (By.ID, "Sdate")

    def date_input(self, *date_input_loc):
        self.find_element(*date_input_loc).click()

    def select_date(self, target_date, *date_input_loc):
        '''
        select a date on the homepage
        :param date: the particular date you want
        :param date_input_loc: the date_iput locator
        :return:
        '''
        self.date_input(*date_input_loc)
        datelist = self.find_elements(By.XPATH, "//div[@class='cal-start']/div[@class='calendar']/div[1]/dl/dd/a")
        for date in datelist:
            if date.text == target_date:
                date.click()
                break

    start_time_input_loc = (By.ID, "Ttime")
    end_time_input_loc = (By.ID, "Stime")

    def time_input(self, *time_input_loc):
        self.find_element(*time_input_loc).click()

    def select_time(self,target_time, *time_input_loc ):
        '''
        select a time you want to get the car
        :param target_time: the partiuclar time
        :param time_input_loc: the time_input locator
        :return:
        '''
        self.time_input(*time_input_loc)
        i = int(target_time.strip()[0:2])
        if i < 11:
            column_loc = 'div[1]/a'
        elif 11 <= i < 14:
            column_loc = 'div[2]/a'
        elif 14<= i <17:
            column_loc = 'div[3]/a'
        elif 17<= i < 20:
            column_loc = 'div[4]/a'
        else:
            column_loc = 'div[5]/a'
        time_loc = (By.XPATH,"//div[@class='order-ts-box ts-show ts-time']/div/div/" + column_loc)
        time_list = self.find_elements(*time_loc)
        for item in time_list:
            if item.text == target_time:
                item.click()
                break

    total_days_loc = (By.ID, 'divLease')

    def get_total_days(self):
        return self.find_element(*self.total_days_loc).text

    booking_button_loc = (By.ID, 'btnNext')

    def click_booking_button(self):
        self.find_element(*self.booking_button_loc).click()

    def select_book_info(self,start_date, start_time, end_date, end_time, city='上海', district='长宁区', store='天山店'):
        self.select_city(city)
        self.select_store(district,store)
        self.select_date(start_date, *self.start_date_input_loc)
        self.select_time(start_time, *self.start_time_input_loc)
        self.select_date(end_date, *self.end_date_input_loc)
        self.select_time(end_time, *self.end_time_input_loc)
        self.click_booking_button()


if __name__ == '__main__':
    #driver = webdriver.Firefox()

    driver = Remote(command_executor='http://172.16.250.129:4444/wd/hub',
                    desired_capabilities={'platform':'ANY',
                                          'browserName': 'firefox',
                                          'version': '',
                                          'javascriptEnabled' : True})
    home_page = homePage(driver)
    home_page.open()
    home_page.link_navigator('在线预订')









