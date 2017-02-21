# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
driver = WebDriver()
driver.implicitly_wait(60)

def is_alert_present(driver):
    try:
        driver.switch_to_alert().text
        return True
    except:
        return False

try:
    driver.get("http://www.jared.com/FindAStoreView?storeId=10451&catalogId=10001&langId=-1")
    driver.find_element_by_id("input_location").click()
    driver.find_element_by_id("input_location").clear()
    driver.find_element_by_id("input_location").send_keys("44444")
    driver.find_element_by_id("findStoresBtn").click()
    if not ("Fashion Square" in driver.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
finally:
    driver.quit()
    if not success:
        raise Exception("Test failed.")
