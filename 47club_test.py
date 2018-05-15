# coding: UTF-8
from selenium import webdriver
import threading
import time

def club47():
    while (1==1):
        print("test")
        if "Tue May 15 18:33:00 2018" <= time.ctime():
            driver = webdriver.Chrome(executable_path="C:\WebDriver\chromedriver.exe")
            driver.get("http://stg-01.47club.jp/aaaa/goods/detail/10060731/")
            time.sleep(5)
            driver.find_element_by_xpath(u"//img[@alt='カートに入れる']").click()
            time.sleep(30)
            break

if __name__=="__main__":
    th1 = threading.Thread(target=club47)
    th2 = threading.Thread(target=club47)
    th3 = threading.Thread(target=club47)

    th1.start()
    th2.start()
    th3.start()



