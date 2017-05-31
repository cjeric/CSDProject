# _*_ coding: utf8 _*_
#!/usr/bin/python2.7
#filename: book_sta.py

import unittest, sys
sys.path.append('.\models')
sys.path.append('.\page_obj')
from models import myunit, function
from page_obj.homePage import homePage
from page_obj.bookPage import bookPage

class homeTest(myunit.MyTest):
    def test_input_bookinfo(self):
        page = homePage(self.driver)
        page.open()
        page.select_book_info('13', '19:00', '15', '19:00')
        function.screenshot(self.driver, 'test_input_bookinfo.png')

    def test_navigatortobook(self):
        page=homePage(self.driver)
        page.open()
        page.link_navigator('在线预订')
        self.assertTrue(bookPage(self.driver).on_page())

if __name__ == '__main__':
    unittest.main()
