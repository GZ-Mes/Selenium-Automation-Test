import unittest 
from main import Runmain
#coding = utf-8
import sys
sys.path.append(r"D:\Test_Work\Python\Python36-32\pyscripts\Selenium Automation Test")
from util.operation_excel import Operexcel
from base.base_method import Selenium_base

import os
import HTMLTestRunner
import time

class RunTestmain:
	def __init__(self,filepath= "../dataconfig/Testcase.xls",
					  sheet_id= 2):
		
		self.traversal = Operexcel(filepath,sheet_id)
		self.execute = Selenium_base()
		self.traversal_excel()

	#遍历Execl表用例
	def traversal_excel(self):
		case_lines = self.traversal.get_lines()
		for row in range(1,case_lines):
			#是否运行
			is_run = self.traversal.get_cell_value(row,4)
			#调用方法
			method = self.traversal.get_cell_value(row,5)
			print (method,self.traversal.get_cell_value(row,2))

			if is_run == "yes" and method != "":				
				#用例执行的时间间隔
				time.sleep(1.5)
								
				#定位元素
				element = self.traversal.get_cell_value(row,6)
				#输入参数
				input_value = self.traversal.get_cell_value(row,7)
				#print (method,element,input_value)
			
				self.execute_method(method,element,input_value)
			#判断是否需要验证测试
			self.verify_method(row)
	
	#调用验证方法
	def verify_method(self,row):
		#验证方法
		verify_method = self.traversal.get_cell_value(row,8)

		if verify_method != "":
			#验证元素
			verify_element = self.traversal.get_cell_value(row,9) 
			#验证参数
			verify_value = self.traversal.get_cell_value(row,10)
			#验证描述
			verify_describe = self.traversal.get_cell_value(row,11)
			#测试结果
			test_result = self.traversal.get_cell_value(row,12)

			self.execute_method(verify_method,verify_element,verify_value)

	#执行方法
	def execute_method(self,method,element=None,input_value=None):
		#把获取的字符串，转化为方法调用，根据方法的形参传入实参
		action_function = getattr(self.execute,method)
		if input_value == "" and element == "":
			action_function()
		elif element == "":

			action_function(input_value)
		elif input_value == "":
			action_function(element)
		else:
			action_function(element,input_value)
class Testcase(unittest.TestCase):
	def setUp(self):
		print ("Start")

	def test_Web(self):
	 	Execute_main_3 = Runmain(filepath = "../dataconfig/Testcase.xls",
	 							sheet_id = 2)
	 	Execute_main_3.traversal_excel()
	 	print ("running")		

	def tearDown(self):
		print ("Over")

if __name__ == '__main__':
	 #Execute_main= Runmain()
	 #Execute_main.traversal_excel()
	 '''
	 Execute_main_two = Runmain(filepath = "../dataconfig/Testcase.xls",
	 							sheet_id = 1)
	 Execute_main_two.traversal_excel()
	 '''
	 #Execute_main_3 = Runmain(filepath = "../dataconfig/Testcase.xls",
	 #							sheet_id = 2)
	 #Execute_main_3.traversal_excel()

	 #suite = Testcase()

	 #suite.addTest(RunTestmain("../dataconfig/Testcase.xls",2))
	 unittest.main()

