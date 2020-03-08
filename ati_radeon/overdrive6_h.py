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


ADL2_OVERDRIVE6_CAPABILITIES_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6Capabilities)
)
ADL_OVERDRIVE6_CAPABILITIES_GET = int(
    INT,
    POINTER(ADLOD6Capabilities)
)
ADL2_OVERDRIVE6_STATEINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLOD6StateInfo)
)
ADL_OVERDRIVE6_STATEINFO_GET = int(
    INT,
    INT,
    POINTER(ADLOD6StateInfo)
)
ADL2_OVERDRIVE6_STATE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLOD6StateInfo)
)
ADL_OVERDRIVE6_STATE_SET = int(
    INT,
    INT,
    POINTER(ADLOD6StateInfo)
)
ADL2_OVERDRIVE6_STATE_RESET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_OVERDRIVE6_STATE_RESET = int(
    INT,
    INT
)
ADL2_OVERDRIVE6_CURRENTSTATUS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6CurrentStatus)
)
ADL_OVERDRIVE6_CURRENTSTATUS_GET = int(
    INT,
    POINTER(ADLOD6CurrentStatus)
)
ADL2_OVERDRIVE6_THERMALCONTROLLER_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6ThermalControllerCaps)
)
ADL_OVERDRIVE6_THERMALCONTROLLER_CAPS = int(
    INT,
    POINTER(ADLOD6ThermalControllerCaps)
)
ADL2_OVERDRIVE6_TEMPERATURE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_OVERDRIVE6_TEMPERATURE_GET = int(
    INT,
    POINTER(INT)
)
ADL2_OVERDRIVE6_FANSPEED_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6FanSpeedInfo)
)
ADL_OVERDRIVE6_FANSPEED_GET = int(
    INT,
    POINTER(ADLOD6FanSpeedInfo)
)
ADL2_OVERDRIVE6_FANSPEED_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6FanSpeedValue)
)
ADL_OVERDRIVE6_FANSPEED_SET = int(
    INT,
    POINTER(ADLOD6FanSpeedValue)
)
ADL2_OVERDRIVE6_FANSPEED_RESET = int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_OVERDRIVE6_FANSPEED_RESET = int(
    INT
)
ADL2_OVERDRIVE6_POWERCONTROL_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_OVERDRIVE6_POWERCONTROL_CAPS = int(
    INT,
    POINTER(INT)
)
ADL2_OVERDRIVE6_POWERCONTROLINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6PowerControlInfo)
)
ADL_OVERDRIVE6_POWERCONTROLINFO_GET = int(
    INT,
    POINTER(ADLOD6PowerControlInfo)
)
ADL2_OVERDRIVE6_POWERCONTROL_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_OVERDRIVE6_POWERCONTROL_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_OVERDRIVE6_POWERCONTROL_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_OVERDRIVE6_POWERCONTROL_SET = int(
    INT,
    INT
)
ADL2_OVERDRIVE6_VOLTAGECONTROLINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6VoltageControlInfo)
)
ADL_OVERDRIVE6_VOLTAGECONTROLINFO_GET = int(
    INT,
    POINTER(ADLOD6VoltageControlInfo)
)
ADL2_OVERDRIVE6_VOLTAGECONTROL_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_OVERDRIVE6_VOLTAGECONTROL_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_OVERDRIVE6_VOLTAGECONTROL_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_OVERDRIVE6_VOLTAGECONTROL_SET = int(
    INT,
    INT
)
ADL2_OVERDRIVE6_CAPABILITIESEX_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6CapabilitiesEx)
)
ADL_OVERDRIVE6_CAPABILITIESEX_GET = int(
    INT,
    POINTER(ADLOD6CapabilitiesEx)
)
ADL2_OVERDRIVE6_STATEEX_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLOD6StateEx)
)
ADL_OVERDRIVE6_STATEEX_GET = int(
    INT,
    INT,
    POINTER(ADLOD6StateEx)
)
ADL2_OVERDRIVE6_STATEEX_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLOD6StateEx)
)
ADL_OVERDRIVE6_STATEEX_SET = int(
    INT,
    INT,
    POINTER(ADLOD6StateEx)
)
ADL_OVERDRIVE6_THERMALLIMITUNLOCK_SET = int(
    INT,
    INT,
    INT
)
ADL2_OVERDRIVE6_THERMALLIMITUNLOCK_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_OVERDRIVE6_THERMALLIMITUNLOCK_GET = int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_OVERDRIVE6_THERMALLIMITUNLOCK_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_OVERDRIVE6_ADVANCEDFAN_CAPS = int(
    INT,
    POINTER(INT)
)
ADL2_OVERDRIVE6_ADVANCEDFAN_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_OVERDRIVE6_TARGETTEMPERATURERANGEINFO_GET = int(
    INT,
    POINTER(ADLOD6ParameterRange)
)
ADL2_OVERDRIVE6_TARGETTEMPERATURERANGEINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6ParameterRange)
)
ADL_OVERDRIVE6_TARGETTEMPERATUREDATA_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_OVERDRIVE6_TARGETTEMPERATUREDATA_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_OVERDRIVE6_TARGETTEMPERATUREDATA_SET = int(
    INT,
    INT
)
ADL2_OVERDRIVE6_TARGETTEMPERATUREDATA_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_OVERDRIVE6_FANPWMLIMITRANGEINFO_GET = int(
    INT,
    POINTER(ADLOD6ParameterRange)
)
ADL2_OVERDRIVE6_FANPWMLIMITRANGEINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD6ParameterRange)
)
ADL_OVERDRIVE6_FANPWMLIMITDATA_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_OVERDRIVE6_FANPWMLIMITDATA_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_OVERDRIVE6_FANPWMLIMITDATA_SET = int(
    INT,
    INT
)
ADL2_OVERDRIVE6_FANPWMLIMITDATA_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL2_OVERDRIVE6_CURRENTPOWER_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)


# Function to retrieve the current Overdrive capabilities.
_ADL2_Overdrive6_Capabilities_Get = ADL2_OVERDRIVE6_CAPABILITIES_GET

# Function to retrieve the current Overdrive capabilities.
_ADL_Overdrive6_Capabilities_Get = ADL_OVERDRIVE6_CAPABILITIES_GET

# Function to retrieve the current or default Overdrive clock ranges.
_ADL2_Overdrive6_StateInfo_Get = ADL2_OVERDRIVE6_STATEINFO_GET

# Function to retrieve the current or default Overdrive clock ranges.
_ADL_Overdrive6_StateInfo_Get = ADL_OVERDRIVE6_STATEINFO_GET

# Function to set the current Overdrive clock ranges.
_ADL2_Overdrive6_State_Set = ADL2_OVERDRIVE6_STATE_SET

# Function to set the current Overdrive clock ranges.
_ADL_Overdrive6_State_Set = ADL_OVERDRIVE6_STATE_SET

# Function to reset the Overdrive clock ranges to default.
_ADL2_Overdrive6_State_Reset = ADL2_OVERDRIVE6_STATE_RESET

# Function to reset the Overdrive clock ranges to default.
_ADL_Overdrive6_State_Reset = ADL_OVERDRIVE6_STATE_RESET

# Function to retrieve current Overdrive and performance-related activity.
_ADL2_Overdrive6_CurrentStatus_Get = ADL2_OVERDRIVE6_CURRENTSTATUS_GET

# Function to retrieve current Overdrive and performance-related activity.
_ADL_Overdrive6_CurrentStatus_Get = ADL_OVERDRIVE6_CURRENTSTATUS_GET

# Function to retrieve capabilities of the GPU thermal controller.
_ADL2_Overdrive6_ThermalController_Caps = ADL2_OVERDRIVE6_THERMALCONTROLLER_CAPS

# Function to retrieve capabilities of the GPU thermal controller.
_ADL_Overdrive6_ThermalController_Caps = ADL_OVERDRIVE6_THERMALCONTROLLER_CAPS

# Function to retrieve GPU temperature from the thermal controller.
_ADL2_Overdrive6_Temperature_Get = ADL2_OVERDRIVE6_TEMPERATURE_GET

# Function to retrieve GPU temperature from the thermal controller.
_ADL_Overdrive6_Temperature_Get = ADL_OVERDRIVE6_TEMPERATURE_GET

# Function to retrieve the fan speed reported by the thermal controller.
_ADL2_Overdrive6_FanSpeed_Get = ADL2_OVERDRIVE6_FANSPEED_GET

# Function to retrieve the fan speed reported by the thermal controller.
_ADL_Overdrive6_FanSpeed_Get = ADL_OVERDRIVE6_FANSPEED_GET

# Function to set the fan speed.
_ADL2_Overdrive6_FanSpeed_Set = ADL2_OVERDRIVE6_FANSPEED_SET

# Function to set the fan speed.
_ADL_Overdrive6_FanSpeed_Set = ADL_OVERDRIVE6_FANSPEED_SET

# Function to reset the fan speed to the default.
_ADL2_Overdrive6_FanSpeed_Reset = ADL2_OVERDRIVE6_FANSPEED_RESET

# Function to reset the fan speed to the default.
_ADL_Overdrive6_FanSpeed_Reset = ADL_OVERDRIVE6_FANSPEED_RESET

# Function to check for PowerControl capabilities.
_ADL2_Overdrive6_PowerControl_Caps = ADL2_OVERDRIVE6_POWERCONTROL_CAPS

# Function to check for PowerControl capabilities.
_ADL_Overdrive6_PowerControl_Caps = ADL_OVERDRIVE6_POWERCONTROL_CAPS

# Function to get the PowerControl adjustment range.
_ADL2_Overdrive6_PowerControlInfo_Get = ADL2_OVERDRIVE6_POWERCONTROLINFO_GET

# Function to get the PowerControl adjustment range.
_ADL_Overdrive6_PowerControlInfo_Get = ADL_OVERDRIVE6_POWERCONTROLINFO_GET

# Function to get the current and default PowerControl adjustment values.
_ADL2_Overdrive6_PowerControl_Get = ADL2_OVERDRIVE6_POWERCONTROL_GET

# Function to get the current and default PowerControl adjustment values.
_ADL_Overdrive6_PowerControl_Get = ADL_OVERDRIVE6_POWERCONTROL_GET

# Function to set the current PowerControl adjustment value.
_ADL2_Overdrive6_PowerControl_Set = ADL2_OVERDRIVE6_POWERCONTROL_SET

# Function to set the current PowerControl adjustment value.
_ADL_Overdrive6_PowerControl_Set = ADL_OVERDRIVE6_POWERCONTROL_SET

# Function to get the VoltageControl adjustment range.
_ADL2_Overdrive6_VoltageControlInfo_Get = ADL2_OVERDRIVE6_VOLTAGECONTROLINFO_GET

# Function to get the VoltageControl adjustment range.
_ADL_Overdrive6_VoltageControlInfo_Get = ADL_OVERDRIVE6_VOLTAGECONTROLINFO_GET

# Function to get the current and default VoltageControl adjustment values.
_ADL2_Overdrive6_VoltageControl_Get = ADL2_OVERDRIVE6_VOLTAGECONTROL_GET

# Function to get the current and default VoltageControl adjustment values.
_ADL_Overdrive6_VoltageControl_Get = ADL_OVERDRIVE6_VOLTAGECONTROL_GET

# Function to set the current VoltageControl adjustment value.
_ADL2_Overdrive6_VoltageControl_Set = ADL2_OVERDRIVE6_VOLTAGECONTROL_SET

# Function to set the current VoltageControl adjustment value.
_ADL_Overdrive6_VoltageControl_Set = ADL_OVERDRIVE6_VOLTAGECONTROL_SET

# Function to retrieve the current Overdrive extension capabilities .
_ADL2_Overdrive6_CapabilitiesEx_Get = ADL2_OVERDRIVE6_CAPABILITIESEX_GET

# Function to retrieve the current Overdrive extension capabilities.
_ADL_Overdrive6_CapabilitiesEx_Get = ADL_OVERDRIVE6_CAPABILITIESEX_GET

# Function to retrieve the current or default Overdrive extension clock ranges.
_ADL2_Overdrive6_StateEx_Get = ADL2_OVERDRIVE6_STATEEX_GET

# Function to retrieve the current or default Overdrive extension clock ranges.
_ADL_Overdrive6_StateEx_Get = ADL_OVERDRIVE6_STATEEX_GET

# Function to set the current Overdrive extension clock ranges.
_ADL2_Overdrive6_StateEx_Set = ADL2_OVERDRIVE6_STATEEX_SET

# Function to set the current Overdrive extension clock ranges.
_ADL_Overdrive6_StateEx_Set = ADL_OVERDRIVE6_STATEEX_SET

# Function to enable the current Thermal Limit Unlock feature.
_ADL_Overdrive6_ThermalLimitUnlock_Set = ADL_OVERDRIVE6_THERMALLIMITUNLOCK_SET

# Function to enable the current Thermal Limit Unlock feature.
_ADL2_Overdrive6_ThermalLimitUnlock_Set = ADL2_OVERDRIVE6_THERMALLIMITUNLOCK_SET

# Function to retrieve the current Thermal Limit Unlock feature status.
_ADL_Overdrive6_ThermalLimitUnlock_Get = ADL_OVERDRIVE6_THERMALLIMITUNLOCK_GET

# Function to retrieve the current Thermal Limit Unlock feature status.
_ADL2_Overdrive6_ThermalLimitUnlock_Get = ADL2_OVERDRIVE6_THERMALLIMITUNLOCK_GET

# Function returns the advanced fan control capability of the specified adapter. Advanced fan control is the feature which makes the fan speed is always kept to a minimum within current settings so the acoustics are also minimized. The end users are able to select the target ASIC temperature and fan PWM% via the CCC or other applications.
_ADL_Overdrive6_AdvancedFan_Caps = ADL_OVERDRIVE6_ADVANCEDFAN_CAPS

# Function returns the advanced fan control capability of the specified adapter. Advanced fan control is the feature which makes the fan speed is always kept to a minimum so the acoustics are also minimized. The end user will be able to select the target ASIC temperature and fan PWM% via the CCC or other applications.
_ADL2_Overdrive6_AdvancedFan_Caps = ADL2_OVERDRIVE6_ADVANCEDFAN_CAPS

# Function returns the target temperature range of the specified adapter .
_ADL_Overdrive6_TargetTemperatureRangeInfo_Get = ADL_OVERDRIVE6_TARGETTEMPERATURERANGEINFO_GET

# Function returns the target temperature range of the specified adapter .
_ADL2_Overdrive6_TargetTemperatureRangeInfo_Get = ADL2_OVERDRIVE6_TARGETTEMPERATURERANGEINFO_GET

# Function returns default target temperature and current temp. value of the specified adapter.
_ADL_Overdrive6_TargetTemperatureData_Get = ADL_OVERDRIVE6_TARGETTEMPERATUREDATA_GET

# Function returns default target temperature and current temp. value of the specified adapter.
_ADL2_Overdrive6_TargetTemperatureData_Get = ADL2_OVERDRIVE6_TARGETTEMPERATUREDATA_GET

# Function changes the target temperature current value of the specified adapter .
_ADL_Overdrive6_TargetTemperatureData_Set = ADL_OVERDRIVE6_TARGETTEMPERATUREDATA_SET

# Function changes the target temperature current value of the specified adapter .
_ADL2_Overdrive6_TargetTemperatureData_Set = ADL2_OVERDRIVE6_TARGETTEMPERATUREDATA_SET

# Function returns the target Fan PWM range of the specified adapter .
_ADL_Overdrive6_FanPWMLimitRangeInfo_Get = ADL_OVERDRIVE6_FANPWMLIMITRANGEINFO_GET

# Function returns the target Fan PWM range of the specified adapter .
_ADL2_Overdrive6_FanPWMLimitRangeInfo_Get = ADL2_OVERDRIVE6_FANPWMLIMITRANGEINFO_GET

# Function returns default target Fan PWM and current Fan PWM value of the specified adapter.
_ADL_Overdrive6_FanPWMLimitData_Get = ADL_OVERDRIVE6_FANPWMLIMITDATA_GET

# Function returns default target Fan PWM and current Fan PWM value of the specified adapter.
_ADL2_Overdrive6_FanPWMLimitData_Get = ADL2_OVERDRIVE6_FANPWMLIMITDATA_GET

# Function changes the target Fan PWM current value of the specified adapter .
_ADL_Overdrive6_FanPWMLimitData_Set = ADL_OVERDRIVE6_FANPWMLIMITDATA_SET

# Function changes the target Fan PWM current value of the specified adapter .
_ADL2_Overdrive6_FanPWMLimitData_Set = ADL2_OVERDRIVE6_FANPWMLIMITDATA_SET

# Function returns the current power of the specified adapter .
_ADL2_Overdrive6_CurrentPower_Get = ADL2_OVERDRIVE6_CURRENTPOWER_GET


def Init(hDLL):
    global _ADL2_Overdrive6_Capabilities_Get
    global _ADL_Overdrive6_Capabilities_Get
    global _ADL2_Overdrive6_StateInfo_Get
    global _ADL_Overdrive6_StateInfo_Get
    global _ADL2_Overdrive6_State_Set
    global _ADL_Overdrive6_State_Set
    global _ADL2_Overdrive6_State_Reset
    global _ADL_Overdrive6_State_Reset
    global _ADL2_Overdrive6_CurrentStatus_Get
    global _ADL_Overdrive6_CurrentStatus_Get
    global _ADL2_Overdrive6_ThermalController_Caps
    global _ADL_Overdrive6_ThermalController_Caps
    global _ADL2_Overdrive6_Temperature_Get
    global _ADL_Overdrive6_Temperature_Get
    global _ADL2_Overdrive6_FanSpeed_Get
    global _ADL_Overdrive6_FanSpeed_Get
    global _ADL2_Overdrive6_FanSpeed_Set
    global _ADL_Overdrive6_FanSpeed_Set
    global _ADL2_Overdrive6_FanSpeed_Reset
    global _ADL_Overdrive6_FanSpeed_Reset
    global _ADL2_Overdrive6_PowerControl_Caps
    global _ADL_Overdrive6_PowerControl_Caps
    global _ADL2_Overdrive6_PowerControlInfo_Get
    global _ADL_Overdrive6_PowerControlInfo_Get
    global _ADL2_Overdrive6_PowerControl_Get
    global _ADL_Overdrive6_PowerControl_Get
    global _ADL2_Overdrive6_PowerControl_Set
    global _ADL_Overdrive6_PowerControl_Set
    global _ADL2_Overdrive6_VoltageControlInfo_Get
    global _ADL_Overdrive6_VoltageControlInfo_Get
    global _ADL2_Overdrive6_VoltageControl_Get
    global _ADL_Overdrive6_VoltageControl_Get
    global _ADL2_Overdrive6_VoltageControl_Set
    global _ADL_Overdrive6_VoltageControl_Set
    global _ADL2_Overdrive6_CapabilitiesEx_Get
    global _ADL_Overdrive6_CapabilitiesEx_Get
    global _ADL2_Overdrive6_StateEx_Get
    global _ADL_Overdrive6_StateEx_Get
    global _ADL2_Overdrive6_StateEx_Set
    global _ADL_Overdrive6_StateEx_Set
    global _ADL_Overdrive6_ThermalLimitUnlock_Set
    global _ADL2_Overdrive6_ThermalLimitUnlock_Set
    global _ADL_Overdrive6_ThermalLimitUnlock_Get
    global _ADL2_Overdrive6_ThermalLimitUnlock_Get
    global _ADL_Overdrive6_AdvancedFan_Caps
    global _ADL2_Overdrive6_AdvancedFan_Caps
    global _ADL_Overdrive6_TargetTemperatureRangeInfo_Get
    global _ADL2_Overdrive6_TargetTemperatureRangeInfo_Get
    global _ADL_Overdrive6_TargetTemperatureData_Get
    global _ADL2_Overdrive6_TargetTemperatureData_Get
    global _ADL_Overdrive6_TargetTemperatureData_Set
    global _ADL2_Overdrive6_TargetTemperatureData_Set
    global _ADL_Overdrive6_FanPWMLimitRangeInfo_Get
    global _ADL2_Overdrive6_FanPWMLimitRangeInfo_Get
    global _ADL_Overdrive6_FanPWMLimitData_Get
    global _ADL2_Overdrive6_FanPWMLimitData_Get
    global _ADL_Overdrive6_FanPWMLimitData_Set
    global _ADL2_Overdrive6_FanPWMLimitData_Set
    global _ADL2_Overdrive6_CurrentPower_Get

    _ADL2_Overdrive6_Capabilities_Get = ADL2_OVERDRIVE6_CAPABILITIES_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_Capabilities_Get")
    )
    _ADL_Overdrive6_Capabilities_Get = ADL_OVERDRIVE6_CAPABILITIES_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_Capabilities_Get")
    )
    _ADL2_Overdrive6_StateInfo_Get = ADL2_OVERDRIVE6_STATEINFO_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_StateInfo_Get")
    )
    _ADL_Overdrive6_StateInfo_Get = ADL_OVERDRIVE6_STATEINFO_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_StateInfo_Get")
    )
    _ADL2_Overdrive6_State_Set = ADL2_OVERDRIVE6_STATE_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_State_Set")
    )
    _ADL_Overdrive6_State_Set = ADL_OVERDRIVE6_STATE_SET(
          GetProcAddress(hDLL, "ADL_Overdrive6_State_Set")
    )
    _ADL2_Overdrive6_State_Reset = ADL2_OVERDRIVE6_STATE_RESET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_State_Reset")
    )
    _ADL_Overdrive6_State_Reset = ADL_OVERDRIVE6_STATE_RESET(
          GetProcAddress(hDLL, "ADL_Overdrive6_State_Reset")
    )
    _ADL2_Overdrive6_CurrentStatus_Get = ADL2_OVERDRIVE6_CURRENTSTATUS_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_CurrentStatus_Get")
    )
    _ADL_Overdrive6_CurrentStatus_Get = ADL_OVERDRIVE6_CURRENTSTATUS_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_CurrentStatus_Get")
    )
    _ADL2_Overdrive6_ThermalController_Caps = ADL2_OVERDRIVE6_THERMALCONTROLLER_CAPS(
          GetProcAddress(hDLL, "ADL2_Overdrive6_ThermalController_Caps")
    )
    _ADL_Overdrive6_ThermalController_Caps = ADL_OVERDRIVE6_THERMALCONTROLLER_CAPS(
          GetProcAddress(hDLL, "ADL_Overdrive6_ThermalController_Caps")
    )
    _ADL2_Overdrive6_Temperature_Get = ADL2_OVERDRIVE6_TEMPERATURE_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_Temperature_Get")
    )
    _ADL_Overdrive6_Temperature_Get = ADL_OVERDRIVE6_TEMPERATURE_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_Temperature_Get")
    )
    _ADL2_Overdrive6_FanSpeed_Get = ADL2_OVERDRIVE6_FANSPEED_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_FanSpeed_Get")
    )
    _ADL_Overdrive6_FanSpeed_Get = ADL_OVERDRIVE6_FANSPEED_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_FanSpeed_Get")
    )
    _ADL2_Overdrive6_FanSpeed_Set = ADL2_OVERDRIVE6_FANSPEED_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_FanSpeed_Set")
    )
    _ADL_Overdrive6_FanSpeed_Set = ADL_OVERDRIVE6_FANSPEED_SET(
          GetProcAddress(hDLL, "ADL_Overdrive6_FanSpeed_Set")
    )
    _ADL2_Overdrive6_FanSpeed_Reset = ADL2_OVERDRIVE6_FANSPEED_RESET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_FanSpeed_Reset")
    )
    _ADL_Overdrive6_FanSpeed_Reset = ADL_OVERDRIVE6_FANSPEED_RESET(
          GetProcAddress(hDLL, "ADL_Overdrive6_FanSpeed_Reset")
    )
    _ADL2_Overdrive6_PowerControl_Caps = ADL2_OVERDRIVE6_POWERCONTROL_CAPS(
          GetProcAddress(hDLL, "ADL2_Overdrive6_PowerControl_Caps")
    )
    _ADL_Overdrive6_PowerControl_Caps = ADL_OVERDRIVE6_POWERCONTROL_CAPS(
          GetProcAddress(hDLL, "ADL_Overdrive6_PowerControl_Caps")
    )
    _ADL2_Overdrive6_PowerControlInfo_Get = ADL2_OVERDRIVE6_POWERCONTROLINFO_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_PowerControlInfo_Get")
    )
    _ADL_Overdrive6_PowerControlInfo_Get = ADL_OVERDRIVE6_POWERCONTROLINFO_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_PowerControlInfo_Get")
    )
    _ADL2_Overdrive6_PowerControl_Get = ADL2_OVERDRIVE6_POWERCONTROL_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_PowerControl_Get")
    )
    _ADL_Overdrive6_PowerControl_Get = ADL_OVERDRIVE6_POWERCONTROL_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_PowerControl_Get")
    )
    _ADL2_Overdrive6_PowerControl_Set = ADL2_OVERDRIVE6_POWERCONTROL_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_PowerControl_Set")
    )
    _ADL_Overdrive6_PowerControl_Set = ADL_OVERDRIVE6_POWERCONTROL_SET(
          GetProcAddress(hDLL, "ADL_Overdrive6_PowerControl_Set")
    )
    _ADL2_Overdrive6_VoltageControlInfo_Get = ADL2_OVERDRIVE6_VOLTAGECONTROLINFO_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_VoltageControlInfo_Get")
    )
    _ADL_Overdrive6_VoltageControlInfo_Get = ADL_OVERDRIVE6_VOLTAGECONTROLINFO_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_VoltageControlInfo_Get")
    )
    _ADL2_Overdrive6_VoltageControl_Get = ADL2_OVERDRIVE6_VOLTAGECONTROL_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_VoltageControl_Get")
    )
    _ADL_Overdrive6_VoltageControl_Get = ADL_OVERDRIVE6_VOLTAGECONTROL_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_VoltageControl_Get")
    )
    _ADL2_Overdrive6_VoltageControl_Set = ADL2_OVERDRIVE6_VOLTAGECONTROL_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_VoltageControl_Set")
    )
    _ADL_Overdrive6_VoltageControl_Set = ADL_OVERDRIVE6_VOLTAGECONTROL_SET(
          GetProcAddress(hDLL, "ADL_Overdrive6_VoltageControl_Set")
    )
    _ADL2_Overdrive6_CapabilitiesEx_Get = ADL2_OVERDRIVE6_CAPABILITIESEX_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_CapabilitiesEx_Get")
    )
    _ADL_Overdrive6_CapabilitiesEx_Get = ADL_OVERDRIVE6_CAPABILITIESEX_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_CapabilitiesEx_Get")
    )
    _ADL2_Overdrive6_StateEx_Get = ADL2_OVERDRIVE6_STATEEX_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_StateEx_Get")
    )
    _ADL_Overdrive6_StateEx_Get = ADL_OVERDRIVE6_STATEEX_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_StateEx_Get")
    )
    _ADL2_Overdrive6_StateEx_Set = ADL2_OVERDRIVE6_STATEEX_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_StateEx_Set")
    )
    _ADL_Overdrive6_StateEx_Set = ADL_OVERDRIVE6_STATEEX_SET(
          GetProcAddress(hDLL, "ADL_Overdrive6_StateEx_Set")
    )
    _ADL_Overdrive6_ThermalLimitUnlock_Set = ADL_OVERDRIVE6_THERMALLIMITUNLOCK_SET(
          GetProcAddress(hDLL, "ADL_Overdrive6_ThermalLimitUnlock_Set")
    )
    _ADL2_Overdrive6_ThermalLimitUnlock_Set = ADL2_OVERDRIVE6_THERMALLIMITUNLOCK_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_ThermalLimitUnlock_Set")
    )
    _ADL_Overdrive6_ThermalLimitUnlock_Get = ADL_OVERDRIVE6_THERMALLIMITUNLOCK_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_ThermalLimitUnlock_Get")
    )
    _ADL2_Overdrive6_ThermalLimitUnlock_Get = ADL2_OVERDRIVE6_THERMALLIMITUNLOCK_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_ThermalLimitUnlock_Get")
    )
    _ADL_Overdrive6_AdvancedFan_Caps = ADL_OVERDRIVE6_ADVANCEDFAN_CAPS(
          GetProcAddress(hDLL, "ADL_Overdrive6_AdvancedFan_Caps")
    )
    _ADL2_Overdrive6_AdvancedFan_Caps = ADL2_OVERDRIVE6_ADVANCEDFAN_CAPS(
          GetProcAddress(hDLL, "ADL2_Overdrive6_AdvancedFan_Caps")
    )
    _ADL_Overdrive6_TargetTemperatureRangeInfo_Get = ADL_OVERDRIVE6_TARGETTEMPERATURERANGEINFO_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_TargetTemperatureRangeInfo_Get")
    )
    _ADL2_Overdrive6_TargetTemperatureRangeInfo_Get = ADL2_OVERDRIVE6_TARGETTEMPERATURERANGEINFO_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_TargetTemperatureRangeInfo_Get")
    )
    _ADL_Overdrive6_TargetTemperatureData_Get = ADL_OVERDRIVE6_TARGETTEMPERATUREDATA_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_TargetTemperatureData_Get")
    )
    _ADL2_Overdrive6_TargetTemperatureData_Get = ADL2_OVERDRIVE6_TARGETTEMPERATUREDATA_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_TargetTemperatureData_Get")
    )
    _ADL_Overdrive6_TargetTemperatureData_Set = ADL_OVERDRIVE6_TARGETTEMPERATUREDATA_SET(
          GetProcAddress(hDLL, "ADL_Overdrive6_TargetTemperatureData_Set")
    )
    _ADL2_Overdrive6_TargetTemperatureData_Set = ADL2_OVERDRIVE6_TARGETTEMPERATUREDATA_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_TargetTemperatureData_Set")
    )
    _ADL_Overdrive6_FanPWMLimitRangeInfo_Get = ADL_OVERDRIVE6_FANPWMLIMITRANGEINFO_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_FanPWMLimitRangeInfo_Get")
    )
    _ADL2_Overdrive6_FanPWMLimitRangeInfo_Get = ADL2_OVERDRIVE6_FANPWMLIMITRANGEINFO_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_FanPWMLimitRangeInfo_Get")
    )
    _ADL_Overdrive6_FanPWMLimitData_Get = ADL_OVERDRIVE6_FANPWMLIMITDATA_GET(
          GetProcAddress(hDLL, "ADL_Overdrive6_FanPWMLimitData_Get")
    )
    _ADL2_Overdrive6_FanPWMLimitData_Get = ADL2_OVERDRIVE6_FANPWMLIMITDATA_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_FanPWMLimitData_Get")
    )
    _ADL_Overdrive6_FanPWMLimitData_Set = ADL_OVERDRIVE6_FANPWMLIMITDATA_SET(
          GetProcAddress(hDLL, "ADL_Overdrive6_FanPWMLimitData_Set")
    )
    _ADL2_Overdrive6_FanPWMLimitData_Set = ADL2_OVERDRIVE6_FANPWMLIMITDATA_SET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_FanPWMLimitData_Set")
    )
    _ADL2_Overdrive6_CurrentPower_Get = ADL2_OVERDRIVE6_CURRENTPOWER_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive6_CurrentPower_Get")
    )


__all__ = (
    '_ADL2_Overdrive6_Capabilities_Get',
    '_ADL_Overdrive6_Capabilities_Get',
    '_ADL2_Overdrive6_StateInfo_Get',
    '_ADL_Overdrive6_StateInfo_Get',
    '_ADL2_Overdrive6_State_Set',
    '_ADL_Overdrive6_State_Set',
    '_ADL2_Overdrive6_State_Reset',
    '_ADL_Overdrive6_State_Reset',
    '_ADL2_Overdrive6_CurrentStatus_Get',
    '_ADL_Overdrive6_CurrentStatus_Get',
    '_ADL2_Overdrive6_ThermalController_Caps',
    '_ADL_Overdrive6_ThermalController_Caps',
    '_ADL2_Overdrive6_Temperature_Get',
    '_ADL_Overdrive6_Temperature_Get',
    '_ADL2_Overdrive6_FanSpeed_Get',
    '_ADL_Overdrive6_FanSpeed_Get',
    '_ADL2_Overdrive6_FanSpeed_Set',
    '_ADL_Overdrive6_FanSpeed_Set',
    '_ADL2_Overdrive6_FanSpeed_Reset',
    '_ADL_Overdrive6_FanSpeed_Reset',
    '_ADL2_Overdrive6_PowerControl_Caps',
    '_ADL_Overdrive6_PowerControl_Caps',
    '_ADL2_Overdrive6_PowerControlInfo_Get',
    '_ADL_Overdrive6_PowerControlInfo_Get',
    '_ADL2_Overdrive6_PowerControl_Get',
    '_ADL_Overdrive6_PowerControl_Get',
    '_ADL2_Overdrive6_PowerControl_Set',
    '_ADL_Overdrive6_PowerControl_Set',
    '_ADL2_Overdrive6_VoltageControlInfo_Get',
    '_ADL_Overdrive6_VoltageControlInfo_Get',
    '_ADL2_Overdrive6_VoltageControl_Get',
    '_ADL_Overdrive6_VoltageControl_Get',
    '_ADL2_Overdrive6_VoltageControl_Set',
    '_ADL_Overdrive6_VoltageControl_Set',
    '_ADL2_Overdrive6_CapabilitiesEx_Get',
    '_ADL_Overdrive6_CapabilitiesEx_Get',
    '_ADL2_Overdrive6_StateEx_Get',
    '_ADL_Overdrive6_StateEx_Get',
    '_ADL2_Overdrive6_StateEx_Set',
    '_ADL_Overdrive6_StateEx_Set',
    '_ADL_Overdrive6_ThermalLimitUnlock_Set',
    '_ADL2_Overdrive6_ThermalLimitUnlock_Set',
    '_ADL_Overdrive6_ThermalLimitUnlock_Get',
    '_ADL2_Overdrive6_ThermalLimitUnlock_Get',
    '_ADL_Overdrive6_AdvancedFan_Caps',
    '_ADL2_Overdrive6_AdvancedFan_Caps',
    '_ADL_Overdrive6_TargetTemperatureRangeInfo_Get',
    '_ADL2_Overdrive6_TargetTemperatureRangeInfo_Get',
    '_ADL_Overdrive6_TargetTemperatureData_Get',
    '_ADL2_Overdrive6_TargetTemperatureData_Get',
    '_ADL_Overdrive6_TargetTemperatureData_Set',
    '_ADL2_Overdrive6_TargetTemperatureData_Set',
    '_ADL_Overdrive6_FanPWMLimitRangeInfo_Get',
    '_ADL2_Overdrive6_FanPWMLimitRangeInfo_Get',
    '_ADL_Overdrive6_FanPWMLimitData_Get',
    '_ADL2_Overdrive6_FanPWMLimitData_Get',
    '_ADL_Overdrive6_FanPWMLimitData_Set',
    '_ADL2_Overdrive6_FanPWMLimitData_Set',
    '_ADL2_Overdrive6_CurrentPower_Get',
)