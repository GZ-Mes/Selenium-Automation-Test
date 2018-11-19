#coding=utf-8
'''
操作excel表格
by:Mes
'''
import xlrd
from xlutils.copy import copy

class Operexcel:
	def __init__ (self,filepath=None,sheet_id=None):
		if filepath == None:
			self.filepath = "../dataconfig/Testcase.xls"
			self.sheet_id = 0

		else:
			self.filepath = filepath
			self.sheet_id = sheet_id
			
		
		self.sheet = self.open_sheet()
		
	#打开excel表格并打开指定的工作薄
	def open_sheet(self):
		self.workbook = xlrd.open_workbook(self.filepath,formatting_info=True)
		sheet = self.workbook.sheets()[self.sheet_id]
		return sheet

	#获取excel表的总行数
	def get_lines(self):
		tables = self.sheet
		return tables.nrows

	#获取单元格内的内容
	def get_cell_value(self,row,col):
		tables = self.sheet
		return tables.cell_value(row,col)

	#写入单元格数据
	def write_value(self,row,col,value):
		self.workbook = xlrd.open_workbook(self.filepath,formatting_info=True)
		#tables = self.sheet
		write_data = copy(self.workbook)
		sheet_data = write_data.get_sheet(self.sheet_id)
		sheet_data.write(row,col,value)
		write_data.save(self.filepath)
		self.workbook = xlrd.open_workbook(self.filepath,formatting_info=True)
		#read_data =  xlrd.open_workbook(self.filepath)



if __name__ == '__main__':
	operation = Operexcel()
	print (operation.write_value(7,2,"Hello,World"))
	print (operation.get_cell_value(7,2))