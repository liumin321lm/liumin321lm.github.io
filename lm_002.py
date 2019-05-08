from selenium import webdriver
import logging
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import *
import os
import time
from model import function,myunit

def insert_img(filename):
    driver=webdriver.Chrome()
    func_path=os.path.dirname(__file__)
    print(func_path)
    base_dir=os.path.dirname(func_path)
    print(base_dir)

    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    print(base_dir)
    base=base_dir.split('/Website')[0]
    print(base)
    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)

def get_windows_img(self):
    #self.logger = logging.getLogger(__name__)
    func_path=os.path.dirname(__file__)
    print(func_path)
    base_dir=os.path.dirname(func_path)
    print(base_dir)

    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\', '/')
    print(base_dir)
    base=base_dir.split('/Website')[0]
    print(base)
    filepath='/Website/test_report/screenshot/'
    rq=time.strftime("%Y-%m-%d %H_%M_%S")
    #rq=time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screen_name=filepath+rq+'.png'
    print(screen_name)
    self.driver.get_screenshot_as_file(screen_name)



insert_img("lmtest1.png")
