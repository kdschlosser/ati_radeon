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
    VOID,
    ctypes.c_size_t,
)
ADL_MAIN_FREE_CALLBACK = ctypes.CFUNCTYPE(
    None,
    VOID,
)


def load_library(lib):
    dll_path = ctypes.util.find_library(lib)
    if dll_path is not None:
        try:
            return ctypes.cdll.LoadLibrary(dll_path)
        except:
            pass


_malloc = None
_free = None
_is_init = False
libc = None


class Adapters(object):

    def __iter__(self):
        global _is_init

        if not _is_init:
            res = InitADL()
            if res != ADL_OK:
                raise RuntimeError('Failed to initilize the adl (' + str(res) + ')')

            _is_init = True

        num_adapters = INT(-1)
        from .adapter_h import (
            _ADL2_Adapter_NumberOfAdapters_Get,
            _ADL2_Adapter_AdapterInfo_Get,
            _ADL2_Adapter_ID_Get,
            Adapter
        )

        found_ids = []

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_NumberOfAdapters_Get(
                context,
                ctypes.byref(num_adapters)
            ) != ADL_OK:
                raise RuntimeError('Unable to get adapter count')

            adapterInfoArray = (AdapterInfo * num_adapters.value)()

            if _ADL2_Adapter_AdapterInfo_Get(
                context,
                adapterInfoArray,
                ctypes.sizeof(adapterInfoArray)
            ) != ADL_OK:
                raise RuntimeError("ADL2_Adapter_AdapterInfo_Get failed.")

            for i, lpInfo in enumerate(adapterInfoArray):
                lpAdapterID = INT()
                iAdapterIndex = INT(lpInfo.iAdapterIndex)

                if _ADL2_Adapter_ID_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpAdapterID)
                ) != ADL_OK:
                    continue

                if lpAdapterID.value not in found_ids:
                    found_ids += [lpAdapterID.value]
                    yield Adapter(lpAdapterID.value, i)


def InitADL():
    global _malloc
    global _free
    global libc
    if defined(LINUX):
        from ctypes import RTLD_GLOBAL
        ctypes.CDLL("libXext.so.6", mode=RTLD_GLOBAL)
        hDLL = load_library('libatiadlxx.so')
        libc = ctypes.CDLL("libc.so.6")

    elif defined(_WIN64):
        hDLL = load_library('atiadlxx.dll')
        libc = ctypes.cdll.msvcrt

    elif defined(_WIN32):
        hDLL = load_library('atiadlxy.dll')
        libc = ctypes.cdll.msvcrt

    else:
        raise RuntimeError('Unsupported OS')

    _malloc = libc.malloc
    _malloc.argtypes = [ctypes.c_size_t]
    _malloc.restype = ctypes.c_void_p
    _free = libc.free
    _free.argtypes = [ctypes.c_void_p]

    if hDLL is None:
        return ADL_ERR

    from .adapter_h import Init as _adapter_init
    from .adl_h import Init as adl_init
    from .appprofiles_h import Init as appprofiles_init
    from .controller_h import Init as controller_init
    from .crossdisplay_h import Init as crossdisplay_init
    from .display_h import Init as display_init
    from .displaysmanager_h import Init as displaysmanager_init
    from .graphics_h import Init as graphics_init
    from .overdrive5_h import Init as overdrive5_init
    from .overdrive6_h import Init as overdrive6_init
    from .overdrive8_h import Init as overdrive8_init
    from .overdriven_h import Init as overdriven_init
    from .powerxpress_h import Init as powerxpress_init
    from .workstation_h import Init as workstation_init

    _adapter_init(hDLL)
    adl_init(hDLL)
    appprofiles_init(hDLL)
    controller_init(hDLL)
    crossdisplay_init(hDLL)
    display_init(hDLL)
    displaysmanager_init(hDLL)
    graphics_init(hDLL)
    overdrive5_init(hDLL)
    overdrive6_init(hDLL)
    overdrive8_init(hDLL)
    overdriven_init(hDLL)
    powerxpress_init(hDLL)
    workstation_init(hDLL)

    libc.strtok.restype = POINTER(ctypes.c_char)

    return ADL_OK


@ADL_MAIN_MALLOC_CALLBACK
def ADL_Main_Memory_Alloc(iSize):
    return _malloc(iSize)


@ADL_MAIN_FREE_CALLBACK
def ADL_Main_Memory_Free(lpBuffer):
    if lpBuffer[0] is not None:
        _free(lpBuffer[0])
        lpBuffer[0] = None


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

try:
    unicode = unicode
except NameError:
    unicode = bytes


class AdapterBase(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @staticmethod
    def _get_string(data):
        res = ''

        if isinstance(data, (str, unicode)):
            data = list(data)

            while data:
                char = data.pop(0)
                res += chr(char)

        else:
            i = 0
            while True:
                char = data[i]
                if isinstance(char, unicode):
                    char = str(char).encode('utf-8')

                if char in ('\x00', 0x00):
                    break

                if isinstance(char, int):
                    char = chr(char)

                res += char
                i += 1

        return res
