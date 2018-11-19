#coding = utf-8
#by:Mes
#data:2018/10/26
#version:1.0.0
import sys
sys.path.append(r"D:\Test_Work\Python\Python36-32\pyscripts\Selenium Automation Test")
from util.operation_excel import Operexcel
from base.base_method import Selenium_base

import os
import time
import datetime
from util.other import otherutil
from test_report.config import Data

pass_count = []
fail_count = []
error_count = []
run_count = []

class Runmain:
	def __init__(self,filepath=None,sheet_id=None):
	
		self.traversal = Operexcel(filepath,sheet_id)		
		self.execute = Selenium_base()
		self.ou = otherutil() 


	#遍历Execl表用例
	def traversal_excel(self):

		case_lines = self.traversal.get_lines()
		for row in range(1,case_lines):
			#是否运行
			is_run = self.traversal.get_cell_value(row,4)
			#调用方法
			method = self.traversal.get_cell_value(row,5)

			if is_run == "yes" and method != "":				
				#记录执行用例的总数
				run_count.append(row)
				#步骤id
				self.stepid = self.traversal.get_cell_value(row,2)					
				#用例执行的时间间隔
				time.sleep(1.5)
								
				#定位元素
				element = self.traversal.get_cell_value(row,6)
				#输入参数
				input_value = self.traversal.get_cell_value(row,7)
				#print (method,element,input_value)
				
				#根据操作的执行结果写入Excel
				execute_result = self.execute_method(method,element,input_value)
				
				#获取driver
				driver = self.execute.get_driver()
				self.driver = self.execute.get_driver()
				if execute_result == True:
					self.traversal.write_value(row,12,"Pass")
					#截取用例通过的页面
					self.ou.get_screenshot(self.driver,"Pass",self.stepid)
					#记录测试通过的行号
					pass_count.append(row)
				
				elif execute_result == False:
					self.traversal.write_value(row,12,"Error")
					#截取用例失败的页面
					self.ou.get_screenshot(self.driver,"Error",self.stepid)
					#记录测试错误行号
					error_count.append(row)				
			#判断是否需要验证测试
			self.verify_method(is_run,row)

	
	#调用验证方法
	def verify_method(self,is_run,row):
		#验证方法
		verify_method = self.traversal.get_cell_value(row,8)

		if is_run == "yes" and verify_method != "":
			#记录执行用例的总数
			run_count.append(row)
			#验证元素
			verify_element = self.traversal.get_cell_value(row,9) 
			#验证参数
			verify_value = self.traversal.get_cell_value(row,10)
			#验证描述
			verify_describe = self.traversal.get_cell_value(row,11)
			#测试结果
			test_result = self.traversal.get_cell_value(row,12)

			verify_result = self.execute_method(verify_method,verify_element,verify_value)
			#print (verify_method,verify_result)


			#根据校验结果写入Excel
			if verify_result == True:
				self.traversal.write_value(row,13,"Pass")
				#截取用例通过的页面
				self.ou.get_screenshot(self.driver,"Pass",self.stepid)
				#记录测试通过的行号
				pass_count.append(row)
			
			elif verify_result == False:
				self.traversal.write_value(row,13,"Fail")
				#截取用例失败的页面
				self.ou.get_screenshot(self.driver,"Fail",self.stepid)
				#记录测试失败的行号
				fail_count.append(row)
	#执行方法
	def execute_method(self,method,element=None,input_value=None):

		#把获取的字符串，转化为方法调用，根据方法的形参传入实参
		action_function = getattr(self.execute,method)
		if input_value == "" and element == "":
			return action_function()		
		elif element == "":	
			return action_function(input_value)

		elif input_value == "":
			return action_function(element)

		else:
			return action_function(element,input_value)

	def insert_data(self):
		global pass_count
		global fail_count
		global error_count
		global run_count
		global run_time
		run_count = len(run_count) - 2 #减去开启和关闭浏览器
		pass_count = len(pass_count)
		fail_count = len(fail_count)
		error_count = len(error_count)
		pass_rate = format(pass_count/run_count,'0.1%')
		run_time = str(run_time) + "秒"
		print ("用例执行总数：",run_count)
		print ("测试通过总数：",pass_count)
		print ("测试失败总数：",fail_count)
		print ("测试错误总数：",error_count)
		print ("测试执行时长：",run_time)
		print ("测试通过率：",pass_rate)	 
		
		data = {
		 		"test_name": "社区论坛", 
		 		"test_version": "测试环境", 
		 		"test_pl": "Chrome", 
		 		"test_date": exe_time,
		 		"test_sum": run_count, 
		 		"test_success": pass_count, 
		 		"test_failed": fail_count,
		 		"test_error": error_count,
		 		"pass_rate":pass_rate,
		 		"run_time":run_time
		 		 }
		
		return data

if __name__ == '__main__':
	 #计算开始时间
	 starttime = datetime.datetime.now()
	 exe_time = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')

	 Execute_main_3 = Runmain(filepath = "../dataconfig/Testcase.xls",
	 							sheet_id = 2)
	 Execute_main_3.traversal_excel()

	 endtime = datetime.datetime.now()
	 run_time = (endtime - starttime).seconds
	 
	 #生成报告
	 report = Data(exe_time)
	 #预备测试报告的数据
	 data = Execute_main_3.insert_data()
	 #生成测试概况
	 report.total_situation(data)
