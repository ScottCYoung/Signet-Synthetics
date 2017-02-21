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


        log_output("Starting @ http://www.kay.com/en/kaystore/searchterm/731434000/true/731434000")
        driver.get("http://www.kay.com/en/kaystore/searchterm/731434000/true/731434000")

        log_output("Click on first item to customize a ring - don't use /div")
        driver.find_element_by_partial_link_text("Family/Mother's Ring Round Birthstones Design in Silver or Gold").click()

        log_output("Start customizing ring")
        driver.find_element_by_xpath("//div[@class='m-vcb-content-html-modifier']//button[.='Start Customizing']").click()
        if not driver.find_element_by_xpath("//select[@id='configSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='configSelect']//option[2]").click()
        driver.find_element_by_id("btnStartCustomizing").click()

        log_output("Step - Select Metal Type")
        if not driver.find_element_by_xpath("//select[@id='metalTypeSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='metalTypeSelect']//option[2]").click()
        driver.find_element_by_id("next-step").click()


        log_output("Step - Stelect Stone Type")
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//select[@id='stoneTypeSelect']")).perform()
        if not driver.find_element_by_xpath("//select[@id='stoneTypeSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='stoneTypeSelect']//option[2]").click()


        log_output("Step - Click Next")
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//div[@id='tab-stoneType']//a[.='Next']")).perform()
        driver.find_element_by_xpath("//div[@id='tab-stoneType']//a[.='Next']")
        driver.find_element_by_xpath("//div[@id='tab-stoneType']//a[.='Next']").click()

        log_output("Step - Select Birth Stone")
        driver.find_element_by_css_selector("span.month_text").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[2]").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[1]").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/span[1]").click()
        if not driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").is_selected():
            driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul[2]/li[1]/label/input").click()
        driver.find_element_by_link_text("SELECT").click()
        driver.find_element_by_xpath("//a[@id='tab-index-2']//span[.='Select a Stone']").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-2']/div/ul[2]/li[2]/label/span[2]").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-2']/div/ul[2]/li[2]/label/span[1]").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-2']/div/ul[2]/li[2]/label/input").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-2']/div/ul[2]/li[2]/label/span[1]").click()
        if not driver.find_element_by_xpath("//div[@id='tab-stones-2']/div/ul[2]/li[2]/label/input").is_selected():
            driver.find_element_by_xpath("//div[@id='tab-stones-2']/div/ul[2]/li[2]/label/input").click()
        driver.find_element_by_link_text("SELECT").click()
        driver.find_element_by_xpath("//div[@id='tab-stones']//a[.='Next']").click()

        log_output("Step - Select Ring Size")
        if not driver.find_element_by_xpath("//select[@id='sizeSelect']//option[7]").is_selected():
            driver.find_element_by_xpath("//select[@id='sizeSelect']//option[7]").click()
        driver.find_element_by_xpath("//div[@id='tab-sizes']//a[.='Next']").click()

        log_output("Add to Cart and Checkout")
        driver.find_element_by_id("addToCart").click()
        driver.find_element_by_link_text("CHECKOUT").click()

    finally:
        driver.quit()
        if not success:
            raise Exception("Test failed.")

def main():
    syn_test_script()


if __name__ == '__main__':
    header('Kay - Customize Family Birthstone Ring')
    main()