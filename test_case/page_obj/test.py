# _*_ coding: utf-8 _*_
#!/usr/bin/python2.7
#Filename: test.py

from selenium import webdriver
from selenium.common import exceptions
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.chesudi.com")
city_get = driver.find_element_by_id("cityGet")
city_get.click()
city_selector = driver.find_element_by_link_text("上海")
city_selector.click()
store_get = driver.find_element_by_id("storeGet")
store_get.get_attribute()
store_get.click()
district_selector = driver.find_element_by_link_text("闵行区")
district_selector.click()
store_selector = driver.find_element_by_link_text("虹桥爱博店")
get_date_selector = driver.find_element_by_id("Tdate")
get_date_selector.click()
time.sleep(1)
datelist_start = driver.find_elements_by_xpath("//div[@class='cal-start']/div[@class='calendar']/div[1]/dl/dd/a")
for date in datelist_start:
    if date.text == '18':
        date.click()
        break

time.sleep(1)

datelist_end = driver.find_elements_by_xpath("//div[@class='cal-end']/div[@class='calendar']/div[1]/dl/dd/a")
for date in datelist_end:
    if date.text == '19':
        date.click()
        break

get_time_selector = driver.find_element_by_id("Ttime")
get_time_selector.click()
timelist_start = driver.find_elements_by_xpath("//div[@class='order-ts-box ts-show ts-time']/div/div/div[2]/a")
for item in timelist_start:
    if item.text == '11:00':
        item.click()
        break


time.sleep(2)
driver.quit()
