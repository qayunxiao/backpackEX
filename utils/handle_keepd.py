# -*- coding: utf-8 -*-
# -------------------------
# @Time    :  2024/3/13 16:11
# @Author  : alvin
# @Description:  func
# -------------------------
import math
from decimal import Decimal, ROUND_HALF_UP


def math_ceil_float(num, digits=3):
    """
    向上取整
    如81.521和81.529 都变成 81.53
    """
    float_num = float(num)
    new_str = str(float_num)[:str(float_num).index('.') + digits+2]
    if new_str[-1] == "0":
        #小数第3位是0的处理
        value_d=Decimal(float(num)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        value_f=float(value_d)
        # print("value_f is :{} ,type is :{}".format(value_f,type(value_f)))
        return value_f
    value = math.ceil(float_num * 10 ** digits) / 10 ** digits
    # print("value is :{} ,type is :{}".format(value,type(value)))
    return value


if __name__ == '__main__':
    a=math_ceil_float(0.23433)
    print(a)