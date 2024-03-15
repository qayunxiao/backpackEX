# -*- coding: utf-8 -*-
# -------------------------
# @Time    :  2023/7/10 13:50
# @Author  : alvin
# @Description:  func
import datetime
import os.path
import logging
import colorlog
from utils.handle_path import log_path,log_testpath


def logger(flag=True, name=__name__):
    # 项目名称
    pname = 'Web3_Tools'
    # 设置颜色
    log_colors_config = {
        'DEBUG': 'white',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'bold_red',
        'CRITICAL': 'red',
    }

    # log 文件名，路径+｛时间｝.log
    logDir = os.path.join(log_path, ("{}_{}.log".format(pname, datetime.datetime.now().strftime('%Y%m%d_%H%M'))))
    # 1\创建日志对象
    logObject = logging.getLogger(name)
    # 2\设置级别，默认info
    logObject.setLevel(logging.INFO)
    # 3设置日志内容格式
    fmt = '%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d]:%(message)s'
    format = logging.Formatter(fmt)
    file_format = colorlog.ColoredFormatter(
        fmt='%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d]:%(message)s', log_colors=log_colors_config
    )
    # 看输入文件还上控制台
    if flag:
        # 设置日志渠道-文件方式
        handle = logging.FileHandler(logDir, encoding='utf-8')
        # 日志内容渠道绑定
        # handle.setFormatter(file_format)
        handle.setFormatter(format)
        # 日志对象跟渠道绑定
        logObject.addHandler(handle)
    else:
        # 设置日志渠道-控制台方式
        handle = logging.StreamHandler()
        # 日志内容渠道绑定
        handle.setFormatter(file_format)
        # 日志对象跟渠道绑定
        logObject.addHandler(handle)

    return logObject


log = logger()

if __name__ == '__main__':
    # print(os.path.join(log_path,("{}.log".format(datetime.datetime.now().strftime('%Y%m%d%H%M')))))
    log.info("qatest")
