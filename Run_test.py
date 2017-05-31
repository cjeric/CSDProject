#_*_coding: utf-8_*_
#!/usr/bin/python2.7
#filename:Run_test.py

import sys
#sys.path.append('./test_case')
from test_case.models import function
import HTMLTestRunner
import time, unittest
import os

def new_report(reportPath):
    lists = os.listdir(reportPath)
    lists.sort(key=lambda fn: os.path.getmtime(reportPath + '/' + fn))
    file_new = os.path.join(reportPath, lists[-1])
    print file_new
    return file_new


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = '/home/cj/PycharmProjects/csdproject/report/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title='csd', description = 'hahahahha')
    discover = unittest.defaultTestLoader.discover('./test_case', pattern = '*_sta.py')
    runner.run(discover)
    fp.close()
    file_path=new_report('/home/cj/PycharmProjects/csdproject/report/')


