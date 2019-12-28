# -*- coding: utf-8 -*-
import io
import sys
import time
import datetime
import copy
import sxtwl
import logger_set
from exception_info import print_exception
from send_mail import send_mail

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
logger = logger_set.set_logger("./log/" + __file__)
lunar = sxtwl.Lunar()

Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
# ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
ymc = [11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
#rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]
rmc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
       22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

# 如果是农历，只用写日月， 如：12-03
# 如果是阳历，要填写完格式
# "type": 1为阳历，2为农历
# "repeat": 是否重复，0：不重得，1：重复
reminder_events = [{"提醒时间": "12-03", "提醒内容": "老妹生日，快去祝福",
                    "repeat": 1, "type": 1},
                   ]

def run():
    while True:
        # 记录当前日期，用于判断是否到下一天
        now = datetime.datetime.now() 
        date_old = now.strftime("%Y-%m-%d")
        # 重新加载配置
        r_events = copy.deepcopy(reminder_events)

        while True:
            now = datetime.datetime.now()        
            strYangLiTime = now.strftime("%Y-%m-%d %H:%M:%S")
            logger.info(strYangLiTime) 
            day = lunar.getDayBySolar(now.year, now.month, now.day)
            strNongLiTime = "{}-{:0>2}".format(ymc[day.Lmc], rmc[day.Ldi])

            logger.info("阳历:" + strYangLiTime)
            logger.info("农历:" + strNongLiTime)

            for item in r_events[:]:
                # 查看是否是农历提醒
                if item["type"] == 1 and item["提醒时间"] == strNongLiTime:
                    logger.info(item["提醒内容"])
                    send_mail("313342505@qq.com", logger.info(item["提醒内容"]))
                    # 提醒过，不再提醒
                    r_events.remove(item)
                    # 如果不用重复提醒，删除全局的
                    if item["repeat"] != 1:
                        reminder_events.remove(item)

            time.sleep(5)

def main(argv):
    run()


if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as result:
        print_exception(logger.error)
