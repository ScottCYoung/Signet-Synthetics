# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

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
        log_output("Testing www.xceligentpro.com")





    finally:
        driver.quit()
        if not success:
            raise Exception("Test failed.")

def main():
    syn_test_script()


if __name__ == '__main__':
    header('Industrial Search')
    main()