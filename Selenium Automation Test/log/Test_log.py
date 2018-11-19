#coding = utf-8
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#控制台输出日志
consle = logging.StreamHandler()
logger.addHandler(consle)

#文件输出日志
file_handler = logging.FileHandler(r"D:\Test_Work\Python\Python36-32\pyscripts\Selenium Automation Test\log\log\debug.log")
#日志格式设置
formatter = logging.Formatter("%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ------>%(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("test")
file_handler.close()
logger.removeHandler(file_handler)