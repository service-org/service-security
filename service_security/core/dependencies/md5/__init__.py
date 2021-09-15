#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import typing as t

from logging import getLogger

from service_core.core.context import WorkerContext
from service_security.core.client.md5 import MD5Client
from service_core.core.service.dependency import Dependency

logger = getLogger(__name__)


class MD5(Dependency):
    """ MD5依赖类 """

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """ 初始化实例

        @param args: 位置参数
        @param kwargs: 命名参数
        """
        super(MD5, self).__init__(*args, **kwargs)

    def get_instance(self, context: WorkerContext) -> t.Any:
        """ 获取注入对象
        @param context: 上下文对象
        @return: t.Any
        """
        return MD5Client()
