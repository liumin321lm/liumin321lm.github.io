from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
#引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import urllib
import urllib.response
from selenium.webdriver.chrome.options import Options
import win32gui
import win32api
import win32con


import time

from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
driver.get("http://www.openbookdata.com.cn/")

driver.find_element_by_id("txtloginname").send_keys('afanotes@qq.com')

driver.find_element_by_id("txtpassword").send_keys('7345e9c7e2')

driver.find_element_by_id("btnlogin").click()
sleep(2)
driver.get('http://www.openbookdata.com.cn/WeekBookList/2019-01-01_2019-01-31_.html')
sleep(2)
# driver.find_element_by_link_text(u"更多>>").click()
# driver.find_element_by_id("Y_ucOnceWeekBooks_a_more").click()
# sleep(2)
# ActionChains(driver).send_keys(Keys.END)
# sleep(2)
# ActionChains(driver).send_keys(Keys.END)






# def scroll(driver):
#     driver.execute_script("""
#         (function () {
#             var y = document.body.scrollTop;
#             var step = 100;
#             window.scroll(0, y);
#             function f() {
#                 if (y < document.body.scrollHeight) {
#                     y += step;
#                     window.scroll(0, y);
#                     setTimeout(f, 50);
#                 }
#                 else {
#                     window.scroll(0, y);
#                     document.title += "scroll-done";
#                 }
#             }
#             setTimeout(f, 1000);
#         })();
#         """)
# scroll(driver)
#
print('下拉开始，，，，，，')
driver.execute_script("""
    (function () {
        var y = document.body.scrollTop;
        var step = 100;
        window.scroll(0, y);
        function f() {
            if (y < document.body.scrollHeight) {
                y += step;
                window.scroll(0, y);
                setTimeout(f, 50);
            }
            else {
                window.scroll(0, y);
                document.title += "scroll-done";
            }
        }
        setTimeout(f, 1000);
    })();
    """)


#sleep(1800)
win32api.keybd_event(35, 0, 0, 0)  # 按下ctrl
# win32api.keybd_event(17, 0, 0, 0)  # 按下ctrl
# win32api.keybd_event(83, 0, 0, 0)  # 按下s
# win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放s
# win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放ctrl
#hd = win32gui.FindWindow(u"#32770", u"另存为")
# hd = win32gui.FindWindow(u"另存为")
# win32gui.SetForegroundWindow(hd)

# sleep(1)
#
# win32api.keybd_event(13, 0, 0, 0)  # 按下enter
# win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放enter
# ActionChains(driver).send_keys(Keys.ENTER).perform()
# print('保存。。。。。')
# sleep(10)

