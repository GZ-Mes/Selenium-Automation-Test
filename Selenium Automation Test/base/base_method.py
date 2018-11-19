#coding=utf-8
'''
selenium操作浏览器方法、验证方法
'''
from selenium import webdriver
import time
import sys
sys.path.append(r"D:\Test_Work\Python\Python36-32\pyscripts\Selenium Automation Test")
from util.element_type import element_type
import datetime
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from util.operation_excel import Operexcel


class Selenium_base:
	"""操作Selenium-打开浏览器"""
	def __init__(self):
		pass

	#打开浏览器
	def open_browser(self,browser):

		if browser == "chrome":
			self.disable_run()
			self.driver = webdriver.Chrome(chrome_options=self.option)
		elif browser == "firefox":
			self.driver = webdriver.Firefox()
		elif browser == "ie":
			self.driver = webdriver.Ie()


	#Webdriver属性设置
	def disable_run(self):
		self.option = webdriver.ChromeOptions()
		#隐藏“Chrome正在受自动软件控制”
		self.option.add_argument("disable-infobars")
		#静默后台运行webdriver
		self.option.add_argument("headless")
	
	def get_driver(self):
		driver = self.driver
		return driver
	
	#打开url地址		
	def get_url(self,url):
		self.driver.get(url)
		return True

	#获取页面元素
	def get_element(self,element_data):
		try:
			element = element_type(self.driver)
			
			locator = element.EC_get(element_data)
			element_value = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
			return element_value
		except Exception as e:
			print ("Time out")
			print(format(e))   
			#return False
		
		#element_value = element.get(element_data)
		#test = EC.visibility_of_element_located(element_value)

		#print ("当前获取的元素:",element_value)

	

	#在该元素输入文本内容
	def element_send_keys(self,element_data,input_value):
		element = self.get_element(element_data)
		#获取Excel的数值会转为浮点数，需要判断转为整形
		try:
			if type(input_value) == float:
				input_value = int(input_value)
			#输入文本
			element.send_keys(input_value)

			return True
		except Exception as e:
			print("输入失败，Errormessage:",format(e))
		
			return False

	#点击事件
	def element_click(self,element_data):
		element = self.get_element(element_data)		
		try:
			element.click()
			time.sleep(0.5)
			return True
		except Exception as e:
			print("点击失败，Errormessage:",format(e))
			return False


	#清理输入框数据
	def input_clear(self,element_data):
		element = self.get_element(element_data)
		element.clear()


	#等待时间
	def sleep_time(self,seconds):
		time.sleep(seconds)
		return True

	#浏览器最大化
	def browser_size(self):
		self.driver.maximize_window()
		return True
	
	#切换到当前最新打开的窗口
	def get_handle(self):
		handles = self.driver.window_handles
		print (self.driver.switch_to_window(handles[-1]))
		return True

	#定位frame标签
	def get_frame(self,frame_element):
		self.driver.switch_to.frame(frame_element)

	#从frame中切回主页面
	def back_defaultcontent(self):
		self.driver.switch_to.default_content()
		#self.driver.switch_to.parent_frame()


	#新增cookie
	def add_cookie(self,cookie_data):
		if type(cookie_data) == str:
			cookie_data = json.loads(cookie_data)
		else:
			cookie_data = cookie_data

		self.driver.add_cookie(cookie_data)

	#刷新页面
	def refresh(self):
		self.driver.refresh()
		return True
	
	#关闭当前标签页
	def close_browser(self):
		self.driver.close()
		return True

    #关闭当前浏览器所有标签页
	def quit_browser(self):
		self.driver.quit()
		
    
	'''验证方法'''
    #检查页面
	def check_element(self,elementname):
		a = EC.title_contains(elementname)
		print ("检查页面是否正确：",a)

	#检查页面元素是否可见
	def check_is_visibility(self,element_data):
		element = element_type(self.driver)
		locator = element.EC_get(element_data)#(By_type,element_value)
		#获取元素失败时，获取异常提示，防止中断测试
		try:
			visibility = WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(locator))
			#WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(locator)(self.driver))
			#visibility = EC.visibility_of_element_located(locator)(self.driver)

			#print(visibility)
			if visibility:
				return True
			elif visibility == False:
				return False		
		
		except Exception as e:
			print("检查元素失败：",format(e))

			return False

	#检查当前页面所在的Url地址
	def check_url(self,except_url):
		now_url = self.driver.current_url
		print (now_url)
		print (except_url)
		if except_url == now_url:
			return True
		else:
			return False
	#检查页面的文字是否和预期一致
	def check_text(self,element_data,except_text):
		element = element_type(self.driver)
		locator = element.EC_get(element_data)#(By_type,element_value)
		#获取元素失败时，获取异常提示，防止中断测试
		try:
			now_text = WebDriverWait(self.driver, 20, 0.5).until(EC.text_to_be_present_in_element(locator,except_text))
			#WebDriverWait(self.driver, 20, 0.5).until(EC.text_to_be_present_in_element(locator)(self.driver))	
			#now_text = EC.text_to_be_present_in_element(locator,except_text)(self.driver)
			if  now_text:
				return True
			else:
				return False
		except Exception as e:
			print("检查文字失败：",format(e))
			return False


if __name__ == '__main__':
	Driver = Selenium_base()
	Driver.open_browser("chrome")
	Driver.get_url("http://www.gfs20.cn/admin/index.html")
	Driver.sleep_time(1)
	'''
	Driver.get_cookie({"name":"_qdda","value":"3-1.48l2he"})
	Driver.get_cookie({"name":"_qddab","value":"3-y96trv.jkrw4eng"})
	Driver.get_cookie({"name":"_qddac","value":"3-3-1.2wv18b.1kyi7.jkrumwto"})
	Driver.get_cookie({"name":"_qddamta_400963220","value":"3-0"})
	Driver.get_cookie({"name":"_qddaz","value":"QD.h02e7k.ni1dje.jimknmxn"})
	'''


	#Driver.get_cookie({"name":"ASP.NET_SessionId","value":"ixmw15kswtlvjbpxzoj3q1mb"})
	#Driver.get_cookie({"name":"CNZZDATA1261621935","value":"823353743-1534128465-http%253A%252F%252Fwww.gfs20.cn%252F%7C1534128465"})
	#Driver.get_cookie({"name":"GFS_USER_DATAS_AREA","value":"%E4%B8%9C%E5%9F%8E%E5%8C%BA"})
	#Driver.get_cookie({"name":"GFS_USER_DATAS_CITY","value":"%E5%8C%97%E4%BA%AC"})
	Driver.add_cookie({"name":"GFS_USER_DATAS_CITYTYPE","value":"1"})
	#Driver.get_cookie({"name":"GFS_USER_DATAS_CODE","value":""})

	Driver.add_cookie({"name":"GFS_USER_DATAS_NAME","value":"%E7%8E%8B%E8%80%81%E8%8F%8A"})
	
	#Driver.get_cookie({"name":"GFS_USER_DATAS_SCHOOL","value":"%E5%8C%97%E9%BC%BB%E4%B8%AD%E5%AD%A6"})


	Driver.add_cookie({"name":"GFS_USER_DATAS_PHONE","value":"15020180801"})
	Driver.add_cookie({"name":"GFS_USER_DATAS_TAKEON","value":"cc5e6234-91e7-4d2c-9968-fb4bcc85f6e0"})
	#Driver.get_cookie({"name":"tencentSig","value":"2154129408"})
	#Driver.get_cookie({"name":"UM_distinctid","value":"1641b495f6f3e8-055756140aef73-737356c-1fa400-1641b495f70bdc"})


	Driver.sleep_time(1)
	Driver.get_url("http://www.gfs20.cn/admin/index.html")
	Driver.browser_size()
	#Driver.refresh()



	'''
	管理后台测试demo
	Driver.get_url("http://apitest.gfs20.cn/iboss/login.aspx")
	Driver.element_send_keys("id==txtUserName","School035")
	Driver.element_send_keys("id==txtPassword","123456")
	Driver.element_click("id==btnSubmit")
	Driver.get_frame("mainframe")
	#Driver.browser_size()
	Driver.sleep_time(2)
	Driver.browser_size()
	#Driver.get_handle()
	Driver.element_send_keys("id==txtKeywords","hello")
	Driver.element_click("id==rptList_ctl01_Button1")
	Driver.get_screenshot()
	#Driver.sleep_time(3)
	#Driver.close_browser()
	'''