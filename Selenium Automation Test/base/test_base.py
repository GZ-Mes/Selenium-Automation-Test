#coding=utf-8
from selenium import webdriver
import time
import os
'''
os_filepath = os.path.dirname(__file__)
project_path =  os.path.dirname(os_filepath)
project_path = project_path.replace("\\","/")
print(project_path)
'''

driver = webdriver.Chrome()

driver.get("http://apitest.gfs100.cn/iboss/login.aspx")
driver.find_element_by_id("txtUserName")
driver.maximize_window()
time.sleep(0.5)
driver.get_screenshot_as_file\
(r"../test_report/error_screenshot/登录页3.png")
#.send_keys("School035")
#driver.find_element_by_id("txtPassword").send_keys("123456")
#driver.find_element_by_id("btnSubmit").click()
