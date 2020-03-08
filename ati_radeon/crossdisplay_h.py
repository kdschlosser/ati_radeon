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


ADL2_ADAPTER_CROSSDISPLAYADAPTERROLE_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(INT)),
    POINTER(INT),
    POINTER(POINTER(INT)),
    POINTER(INT)
)
ADL_ADAPTER_CROSSDISPLAYADAPTERROLE_CAPS = int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(INT)),
    POINTER(INT),
    POINTER(POINTER(INT)),
    POINTER(INT)
)
ADL2_ADAPTER_CROSSDISPLAYINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(INT)),
    POINTER(INT),
    POINTER(POINTER(INT)),
    POINTER(INT)
)
ADL_ADAPTER_CROSSDISPLAYINFO_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(INT)),
    POINTER(INT),
    POINTER(POINTER(INT)),
    POINTER(INT)
)
ADL2_ADAPTER_CROSSDISPLAYINFO_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_CROSSDISPLAYINFO_SET = int(
    INT,
    INT,
    INT,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_CROSSDISPLAYPLATFORMINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_CROSSDISPLAYPLATFORMINFO_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_CROSSDISPLAYINFOX2_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_CROSSDISPLAYINFOX2_SET = int(
    INT,
    INT,
    INT,
    INT,
    INT,
    POINTER(INT)
)


# Function to retrieve CrossDisplay capabilities.
_ADL2_Adapter_CrossdisplayAdapterRole_Caps = ADL2_ADAPTER_CROSSDISPLAYADAPTERROLE_CAPS

# Function to retrieve CrossDisplay capabilities.
_ADL_Adapter_CrossdisplayAdapterRole_Caps = ADL_ADAPTER_CROSSDISPLAYADAPTERROLE_CAPS

# Function to retrieve CrossDisplay state information.
_ADL2_Adapter_CrossdisplayInfo_Get = ADL2_ADAPTER_CROSSDISPLAYINFO_GET

_ADL_Adapter_CrossdisplayInfo_Get = ADL_ADAPTER_CROSSDISPLAYINFO_GET

# Function to set the system configuration to CrossDisplay mode or multi-adapter mode.
_ADL2_Adapter_CrossdisplayInfo_Set = ADL2_ADAPTER_CROSSDISPLAYINFO_SET

# Function to set the system configuration to CrossDisplay mode or multi-adapter mode.
_ADL_Adapter_CrossdisplayInfo_Set = ADL_ADAPTER_CROSSDISPLAYINFO_SET

# Function to get the graphics platform information of of an adapter.
_ADL2_Adapter_CrossDisplayPlatformInfo_Get = ADL2_ADAPTER_CROSSDISPLAYPLATFORMINFO_GET

# Function to get the graphics platform information of of an adapter.
_ADL_Adapter_CrossDisplayPlatformInfo_Get = ADL_ADAPTER_CROSSDISPLAYPLATFORMINFO_GET

# Function to set the system configuration to CrossDisplay mode or multi-adapter mode.
_ADL2_Adapter_CrossdisplayInfoX2_Set = ADL2_ADAPTER_CROSSDISPLAYINFOX2_SET

# Function to set the system configuration to CrossDisplay mode or multi-adapter mode.
_ADL_Adapter_CrossdisplayInfoX2_Set = ADL_ADAPTER_CROSSDISPLAYINFOX2_SET


def Init(hDLL):
    global _ADL2_Adapter_CrossdisplayAdapterRole_Caps
    global _ADL_Adapter_CrossdisplayAdapterRole_Caps
    global _ADL2_Adapter_CrossdisplayInfo_Get
    global _ADL_Adapter_CrossdisplayInfo_Get
    global _ADL2_Adapter_CrossdisplayInfo_Set
    global _ADL_Adapter_CrossdisplayInfo_Set
    global _ADL2_Adapter_CrossDisplayPlatformInfo_Get
    global _ADL_Adapter_CrossDisplayPlatformInfo_Get
    global _ADL2_Adapter_CrossdisplayInfoX2_Set
    global _ADL_Adapter_CrossdisplayInfoX2_Set

    _ADL2_Adapter_CrossdisplayAdapterRole_Caps = ADL2_ADAPTER_CROSSDISPLAYADAPTERROLE_CAPS(
          GetProcAddress(hDLL, "ADL2_Adapter_CrossdisplayAdapterRole_Caps")
    )
    _ADL_Adapter_CrossdisplayAdapterRole_Caps = ADL_ADAPTER_CROSSDISPLAYADAPTERROLE_CAPS(
          GetProcAddress(hDLL, "ADL_Adapter_CrossdisplayAdapterRole_Caps")
    )
    _ADL2_Adapter_CrossdisplayInfo_Get = ADL2_ADAPTER_CROSSDISPLAYINFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_CrossdisplayInfo_Get")
    )
    _ADL_Adapter_CrossdisplayInfo_Get = ADL_ADAPTER_CROSSDISPLAYINFO_GET(
          GetProcAddress(hDLL, "ADL_Adapter_CrossdisplayInfo_Get")
    )
    _ADL2_Adapter_CrossdisplayInfo_Set = ADL2_ADAPTER_CROSSDISPLAYINFO_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_CrossdisplayInfo_Set")
    )
    _ADL_Adapter_CrossdisplayInfo_Set = ADL_ADAPTER_CROSSDISPLAYINFO_SET(
          GetProcAddress(hDLL, "ADL_Adapter_CrossdisplayInfo_Set")
    )
    _ADL2_Adapter_CrossDisplayPlatformInfo_Get = ADL2_ADAPTER_CROSSDISPLAYPLATFORMINFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_CrossDisplayPlatformInfo_Get")
    )
    _ADL_Adapter_CrossDisplayPlatformInfo_Get = ADL_ADAPTER_CROSSDISPLAYPLATFORMINFO_GET(
          GetProcAddress(hDLL, "ADL_Adapter_CrossDisplayPlatformInfo_Get")
    )
    _ADL2_Adapter_CrossdisplayInfoX2_Set = ADL2_ADAPTER_CROSSDISPLAYINFOX2_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_CrossdisplayInfoX2_Set")
    )
    _ADL_Adapter_CrossdisplayInfoX2_Set = ADL_ADAPTER_CROSSDISPLAYINFOX2_SET(
          GetProcAddress(hDLL, "ADL_Adapter_CrossdisplayInfoX2_Set")
    )


__all__ = (
    '_ADL2_Adapter_CrossdisplayAdapterRole_Caps',
    '_ADL_Adapter_CrossdisplayAdapterRole_Caps',
    '_ADL2_Adapter_CrossdisplayInfo_Get',
    '_ADL_Adapter_CrossdisplayInfo_Get',
    '_ADL2_Adapter_CrossdisplayInfo_Set',
    '_ADL_Adapter_CrossdisplayInfo_Set',
    '_ADL2_Adapter_CrossDisplayPlatformInfo_Get',
    '_ADL_Adapter_CrossDisplayPlatformInfo_Get',
    '_ADL2_Adapter_CrossdisplayInfoX2_Set',
    '_ADL_Adapter_CrossdisplayInfoX2_Set',
    'CrossDisplay'
)


from .adl_sdk_h import AdapterBase, ADL2_Main_Control_Create  # NOQA


class CrossDisplay(AdapterBase):

    @property
    def __crossdisplay_caps(self):
        lpCrossDisplaySupport = INT()
        lpAdapterRole = INT()
        lpNumPossDisplayAdapters = INT()
        lppPossDisplayAdapters = (INT * 1)()
        lpNnumPosRenderingAdapters = INT()
        lppPosRenderingAdapters = (INT * 1)()
        lpErrorStatus = INT()

        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_CrossdisplayAdapterRole_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpCrossDisplaySupport),
                    ctypes.byref(lpAdapterRole),
                    ctypes.byref(lpNumPossDisplayAdapters),
                    ctypes.byref(lppPossDisplayAdapters),
                    ctypes.byref(lpNnumPosRenderingAdapters),
                    ctypes.byref(lppPosRenderingAdapters),
                    ctypes.byref(lpErrorStatus),
            ) == ADL_OK:
                return (
                    lpCrossDisplaySupport,
                    lpAdapterRole,
                    lpNumPossDisplayAdapters,
                    lppPossDisplayAdapters,
                    lpNnumPosRenderingAdapters,
                    lppPosRenderingAdapters,
                    lpErrorStatus
                )

    @property
    def adapter_role(self):
        """
        0: The input adapter does not support any CrossDisplay roles.
        1: The input adapter supports a rendering role.
        2: The input adpater supports a display role.
        3: The input adapter supports both rendering and display roles.
        :return:
        """

        lpCrossDisplaySupport = self.__crossdisplay_caps

        if lpCrossDisplaySupport is not None:
            return lpCrossDisplaySupport[0].value == 1

    @property
    def is_supported(self):
        lpAdapterRole = self.__crossdisplay_caps

        if lpAdapterRole is not None:
            return lpAdapterRole[1].value

    @property
    def error_status(self):
        lpErrorStatus = self.__crossdisplay_caps

        if lpErrorStatus is not None:
            return lpErrorStatus[-1].value

    @property
    def rendering_adapters(self):
        info = self.__crossdisplay_caps

        if info is None:
            return []

        lpNnumPosRenderingAdapters, lppPosRenderingAdapters = info[4:-1]
        lppPosRenderingAdapters = ctypes.cast(lppPosRenderingAdapters, POINTER(INT))

        res = []
        for i in range(lpNnumPosRenderingAdapters.value):
            res += [lppPosRenderingAdapters[i]]

        return res

    @property
    def display_adapters(self):
        info = self.__crossdisplay_caps

        if info is None:
            return []
        lpNumPossDisplayAdapters, lppPossDisplayAdapters = info[2:-3]

        lppPossDisplayAdapters = ctypes.cast(lppPossDisplayAdapters, POINTER(INT))

        res = []
        for i in range(lpNumPossDisplayAdapters.value):
            res += [lppPossDisplayAdapters[i]]

        return res

    @property
    def display_mode(self):
        """
        0: Multi-adapter mode.
        1: CrossDisplay mode.
        :return:
        """

        lpAdapterRole = INT()
        lpCrossdisplayMode = INT()
        lpNumDisplayAdapters = INT()
        lppDisplayAdapters = (INT * 1)()
        lpNumRenderingAdapters = INT()
        lppRenderingAdapters = (INT * 1)()
        lpErrorCodeStatus = INT()

        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_CrossdisplayInfo_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpAdapterRole),
                    ctypes.byref(lpCrossdisplayMode),
                    ctypes.byref(lpNumDisplayAdapters),
                    ctypes.byref(lppDisplayAdapters),
                    ctypes.byref(lpNumRenderingAdapters),
                    ctypes.byref(lppRenderingAdapters),
                    ctypes.byref(lpErrorCodeStatus),
            ) == ADL_OK:
                return lpCrossdisplayMode.value

