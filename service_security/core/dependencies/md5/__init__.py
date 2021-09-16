#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import typing as t

from logging import getLogger

from service_core.core.context import WorkerContext
from service_security.core.client.md5 import Md5Client
from service_security.constants import SECURITY_CONFIG_KEY
from service_core.core.service.dependency import Dependency

logger = getLogger(__name__)


class Md5(Dependency):
    """ Md5依赖类 """

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
        self.alias = alias
        self.encrypt_options = encrypt_options or {}
        super(Md5, self).__init__(**kwargs)

    def setup(self) -> None:
        """ 生命周期 - 载入阶段

        @return: None
        """
        encrypt_options = self.container.config.get(f'{SECURITY_CONFIG_KEY}.{self.alias}.md5.encrypt_options', {})
        # 防止YAML中声明值为None
        self.encrypt_options = (encrypt_options or {}) | self.encrypt_options

    def get_instance(self, context: WorkerContext) -> t.Any:
        """ 获取注入对象
        @param context: 上下文对象
        @return: t.Any
        """
        return Md5Client(**self.encrypt_options)
