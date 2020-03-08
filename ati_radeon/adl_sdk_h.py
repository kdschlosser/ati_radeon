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
import ctypes.util
from .adl_structures_h import *  # NOQA
import ctypes
import threading


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
# / \file adl_sdk.h
# / \brief Contains the definition of the Memory Allocation Callback.\n < b >
# Included in ADL SDK < /b >
# /
# / \n\n
# / This file contains the definition of the Memory Allocation Callback.\n
# / It also includes definitions of the respective structures and constants.\n
# / < b > This is the only header file to be included in a C/C + + project
# using ADL < /b >

LPVOID = POINTER(VOID)
# / Memory Allocation Call back
# void* ( __stdcall *ADL_MAIN_MALLOC_CALLBACK )( INT );
ADL_MAIN_MALLOC_CALLBACK = ctypes.CFUNCTYPE(
    LPVOID,
    INT,
)


def load_library(lib):
    dll_path = ctypes.util.find_library(lib)
    if dll_path is not None:
        try:
            return ctypes.cdll.LoadLibrary(dll_path)
        except:
            pass


def InitADL():
    if defined(LINUX):
        hDLL = load_library('libatiadlxx.so')
    else:
        for lib in ('atiadlxx.dll', 'atiadlxy.dll'):
            hDLL = load_library(lib)
            if hDLL is not None:
                break
        else:
            hDLL = NULL

    if hDLL is None:
        return ADL_ERR

    return ADL_OK


def _ADL_Main_Memory_Alloc(iSize):
    lpBuffer = (LPVOID * iSize)()
    return lpBuffer


ADL_Main_Memory_Alloc = ADL_MAIN_MALLOC_CALLBACK(_ADL_Main_Memory_Alloc)


class _ADL2_Main_Control_Create(object):

    def __init__(self):
        self.ref_count = 0
        self._context = None
        self.lock = threading.Lock()

    def __enter__(self):
        with self.lock:
            self.ref_count += 1
            if self._context is None:
                self._context = ADL_CONTEXT_HANDLE()

                from . import adl_h

                if adl_h._ADL2_Main_Control_Create(
                        ADL_Main_Memory_Alloc,
                        1,
                        ctypes.byref(self._context)
                ) != ADL_OK:
                    raise RuntimeError('Unable to create ADL control')
            return self._context

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self.lock:
            self.ref_count -= 1

            if self.ref_count == 0:
                from . import adl_h

                if ADL_OK != adl_h._ADL2_Main_Control_Destroy(self._context):
                    raise RuntimeError('Unable to destroy ADL control')

                self._context = None


ADL2_Main_Control_Create = _ADL2_Main_Control_Create()


class AdapterBase(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @staticmethod
    def _get_string(data):
        res = ''
        i = 0
        while True:
            char = data[i]

            if char in ('\x00', 0x00):
                break
            res += char

        return res
