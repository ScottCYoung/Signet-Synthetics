# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time
from selenium.webdriver.common.action_chains import ActionChains


def header(data):
    print("\n" +'------------------------------------------')
    print("   {}").format(data)
    print('------------------------------------------')
    print('')


def log_output(data):
    print("\t" +data)


def syn_test_script():

    try:
        success = True
        driver = WebDriver()
        driver.implicitly_wait(30)
        # Disabled page sizing and instead used action chains to move mouse around
        #driver.set_window_size(1920, 1080)


        # Use Action chains to navigate page when there is an issue with the selection menus
        # If the menu item does not appear to select, it means there was a page movement that happened
        # out of sync with the action.

        #------Insert Script between these lines-----#
        driver.get("http://www.jared.com/en/jaredstore/searchterm/731434000/true/731434000")

        # Search HTML for text to verify page
        log_output("Step - Verify Search worked")
        if not ("items" in driver.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")

        log_output("Step - Select item via partial link text")
        driver.find_element_by_partial_link_text("Mother's Bracelet Round Birthstones Design in Silver").click()

        log_output("Start customizing Jewelery")

        log_output("    Select Number of stones (1)")
        if not driver.find_element_by_xpath("//select[@id='configSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='configSelect']//option[2]").click()
        driver.find_element_by_id("btnStartCustomizing").click()

        log_output("    Select metal type")
        if not driver.find_element_by_xpath("//select[@id='metalTypeSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='metalTypeSelect']//option[2]").click()
        driver.find_element_by_id("next-step").click()

        log_output("    Select stone type")
        if not driver.find_element_by_xpath("//select[@id='stoneTypeSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='stoneTypeSelect']//option[2]").click()
        driver.find_element_by_xpath("//div[@id='tab-stoneType']//a[.='Next']").click()

        log_output("    Select birthstone")
        driver.find_element_by_css_selector("span.month_text").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[2]").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[1]").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[1]").click()
        if not driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").is_selected():
            driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").click()
        driver.find_element_by_link_text("SELECT").click()
        driver.find_element_by_xpath("//div[@id='tab-stones']//a[.='Next']").click()
        driver.find_element_by_id("addToCart").click()
        driver.find_element_by_link_text("CHECKOUT").click()
        if not ("Shopping Bag (1 Item)" in driver.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")



        #------Insert Script between these lines-----#


    finally:
        driver.quit()
        if not success:
            raise Exception("Test failed.")

def main():
    syn_test_script()


if __name__ == '__main__':
    header('Jared Search')
    main()