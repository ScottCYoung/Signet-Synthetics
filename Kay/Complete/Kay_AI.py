# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time
from selenium.webdriver.common.action_chains import ActionChains


def header(data):
    print("\n" + '------------------------------------------')
    print("   {}").format(data)
    print('------------------------------------------')
    print('')


def log_output(data):
    print("\t" + data)


def syn_test_script():
    try:
        success = True
        driver = WebDriver()
        driver.implicitly_wait(30)
        # Disabled page sizing and instead used action chains to move mouse around
        # driver.set_window_size(1920, 1080)


        # Use Action chains to navigate page when there is an issue with the selection menus
        # If the menu item does not appear to select, it means there was a page movement that happened
        # out of sync with the action.


        log_output("Starting @ http://www.kay.com/en/kaystore/searchterm/732541000/true/732541000")
        driver.get("http://www.kay.com/en/kaystore/searchterm/732541000/true/732541000")

        log_output("Verify Search Results on page")
        html_text = driver.find_element_by_tag_name("html").text
        if not ("Home Search Results" in html_text):
            success = False
            print("verifyTextPresent failed")

        log_output("Click on first item - using div tag")
        driver.find_element_by_xpath("//div[@id='product-grid']/div[1]/div/a/h3").click()

        log_output("Start customizing ring")
        driver.find_element_by_xpath(
            "//div[@class='m-vcb-content-html-modifier']//button[.='Start Customizing']").click()

        log_output("Choose number of stones and birth Stone")

        if not driver.find_element_by_xpath("//select[@id='birthStoneSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='birthStoneSelect']//option[2]").click()
        driver.find_element_by_id("btnStartCustomizing").click()

        log_output("Step - Select Stone Type")
        ActionChains(driver).move_to_element(driver.find_element_by_css_selector("span.month_text")).perform()
        driver.find_element_by_css_selector("span.month_text").click()
        driver.find_element_by_xpath("//div[@id='tab-stones-1']/div/ul/li[1]/label").click()
        if not driver.find_element_by_name("stoneId1").is_selected():
            driver.find_element_by_name("stoneId1").click()
        driver.find_element_by_link_text("SELECT").click()
        driver.find_element_by_xpath("//div[@id='cs']//a[.='Next']").click()

        log_output("Step - Select Metal Type")
        if not driver.find_element_by_xpath("//select[@id='metalTypeSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='metalTypeSelect']//option[2]").click()
        log_output("clicking next")
        driver.find_element_by_xpath("//div[@id='m']//a[.='Next']").click()

        log_output("Step - Select ring size")
        if not driver.find_element_by_xpath("//select[@id='sizeSelect']//option[2]").is_selected():
            driver.find_element_by_xpath("//select[@id='sizeSelect']//option[2]").click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//div[@id='rs']//a[.='Next']")).perform()
        next_click = driver.find_element_by_xpath("//div[@id='rs']//a[.='Next']")
        next_click.click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//div[@id='engr']//a[.='Next']")).perform()
        driver.find_element_by_xpath("//div[@id='engr']//a[.='Next']").click()

        log_output("Step - Add item to bag")
        driver.find_element_by_id("addToCart").click()
        # driver.find_element_by_link_text("ADD TO BAG").click()


        log_output("Step - Goto Checkout")
        driver.find_element_by_link_text("CHECKOUT").click()

        log_output("Verify text on page - Shopping Bag")
        html_text = driver.find_element_by_tag_name("html").text
        if not ("Shopping Bag" in html_text):
            success = False
            print("verifyTextPresent failed")



    finally:
        driver.quit()
        if not success:
            raise Exception("Test failed.")


def main():
    syn_test_script()


if __name__ == '__main__':
    header('Kay A&I')
    main()
