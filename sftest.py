#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:sfuitest.py
@time:2021/05/12
@功能：存放一些公共方法
"""
import datetime
import random
import time


def sleep(tmie=2):
    '''
    强制等待时间吗
    :return:
    '''
    return time.sleep(tmie)


def get_random_number(digit: int):
    '''
    生成随机数
    Args:
        digit: 需要生成多少位的随机数

    Returns:所需要的随机数

    '''
    return ''.join([random.choice([str(i) for i in range(9)]) for i in range(digit)])


def create_ident_generator():
    '''随机生成身份证'''

    # 身份证号的前两位，省份代号
    sheng = (
        '11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
        '44',
        '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '66')
    # 随机选择距离今天在7000到25000的日期作为出生日期（没有特殊要求我就随便设置的，有特殊要求的此处可以完善下）
    birthdate = (datetime.date.today() - datetime.timedelta(days=random.randint(7000, 25000)))
    # 拼接出身份证号的前17位（第3-第6位为市和区的代码，中国太大此处就偷懒了写了定值，有要求的可以做个随机来完善下；第15-第17位为出生的顺序码，随机在100到199中选择）
    ident = sheng[random.randint(0, 31)] + '0101' + birthdate.strftime("%Y%m%d") + str(random.randint(100, 199))

    # 前17位每位需要乘上的系数，用字典表示，比如第一位需要乘上7，最后一位需要乘上2
    coe = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10, 14: 5, 15: 8, 16: 4,
           17: 2}
    summation = 0

    # for循环计算前17位每位乘上系数之后的和
    for i in range(17):
        summation = summation + int(ident[i:i + 1]) * coe[i + 1]  # ident[i:i+1]使用的是python的切片获得每位数字

    # 前17位每位乘上系数之后的和除以11得到的余数对照表，比如余数是0，那第18位就是1
    key = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}

    # 拼接得到完整的18位身份证号
    return ident + key[summation % 11]


def create_phone_generator():
    '''
    随机生成手机号
    Returns:

    '''
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


def get_time(days=0, hours=0, minutes=0):
    now_time = datetime.datetime.now()

    return (now_time + datetime.timedelta(days=days, hours=hours, minutes=minutes)).strftime("%Y%m%d%H%M%S")  # 获取后一天


if __name__ == '__main__':
    print(create_ident_generator())
    print(create_phone_generator())
    print(get_random_number(8))
