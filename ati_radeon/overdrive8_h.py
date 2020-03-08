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


ADL2_OVERDRIVE8_INIT_SETTING_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD8InitSetting)
)
ADL2_OVERDRIVE8_CURRENT_SETTING_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD8CurrentSetting)
)
ADL2_OVERDRIVE8_SETTING_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD8SetSetting),
    POINTER(ADLOD8CurrentSetting)
)
ADL2_NEW_QUERYPMLOGDATA_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPMLogDataOutput)
)
ADL2_OVERDRIVE8_INIT_SETTINGX2_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLOD8SingleInitSetting))
)
ADL2_OVERDRIVE8_CURRENT_SETTINGX2_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(INT))
)


# Function to retrieve the Overdrive8 initial settings.
_ADL2_Overdrive8_Init_Setting_Get = ADL2_OVERDRIVE8_INIT_SETTING_GET

# Function to retrieve the Overdrive8 current settings.
_ADL2_Overdrive8_Current_Setting_Get = ADL2_OVERDRIVE8_CURRENT_SETTING_GET

# Function to set the Overdrive8 settings.
_ADL2_Overdrive8_Setting_Set = ADL2_OVERDRIVE8_SETTING_SET

# Function to retrieve the Overdrive8 current settings.
_ADL2_New_QueryPMLogData_Get = ADL2_NEW_QUERYPMLOGDATA_GET

# Function to retrieve the Overdrive8 current range settings. This is new versin of ADL2_Overdrive8_Init_Setting_Get. It supports new features and does not need to change the PAI.
_ADL2_Overdrive8_Init_SettingX2_Get = ADL2_OVERDRIVE8_INIT_SETTINGX2_GET

# Function to retrieve the Overdrive8 current settings. This is new versin of ADL2_Overdrive8_Current_SettingX2_Get. It supports new features and does not need to change the PAI.
_ADL2_Overdrive8_Current_SettingX2_Get = ADL2_OVERDRIVE8_CURRENT_SETTINGX2_GET


def Init(hDLL):
    global _ADL2_Overdrive8_Init_Setting_Get
    global _ADL2_Overdrive8_Current_Setting_Get
    global _ADL2_Overdrive8_Setting_Set
    global _ADL2_New_QueryPMLogData_Get
    global _ADL2_Overdrive8_Init_SettingX2_Get
    global _ADL2_Overdrive8_Current_SettingX2_Get

    _ADL2_Overdrive8_Init_Setting_Get = ADL2_OVERDRIVE8_INIT_SETTING_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive8_Init_Setting_Get")
    )
    _ADL2_Overdrive8_Current_Setting_Get = ADL2_OVERDRIVE8_CURRENT_SETTING_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive8_Current_Setting_Get")
    )
    _ADL2_Overdrive8_Setting_Set = ADL2_OVERDRIVE8_SETTING_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive8_Setting_Set")
    )
    _ADL2_New_QueryPMLogData_Get = ADL2_NEW_QUERYPMLOGDATA_GET(
          GetProcAddress(hDLL, "ADL2_New_QueryPMLogData_Get")
    )
    _ADL2_Overdrive8_Init_SettingX2_Get = ADL2_OVERDRIVE8_INIT_SETTINGX2_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive8_Init_SettingX2_Get")
    )
    _ADL2_Overdrive8_Current_SettingX2_Get = ADL2_OVERDRIVE8_CURRENT_SETTINGX2_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive8_Current_SettingX2_Get")
    )


__all__ = (
    '_ADL2_Overdrive8_Init_Setting_Get',
    '_ADL2_Overdrive8_Current_Setting_Get',
    '_ADL2_Overdrive8_Setting_Set',
    '_ADL2_New_QueryPMLogData_Get',
    '_ADL2_Overdrive8_Init_SettingX2_Get',
    '_ADL2_Overdrive8_Current_SettingX2_Get',
)