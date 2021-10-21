#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import typing as t

from logging import getLogger
from Crypto.Cipher import AES

from .mixins.aes import AesMixin

logger = getLogger(__name__)


class AesEBCClient(AesMixin, object):
    """ aes-ebc算法类 - AES/EBC/pkcs7padding """

    def __init__(self, key: t.Text) -> None:
        """ 初始化实例

        @param key: 对称密钥,仅支持16(AES-128), 24(AES-192), 32(AES-256)
        """
        self.key = self.padding_secret(key.encode())

    def encrypt(self, data: bytes, step: int = 128) -> bytes:
        """ 加密数据

        @param data: 原始数据
        @param step: 加密步长
        @return: bytes
        """
        data = self.padding_source(data)
        result = b''
        cipher = AES.new(self.key, mode=AES.MODE_ECB)
        for i in range(0, len(data), step):
            result += cipher.encrypt(data[i: i + step])
        return result

    def decrypt(self, data: bytes, step: int = 128) -> bytes:
        """ 解密数据

        @param data: 加密数据
        @param step: 加密步长
        @return: bytes
        """
        result = b''
        cipher = AES.new(self.key, mode=AES.MODE_ECB)
        for i in range(0, len(data), step):
            result += cipher.decrypt(data[i: i + step])
        return self.cleanup_result(result)
