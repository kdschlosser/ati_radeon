# -*- coding: utf-8 -*-
#
# ***********************************************************************************
# MIT License
#
# Copyright (c) 2020 Kevin G. Schlosser
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# ***********************************************************************************

import sys
import six


PY2 = sys.version_info[0] < 3


class InstanceSingleton(type):

    def __init__(cls, name, bases, dct):
        super(InstanceSingleton, cls).__init__(name, bases, dct)
        cls._instances = {}

    def __call__(cls, adapter_index):
        if adapter_index not in cls._instances:
            cls._instances[adapter_index] = super(InstanceSingleton, cls).__call__(adapter_index)

        return cls._instances[adapter_index]


def instance_singleton(cls):
    return six.add_metaclass(InstanceSingleton)(cls)


def get_string(data):
    i = 0
    res = ''

    try:
        data = bytearray(data)
    except:
        pass

    while data:
        try:
            char = data.pop(0)
        except:
            char = data[i]

        if PY2:
            if isinstance(char, unicode):
                char = str(char).encode('utf-8')
        else:
            if isinstance(char, bytes):
                char = str(char)

        if char in ('\x00', 0x00):
            break

        if isinstance(char, int):
            char = chr(char)

        res += char
        i += 1

    return res


def remap(value, old_min, old_max, new_min, new_max):
    old_range = old_max - old_min
    new_range = new_max - new_min
    return (((value - old_min) * new_range) / old_range) + new_min


def get_bit(value, idx):
    return (value & (1 << idx)) != 0
