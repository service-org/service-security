#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import typing as t

from logging import getLogger

from service_core.core.context import WorkerContext
from service_security.core.client.md5 import Md5Client
from service_core.core.service.dependency import Dependency

logger = getLogger(__name__)


class Rsa(Dependency):
    """ Rsa依赖类 """

    def __init__(
            self,
            alias: t.Text,
            encrypt_options: t.Optional[t.Dict[t.Text, t.Any]] = None,
            **kwargs: t.Any
    ) -> None:
        """ 初始化实例

        @param alias: 配置别名
        @param encrypt_options: 加密配置
        """
        super(Rsa, self).__init__(**kwargs)

    def get_instance(self, context: WorkerContext) -> t.Any:
        """ 获取注入对象
        @param context: 上下文对象
        @return: t.Any
        """
        return Md5Client()
