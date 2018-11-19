# -*- coding: utf-8 -*-
import xlsxwriter

class excel_style:
    def __init__(self):
        pass

    #设置单元格格式
    def get_format(self,wd, option={}):
        return wd.add_format(option)

    # 设置居中
    def get_format_center(self,wd,num=1):
        return wd.add_format({'align': 'center','valign': 'vcenter','border':num})
    
    def set_border_(self,wd, num=1):
        return wd.add_format({}).set_border(num)

    # 写数据
    def _write_center(self,worksheet, cl, data, wd):
        return worksheet.write(cl, data, self.get_format_center(wd))

    def test_detail(self,worksheet):

        # 设置列行的宽高
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)
        worksheet.set_column("H:H", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)
        worksheet.set_row(7, 30)



        worksheet.merge_range('A1:H1', '测试详情', self.get_format(workbook, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': 'blue', 'font_color': '#ffffff'}))
        self._write_center(worksheet, "A2", '用例ID', workbook)
        self._write_center(worksheet, "B2", '接口名称', workbook)
        self._write_center(worksheet, "C2", '接口协议', workbook)
        self._write_center(worksheet, "D2", 'URL', workbook)
        self._write_center(worksheet, "E2", '参数', workbook)
        self._write_center(worksheet, "F2", '预期值', workbook)
        self._write_center(worksheet, "G2", '实际值', workbook)
        self._write_center(worksheet, "H2", '测试结果', workbook)

        data = {"info": [{"t_id": "1001", "t_name": "登陆", "t_method": "post", "t_url": "http://XXX?login", "t_param": "{user_name:test,pwd:111111}",
                          "t_hope": "{code:1,msg:登陆成功}", "t_actual": "{code:0,msg:密码错误}", "t_result": "失败"}, {"t_id": "1002", "t_name": "商品列表", "t_method": "get", "t_url": "http://XXX?getFoodList", "t_param": "{}",
                          "t_hope": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_actual": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_result": "成功"}],
                "test_sum": 100,"test_success": 20, "test_failed": 80}
        temp = 4
        for item in data["info"]:
            self._write_center(worksheet, "A"+str(temp), item["t_id"], workbook)
            self._write_center(worksheet, "B"+str(temp), item["t_name"], workbook)
            self._write_center(worksheet, "C"+str(temp), item["t_method"], workbook)
            self._write_center(worksheet, "D"+str(temp), item["t_url"], workbook)
            self._write_center(worksheet, "E"+str(temp), item["t_param"], workbook)
            self._write_center(worksheet, "F"+str(temp), item["t_hope"], workbook)
            self._write_center(worksheet, "G"+str(temp), item["t_actual"], workbook)
            self._write_center(worksheet, "H"+str(temp), item["t_result"], workbook)
            temp = temp -1

if __name__ == '__main__':    
    test1 = excel_style()
    test1.init(worksheet)
    test1.test_detail(worksheet2)

    workbook.close()