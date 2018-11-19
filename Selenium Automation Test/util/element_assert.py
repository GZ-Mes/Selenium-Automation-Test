#coding = utf-8

class Test_assert():
	def __init__ (self,driver):
		self.driver = driver
	
	def Isdisplayed(self,element_type,element_value):
		if element_type == "id":
			return self.driver.find_element_by_id(element_value).is_displayed()
		
		elif element_type == "name":
			return self.driver.find_element_by_name(element_value).is_displayed()
		
		elif element_type == "class":
			return self.driver.find_element_by_class_name(element_value).is_displayed()
		
		elif element_type == "link":
			return self.driver.find_element_by_link_text(element_value).is_displayed()
		
		elif element_type == "xpath":
			return self.driver.find_element_by_xpath(element_value).is_displayed()