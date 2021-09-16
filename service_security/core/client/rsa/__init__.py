#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

import typing as t

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


class RsaClient(object):
    """ rsa算法类 """

    def __init__(self, private_key: t.Optional[t.Text] = None, public_key: t.Optional[t.Text] = None) -> None:
        """ 初始化实例

        @param private_key: 私钥
        @param public_key: 公钥
        """
        self.private_key = private_key or ''
        self.public_key = public_key or ''

    def encrypt(self, data: bytes) -> bytes:
        """ 加密数据

        @param data: 原始数据
        @return: t.Text
        """
        public_obj = PKCS1_v1_5.new(RSA.importKey(self.public_key))
        return public_obj.encrypt(data)

    def decrypt(self, data: bytes) -> bytes:
        """ 解密数据

        @param data: 加密数据
        @return: bytes
        """
        private_obj = PKCS1_v1_5.new(RSA.importKey(self.private_key))
        return private_obj.decrypt(data, b'')
