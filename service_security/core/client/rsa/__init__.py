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

    def encrypt(self, data: bytes, step: int = 100) -> bytes:
        """ 加密数据

        注意: 分段加密长度不可以超过密钥长度(如1024)/8-11

        @param data: 原始数据
        @param step: 加密步长
        @return: t.Text
        """
        public_obj = PKCS1_v1_5.new(RSA.importKey(self.public_key))
        result = b''
        for i in range(0, len(data), step):
            result += public_obj.encrypt(data[i:i+step])
        return result

    def decrypt(self, data: bytes, step: int = 128) -> bytes:
        """ 解密数据

        注意: 分段解密时密钥长度1024步长是128,2046步长为256

        @param data: 加密数据
        @param step: 解密步长
        @return: bytes
        """
        private_obj = PKCS1_v1_5.new(RSA.importKey(self.private_key))
        result = b''
        for i in range(0, len(data), step):
            result += private_obj.decrypt(data[i:i+step], b'')
        return result
