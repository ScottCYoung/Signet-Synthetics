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
    wd.get("http://www.jared.com/en/jaredstore/searchterm/731434000/true/731434000")
    if not ("items" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
    wd.find_element_by_partial_link_text("Mother's Bracelet Round Birthstones Design in Silver").click()
    if not wd.find_element_by_xpath("//select[@id='configSelect']//option[2]").is_selected():
        wd.find_element_by_xpath("//select[@id='configSelect']//option[2]").click()
    wd.find_element_by_id("btnStartCustomizing").click()
    if not wd.find_element_by_xpath("//select[@id='metalTypeSelect']//option[2]").is_selected():
        wd.find_element_by_xpath("//select[@id='metalTypeSelect']//option[2]").click()
    wd.find_element_by_id("next-step").click()
    if not wd.find_element_by_xpath("//select[@id='stoneTypeSelect']//option[2]").is_selected():
        wd.find_element_by_xpath("//select[@id='stoneTypeSelect']//option[2]").click()
    wd.find_element_by_xpath("//div[@id='tab-stoneType']//a[.='Next']").click()
    wd.find_element_by_css_selector("span.month_text").click()
    wd.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[2]").click()
    wd.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[1]").click()
    wd.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").click()
    wd.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[1]").click()
    if not wd.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").is_selected():
        wd.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").click()
    wd.find_element_by_link_text("SELECT").click()
    wd.find_element_by_xpath("//div[@id='tab-stones']//a[.='Next']").click()
    wd.find_element_by_id("addToCart").click()
    wd.find_element_by_link_text("CHECKOUT").click()
    if not ("Shopping Bag (1 Item)" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
