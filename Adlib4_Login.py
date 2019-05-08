# -*- coding: utf-8 -*-
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep
#driver=webdriver.Chrome()
#driver.get("http://192.168.11.7")

# class Login():
#     def user_login(self,driver):
#         driver.find_element_by_id("username").clear()
#         driver.find_element_by_id("username").send_keys("pc5")
#         driver.find_element_by_id("password").clear()
#         driver.find_element_by_id("password").send_keys("1")
#         driver.find_element_by_id("myLayer01").click()
#
#     def user_logout(self,driver):
#         driver.find_element_by_css_selector("#userName").click()
#         driver.find_element_by_css_selector("i.lms.lms_exit").click()
class Login():
    def user_login(self,driver,username,password):
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("myLayer01").click()


    def jieshu(self,driver):
        driver.find_element_by_css_selector('#treemenu_49_span').click()
        driver.find_element_by_css_selector('#treemenu_50_span').click()
        driver.switch_to.frame('400000100frame')
        driver.find_element_by_css_selector("#number").send_keys('30400')
        driver.find_element_by_css_selector('#btnReaderInfo').click()





    def user_logout(self,driver):
        driver.find_element_by_css_selector("#userName").click()
        driver.find_element_by_css_selector("i.lms.lms_exit").click()



if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("http://192.168.11.7")
    Login().user_login(driver,'pc5','1')

    sleep(2)
    Login().jieshu(driver)
    sleep(4)
    Login().user_logout(driver)

