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
from .adl_structures_h import *  # NOQA

# Copyright (c) 2016 Advanced Micro Devices, Inc. All rights reserved.
# MIT LICENSE:
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


def GetProcAddress(pLibrary, name):
    return getattr(pLibrary, name, NULL)


def int(*args):
    def wrapper(*func):
        func = func[0]

        if func is None:
            return NULL

        func.argtypes = list(args)
        func.restype = INT

        return func

    return wrapper


ADL2_DISPLAY_UNDERSCANSUPPORT_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_UNDERSCANSTATE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_UNDERSCANSTATE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL2_DISPLAY_UNDERSCAN_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_UNDERSCAN_SET = int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_UNDERSCAN_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_UNDERSCAN_GET = int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)


ADL2_DISPLAY_OVERSCAN_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_OVERSCAN_SET = int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_OVERSCAN_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_OVERSCAN_GET = int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)


_ADL2_Display_Overscan_Set = ADL2_DISPLAY_OVERSCAN_SET

_ADL_Display_Overscan_Set = ADL_DISPLAY_OVERSCAN_SET

_ADL2_Display_Overscan_Get = ADL2_DISPLAY_OVERSCAN_GET

_ADL_Display_Overscan_Get = ADL_DISPLAY_OVERSCAN_GET

# Function to get the value of under scan support.
_ADL2_Display_UnderscanSupport_Get = ADL2_DISPLAY_UNDERSCANSUPPORT_GET

# Function to get the value of under scan enabled.
_ADL2_Display_UnderscanState_Get = ADL2_DISPLAY_UNDERSCANSTATE_GET

# Function to set the value of under scan enabled.
_ADL2_Display_UnderscanState_Set = ADL2_DISPLAY_UNDERSCANSTATE_SET

# Function to set the current value of underscan.
_ADL2_Display_Underscan_Set = ADL2_DISPLAY_UNDERSCAN_SET

# Function to set the current value of underscan.
_ADL_Display_Underscan_Set = ADL_DISPLAY_UNDERSCAN_SET

# Function to retrieve the detailed information for underscan.
_ADL2_Display_Underscan_Get = ADL2_DISPLAY_UNDERSCAN_GET

# Function to retrieve the detailed information for underscan.
_ADL_Display_Underscan_Get = ADL_DISPLAY_UNDERSCAN_GET


def Init(hDLL):
    global _ADL2_Display_UnderscanSupport_Get
    global _ADL2_Display_UnderscanState_Get
    global _ADL2_Display_UnderscanState_Set
    global _ADL2_Display_Underscan_Set
    global _ADL_Display_Underscan_Set
    global _ADL2_Display_Underscan_Get
    global _ADL_Display_Underscan_Get
    global _ADL2_Display_Overscan_Set
    global _ADL_Display_Overscan_Set
    global _ADL2_Display_Overscan_Get
    global _ADL_Display_Overscan_Get

    _ADL2_Display_UnderscanSupport_Get = ADL2_DISPLAY_UNDERSCANSUPPORT_GET(
          GetProcAddress(hDLL, "ADL2_Display_UnderscanSupport_Get")
    )
    _ADL2_Display_UnderscanState_Get = ADL2_DISPLAY_UNDERSCANSTATE_GET(
          GetProcAddress(hDLL, "ADL2_Display_UnderscanState_Get")
    )
    _ADL2_Display_UnderscanState_Set = ADL2_DISPLAY_UNDERSCANSTATE_SET(
          GetProcAddress(hDLL, "ADL2_Display_UnderscanState_Set")
    )
    _ADL2_Display_Underscan_Set = ADL2_DISPLAY_UNDERSCAN_SET(
          GetProcAddress(hDLL, "ADL2_Display_Underscan_Set")
    )
    _ADL_Display_Underscan_Set = ADL_DISPLAY_UNDERSCAN_SET(
          GetProcAddress(hDLL, "ADL_Display_Underscan_Set")
    )
    _ADL2_Display_Underscan_Get = ADL2_DISPLAY_UNDERSCAN_GET(
          GetProcAddress(hDLL, "ADL2_Display_Underscan_Get")
    )
    _ADL_Display_Underscan_Get = ADL_DISPLAY_UNDERSCAN_GET(
          GetProcAddress(hDLL, "ADL_Display_Underscan_Get")
    )
    _ADL2_Display_Overscan_Set = ADL2_DISPLAY_OVERSCAN_SET(
        GetProcAddress(hDLL, "ADL2_Display_Overscan_Set")
    )
    _ADL_Display_Overscan_Set = ADL_DISPLAY_OVERSCAN_SET(
        GetProcAddress(hDLL, "ADL_Display_Overscan_Set")
    )
    _ADL2_Display_Overscan_Get = ADL2_DISPLAY_OVERSCAN_GET(
        GetProcAddress(hDLL, "ADL2_Display_Overscan_Get")
    )
    _ADL_Display_Overscan_Get = ADL_DISPLAY_OVERSCAN_GET(
        GetProcAddress(hDLL, "ADL_Display_Overscan_Get")
    )


__all__ = (
    '_ADL2_Display_UnderscanSupport_Get',
    '_ADL2_Display_UnderscanState_Get',
    '_ADL2_Display_UnderscanState_Set',
    '_ADL2_Display_Underscan_Set',
    '_ADL_Display_Underscan_Set',
    '_ADL2_Display_Underscan_Get',
    '_ADL_Display_Underscan_Get',
    '_ADL2_Display_Overscan_Set',
    '_ADL_Display_Overscan_Set',
    '_ADL2_Display_Overscan_Get',
    '_ADL_Display_Overscan_Get',
    'ValueWrapper'
)


from .adl_sdk_h import ADL2_Main_Control_Create  # NOQA


# noinspection PyUnresolvedReferences
class ValueWrapper(__builtin__.int):

    def __init__(self, value=None):
        if value is None:
            __builtin__.int.__init__(self)
        else:
            try:
                __builtin__.int.__init__(self, value)
            except TypeError:
                __builtin__.int.__init__(self)

        self.__obj = None

    def _set_object(self, obj):
        self.__obj = obj

    @property
    def min(self):
        return self.__obj.min

    @property
    def max(self):
        return self.__obj.max

    @property
    def step(self):
        return self.__obj.step

    @property
    def default(self):
        return self.__obj.default
