from selenium import webdriver
from time import sleep

class Page():
    def __init__(self,driver):
        self.base_url="http://192.168.11.67:8003"
        self.driver=driver
        self.timeout=10
    #打开不同子页面_open私有，不可调用
    def _open(self,url):
        url_=self.base_url+url
        print("Test page is: %s" %url)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url==url_,'Did not land on %s' %url_

    def open(self):
        self._open(self.url)
    #元素定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

