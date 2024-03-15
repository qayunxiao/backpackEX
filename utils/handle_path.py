# -*- coding: utf-8 -*-
# -------------------------
# @Time    :  2023/7/10 12:50
# @Author  : alvin
# @Description:  func
# -------------------------

import os
"""
需求：代码在任意路径都可以获取到项目工程的绝对路径
"""
# print(__file__)#当前文件所在的路径
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
#1- 工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("project_path",project_path)

#2- utils
utils_path = os.path.join(project_path,'utils')

#2- 配置路径

config_path_ini = os.path.join(project_path,'configs','configs.ini')
config_path_env = os.path.join(project_path,'configs','env_properties.yal')
# print("config_path_ini",config_path_ini)

dirver_path = os.path.join(project_path,'extends','chromedriver.exe')
dirver_Firefoxpath = os.path.join(project_path,'extends','geckodriver.exe')

#3- 测试数据路径
qatestData_path = os.path.join(project_path,'testdata')
# print(qatestData_path)

#4- 测试报告路径
allure_report_path = os.path.join(project_path,r'report')
allure_html_path = os.path.join(project_path,'report','allure')
allure_html_file = os.path.join(project_path,'report','allure','index.html')
allure_json_path = os.path.join(project_path,r'report\allure_json')
coverageresult =  os.path.join(project_path,'report','coverageresult')
# print("allure_json_path:",allure_json_path)
# print("allure_report_path:",allure_report_path)


#5- log路径
log_path = os.path.join(project_path,r'logs')
log_testpath = os.path.join(project_path,r'logstest')
#print(log_path)