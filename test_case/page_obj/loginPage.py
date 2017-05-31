# _*_ coding: utf-8 _*_
#!/usr/bin/python2.7
#Filename: loginPage.py

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from selenium import webdriver

class Login(Page):
    '''user login'''
    url = '/UserManage/Login'

    login_username_loc = (By.ID, "txtUInfo")
    login_password_loc = (By.ID, "txtpwd")
    login_button_loc = (By.LINK_TEXT,"登   录")

    #input username
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #input_password
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #click login button
    def login_button(self):
        self.find_element(*self.login_button_loc).click()
    #login
    def user_login(self, username="13636317279", password="456852"):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()

    error_hint_loc = (By.ID, "sperrtip")
    login_success_loc = (By.ID, "ausername")

    #login error message
    def error_hint(self):
        return self.find_element(*self.error_hint_loc).text

    #login successfully
    def user_login_success(self):
        return self.find_element(*self.login_success_loc).text

if __name__ == "__main__":
    driver = webdriver.Firefox()
    Login(driver).user_login(username='123')
    print(Login(driver).error_hint())
    driver.quit()
