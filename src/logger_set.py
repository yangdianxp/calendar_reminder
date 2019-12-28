# 设置日志

import logging
import os
from logging.handlers import TimedRotatingFileHandler

logger = None

def set_logger(fname):
    global logger
    fname = os.path.splitext(fname)[0] + ".log"
    logHandler = TimedRotatingFileHandler(fname, when="MIDNIGHT", encoding='utf-8')
    logFormatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logHandler.setFormatter(logFormatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)
    return logger
