# _*_ coding: utf-8 _*_
#!/usr/bin/python2.7
#Filename: myunit.py

from selenium import webdriver
from driver import browser
import unittest
import os

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.set_window_position(0,0)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()