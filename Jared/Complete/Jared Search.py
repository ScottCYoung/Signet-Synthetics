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


        driver.get("http://www.jared.com/en/jaredstore")

        log_output("Searching for Engagement")
        driver.find_element_by_id("SimpleSearchForm_SearchTerm").click()
        driver.find_element_by_id("SimpleSearchForm_SearchTerm").clear()
        driver.find_element_by_id("SimpleSearchForm_SearchTerm").send_keys("Engagement")
        driver.find_element_by_id("searchButton").click()

        log_output("Verify text on page")
        if not ("Engagement" in driver.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")

    finally:
        driver.quit()
        if not success:
            raise Exception("Test failed.")

def main():
    syn_test_script()


if __name__ == '__main__':
    header('Jared Search')
    main()