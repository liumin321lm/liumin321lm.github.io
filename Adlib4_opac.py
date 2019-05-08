from selenium import webdriver
from time import sleep


class Search():
    def sample_search(self,driver):
        driver.find_element_by_css_selector("#key").clear()
        driver.find_element_by_css_selector("#key").send_keys("java")
        driver.find_element_by_css_selector("a.searchbtn").click()

    def advanced_search(self,driver):
        driver.find_element_by_css_selector("#myLayer").click()
        driver.find_element_by_css_selector("#key0").click()
        driver.find_element_by_css_selector("#key0").send_keys("java")
        driver.find_element_by_css_selector("#queryterm1").click()
        driver.find_element_by_css_selector("#queryterm1 > option[value='indexNumber']").click()
        driver.find_element_by_css_selector("#key1").send_keys("TP312JA S267.3y")
        driver.find_element_by_css_selector("a.layui-layer-btn0").click()


if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get("http://192.168.11.67:8003/opac")
    Search().sample_search(driver)
    sleep(2)

    Search().advanced_search(driver)
    sleep(2)
    driver.quit()





