# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

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
        driver.implicitly_wait(60)
        log_output("Starting @ http://www.kay.com/en/kaystore")

        driver.get("http://www.kay.com/en/kaystore")
        driver.find_element_by_id("site-search__input").click()
        driver.find_element_by_id("site-search__input").clear()
        driver.find_element_by_id("site-search__input").send_keys("engagement")
        driver.find_element_by_id("searchButton").click()
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
    header('Kay - Engagement Search')
    main()