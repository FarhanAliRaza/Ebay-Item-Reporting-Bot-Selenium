from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
print("___________________________EBAYBOT___________________________________")
counter = int(input("How many Time You want to report: "))
driver = webdriver.Chrome()
url = "https://ocswf.ebay.com/rti/compose?items=233768143622&seller=noel_36robiquet&rt=nc&_trksid=p2047675.l2566"
def run():
    driver.get("https://ocswf.ebay.com/rti/compose?items=233768143622&seller=noel_36robiquet&rt=nc&_trksid=p2047675.l2566")

def report():
    try:
        driver.find_element_by_id("btn_reason-code-1").click()
        time.sleep(1)

        driver.find_element_by_id("reason-code-1_0").click()
        time.sleep(1)

        driver.find_element_by_id("btn_reason-code-2").click()
        time.sleep(1)
    
        driver.find_element(By.XPATH, '//li[text()="Counterfeit item or authenticity disclaimer"]').click()
        time.sleep(1)
    
        driver.find_element_by_id("btn_reason-code-3").click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//li[text()="Counterfeit, fake, or replica items"]').click()
        time.sleep(3)
        driver.find_element_by_id("continue").click()
        time.sleep(2)
        msg = driver.find_element_by_id("c3-msg")
        msg.send_keys('SomThing')
        driver.find_element_by_id("s0-0-29-49-send").click()
        time.sleep(5)
        driver.get(url)
        

    except:
        time.sleep(5)
        report()



def main():
    run()
    time.sleep(50)
    for i in range(0, counter):
        time.sleep(5)
        report()
        i += 1


if __name__ == "__main__":
    main()
