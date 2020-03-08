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


ADL2_DESKTOPCONFIG_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DESKTOPCONFIG_GET = int(
    INT,
    POINTER(INT)
)
ADL2_DESKTOPCONFIG_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_DESKTOPCONFIG_SET = int(
    INT,
    INT
)
ADL2_NUMBEROFDISPLAYENABLE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_NUMBEROFDISPLAYENABLE_GET = int(
    INT,
    POINTER(INT)
)
ADL2_DISPLAYENABLE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    INT,
    INT
)
ADL_DISPLAYENABLE_SET = int(
    INT,
    POINTER(INT),
    INT,
    INT
)
ADL2_DISPLAY_IDENTIFYDISPLAY = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT,
    INT,
    INT,
    INT
)
ADL_DISPLAY_IDENTIFYDISPLAY = int(
    INT,
    INT,
    INT,
    INT,
    INT,
    INT,
    INT
)
ADL2_DISPLAY_LUTCOLOR_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    ADLGamma
)
ADL_DISPLAY_LUTCOLOR_SET = int(
    INT,
    INT,
    ADLGamma
)
ADL2_DISPLAY_LUTCOLOR_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLGamma),
    POINTER(ADLGamma),
    POINTER(ADLGamma),
    POINTER(ADLGamma)
)
ADL_DISPLAY_LUTCOLOR_GET = int(
    INT,
    INT,
    POINTER(ADLGamma),
    POINTER(ADLGamma),
    POINTER(ADLGamma),
    POINTER(ADLGamma)
)
ADL2_ADAPTER_XSCREENINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    LPXScreenInfo,
    INT
)
ADL_ADAPTER_XSCREENINFO_GET = int(
    LPXScreenInfo,
    INT
)
ADL2_DISPLAY_XRANDRDISPLAYNAME_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(CHAR),
    INT
)
ADL_DISPLAY_XRANDRDISPLAYNAME_GET = int(
    INT,
    INT,
    POINTER(CHAR),
    INT
)
ADL2_ADAPTER_TEAR_FREE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_TEAR_FREE_SET = int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_TEAR_FREE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_TEAR_FREE_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_TEAR_FREE_CAP = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)


# Function to get the Desktop Configuration.
_ADL2_DesktopConfig_Get = ADL2_DESKTOPCONFIG_GET

# Function to get the Desktop Configuration.
_ADL_DesktopConfig_Get = ADL_DESKTOPCONFIG_GET

# Function to set the Desktop Configuration.
_ADL2_DesktopConfig_Set = ADL2_DESKTOPCONFIG_SET

# Function to set the Desktop Configuration.
_ADL_DesktopConfig_Set = ADL_DESKTOPCONFIG_SET

# Function to retrieve the number of enabled displays.
_ADL2_NumberOfDisplayEnable_Get = ADL2_NUMBEROFDISPLAYENABLE_GET

# Function to retrieve the number of enabled displays.
_ADL_NumberOfDisplayEnable_Get = ADL_NUMBEROFDISPLAYENABLE_GET

# Function to dynamically enable displays on a GPU.
_ADL2_DisplayEnable_Set = ADL2_DISPLAYENABLE_SET

# Function to dynamically enable displays on a GPU.
_ADL_DisplayEnable_Set = ADL_DISPLAYENABLE_SET

# Function to set the desktop configuration.
_ADL2_Display_IdentifyDisplay = ADL2_DISPLAY_IDENTIFYDISPLAY

# Function to set the desktop configuration.
_ADL_Display_IdentifyDisplay = ADL_DISPLAY_IDENTIFYDISPLAY

# Function to set the current gamma value for a LUT (controller).
_ADL2_Display_LUTColor_Set = ADL2_DISPLAY_LUTCOLOR_SET

# Function to set the current gamma value for a LUT (controller).
_ADL_Display_LUTColor_Set = ADL_DISPLAY_LUTCOLOR_SET

# Function to get the current value of gamma for a LUT (controller).
_ADL2_Display_LUTColor_Get = ADL2_DISPLAY_LUTCOLOR_GET

# Function to get the current value of gamma for a LUT (controller).
_ADL_Display_LUTColor_Get = ADL_DISPLAY_LUTCOLOR_GET

# Function to retrieve all X Screen information for all OS-known adapters.
_ADL2_Adapter_XScreenInfo_Get = ADL2_ADAPTER_XSCREENINFO_GET

# Function to retrieve all X Screen information for all OS-known adapters.
_ADL_Adapter_XScreenInfo_Get = ADL_ADAPTER_XSCREENINFO_GET

# Function to retrieve the name of the Xrandr display.
_ADL2_Display_XrandrDisplayName_Get = ADL2_DISPLAY_XRANDRDISPLAYNAME_GET

# Function to retrieve the name of the Xrandr display.
_ADL_Display_XrandrDisplayName_Get = ADL_DISPLAY_XRANDRDISPLAYNAME_GET

# Set the requested tear free desktop setting.
_ADL2_Adapter_Tear_Free_Set = ADL2_ADAPTER_TEAR_FREE_SET

# Set the requested tear free desktop setting.
_ADL_Adapter_Tear_Free_Set = ADL_ADAPTER_TEAR_FREE_SET

# Get the requested tear free desktop setting and current status.
_ADL2_Adapter_Tear_Free_Get = ADL2_ADAPTER_TEAR_FREE_GET

# Get the requested tear free desktop setting and current status.
_ADL_Adapter_Tear_Free_Get = ADL_ADAPTER_TEAR_FREE_GET

# Functions to retreive Tear Free setting capabilities of the system.
_ADL2_Adapter_Tear_Free_Cap = ADL2_ADAPTER_TEAR_FREE_CAP


def Init(hDLL):
    global _ADL2_DesktopConfig_Get
    global _ADL_DesktopConfig_Get
    global _ADL2_DesktopConfig_Set
    global _ADL_DesktopConfig_Set
    global _ADL2_NumberOfDisplayEnable_Get
    global _ADL_NumberOfDisplayEnable_Get
    global _ADL2_DisplayEnable_Set
    global _ADL_DisplayEnable_Set
    global _ADL2_Display_IdentifyDisplay
    global _ADL_Display_IdentifyDisplay
    global _ADL2_Display_LUTColor_Set
    global _ADL_Display_LUTColor_Set
    global _ADL2_Display_LUTColor_Get
    global _ADL_Display_LUTColor_Get
    global _ADL2_Adapter_XScreenInfo_Get
    global _ADL_Adapter_XScreenInfo_Get
    global _ADL2_Display_XrandrDisplayName_Get
    global _ADL_Display_XrandrDisplayName_Get
    global _ADL2_Adapter_Tear_Free_Set
    global _ADL_Adapter_Tear_Free_Set
    global _ADL2_Adapter_Tear_Free_Get
    global _ADL_Adapter_Tear_Free_Get
    global _ADL2_Adapter_Tear_Free_Cap

    _ADL2_DesktopConfig_Get = ADL2_DESKTOPCONFIG_GET(
          GetProcAddress(hDLL, "ADL2_DesktopConfig_Get")
    )
    _ADL_DesktopConfig_Get = ADL_DESKTOPCONFIG_GET(
          GetProcAddress(hDLL, "ADL_DesktopConfig_Get")
    )
    _ADL2_DesktopConfig_Set = ADL2_DESKTOPCONFIG_SET(
          GetProcAddress(hDLL, "ADL2_DesktopConfig_Set")
    )
    _ADL_DesktopConfig_Set = ADL_DESKTOPCONFIG_SET(
          GetProcAddress(hDLL, "ADL_DesktopConfig_Set")
    )
    _ADL2_NumberOfDisplayEnable_Get = ADL2_NUMBEROFDISPLAYENABLE_GET(
          GetProcAddress(hDLL, "ADL2_NumberOfDisplayEnable_Get")
    )
    _ADL_NumberOfDisplayEnable_Get = ADL_NUMBEROFDISPLAYENABLE_GET(
          GetProcAddress(hDLL, "ADL_NumberOfDisplayEnable_Get")
    )
    _ADL2_DisplayEnable_Set = ADL2_DISPLAYENABLE_SET(
          GetProcAddress(hDLL, "ADL2_DisplayEnable_Set")
    )
    _ADL_DisplayEnable_Set = ADL_DISPLAYENABLE_SET(
          GetProcAddress(hDLL, "ADL_DisplayEnable_Set")
    )
    _ADL2_Display_IdentifyDisplay = ADL2_DISPLAY_IDENTIFYDISPLAY(
          GetProcAddress(hDLL, "ADL2_Display_IdentifyDisplay")
    )
    _ADL_Display_IdentifyDisplay = ADL_DISPLAY_IDENTIFYDISPLAY(
          GetProcAddress(hDLL, "ADL_Display_IdentifyDisplay")
    )
    _ADL2_Display_LUTColor_Set = ADL2_DISPLAY_LUTCOLOR_SET(
          GetProcAddress(hDLL, "ADL2_Display_LUTColor_Set")
    )
    _ADL_Display_LUTColor_Set = ADL_DISPLAY_LUTCOLOR_SET(
          GetProcAddress(hDLL, "ADL_Display_LUTColor_Set")
    )
    _ADL2_Display_LUTColor_Get = ADL2_DISPLAY_LUTCOLOR_GET(
          GetProcAddress(hDLL, "ADL2_Display_LUTColor_Get")
    )
    _ADL_Display_LUTColor_Get = ADL_DISPLAY_LUTCOLOR_GET(
          GetProcAddress(hDLL, "ADL_Display_LUTColor_Get")
    )
    _ADL2_Adapter_XScreenInfo_Get = ADL2_ADAPTER_XSCREENINFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_XScreenInfo_Get")
    )
    _ADL_Adapter_XScreenInfo_Get = ADL_ADAPTER_XSCREENINFO_GET(
          GetProcAddress(hDLL, "ADL_Adapter_XScreenInfo_Get")
    )
    _ADL2_Display_XrandrDisplayName_Get = ADL2_DISPLAY_XRANDRDISPLAYNAME_GET(
          GetProcAddress(hDLL, "ADL2_Display_XrandrDisplayName_Get")
    )
    _ADL_Display_XrandrDisplayName_Get = ADL_DISPLAY_XRANDRDISPLAYNAME_GET(
          GetProcAddress(hDLL, "ADL_Display_XrandrDisplayName_Get")
    )
    _ADL2_Adapter_Tear_Free_Set = ADL2_ADAPTER_TEAR_FREE_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_Tear_Free_Set")
    )
    _ADL_Adapter_Tear_Free_Set = ADL_ADAPTER_TEAR_FREE_SET(
          GetProcAddress(hDLL, "ADL_Adapter_Tear_Free_Set")
    )
    _ADL2_Adapter_Tear_Free_Get = ADL2_ADAPTER_TEAR_FREE_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_Tear_Free_Get")
    )
    _ADL_Adapter_Tear_Free_Get = ADL_ADAPTER_TEAR_FREE_GET(
          GetProcAddress(hDLL, "ADL_Adapter_Tear_Free_Get")
    )
    _ADL2_Adapter_Tear_Free_Cap = ADL2_ADAPTER_TEAR_FREE_CAP(
          GetProcAddress(hDLL, "ADL2_Adapter_Tear_Free_Cap")
    )
    
__all__ = (
    '_ADL2_DesktopConfig_Get',
    '_ADL_DesktopConfig_Get',
    '_ADL2_DesktopConfig_Set',
    '_ADL_DesktopConfig_Set',
    '_ADL2_NumberOfDisplayEnable_Get',
    '_ADL_NumberOfDisplayEnable_Get',
    '_ADL2_DisplayEnable_Set',
    '_ADL_DisplayEnable_Set',
    '_ADL2_Display_IdentifyDisplay',
    '_ADL_Display_IdentifyDisplay',
    '_ADL2_Display_LUTColor_Set',
    '_ADL_Display_LUTColor_Set',
    '_ADL2_Display_LUTColor_Get',
    '_ADL_Display_LUTColor_Get',
    '_ADL2_Adapter_XScreenInfo_Get',
    '_ADL_Adapter_XScreenInfo_Get',
    '_ADL2_Display_XrandrDisplayName_Get',
    '_ADL_Display_XrandrDisplayName_Get',
    '_ADL2_Adapter_Tear_Free_Set',
    '_ADL_Adapter_Tear_Free_Set',
    '_ADL2_Adapter_Tear_Free_Get',
    '_ADL_Adapter_Tear_Free_Get',
    '_ADL2_Adapter_Tear_Free_Cap',
)

