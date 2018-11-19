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
	    self.worksheet.set_column("B:B", 20)
	    self.worksheet.set_column("C:C", 20)
	    self.worksheet.set_column("D:D", 20)
	    self.worksheet.set_column("E:E", 20)
	    self.worksheet.set_column("G:G", 20)

	    #设置测试总况行的高度
	    self.worksheet.set_row(1, 30)
	    self.worksheet.set_row(2, 30)
	    self.worksheet.set_row(3, 30)
	    self.worksheet.set_row(4, 30)
	    self.worksheet.set_row(5, 30)



	    #设置字体加粗，文字大小
	    define_format_H1 = self.operation.get_format(self.workbook, {'bold': True, 'font_size': 18})
	    define_format_H2 = self.operation.get_format(self.workbook, {'bold': True, 'font_size': 14})
	    
	    define_format_H1.set_border(1)
	    define_format_H2.set_border(1)

	    #设置文本居中对齐
	    define_format_H1.set_align("center")
	    define_format_H2.set_align("center")

	    #设置背景颜色
	    define_format_H1.set_bg_color("#DCDCDC")	    
	    #define_format_H1.set_color("#00EC00")


	    # Create a new Chart object.
	    #合并单元格并添加设置的单元格属性
	    self.worksheet.merge_range('A1:F1', '测试报告总概况', define_format_H1)
	    self.worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
	    #self.worksheet.merge_range('A3:A6', '这里放图片', self.operation.get_format_center(self.workbook))
	    self.worksheet.merge_range('A4:A6', data['test_date'], self.operation.get_format_center(self.workbook))
	    
	    #写入单元格的常量数据
	    self.operation._write_center(self.worksheet, "A3", '测试日期', self.workbook)
	    self.operation._write_center(self.worksheet, "B3", '项目名称', self.workbook)
	    self.operation._write_center(self.worksheet, "B4", '运行环境', self.workbook)
	    self.operation._write_center(self.worksheet, "B5", '客户端环境', self.workbook)
	    self.operation._write_center(self.worksheet, "B6", '测试执行时长', self.workbook)


	    #data = {"test_name": "社区论坛", "test_version": "测试环境", "test_pl": "Chrome", "test_date": "2018-10-10 12:10"}
	    self.operation._write_center(self.worksheet, "C3", data['test_name'], self.workbook)
	    self.operation._write_center(self.worksheet, "C4", data['test_version'], self.workbook)
	    self.operation._write_center(self.worksheet, "C5", data['test_pl'], self.workbook)
	    self.operation._write_center(self.worksheet, "C6", data['run_time'], self.workbook)

	    self.operation._write_center(self.worksheet, "D3", "用例总数", self.workbook)
	    self.operation._write_center(self.worksheet, "D4", "通过总数", self.workbook)
	    self.operation._write_center(self.worksheet, "D5", "失败总数", self.workbook)
	    self.operation._write_center(self.worksheet, "D6", "错误总数", self.workbook)



	    #data = {"test_sum": 100, "test_success": 80, "test_failed": 5, "test_error": 5}
	    self.operation._write_center(self.worksheet, "E3", data['test_sum'], self.workbook)
	    self.operation._write_center(self.worksheet, "E4", data['test_success'], self.workbook)
	    self.operation._write_center(self.worksheet, "E5", data['test_failed'], self.workbook)
	    self.operation._write_center(self.worksheet, "E6", data['test_error'], self.workbook)

	    self.operation._write_center(self.worksheet, "F3", "通过率", self.workbook)


	    self.worksheet.merge_range('F4:F6', data['pass_rate'], self.operation.get_format_center(self.workbook))

	    #生成柱状图
	    self.graph(self.workbook, self.worksheet,'column',"A9")
	    #生成饼状图
	    self.graph(self.workbook, self.worksheet,'pie',"A24")
	    self.workbook.close()
	
	# 生成图表
	def graph(self,workbook, worksheet,graphtype,index):
		chart1 = workbook.add_chart({'type': graphtype})
		chart1.add_series({
		'name':       'Web功能测试统计',
		'categories':'=测试总况!$D$4:$D$6',
		'values':    '=测试总况!$E$4:$E$6',
		"points":[
		{"fill":{"color":"#00CD00"}},
        {"fill":{"color":"red"}},
        {"fill":{"color":"yellow"}}]
   		})
		chart1.set_title({'name': '结果统计'})
		chart1.set_style(10)
		#位置极大小
		worksheet.insert_chart(index, chart1, {'x_offset': 25, 'y_offset': 10})

if __name__ == '__main__':
	run_time = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
	test1 = Data(run_time)
	test1.total_situation()