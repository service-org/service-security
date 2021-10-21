#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

import typing as t

from Crypto.Cipher import AES
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms


class AesMixin(object):
    """ aes算法类辅助 """

    @staticmethod
    def padding_secret(data: bytes) -> bytes:
        """ 填充密钥数据

        注意: AES key must be either 16, 24, or 32 bytes long

        @param data: 原始数据
        @return: bytes
        """
        length = AES.key_size[-1]
        for size in AES.key_size:
            if len(data) > size:
                continue
            length = size
            break
        while len(data) % length != 0:
            data += b'\0'
        else:
            return data

    @staticmethod
    def padding_base64(data: t.Text) -> t.Text:
        """ 填充B64数据

        注意: Base64加密的数据长度必须是4的倍数

        @param data: 原始数据
        @return: t.Text
        """
        length = 4 - len(data) % 4
        return data + '=' * length if length else data

    @staticmethod
    def padding_source(data: bytes) -> bytes:
        """ 填充原始数据

        @param data: 原始数据
        @return: bytes
        """
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        return padder.update(data) + padder.finalize()

    @staticmethod
    def cleanup_result(data: bytes) -> bytes:
        """ 清理结果数据

        @param data: 结果数据
        @return: bytes
        """
        return data \
            .rstrip(b'\x01').rstrip(b'\x02').rstrip(b'\x03') \
            .rstrip(b'\x04').rstrip(b'\x05').rstrip(b'\x06') \
            .rstrip(b'\x07').rstrip(b'\x08').rstrip(b'\x09') \
            .rstrip(b'\x0a').rstrip(b'\x0b').rstrip(b'\x0c') \
            .rstrip(b'\x0d').rstrip(b'\x0e').rstrip(b'\x0f') \
            .rstrip(b'\x10')
