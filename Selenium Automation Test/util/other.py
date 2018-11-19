#coding=utf-8
import sys
sys.path.append(r"D:\Test_Work\Python\Python36-32\pyscripts\Selenium Automation Test")
import datetime

class otherutil:
	def __init__(self):
		pass

	#截图
	def get_screenshot(self,driver,screen_type,stepid):
		now_time = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
		self.driver = driver
		print (stepid)
		if screen_type == "Pass":
			filepath = r"../test_report/Pass_screenshot/" +  stepid + "~" +  now_time + ".png"
		
		elif screen_type == "Fail":
			filepath = r"../test_report/Fail_screenshot/" +  stepid + "~" + now_time + ".png"
		
		elif screen_type == "Error":
			filepath = r"../test_report/error_screenshot/" +  stepid + "~" + now_time + ".png"

		self.driver.get_screenshot_as_file(filepath)
if __name__ == '__main__':
	ot = otherutil()
	ot.get_screenshot("error","step1")