#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

import hashlib
import typing as t


class Md5Client(object):
    """ md5算法类 """

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """ 初始化实例

        @param args: 位置参数
        @param kwargs: 命名参数
        """
        pass

    @staticmethod
    def encrypt(data: bytes, step: int = 128) -> t.Text:
        """ 加密数据

        @param data: 原始数据
        @param step: 加密步长
        @return: t.Text
        """
        md5 = hashlib.md5()
        for i in range(0, len(data), step):
            md5.update(data[i:i + step])
        return md5.hexdigest()
