# 打印异常信息

import traceback
import sys

def print_exception(logger):
    ex_type, ex_val, ex_stack = sys.exc_info()
    logger(ex_type)
    logger(ex_val)
    for stack in traceback.extract_tb(ex_stack):
        logger(stack)


