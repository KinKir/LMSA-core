import sys
import time
sys.path.append('/Users/smccaffrey/Desktop/LMSA-core/src/')
import pandas as pd
from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from lmsa.lms.blackboard.BB_Editor import BB_Editor
from selenium import webdriver

filename = '/Users/smccaffrey/Desktop/PHY122_Fall2017_due_dates.csv'
p = 'PHY 122: University Physics Lab I (2017 Fall)-'
q = '2017Fall-T-PHY122-71848: PHY 122: University Physics Lab I (2017 Fall)'
df1 = pd.read_csv(filename, dtype=str, delimiter=',', header=None)
driver = webdriver.Chrome('/Users/smccaffrey/Projects/drivers/chromedriver')
BB_HOME = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'
MASTER_SITE = 'https://myasucourses.asu.edu/webapps/blackboard/execute/announcement?method=search&context=course&course_id=_366890_1&handle=cp_announcements&mode=cpview'

"""Change when ready to save changes"""
DRYRUN = False

"""Declare objects"""
institution = ASU_manipulator(driver)
form = BB_Editor(driver)

"""Login"""
institution.login()

driver.get(BB_HOME)
time.sleep(4)

"""Bulk Edit"""
i = 1
for i in range(1, len(df1[0])):
    driver.find_element_by_link_text('2017Fall-T-PHY122-' + str(df1[0][i]) + ': PHY 122: University Physics Lab I (2017 Fall)').click()
    print('Updating Section: ' + str(df1[0][i]))
    time.sleep(2)
    driver.find_element_by_xpath('//*[@title="MASTER SITE menu item options"]').click()
    time.sleep(2)
    driver.find_element_by_link_text('Web Link').click()
    time.sleep(2)
    driver.find_element_by_id('externalLinkUrlInputId').clear()
    time.sleep(1)
    driver.find_element_by_id('externalLinkUrlInputId').send_keys(MASTER_SITE)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="modifyExternalLinkFormSubmit"]').click()
    time.sleep(1)
    """Navigate Home"""
    driver.get(BB_HOME)
    time.sleep(3)
