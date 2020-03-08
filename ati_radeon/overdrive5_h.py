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


ADL2_OVERDRIVE5_CURRENTACTIVITY_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPMActivity)
)
ADL_OVERDRIVE5_CURRENTACTIVITY_GET = int(
    INT,
    POINTER(ADLPMActivity)
)
ADL2_OVERDRIVE5_THERMALDEVICES_ENUM = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLThermalControllerInfo)
)
ADL_OVERDRIVE5_THERMALDEVICES_ENUM = int(
    INT,
    INT,
    POINTER(ADLThermalControllerInfo)
)
ADL2_OVERDRIVE5_TEMPERATURE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLTemperature)
)
ADL_OVERDRIVE5_TEMPERATURE_GET = int(
    INT,
    INT,
    POINTER(ADLTemperature)
)
ADL2_OVERDRIVE5_FANSPEEDINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLFanSpeedInfo)
)
ADL_OVERDRIVE5_FANSPEEDINFO_GET = int(
    INT,
    INT,
    POINTER(ADLFanSpeedInfo)
)
ADL2_OVERDRIVE5_FANSPEED_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLFanSpeedValue)
)
ADL_OVERDRIVE5_FANSPEED_GET = int(
    INT,
    INT,
    POINTER(ADLFanSpeedValue)
)
ADL2_OVERDRIVE5_FANSPEED_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLFanSpeedValue)
)
ADL_OVERDRIVE5_FANSPEED_SET = int(
    INT,
    INT,
    POINTER(ADLFanSpeedValue)
)
ADL2_OVERDRIVE5_FANSPEEDTODEFAULT_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_OVERDRIVE5_FANSPEEDTODEFAULT_SET = int(
    INT,
    INT
)
ADL2_OVERDRIVE5_ODPARAMETERS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODParameters)
)
ADL_OVERDRIVE5_ODPARAMETERS_GET = int(
    INT,
    POINTER(ADLODParameters)
)
ADL2_OVERDRIVE5_ODPERFORMANCELEVELS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLODPerformanceLevels)
)
ADL_OVERDRIVE5_ODPERFORMANCELEVELS_GET = int(
    INT,
    INT,
    POINTER(ADLODPerformanceLevels)
)
ADL2_OVERDRIVE5_ODPERFORMANCELEVELS_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODPerformanceLevels)
)
ADL_OVERDRIVE5_ODPERFORMANCELEVELS_SET = int(
    INT,
    POINTER(ADLODPerformanceLevels)
)
ADL2_OVERDRIVE5_POWERCONTROL_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_OVERDRIVE5_POWERCONTROL_CAPS = int(
    INT,
    POINTER(INT)
)
ADL2_OVERDRIVE5_POWERCONTROLINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPowerControlInfo)
)
ADL_OVERDRIVE5_POWERCONTROLINFO_GET = int(
    INT,
    POINTER(ADLPowerControlInfo)
)
ADL2_OVERDRIVE5_POWERCONTROL_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_OVERDRIVE5_POWERCONTROL_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_OVERDRIVE5_POWERCONTROL_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_OVERDRIVE5_POWERCONTROL_SET = int(
    INT,
    INT
)
ADL2_OVERDRIVE_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_OVERDRIVE_CAPS = int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)


# Function to retrieve current power management-related activity.
_ADL2_Overdrive5_CurrentActivity_Get = ADL2_OVERDRIVE5_CURRENTACTIVITY_GET

# Function to retrieve current power management-related activity.
_ADL_Overdrive5_CurrentActivity_Get = ADL_OVERDRIVE5_CURRENTACTIVITY_GET

# Function to retrieve thermal devices information.
_ADL2_Overdrive5_ThermalDevices_Enum = ADL2_OVERDRIVE5_THERMALDEVICES_ENUM

# Function to retrieve thermal devices information.
_ADL_Overdrive5_ThermalDevices_Enum = ADL_OVERDRIVE5_THERMALDEVICES_ENUM

# Function to retrieve thermal controller temperatures.
_ADL2_Overdrive5_Temperature_Get = ADL2_OVERDRIVE5_TEMPERATURE_GET

# Function to retrieve thermal controller temperatures.
_ADL_Overdrive5_Temperature_Get = ADL_OVERDRIVE5_TEMPERATURE_GET

# Function to retrieve the fan speed reporting capability for thermal controllers.
_ADL2_Overdrive5_FanSpeedInfo_Get = ADL2_OVERDRIVE5_FANSPEEDINFO_GET

# Function to retrieve the fan speed reporting capability for thermal controllers.
_ADL_Overdrive5_FanSpeedInfo_Get = ADL_OVERDRIVE5_FANSPEEDINFO_GET

# Function to retrieve the fan speed reported by the thermal controller.
_ADL2_Overdrive5_FanSpeed_Get = ADL2_OVERDRIVE5_FANSPEED_GET

# Function to retrieve the fan speed reported by the thermal controller.
_ADL_Overdrive5_FanSpeed_Get = ADL_OVERDRIVE5_FANSPEED_GET

# Function to set the fan speed.
_ADL2_Overdrive5_FanSpeed_Set = ADL2_OVERDRIVE5_FANSPEED_SET

# Function to set the fan speed.
_ADL_Overdrive5_FanSpeed_Set = ADL_OVERDRIVE5_FANSPEED_SET

# Function to set the fan speed to the default fan speed value.
_ADL2_Overdrive5_FanSpeedToDefault_Set = ADL2_OVERDRIVE5_FANSPEEDTODEFAULT_SET

# Function to set the fan speed to the default fan speed value.
_ADL_Overdrive5_FanSpeedToDefault_Set = ADL_OVERDRIVE5_FANSPEEDTODEFAULT_SET

# Function to retrieve the current Overdrive parameters.
_ADL2_Overdrive5_ODParameters_Get = ADL2_OVERDRIVE5_ODPARAMETERS_GET

# Function to retrieve the current Overdrive parameters.
_ADL_Overdrive5_ODParameters_Get = ADL_OVERDRIVE5_ODPARAMETERS_GET

# Function to retrieve the current or default Overdrive performance levels.
_ADL2_Overdrive5_ODPerformanceLevels_Get = ADL2_OVERDRIVE5_ODPERFORMANCELEVELS_GET

# Function to retrieve the current or default Overdrive performance levels.
_ADL_Overdrive5_ODPerformanceLevels_Get = ADL_OVERDRIVE5_ODPERFORMANCELEVELS_GET

# Function to set the current Overdrive performance levels.
_ADL2_Overdrive5_ODPerformanceLevels_Set = ADL2_OVERDRIVE5_ODPERFORMANCELEVELS_SET

# Function to set the current Overdrive performance levels.
_ADL_Overdrive5_ODPerformanceLevels_Set = ADL_OVERDRIVE5_ODPERFORMANCELEVELS_SET

# Function to check for PowerControl capabilities.
_ADL2_Overdrive5_PowerControl_Caps = ADL2_OVERDRIVE5_POWERCONTROL_CAPS

# Function to check for PowerControl capabilities.
_ADL_Overdrive5_PowerControl_Caps = ADL_OVERDRIVE5_POWERCONTROL_CAPS

# Function to get values of PowerControl information.
_ADL2_Overdrive5_PowerControlInfo_Get = ADL2_OVERDRIVE5_POWERCONTROLINFO_GET

# Function to get values of PowerControl information.
_ADL_Overdrive5_PowerControlInfo_Get = ADL_OVERDRIVE5_POWERCONTROLINFO_GET

# Function to get values of PowerControl.
_ADL2_Overdrive5_PowerControl_Get = ADL2_OVERDRIVE5_POWERCONTROL_GET

# Function to get values of PowerControl.
_ADL_Overdrive5_PowerControl_Get = ADL_OVERDRIVE5_POWERCONTROL_GET

# Function to set values of PowerControl.
_ADL2_Overdrive5_PowerControl_Set = ADL2_OVERDRIVE5_POWERCONTROL_SET

# Function to set values of PowerControl.
_ADL_Overdrive5_PowerControl_Set = ADL_OVERDRIVE5_POWERCONTROL_SET

# Function to retrieve current power management capabilities.
_ADL2_Overdrive_Caps = ADL2_OVERDRIVE_CAPS

# Function to retrieve current power management capabilities.
_ADL_Overdrive_Caps = ADL_OVERDRIVE_CAPS


def Init(hDLL):
    global _ADL2_Overdrive5_CurrentActivity_Get
    global _ADL_Overdrive5_CurrentActivity_Get
    global _ADL2_Overdrive5_ThermalDevices_Enum
    global _ADL_Overdrive5_ThermalDevices_Enum
    global _ADL2_Overdrive5_Temperature_Get
    global _ADL_Overdrive5_Temperature_Get
    global _ADL2_Overdrive5_FanSpeedInfo_Get
    global _ADL_Overdrive5_FanSpeedInfo_Get
    global _ADL2_Overdrive5_FanSpeed_Get
    global _ADL_Overdrive5_FanSpeed_Get
    global _ADL2_Overdrive5_FanSpeed_Set
    global _ADL_Overdrive5_FanSpeed_Set
    global _ADL2_Overdrive5_FanSpeedToDefault_Set
    global _ADL_Overdrive5_FanSpeedToDefault_Set
    global _ADL2_Overdrive5_ODParameters_Get
    global _ADL_Overdrive5_ODParameters_Get
    global _ADL2_Overdrive5_ODPerformanceLevels_Get
    global _ADL_Overdrive5_ODPerformanceLevels_Get
    global _ADL2_Overdrive5_ODPerformanceLevels_Set
    global _ADL_Overdrive5_ODPerformanceLevels_Set
    global _ADL2_Overdrive5_PowerControl_Caps
    global _ADL_Overdrive5_PowerControl_Caps
    global _ADL2_Overdrive5_PowerControlInfo_Get
    global _ADL_Overdrive5_PowerControlInfo_Get
    global _ADL2_Overdrive5_PowerControl_Get
    global _ADL_Overdrive5_PowerControl_Get
    global _ADL2_Overdrive5_PowerControl_Set
    global _ADL_Overdrive5_PowerControl_Set
    global _ADL2_Overdrive_Caps
    global _ADL_Overdrive_Caps

    _ADL2_Overdrive5_CurrentActivity_Get = ADL2_OVERDRIVE5_CURRENTACTIVITY_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_CurrentActivity_Get")
    )
    _ADL_Overdrive5_CurrentActivity_Get = ADL_OVERDRIVE5_CURRENTACTIVITY_GET(
          GetProcAddress(hDLL, "ADL_Overdrive5_CurrentActivity_Get")
    )
    _ADL2_Overdrive5_ThermalDevices_Enum = ADL2_OVERDRIVE5_THERMALDEVICES_ENUM(
          GetProcAddress(hDLL, "ADL2_Overdrive5_ThermalDevices_Enum")
    )
    _ADL_Overdrive5_ThermalDevices_Enum = ADL_OVERDRIVE5_THERMALDEVICES_ENUM(
          GetProcAddress(hDLL, "ADL_Overdrive5_ThermalDevices_Enum")
    )
    _ADL2_Overdrive5_Temperature_Get = ADL2_OVERDRIVE5_TEMPERATURE_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_Temperature_Get")
    )
    _ADL_Overdrive5_Temperature_Get = ADL_OVERDRIVE5_TEMPERATURE_GET(
          GetProcAddress(hDLL, "ADL_Overdrive5_Temperature_Get")
    )
    _ADL2_Overdrive5_FanSpeedInfo_Get = ADL2_OVERDRIVE5_FANSPEEDINFO_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_FanSpeedInfo_Get")
    )
    _ADL_Overdrive5_FanSpeedInfo_Get = ADL_OVERDRIVE5_FANSPEEDINFO_GET(
          GetProcAddress(hDLL, "ADL_Overdrive5_FanSpeedInfo_Get")
    )
    _ADL2_Overdrive5_FanSpeed_Get = ADL2_OVERDRIVE5_FANSPEED_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_FanSpeed_Get")
    )
    _ADL_Overdrive5_FanSpeed_Get = ADL_OVERDRIVE5_FANSPEED_GET(
          GetProcAddress(hDLL, "ADL_Overdrive5_FanSpeed_Get")
    )
    _ADL2_Overdrive5_FanSpeed_Set = ADL2_OVERDRIVE5_FANSPEED_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_FanSpeed_Set")
    )
    _ADL_Overdrive5_FanSpeed_Set = ADL_OVERDRIVE5_FANSPEED_SET(
          GetProcAddress(hDLL, "ADL_Overdrive5_FanSpeed_Set")
    )
    _ADL2_Overdrive5_FanSpeedToDefault_Set = ADL2_OVERDRIVE5_FANSPEEDTODEFAULT_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_FanSpeedToDefault_Set")
    )
    _ADL_Overdrive5_FanSpeedToDefault_Set = ADL_OVERDRIVE5_FANSPEEDTODEFAULT_SET(
          GetProcAddress(hDLL, "ADL_Overdrive5_FanSpeedToDefault_Set")
    )
    _ADL2_Overdrive5_ODParameters_Get = ADL2_OVERDRIVE5_ODPARAMETERS_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_ODParameters_Get")
    )
    _ADL_Overdrive5_ODParameters_Get = ADL_OVERDRIVE5_ODPARAMETERS_GET(
          GetProcAddress(hDLL, "ADL_Overdrive5_ODParameters_Get")
    )
    _ADL2_Overdrive5_ODPerformanceLevels_Get = ADL2_OVERDRIVE5_ODPERFORMANCELEVELS_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_ODPerformanceLevels_Get")
    )
    _ADL_Overdrive5_ODPerformanceLevels_Get = ADL_OVERDRIVE5_ODPERFORMANCELEVELS_GET(
          GetProcAddress(hDLL, "ADL_Overdrive5_ODPerformanceLevels_Get")
    )
    _ADL2_Overdrive5_ODPerformanceLevels_Set = ADL2_OVERDRIVE5_ODPERFORMANCELEVELS_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_ODPerformanceLevels_Set")
    )
    _ADL_Overdrive5_ODPerformanceLevels_Set = ADL_OVERDRIVE5_ODPERFORMANCELEVELS_SET(
          GetProcAddress(hDLL, "ADL_Overdrive5_ODPerformanceLevels_Set")
    )
    _ADL2_Overdrive5_PowerControl_Caps = ADL2_OVERDRIVE5_POWERCONTROL_CAPS(
          GetProcAddress(hDLL, "ADL2_Overdrive5_PowerControl_Caps")
    )
    _ADL_Overdrive5_PowerControl_Caps = ADL_OVERDRIVE5_POWERCONTROL_CAPS(
          GetProcAddress(hDLL, "ADL_Overdrive5_PowerControl_Caps")
    )
    _ADL2_Overdrive5_PowerControlInfo_Get = ADL2_OVERDRIVE5_POWERCONTROLINFO_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_PowerControlInfo_Get")
    )
    _ADL_Overdrive5_PowerControlInfo_Get = ADL_OVERDRIVE5_POWERCONTROLINFO_GET(
          GetProcAddress(hDLL, "ADL_Overdrive5_PowerControlInfo_Get")
    )
    _ADL2_Overdrive5_PowerControl_Get = ADL2_OVERDRIVE5_POWERCONTROL_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_PowerControl_Get")
    )
    _ADL_Overdrive5_PowerControl_Get = ADL_OVERDRIVE5_POWERCONTROL_GET(
          GetProcAddress(hDLL, "ADL_Overdrive5_PowerControl_Get")
    )
    _ADL2_Overdrive5_PowerControl_Set = ADL2_OVERDRIVE5_POWERCONTROL_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive5_PowerControl_Set")
    )
    _ADL_Overdrive5_PowerControl_Set = ADL_OVERDRIVE5_POWERCONTROL_SET(
          GetProcAddress(hDLL, "ADL_Overdrive5_PowerControl_Set")
    )
    _ADL2_Overdrive_Caps = ADL2_OVERDRIVE_CAPS(
          GetProcAddress(hDLL, "ADL2_Overdrive_Caps")
    )
    _ADL_Overdrive_Caps = ADL_OVERDRIVE_CAPS(
          GetProcAddress(hDLL, "ADL_Overdrive_Caps")
    )


__all__ = (
    '_ADL2_Overdrive5_CurrentActivity_Get',
    '_ADL_Overdrive5_CurrentActivity_Get',
    '_ADL2_Overdrive5_ThermalDevices_Enum',
    '_ADL_Overdrive5_ThermalDevices_Enum',
    '_ADL2_Overdrive5_Temperature_Get',
    '_ADL_Overdrive5_Temperature_Get',
    '_ADL2_Overdrive5_FanSpeedInfo_Get',
    '_ADL_Overdrive5_FanSpeedInfo_Get',
    '_ADL2_Overdrive5_FanSpeed_Get',
    '_ADL_Overdrive5_FanSpeed_Get',
    '_ADL2_Overdrive5_FanSpeed_Set',
    '_ADL_Overdrive5_FanSpeed_Set',
    '_ADL2_Overdrive5_FanSpeedToDefault_Set',
    '_ADL_Overdrive5_FanSpeedToDefault_Set',
    '_ADL2_Overdrive5_ODParameters_Get',
    '_ADL_Overdrive5_ODParameters_Get',
    '_ADL2_Overdrive5_ODPerformanceLevels_Get',
    '_ADL_Overdrive5_ODPerformanceLevels_Get',
    '_ADL2_Overdrive5_ODPerformanceLevels_Set',
    '_ADL_Overdrive5_ODPerformanceLevels_Set',
    '_ADL2_Overdrive5_PowerControl_Caps',
    '_ADL_Overdrive5_PowerControl_Caps',
    '_ADL2_Overdrive5_PowerControlInfo_Get',
    '_ADL_Overdrive5_PowerControlInfo_Get',
    '_ADL2_Overdrive5_PowerControl_Get',
    '_ADL_Overdrive5_PowerControl_Get',
    '_ADL2_Overdrive5_PowerControl_Set',
    '_ADL_Overdrive5_PowerControl_Set',
    '_ADL2_Overdrive_Caps',
    '_ADL_Overdrive_Caps',
)