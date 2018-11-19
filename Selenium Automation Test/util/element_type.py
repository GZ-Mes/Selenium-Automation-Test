#coding = utf-8
#管理不同类型的页面元素
import sys
sys.path.append(r"D:\Test_Work\Python\Python36-32\pyscripts\Selenium Automation Test\util")
from util.element_assert import Test_assert
from selenium.webdriver.common.by import By

class element_type:
	def __init__ (self,driver):
		self.driver = driver
		self.Test_assert = Test_assert(self.driver)

	def get(self,element_data):
		#"id==btnSubmit"分割字符串
		element_type = element_data.split("==")[0]
		element_value = element_data.split("==")[1]
		
		try: 

			if element_type == "id":
					
				return self.driver.find_element_by_id(element_value)
				
			elif element_type == "name":

				return self.driver.find_element_by_name(element_value)
				
			elif element_type == "class":

				return self.driver.find_element_by_class_name(element_value)
				
			elif element_type == "link":

				return self.driver.find_element_by_link_text(element_value)
				
			elif element_type == "xpath":

				return self.driver.find_element_by_xpath(element_value)
		except Exception as e:
			print("获取元素失败，message:",format(e))
	def EC_get(self,element_data):
		
		element_type = element_data.split("==")[0]
		element_value = element_data.split("==")[1]
		if element_type == "id":
			return By.ID,element_value
				
		elif element_type == "name":
			return By.NAME,element_value
				
		elif element_type == "class":
			return By.CLASS_NAME,element_value
				
		elif element_type == "link":
			return By.LINK_TEXT,element_value
				
		elif element_type == "xpath":
			return By.XPATH,element_value