# _*_ coding: utf-8 _*_
#!/usr/bin/python2.7
#Filename: login_sta.py

from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import Login

class loginTest(myunit.MyTest):

    def test_login1(self):
        page = Login(self.driver)
        page.user_login()
        self.assertEquals(page.user_login_success(), '程捷'.decode('utf-8'))
        function.screenshot(self.driver,'testlogin1.png')

    def test_login2(self):
        '''The test case will be failed'''
        page = Login(self.driver)
        page.user_login()
        self.assertEquals(page.user_login_success(), 'cj'.decode('utf-8'))
        function.screenshot(self.driver, 'testlogin2.png')

    def test_login_3(self):
        '''wrong pwd'''
        page = Login(self.driver)
        page.user_login('13636317279','111111')
        self.assertEquals(page.error_hint(), '密码错误，请重新输入密码'.decode('utf8'))
        function.screenshot(self.driver, 'testlogin3.png')

if __name__ == '__main__':
    unittest.main()