#coding:utf-8
import sys
sys.path.append(r"D:\Test_Work\Python\Python36-32\pyscripts\Selenium Automation Test")

import datetime
import xlsxwriter
from util.WriteReport import excel_style


class Data:
	"""
	   配置测试报告的格式的常量数据
	   调用excel风格样式的方法
	"""
	def __init__(self,runtime):
		filename = "TestReport" + "-" + runtime + ".xlsx"
		filepath = "../test_report/" + filename
		self.workbook = xlsxwriter.Workbook(filepath)
		self.worksheet = self.workbook.add_worksheet("测试总况")
		#worksheet2 = self.workbook.add_worksheet("测试详情")
		self.operation = excel_style()
	
	def total_situation(self,data=None):
	    #设置测试总况的列行的宽度
	    self.worksheet.set_column("A:A", 20)
	    self.worksheet.set_column("B:B", 15)
	    self.worksheet.set_column("C:C", 15)
	    self.worksheet.set_column("D:D", 15)
	    self.worksheet.set_column("E:E", 15)
	    self.worksheet.set_column("F:F", 15)
	    self.worksheet.set_column("G:G", 15)
	    self.worksheet.set_column("H:H", 15)
	    self.worksheet.set_column("I:I", 15)
	    self.worksheet.set_column("J:J", 15)

	    #设置测试总况行的高度
	    self.worksheet.set_row(1, 30)
	    self.worksheet.set_row(2, 30)
	    self.worksheet.set_row(3, 30)
	    self.worksheet.set_row(4, 30)
	    self.worksheet.set_row(5, 30)

	    #设置字体加粗，文字大小
	    define_format_H1 = self.operation.get_format(self.workbook, {'bold': True, 'font_size': 18})
	    
	    define_format_H1.set_border(1)

	    #设置文本居中对齐
	    define_format_H1.set_align("center")

	    #设置背景颜色
	    define_format_H1.set_bg_color("#DCDCDC")	    

	    # Create a new Chart object.
	    #合并单元格并添加设置的单元格属性
	    self.worksheet.merge_range('A1:J1', '测试报告', define_format_H1)

	    #写入单元格的常量数据
	    self.operation._write_center(self.worksheet, "A2", '测试日期', self.workbook)
	    self.operation._write_center(self.worksheet, "B2", '项目名称', self.workbook)
	    self.operation._write_center(self.worksheet, "C2", '运行环境', self.workbook)
	    self.operation._write_center(self.worksheet, "D2", '客户端环境', self.workbook)
	    self.operation._write_center(self.worksheet, "E2", '测试执行时长', self.workbook)
	    self.operation._write_center(self.worksheet, "F2", "用例总数", self.workbook)
	    self.operation._write_center(self.worksheet, "G2", "通过总数", self.workbook)
	    self.operation._write_center(self.worksheet, "H2", "失败总数", self.workbook)
	    self.operation._write_center(self.worksheet, "I2", "错误总数", self.workbook)
	    self.operation._write_center(self.worksheet, "J2", "通过率", self.workbook)

	    self.operation._write_center(self.worksheet, "A3", data['test_date'], self.workbook)
	    self.operation._write_center(self.worksheet, "B3", data['test_name'], self.workbook)
	    self.operation._write_center(self.worksheet, "C3", data['test_version'], self.workbook)
	    self.operation._write_center(self.worksheet, "D3", data['test_pl'], self.workbook)
	    self.operation._write_center(self.worksheet, "E3", data['run_time'], self.workbook)
	    self.operation._write_center(self.worksheet, "F3", data['test_sum'], self.workbook)
	    self.operation._write_center(self.worksheet, "G3", data['test_success'], self.workbook)
	    self.operation._write_center(self.worksheet, "H3", data['test_failed'], self.workbook)
	    self.operation._write_center(self.worksheet, "I3", data['test_error'], self.workbook)
	    self.operation._write_center(self.worksheet, "J3", data['pass_rate'], self.workbook)

	    #生成柱状图
	    self.graph(self.workbook, self.worksheet,'column',"A4")
	    #生成饼状图
	    self.graph(self.workbook, self.worksheet,'pie',"F4")
	    self.workbook.close()
	
	# 生成图表
	def graph(self,workbook, worksheet,graphtype,index):
		chart1 = workbook.add_chart({'type': graphtype})
		chart1.add_series({
		'name':       'Web功能测试统计',
		'categories':'=测试总况!$G$2:$I$2',
		'values':    '=测试总况!$G$3:$I$3',
		"points":[
		{"fill":{"color":"#00CD00"}},
        {"fill":{"color":"red"}},
        {"fill":{"color":"yellow"}}]
   		})
		chart1.set_title({'name': '测试结果统计'})
		chart1.set_style(10)
		#位置极大小
		worksheet.insert_chart(index, chart1, {'x_offset': 25, 'y_offset': 10})

if __name__ == '__main__':
	run_time = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
	test1 = Data(run_time)
	test1.total_situation()