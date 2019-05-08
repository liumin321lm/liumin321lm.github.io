from Adlib4_Login import *
from time import sleep
from selenium import webdriver


driver=webdriver.Chrome()
driver.get("http://192.168.11.7")
Login().user_login(driver,'pc5','1')
sleep(2)
Login().user_logout(driver)