# 各种通用方法

from datetime import timedelta, datetime
import pickle
import os


def next_month(year, month):
    month = month + 1
    if month > 12:
        month = 1
        year = year + 1
    return year, month

# 生成月份数据库表名, s_year, s_month开始时间， d_year, d_month结束时间
def create_month_table_names(prefix, s_year, s_month, d_year, d_month):
    tables = []
    l_year = s_year
    l_month = s_month
    tables.append("{}{}{:0>2}".format(prefix, l_year, l_month))
    deadline = "{}{}{:0>2}".format(prefix, d_year, d_month)
    while True:
        l_year, l_month = next_month(l_year, l_month)
        table_name = "{}{}{:0>2}".format(prefix, l_year, l_month) 
        tables.append(table_name)
        if table_name == deadline:
            break
    return tables

# 生成日期数据库表名, start, deadline 为datetime类型
def get_date_table_names(prefix, start, deadline):
    tables = []
    l_day = start
    l_day_s = l_day.strftime('%Y%m%d')
    tables.append("{}{}".format(prefix, l_day_s))
    while True:
        l_day += timedelta(1)
        l_day_s = l_day.strftime('%Y%m%d')
        tables.append("{}{}".format(prefix, l_day_s))
        if l_day == deadline:
            break
    return tables

# 全表查询
def full_table_query(db, sql, count = 100):
    begin = 0
    while True:
        query_sql = sql + " limit {}, {}".format(begin, count)
        # print(query_sql)
        res = db.select(query_sql)
        if res and len(res) > 0:
            yield res
        else:
            break
        begin += count

# 查询指定页, 从第0页开始， page_index:第几页， count:每页数量
def query_specified_page(db, sql, page_index, count = 100):
    begin = page_index * count
    query_sql = sql + " limit {}, {}".format(begin, count)
    print(query_sql)
    res = db.select(query_sql)
    return res

def save_data_cover(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def save_data_append(filename, data):
    with open(filename, 'ab') as f:
        pickle.dump(data, f)

def get_data(filename):
    data_list = []
    try:
        with open(filename, 'rb') as f:
            while True:
                data = pickle.load(f)
                data_list.append(data)
    except Exception as result:
        print(result)

    return data_list

def clear_data(filename):
    os.remove(filename)
