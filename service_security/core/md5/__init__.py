#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

import hashlib
import typing as t


class Md5Algorithm(object):
    """ md5算法 """

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """ 初始化实例

        @param args: 位置参数
        @param kwargs: 命名参数
        """
        pass

    @staticmethod
    def encrypt(data) -> t.Text:
        """ 加密数据

        @param data: 原始数据
        @return: t.Text
        """
        md5 = hashlib.md5()
        md5.update(data)
        return md5.hexdigest()
