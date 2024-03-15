# -*- coding: utf-8 -*-
# -------------------------
# @Time    :  2024/3/13 9:38
# @Author  : alvin
# @Description:  func
# -------------------------
import sys

from selenium import webdriver
import time
# 创建一个浏览器实例
from utils.handle_ddmsg import send_ding_msgs
from utils.handle_keepd import math_ceil_float
from utils.handle_log import log
from utils.handle_path import dirver_path,dirver_Firefoxpath

service = webdriver.ChromeService(executable_path=dirver_path)
driver = webdriver.Chrome(service=service)
# service = webdriver.FirefoxService(executable_path=dirver_Firefoxpath)
# driver = webdriver.Firefox(service=service)
# 打开网页
url = "https://app.v2.fjordfoundry.com/pools/0x4856861e67B8a0deBCe9c5C8AB284326Fa3f4f13"
driver.get(url)
driver.maximize_window()
time.sleep(25)  # 等待页面加载完成，根据网速和网页复杂程度适当调整时间
# 定位价格框元素并输入内容
token_count_input = driver.find_element("xpath",'//*[@id="container"]/div[2]/div[2]/div[3]/div[2]/input')
token_count_input.clear()  # 清空输入框内容
time.sleep(3)
token_count_input.send_keys("1")  # 输入个数为1个
log.info("当前页面地址标题:{}".format(driver.title))
time.sleep(3)
input_element_usdc = driver.find_element("xpath",'//*[@id="container"]/div[2]/div[2]/div[1]/div[2]/input')


#当前价格
currentPrice = input_element_usdc.get_attribute("value")
#期望价格
myPrice = 0.45

print("currentPrice is:{}".format(currentPrice))
while True:
    # 设置循环间隔时间，避免频繁请求接口
    # token_count_input.clear()  # 清空输入框内容
    # time.sleep(2)  # 间隔10
    # token_count_input.send_keys("1")  # 输入个数为1个
    # time.sleep(10)  # 间隔10
    currentPrice = input_element_usdc.get_property("value")
    log.info("当前价:{},期望价:{}".format(float(currentPrice),myPrice))
    # print("current price is :{}".format(input_element_usdc.get_attribute("value")))
    # print("current price is :{}".format(input_element_usdc.get_property("value")))
    # print("current price is :{}".format(input_element_usdc.get_attribute("value")))
    #页面价格小于我期望的价格
    if float(currentPrice) < myPrice:
        message = "当前价格:{},低于我期望的价格:{},去手动下单！".format(currentPrice,myPrice)
        print(message)
        log.info(message)
        send_ding_msgs(message)
        # 关闭浏览器
        driver.quit()
        sys.exit(-1)
    time.sleep(60)  # 间隔10
