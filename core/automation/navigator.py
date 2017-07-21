#!/usr/bin/env python
#-*- coding: utf-8 -*-

import selenium
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Navigator(object):

    def __init__(self, driver):
        self.driver = driver

    class SideBar(Navigator):

        def __init__(self, driver):
            self.driver = driver

        def navigate_to(self, element, wait = None):
            try:
                self.driver.find_element_by_link_text(element).click()
                time.sleep(wait)
            except Exception as e:
                pass

    class SectionSelector(Navigator):

        def __init__(self, driver):
            self.driver = driver

        def find_section(self, module, section, wait = None):
            try:
                self.driver.find_element_by_link_text(module + section).click()
                time.sleep(wait)
            except:
                pass
