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
    wd.get("http://www.jared.com/en/jaredstore/")
    wd.find_element_by_link_text("Engagement").click()
    if not ("Engagement" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
    if not wd.find_element_by_id("facet_checkbox8").is_selected():
        wd.find_element_by_id("facet_checkbox8").click()
    wd.find_element_by_id("view-more").click()
    wd.find_element_by_link_text("VAULT VALUE
                        			
								
							
                        
							Vera Wang LOVE 1 Carat tw Diamonds 14K White Gold Ring 
								
							 
						
						
										
											$3,299.99
										
										
											$2,499.99 (24% off)").click()
    if not ("Vera Wang LOVE 1 Carat tw Diamonds 14K White Gold Ring" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
    wd.find_element_by_id("addToCartBtn").click()
    wd.find_element_by_link_text("CHECKOUT").click()
    if not ("Shopping Bag (1 Item)" in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
