#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import typing as t

from logging import getLogger

from service_security.constants import SECURITY_CONFIG_KEY
from service_core.core.service.dependency import Dependency
from service_security.core.client.sha256 import Sha256Client

logger = getLogger(__name__)


class Sha256(Dependency):
    """ Md5依赖类 """

    name = 'Sha256'

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
        self.client = None
        self.encrypt_options = encrypt_options or {}
        super(Sha256, self).__init__(**kwargs)

    def setup(self) -> None:
        """ 生命周期 - 载入阶段

        @return: None
        """
        encrypt_options = self.container.config.get(f'{SECURITY_CONFIG_KEY}.{self.alias}.sha256.encrypt_options', {})
        # 防止YAML中声明值为None
        self.encrypt_options = (encrypt_options or {}) | self.encrypt_options
        self.client = Sha256Client(**self.encrypt_options)

    def get_instance(self) -> Sha256Client:
        """ 获取注入对象

        @return: Sha256Client
        """
        return self.client
