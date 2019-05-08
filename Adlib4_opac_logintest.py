from Adlib4_opac_login import *
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

username='pc5'
password='1'

test_user_login(driver,username,password)


