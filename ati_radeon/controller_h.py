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


ADL2_CONTROLLER_COLOR_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    ADLGamma
)
ADL_CONTROLLER_COLOR_SET = int(
    INT,
    INT,
    ADLGamma
)
ADL2_CONTROLLER_COLOR_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLGamma),
    POINTER(ADLGamma),
    POINTER(ADLGamma),
    POINTER(ADLGamma)
)
ADL_CONTROLLER_COLOR_GET = int(
    INT,
    INT,
    POINTER(ADLGamma),
    POINTER(ADLGamma),
    POINTER(ADLGamma),
    POINTER(ADLGamma)
)


# Function to set the current gamma value for a controller.
_ADL2_Controller_Color_Set = ADL2_CONTROLLER_COLOR_SET

# Function to set the current gamma value for a controller.
_ADL_Controller_Color_Set = ADL_CONTROLLER_COLOR_SET

# Function to get the current value of gamma for a controller.
_ADL2_Controller_Color_Get = ADL2_CONTROLLER_COLOR_GET

# Function to get the current value of gamma for a controller.
_ADL_Controller_Color_Get = ADL_CONTROLLER_COLOR_GET


def Init(hDLL):
    global _ADL2_Controller_Color_Set
    global _ADL_Controller_Color_Set
    global _ADL2_Controller_Color_Get
    global _ADL_Controller_Color_Get

    _ADL2_Controller_Color_Set = ADL2_CONTROLLER_COLOR_SET(
          GetProcAddress(hDLL, "ADL2_Controller_Color_Set")
    )
    _ADL_Controller_Color_Set = ADL_CONTROLLER_COLOR_SET(
          GetProcAddress(hDLL, "ADL_Controller_Color_Set")
    )
    _ADL2_Controller_Color_Get = ADL2_CONTROLLER_COLOR_GET(
          GetProcAddress(hDLL, "ADL2_Controller_Color_Get")
    )
    _ADL_Controller_Color_Get = ADL_CONTROLLER_COLOR_GET(
          GetProcAddress(hDLL, "ADL_Controller_Color_Get")
    )


__all__ = (
    '_ADL2_Controller_Color_Set',
    '_ADL_Controller_Color_Set',
    '_ADL2_Controller_Color_Get',
    '_ADL_Controller_Color_Get',
)