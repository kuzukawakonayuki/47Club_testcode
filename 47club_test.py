#Coding: UTF-8
from selenium import webdriver
import threading
import time

def club47():
    while (1==1):
        print("test")
        if "Tue May 15 03:57:00 2018" <= time.ctime():
            driver = webdriver.Chrome(executable_path="C:\WebDriver\chromedriver.exe")
            driver.get("https://www.yahoo.co.jp")
            time.sleep(30)
            driver.get("https://www.google.co.jp")
            break

if __name__=="__main__":
    th1 = threading.Thread(target=club47)
    th2 = threading.Thread(target=club47)
    th3 = threading.Thread(target=club47)

    th1.start()
    th2.start()
    th3.start()



