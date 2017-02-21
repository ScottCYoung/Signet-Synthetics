# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time

#included to support waiting for item
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


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


        log_output("Starting @ http://www.kay.com/en/kaystore")
        driver.get("http://www.kay.com/en/kaystore")

        log_output("Navigating to Engagement Rings")
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//div[3]/div[2]/div/div/div[3]/nav/div/ul/li[4]/a[2]")).perform()
        driver.find_element_by_xpath("//div[3]/div[2]/div/div/div[3]/nav/div/ul/li[4]/ul/li[2]/div/div/div[2]/ul/li[2]/ul/li/ul/li[1]/a").click()

        time.sleep(2)
        if not ("Engagement" in driver.find_element_by_tag_name("html").text):
            success = False
            print("Did not find word engagement on page in reasonable time")

        log_output("Changing price range to 3rd facet")
        if not driver.find_element_by_id("facet_checkbox7").is_selected():
            driver.find_element_by_id("facet_checkbox7").click()
        time.sleep(3)

        log_output("Viewing more rings")
        driver.find_element_by_id("view-more").click()

        log_output("Select a nice ring")
        driver.find_element_by_xpath("//div[3]/div[2]/div/div/div[4]/div[7]/div[2]/div[2]/div[7]/div[37]/div/a/img").click()

        #log_output("starting timer")
        #time.sleep(5)
        log_output("Add Ring to bag")
        # There is a bit of funkiness with this Product page and the overlay when you add an item to Cart
        # Sometimes the addToCartBtn is not immediately available and can time out or error out
        # The 5 second sleep timer above is disabled, but if we see issues this may need re-anabled
        # or use WebDriverWait
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[@id='addToCartBtn']")).perform()
        driver.find_element_by_xpath("//a[@id='addToCartBtn']")
        driver.find_element_by_xpath("//a[@id='addToCartBtn']").click()

        log_output("Adding coverage")
        driver.find_element_by_link_text("ADD TO BAG").click()

        log_output("Checking out with a beautiful ring!")
        driver.find_element_by_link_text("CHECKOUT").click()
        if not ("Shopping Bag (1 Item)" in driver.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")

    finally:
        driver.quit()
        if not success:
            raise Exception("Test failed.")

def main():
    syn_test_script()


if __name__ == '__main__':
    header('Kay - Engagement Add to Cart')
    main()