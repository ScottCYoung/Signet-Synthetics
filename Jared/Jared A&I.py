# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://www.jared.com/en/jaredstore/searchterm/732541000/true/732541000%20and%20confirm%20all%20objects%20load")
    if not ("items" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
    if not ("Men's Cufflinks Titanium" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
    wd.find_element_by_xpath("//div[@id='product-grid']/div[1]/div/a/img").click()
    wd.find_element_by_id("btnStartCustomizing").click()
    wd.find_element_by_id("e_1").click()
    wd.find_element_by_id("e_1").clear()
    wd.find_element_by_id("e_1").send_keys("App")
    wd.find_element_by_xpath("//div[@id='engr']//a[.='Next']").click()
    wd.find_element_by_id("addToCart").click()
    wd.find_element_by_link_text("CHECKOUT").click()
    if not ("Shopping Bag (1 Item)" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
