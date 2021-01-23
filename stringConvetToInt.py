#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 2:10 PM
# @Author: zhangzhihui.wisdom
# @File:stringConvetToInt.py

import re


def stringConvertToInt(s):
    strings = s.strip()
    if len(strings) > 0:
        firstChar = strings[0]
        if firstChar == '+' or firstChar == '-':
            leftStr = strings[1:]
            if re.findall(r'^\d+', leftStr):
                tempNum = (re.findall(r'\d+', leftStr))[0]
                if firstChar == '-' and int(tempNum) * -1 >= - 2 ** 31:
                    return int(tempNum) * (-1)
                elif firstChar == '-' and int(tempNum) * -1 <= - 2 ** 31:
                    return - 2 ** 31
                elif firstChar == '+' and int(tempNum) < 2 ** 31 - 1:
                    return int(tempNum)
                else:
                    return 2 ** 31 - 1
            else:
                return 0

        elif re.findall(r'^\d+', strings):
            tempNum = (re.findall(r'\d+', strings))[0]
            if int(tempNum) < 2 ** 31 - 1:
                return int(tempNum)
            else:
                return 2 ** 31 - 1
        else:
            return 0


if __name__ == '__main__':
    print('String Convert Int')
    strings = input()
    print(stringConvertToInt(strings))
