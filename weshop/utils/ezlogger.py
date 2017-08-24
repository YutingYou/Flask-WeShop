"""
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
"""

import os
import logging

__all__ = ['get_logger']

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


def get_logger(name, level=DEBUG, use_stream=True, use_file=False):
    # 创建一个logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 定义日志格式
    formatter = logging.Formatter('[%(levelname)s][%(asctime)s][%(name)s][%(lineno)d]: %(message)s')

    # 创建日志文件handler
    if use_file is True:
        fh = logging.FileHandler(os.path.abspath('logs') + '/' + name + '.log')
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    # 创建流日志handler，输出到控制台
    if use_stream is True:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)  # 定义handler输出格式
        logger.addHandler(ch)

    return logger
