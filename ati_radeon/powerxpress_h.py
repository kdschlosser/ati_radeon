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


ADL2_DISPLAY_POWERXPRESSVERSION_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_POWERXPRESSVERSION_GET = int(
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_POWERXPRESSACTIVEGPU_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_POWERXPRESSACTIVEGPU_GET = int(
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_POWERXPRESSACTIVEGPU_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_POWERXPRESSACTIVEGPU_SET = int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_SET = int(
    INT,
    INT,
    INT
)
ADL2_POWERXPRESS_CONFIG_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPXConfigCaps)
)
ADL_POWERXPRESS_CONFIG_CAPS = int(
    INT,
    POINTER(ADLPXConfigCaps)
)
ADL2_POWERXPRESS_SCHEME_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPXScheme),
    POINTER(ADLPXScheme),
    POINTER(ADLPXScheme)
)
ADL_POWERXPRESS_SCHEME_GET = int(
    INT,
    POINTER(ADLPXScheme),
    POINTER(ADLPXScheme),
    POINTER(ADLPXScheme)
)
ADL2_POWERXPRESS_SCHEME_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLPXScheme
)
ADL_POWERXPRESS_SCHEME_SET = int(
    INT,
    ADLPXScheme
)
ADL2_POWERXPRESS_ANCILLARYDEVICES_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLBdf))
)
ADL_POWERXPRESS_ANCILLARYDEVICES_GET = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLBdf))
)
ADL2_SWITCHABLEGRAPHICS_APPLICATIONS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLSGApplicationInfo))
)


# Function to retrieve the PowerXpress version.
_ADL2_Display_PowerXpressVersion_Get = ADL2_DISPLAY_POWERXPRESSVERSION_GET

# Function to retrieve the PowerXpress version.
_ADL_Display_PowerXpressVersion_Get = ADL_DISPLAY_POWERXPRESSVERSION_GET

# Function to get the active GPU in PowerXpress.
_ADL2_Display_PowerXpressActiveGPU_Get = ADL2_DISPLAY_POWERXPRESSACTIVEGPU_GET

# Function to get the active GPU in PowerXpress.
_ADL_Display_PowerXpressActiveGPU_Get = ADL_DISPLAY_POWERXPRESSACTIVEGPU_GET

# Function to set the active GPU in PowerXpress.
_ADL2_Display_PowerXpressActiveGPU_Set = ADL2_DISPLAY_POWERXPRESSACTIVEGPU_SET

# Function to set the active GPU in PowerXpress.
_ADL_Display_PowerXpressActiveGPU_Set = ADL_DISPLAY_POWERXPRESSACTIVEGPU_SET

# Function to retrieve the auto switch configuration setting for PowerXpress. This is not supported when DPPE state switching is configured.
_ADL2_Display_PowerXpress_AutoSwitchConfig_Get = ADL2_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_GET

# Function to retrieve the auto switch configuration setting for PowerXpress. This is not supported when DPPE state switching is configured.
_ADL_Display_PowerXpress_AutoSwitchConfig_Get = ADL_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_GET

# Function to set the auto switch configuration setting for PowerXpress. This is not supported when DPPE state switching is configured.
_ADL2_Display_PowerXpress_AutoSwitchConfig_Set = ADL2_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_SET

# Function to set the auto switch configuration setting for PowerXpress. This is not supported when DPPE state switching is configured.
_ADL_Display_PowerXpress_AutoSwitchConfig_Set = ADL_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_SET

# This function gets the PowerXpress configuration Caps.
_ADL2_PowerXpress_Config_Caps = ADL2_POWERXPRESS_CONFIG_CAPS

# This function gets the PowerXpress configuration Caps.
_ADL_PowerXpress_Config_Caps = ADL_POWERXPRESS_CONFIG_CAPS

# This function gets the PowerXpress scheme.
_ADL2_PowerXpress_Scheme_Get = ADL2_POWERXPRESS_SCHEME_GET

# This function gets the PowerXpress scheme.
_ADL_PowerXpress_Scheme_Get = ADL_POWERXPRESS_SCHEME_GET

# This function sets the PowerXpress scheme.
_ADL2_PowerXpress_Scheme_Set = ADL2_POWERXPRESS_SCHEME_SET

# This function sets the PowerXpress scheme.
_ADL_PowerXpress_Scheme_Set = ADL_POWERXPRESS_SCHEME_SET

# This function gets ancillary GPUs.
_ADL2_PowerXpress_AncillaryDevices_Get = ADL2_POWERXPRESS_ANCILLARYDEVICES_GET

# This function gets ancillary GPUs.
_ADL_PowerXpress_AncillaryDevices_Get = ADL_POWERXPRESS_ANCILLARYDEVICES_GET

# ADL local interface. Function to get all the recently ran and currently running applications.
_ADL2_SwitchableGraphics_Applications_Get = ADL2_SWITCHABLEGRAPHICS_APPLICATIONS_GET


def Init(hDLL):
    global _ADL2_Display_PowerXpressVersion_Get
    global _ADL_Display_PowerXpressVersion_Get
    global _ADL2_Display_PowerXpressActiveGPU_Get
    global _ADL_Display_PowerXpressActiveGPU_Get
    global _ADL2_Display_PowerXpressActiveGPU_Set
    global _ADL_Display_PowerXpressActiveGPU_Set
    global _ADL2_Display_PowerXpress_AutoSwitchConfig_Get
    global _ADL_Display_PowerXpress_AutoSwitchConfig_Get
    global _ADL2_Display_PowerXpress_AutoSwitchConfig_Set
    global _ADL_Display_PowerXpress_AutoSwitchConfig_Set
    global _ADL2_PowerXpress_Config_Caps
    global _ADL_PowerXpress_Config_Caps
    global _ADL2_PowerXpress_Scheme_Get
    global _ADL_PowerXpress_Scheme_Get
    global _ADL2_PowerXpress_Scheme_Set
    global _ADL_PowerXpress_Scheme_Set
    global _ADL2_PowerXpress_AncillaryDevices_Get
    global _ADL_PowerXpress_AncillaryDevices_Get
    global _ADL2_SwitchableGraphics_Applications_Get

    _ADL2_Display_PowerXpressVersion_Get = ADL2_DISPLAY_POWERXPRESSVERSION_GET(
          GetProcAddress(hDLL, "ADL2_Display_PowerXpressVersion_Get")
    )
    _ADL_Display_PowerXpressVersion_Get = ADL_DISPLAY_POWERXPRESSVERSION_GET(
          GetProcAddress(hDLL, "ADL_Display_PowerXpressVersion_Get")
    )
    _ADL2_Display_PowerXpressActiveGPU_Get = ADL2_DISPLAY_POWERXPRESSACTIVEGPU_GET(
          GetProcAddress(hDLL, "ADL2_Display_PowerXpressActiveGPU_Get")
    )
    _ADL_Display_PowerXpressActiveGPU_Get = ADL_DISPLAY_POWERXPRESSACTIVEGPU_GET(
          GetProcAddress(hDLL, "ADL_Display_PowerXpressActiveGPU_Get")
    )
    _ADL2_Display_PowerXpressActiveGPU_Set = ADL2_DISPLAY_POWERXPRESSACTIVEGPU_SET(
          GetProcAddress(hDLL, "ADL2_Display_PowerXpressActiveGPU_Set")
    )
    _ADL_Display_PowerXpressActiveGPU_Set = ADL_DISPLAY_POWERXPRESSACTIVEGPU_SET(
          GetProcAddress(hDLL, "ADL_Display_PowerXpressActiveGPU_Set")
    )
    _ADL2_Display_PowerXpress_AutoSwitchConfig_Get = ADL2_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_GET(
          GetProcAddress(hDLL, "ADL2_Display_PowerXpress_AutoSwitchConfig_Get")
    )
    _ADL_Display_PowerXpress_AutoSwitchConfig_Get = ADL_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_GET(
          GetProcAddress(hDLL, "ADL_Display_PowerXpress_AutoSwitchConfig_Get")
    )
    _ADL2_Display_PowerXpress_AutoSwitchConfig_Set = ADL2_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_SET(
          GetProcAddress(hDLL, "ADL2_Display_PowerXpress_AutoSwitchConfig_Set")
    )
    _ADL_Display_PowerXpress_AutoSwitchConfig_Set = ADL_DISPLAY_POWERXPRESS_AUTOSWITCHCONFIG_SET(
          GetProcAddress(hDLL, "ADL_Display_PowerXpress_AutoSwitchConfig_Set")
    )
    _ADL2_PowerXpress_Config_Caps = ADL2_POWERXPRESS_CONFIG_CAPS(
          GetProcAddress(hDLL, "ADL2_PowerXpress_Config_Caps")
    )
    _ADL_PowerXpress_Config_Caps = ADL_POWERXPRESS_CONFIG_CAPS(
          GetProcAddress(hDLL, "ADL_PowerXpress_Config_Caps")
    )
    _ADL2_PowerXpress_Scheme_Get = ADL2_POWERXPRESS_SCHEME_GET(
          GetProcAddress(hDLL, "ADL2_PowerXpress_Scheme_Get")
    )
    _ADL_PowerXpress_Scheme_Get = ADL_POWERXPRESS_SCHEME_GET(
          GetProcAddress(hDLL, "ADL_PowerXpress_Scheme_Get")
    )
    _ADL2_PowerXpress_Scheme_Set = ADL2_POWERXPRESS_SCHEME_SET(
          GetProcAddress(hDLL, "ADL2_PowerXpress_Scheme_Set")
    )
    _ADL_PowerXpress_Scheme_Set = ADL_POWERXPRESS_SCHEME_SET(
          GetProcAddress(hDLL, "ADL_PowerXpress_Scheme_Set")
    )
    _ADL2_PowerXpress_AncillaryDevices_Get = ADL2_POWERXPRESS_ANCILLARYDEVICES_GET(
          GetProcAddress(hDLL, "ADL2_PowerXpress_AncillaryDevices_Get")
    )
    _ADL_PowerXpress_AncillaryDevices_Get = ADL_POWERXPRESS_ANCILLARYDEVICES_GET(
          GetProcAddress(hDLL, "ADL_PowerXpress_AncillaryDevices_Get")
    )
    _ADL2_SwitchableGraphics_Applications_Get = ADL2_SWITCHABLEGRAPHICS_APPLICATIONS_GET(
          GetProcAddress(hDLL, "ADL2_SwitchableGraphics_Applications_Get")
    )


__all__ = (
    '_ADL2_Display_PowerXpressVersion_Get',
    '_ADL_Display_PowerXpressVersion_Get',
    '_ADL2_Display_PowerXpressActiveGPU_Get',
    '_ADL_Display_PowerXpressActiveGPU_Get',
    '_ADL2_Display_PowerXpressActiveGPU_Set',
    '_ADL_Display_PowerXpressActiveGPU_Set',
    '_ADL2_Display_PowerXpress_AutoSwitchConfig_Get',
    '_ADL_Display_PowerXpress_AutoSwitchConfig_Get',
    '_ADL2_Display_PowerXpress_AutoSwitchConfig_Set',
    '_ADL_Display_PowerXpress_AutoSwitchConfig_Set',
    '_ADL2_PowerXpress_Config_Caps',
    '_ADL_PowerXpress_Config_Caps',
    '_ADL2_PowerXpress_Scheme_Get',
    '_ADL_PowerXpress_Scheme_Get',
    '_ADL2_PowerXpress_Scheme_Set',
    '_ADL_PowerXpress_Scheme_Set',
    '_ADL2_PowerXpress_AncillaryDevices_Get',
    '_ADL_PowerXpress_AncillaryDevices_Get',
    '_ADL2_SwitchableGraphics_Applications_Get',
)
