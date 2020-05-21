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


ADL2_OVERDRIVE5_CURRENTACTIVITY_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPMActivity)
)
ADL_OVERDRIVE5_CURRENTACTIVITY_GET = _int(
    INT,
    POINTER(ADLPMActivity)
)
ADL2_OVERDRIVE5_THERMALDEVICES_ENUM = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLThermalControllerInfo)
)
ADL_OVERDRIVE5_THERMALDEVICES_ENUM = _int(
    INT,
    INT,
    POINTER(ADLThermalControllerInfo)
)
ADL2_OVERDRIVE5_TEMPERATURE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLTemperature)
)
ADL_OVERDRIVE5_TEMPERATURE_GET = _int(
    INT,
    INT,
    POINTER(ADLTemperature)
)
ADL2_OVERDRIVE5_FANSPEEDINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLFanSpeedInfo)
)
ADL_OVERDRIVE5_FANSPEEDINFO_GET = _int(
    INT,
    INT,
    POINTER(ADLFanSpeedInfo)
)
ADL2_OVERDRIVE5_FANSPEED_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLFanSpeedValue)
)
ADL_OVERDRIVE5_FANSPEED_GET = _int(
    INT,
    INT,
    POINTER(ADLFanSpeedValue)
)
ADL2_OVERDRIVE5_FANSPEED_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLFanSpeedValue)
)
ADL_OVERDRIVE5_FANSPEED_SET = _int(
    INT,
    INT,
    POINTER(ADLFanSpeedValue)
)
ADL2_OVERDRIVE5_FANSPEEDTODEFAULT_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_OVERDRIVE5_FANSPEEDTODEFAULT_SET = _int(
    INT,
    INT
)
ADL2_OVERDRIVE5_ODPARAMETERS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODParameters)
)
ADL_OVERDRIVE5_ODPARAMETERS_GET = _int(
    INT,
    POINTER(ADLODParameters)
)
ADL2_OVERDRIVE5_ODPERFORMANCELEVELS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLODPerformanceLevels)
)
ADL_OVERDRIVE5_ODPERFORMANCELEVELS_GET = _int(
    INT,
    INT,
    POINTER(ADLODPerformanceLevels)
)
ADL2_OVERDRIVE5_ODPERFORMANCELEVELS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODPerformanceLevels)
)
ADL_OVERDRIVE5_ODPERFORMANCELEVELS_SET = _int(
    INT,
    POINTER(ADLODPerformanceLevels)
)
ADL2_OVERDRIVE5_POWERCONTROL_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_OVERDRIVE5_POWERCONTROL_CAPS = _int(
    INT,
    POINTER(INT)
)
ADL2_OVERDRIVE5_POWERCONTROLINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPowerControlInfo)
)
ADL_OVERDRIVE5_POWERCONTROLINFO_GET = _int(
    INT,
    POINTER(ADLPowerControlInfo)
)
ADL2_OVERDRIVE5_POWERCONTROL_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_OVERDRIVE5_POWERCONTROL_GET = _int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_OVERDRIVE5_POWERCONTROL_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_OVERDRIVE5_POWERCONTROL_SET = _int(
    INT,
    INT
)
ADL2_OVERDRIVE_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_OVERDRIVE_CAPS = _int(
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
    'OverDrive5'
)


from .adl_sdk_h import ADL2_Main_Control_Create  # NOQA

AMDVENDORID = 1002
ADL_WARNING_NO_DATA = -100


class IntValueWrapper(int):

    def __init__(self, value=None):
        if value is None:
            super(IntValueWrapper, self).__init__(self)
        else:
            try:
                super(IntValueWrapper, self).__init__(value)
            except TypeError:
                super(IntValueWrapper, self).__init__()

        self._obj = None

    def _set_object(self, obj):
        self._obj = obj

    @property
    def min(self):
        return self._obj.min_value

    @property
    def max(self):
        return self._obj.max_value



class FloatValueWrapper(float):

    def __init__(self, value=None):
        if value is None:
            super(FloatValueWrapper, self).__init__(self)
        else:
            try:
                super(FloatValueWrapper, self).__init__(value)
            except TypeError:
                super(FloatValueWrapper, self).__init__()

        self._obj = None

    def _set_object(self, obj):
        self._obj = obj

    @property
    def min(self):
        return self._obj.min_value

    @property
    def max(self):
        return self._obj.max_value



class FanSpeed(IntValueWrapper):

    @property
    def unit_of_measure(self):
        return self._obj.unit


class PowerThreshold(IntValueWrapper):

    @property
    def step(self):
        return self._obj.step


class ODValue(IntValueWrapper):

    @property
    def step(self):
        return self._obj.step

    @property
    def actual(self):
        return self._obj.actual

    @property
    def default(self):
        return self._obj.default


class FloatODValue(FloatValueWrapper):

    @property
    def step(self):
        return self._obj.step

    @property
    def actual(self):
        return self._obj.actual

    @property
    def default(self):
        return self._obj.default


class PerformanceLevel(object):

    def __init__(self, parent, id):
        self.id = id
        self._parent = parent
        self._adapter_index = parent._adapter_index

    @property
    def _current_activity(self):
        iAdapterIndex = INT(self._adapter_index)
        activity = ADLPMActivity()
        activity.iSize = ctypes.sizeof(ADLPMActivity)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive5_CurrentActivity_Get(
                context,
                iAdapterIndex,
                ctypes.byref(activity)
            ) == ADL_OK:
                return activity

    @property
    def is_active(self):
        currentActivity = self._current_activity

        return currentActivity.iCurrentPerformanceLevel.value == self.id

    @property
    def _performance_level(self):
        iAdapterIndex = INT(self._adapter_index)
        overdriveParameters = self._parent._overdrive_parameters

        class ADLODPerformanceLevels(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iReserved', INT),
                ('aLevels', ADLODPerformanceLevel * overdriveParameters.iNumberOfPerformanceLevels),
            ]

        _ADL2_Overdrive5_ODPerformanceLevels_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            INT,
            POINTER(ADLODPerformanceLevels)
        ]

        size = ctypes.sizeof(ADLODPerformanceLevels)
        performanceLevels = ADLODPerformanceLevels()
        performanceLevels.iSize = size

        with ADL2_Main_Control_Create as context:
            res = _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    0,
                    ctypes.byref(performanceLevels)
            )

            if res == ADL_OK:
                return performanceLevels.aLevels[self.id]

    @property
    def _default_performance_level(self):
        iAdapterIndex = INT(self._adapter_index)
        overdriveParameters = self._parent._overdrive_parameters

        class ADLODPerformanceLevels(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iReserved', INT),
                ('aLevels', ADLODPerformanceLevel * overdriveParameters.iNumberOfPerformanceLevels),
            ]

        _ADL2_Overdrive5_ODPerformanceLevels_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            INT,
            POINTER(ADLODPerformanceLevels)
        ]

        size = ctypes.sizeof(ADLODPerformanceLevels)
        performanceLevels = ADLODPerformanceLevels()
        performanceLevels.iSize = size

        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    1,
                    ctypes.byref(performanceLevels)
            ) == ADL_OK:
                return performanceLevels.aLevels[self.id]

    @property
    def engine_clock(self):
        overdriveParameters = self._parent._overdrive_parameters
        defaultPerformanceLevel = self._default_performance_level
        performanceLevel = self._performance_level
        currentActivity = self._current_activity

        min_engine_clock = overdriveParameters.sEngineClock.iMin // 100
        max_engine_clock = overdriveParameters.sEngineClock.iMax // 100
        step_engine_clock = overdriveParameters.sEngineClock.iStep // 100
        default_engine_clock = defaultPerformanceLevel.iEngineClock // 100
        current_engine_clock = performanceLevel.iEngineClock // 100
        actual_engine_clock = currentActivity.iEngineClock // 100

        class EngineClock(object):
            min_value = min_engine_clock
            max_value = max_engine_clock
            step = step_engine_clock
            default = default_engine_clock
            actual = actual_engine_clock

        engine_clock = ODValue(current_engine_clock)
        engine_clock._set_object(EngineClock)
        return engine_clock

    @engine_clock.setter
    def engine_clock(self, value):
        engine_clock = self.engine_clock

        if value % engine_clock.step:
            return

        if engine_clock.min <= value <= engine_clock.max:
            value *= 100

            overdriveParameters = self._parent._overdrive_parameters
            num_performance_levels = (
                overdriveParameters.iNumberOfPerformanceLevels.value
            )
            iAdapterIndex = INT(self._adapter_index)

            size = (
                ctypes.sizeof(ADLODPerformanceLevels) +
                ctypes.sizeof(ADLODPerformanceLevel) *
                (num_performance_levels - 1)
            )
            performanceLevelsBuffer = (VOID * size)()
            ctypes.memset(performanceLevelsBuffer, 0, size)
            performanceLevels = ctypes.cast(
                performanceLevelsBuffer,
                ctypes.POINTER(ADLODPerformanceLevels)
            )
            performanceLevels.contents.iSize = size

            with ADL2_Main_Control_Create as context:
                if _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    0,
                    performanceLevels
                ) == ADL_OK:
                    performanceLevels.contents.aLevels[self.id].iEngineClock = value
                    _ADL2_Overdrive5_ODPerformanceLevels_Set(
                        context,
                        iAdapterIndex,
                        performanceLevels)

    @property
    def memory_clock(self):
        overdriveParameters = self._parent._overdrive_parameters
        performanceLevel = self._performance_level
        defaultPerformanceLevel = self._default_performance_level
        currentActivity = self._current_activity

        min_memory_clock = overdriveParameters.sMemoryClock.iMin // 100
        max_memory_clock = overdriveParameters.sMemoryClock.iMax // 100
        step_memory_clock = overdriveParameters.sMemoryClock.iStep
        current_memory_clock = performanceLevel.iMemoryClock // 100
        default_memory_clock = defaultPerformanceLevel.iMemoryClock // 100
        actual_memory_clock = currentActivity.iMemoryClock // 100

        class MemoryClock(object):
            min_value = min_memory_clock
            max_value = max_memory_clock
            step = step_memory_clock
            default = default_memory_clock
            actual = actual_memory_clock

        memory_clock = ODValue(current_memory_clock)
        memory_clock._set_object(MemoryClock)
        return memory_clock

    @memory_clock.setter
    def memory_clock(self, value):
        memory_clock = self.memory_clock

        if value % memory_clock.step:
            return

        if memory_clock.min <= value <= memory_clock.max:
            value *= 100

            overdriveParameters = self._parent._overdrive_parameters
            num_performance_levels = (
                overdriveParameters.iNumberOfPerformanceLevels.value
            )
            iAdapterIndex = INT(self._adapter_index)

            size = (
                    ctypes.sizeof(ADLODPerformanceLevels) +
                    ctypes.sizeof(ADLODPerformanceLevel) *
                    (num_performance_levels - 1)
            )
            performanceLevelsBuffer = (VOID * size)()
            ctypes.memset(performanceLevelsBuffer, 0, size)
            performanceLevels = ctypes.cast(
                performanceLevelsBuffer,
                ctypes.POINTER(ADLODPerformanceLevels)
            )
            performanceLevels.contents.iSize = size

            with ADL2_Main_Control_Create as context:
                if _ADL2_Overdrive5_ODPerformanceLevels_Get(
                        context,
                        iAdapterIndex,
                        0,
                        performanceLevels
                ) == ADL_OK:
                    performanceLevels.contents.aLevels[self.id].iMemoryClock = value
                    _ADL2_Overdrive5_ODPerformanceLevels_Set(
                        context,
                        iAdapterIndex,
                        performanceLevels
                    )

    @property
    def core_voltage(self):
        overdriveParameters = self._parent._overdrive_parameters
        defaultPerformanceLevel = self._default_performance_level
        performanceLevel = self._performance_level
        currentActivity = self._current_activity

        min_core_voltage = overdriveParameters.sVddc.iMin / 1000.00
        max_core_voltage = overdriveParameters.sVddc.iMax / 1000.00
        step_core_voltage = overdriveParameters.sVddc.iStep / 1000.00
        default_core_voltage = defaultPerformanceLevel.iVddc / 1000.00
        current_core_voltage = performanceLevel.iVddc / 1000.00
        actual_core_voltage = currentActivity.iVddc / 1000.00

        class CoreVoltage(object):
            min_value = min_core_voltage
            max_value = max_core_voltage
            step = step_core_voltage
            default = default_core_voltage
            actual = actual_core_voltage

        core_voltage = FloatODValue(current_core_voltage)
        core_voltage._set_object(CoreVoltage)
        return core_voltage

    @core_voltage.setter
    def core_voltage(self, value):
        core_voltage = self.core_voltage

        if value % core_voltage.step:
            return

        if core_voltage.min <= value <= core_voltage.max:
            value *= 100

            overdriveParameters = self._parent._overdrive_parameters
            num_performance_levels = (
                overdriveParameters.iNumberOfPerformanceLevels.value
            )
            iAdapterIndex = INT(self._adapter_index)

            size = (
                    ctypes.sizeof(ADLODPerformanceLevels) +
                    ctypes.sizeof(ADLODPerformanceLevel) *
                    (num_performance_levels - 1)
            )
            performanceLevelsBuffer = (VOID * size)()
            ctypes.memset(performanceLevelsBuffer, 0, size)
            performanceLevels = ctypes.cast(
                performanceLevelsBuffer,
                ctypes.POINTER(ADLODPerformanceLevels)
            )
            performanceLevels.contents.iSize = size

            with ADL2_Main_Control_Create as context:
                if _ADL2_Overdrive5_ODPerformanceLevels_Get(
                        context,
                        iAdapterIndex,
                        0,
                        performanceLevels
                ) == ADL_OK:
                    performanceLevels.contents.aLevels[self.id].iVddc = value
                    _ADL2_Overdrive5_ODPerformanceLevels_Set(
                        context,
                        iAdapterIndex,
                        performanceLevels
                    )

    @property
    def activity_percent(self):
        overdriveParameters = self._parent._overdrive_parameters
        currentActivity = self._current_activity

        if overdriveParameters.iActivityReportingSupported:
            return currentActivity.iActivityPercent


class PerformanceLevels(object):

    def __init__(self, parent):
        self._parent = parent
        self._adapter_index = parent._adapter_index

    def __iter__(self):
        overdriveParameters = self._parent._overdrive_parameters
        num_performance_levels = (
            overdriveParameters.iNumberOfPerformanceLevels
        )

        for i in range(num_performance_levels):
            yield PerformanceLevel(self._parent, i)

    def __getitem__(self, item):
        performance_levels = list(self)
        return performance_levels[item]


class FanSpeeds(object):

    def __init__(self, parent):
        self._parent = parent
        self._adapter_index = parent._adapter_index

    @property
    def _fan_speed_infos(self):
        iAdapterIndex = INT(self._adapter_index)
        thermalControllerInfos = self._parent._thermal_controller_infos
        res = []

        with ADL2_Main_Control_Create as context:
            for i in range(len(thermalControllerInfos)):
                fanSpeedInfo = ADLFanSpeedInfo()
                fanSpeedInfo.iSize = ctypes.sizeof(ADLFanSpeedInfo)

                if _ADL2_Overdrive5_FanSpeedInfo_Get(
                        context,
                        iAdapterIndex,
                        i,
                        ctypes.byref(fanSpeedInfo)
                ) == ADL_OK:
                    res += [fanSpeedInfo]

        return res

    def __iter__(self):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            for i, fanSpeedInfo in enumerate(self._fan_speed_infos):

                fanSpeedValue = ADLFanSpeedValue()
                if (
                    fanSpeedInfo.iFlags & ADL_DL_FANCTRL_SUPPORTS_RPM_READ ==
                    ADL_DL_FANCTRL_SUPPORTS_RPM_READ
                ):
                    fanSpeedReportingMethod = ADL_DL_FANCTRL_SPEED_TYPE_RPM
                else:
                    fanSpeedReportingMethod = ADL_DL_FANCTRL_SPEED_TYPE_PERCENT

                fanSpeedValue.iSpeedType = fanSpeedReportingMethod

                if _ADL2_Overdrive5_FanSpeed_Get(
                    context,
                    iAdapterIndex,
                    i,
                    ctypes.byref(fanSpeedValue)
                ) == ADL_OK:
                    if fanSpeedReportingMethod == ADL_DL_FANCTRL_SPEED_TYPE_RPM:
                        current_fan_speed = fanSpeedValue.iFanSpeed
                        min_fan_speed = fanSpeedInfo.iMinRPM
                        max_fan_speed = fanSpeedInfo.iMaxRPM
                        unit_of_measure = 'rpm'
                    else:
                        current_fan_speed = fanSpeedValue.iFanSpeed
                        min_fan_speed = fanSpeedInfo.iMinPercent
                        max_fan_speed = fanSpeedInfo.iMaxPercent
                        unit_of_measure = '%'

                    class FanSpeedMetrics(object):
                        min_value = min_fan_speed
                        max_value = max_fan_speed
                        unit = unit_of_measure

                    fan_speed = FanSpeed(current_fan_speed)
                    fan_speed._set_object(FanSpeedMetrics)

                    yield fan_speed

    def __getitem__(self, item):
        fan_speeds = list(self)
        return fan_speeds[item]

    def __setitem__(self, key, value):
        iAdapterIndex = INT(self._adapter_index)
        fanSpeedInfos = self._fan_speed_infos
        fanSpeedInfo = fanSpeedInfos[key]

        if (
            (
                fanSpeedInfo.iFlags & ADL_DL_FANCTRL_SUPPORTS_RPM_WRITE ==
                ADL_DL_FANCTRL_SUPPORTS_RPM_WRITE
            ) or
            (
                fanSpeedInfo.iFlags & ADL_DL_FANCTRL_SUPPORTS_PERCENT_WRITE ==
                ADL_DL_FANCTRL_SUPPORTS_PERCENT_WRITE
            )
        ):
            fan_speed = list(self)[key]
            if fan_speed.min <= value <= fan_speed.max:

                if (
                    fanSpeedInfo.iFlags.value & ADL_DL_FANCTRL_SUPPORTS_RPM_READ ==
                    ADL_DL_FANCTRL_SUPPORTS_RPM_READ
                ):
                    fanSpeedReportingMethod = ADL_DL_FANCTRL_SPEED_TYPE_RPM
                else:
                    fanSpeedReportingMethod = ADL_DL_FANCTRL_SPEED_TYPE_PERCENT

                newFanSpeed = ADLFanSpeedValue()
                newFanSpeed.iSpeedType = fanSpeedReportingMethod
                newFanSpeed.iFanSpeed = value
                with ADL2_Main_Control_Create as context:
                    _ADL2_Overdrive5_FanSpeed_Set(
                        context,
                        iAdapterIndex,
                        key,
                        ctypes.byref(newFanSpeed)
                    )


class OverDrive5(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def _thermal_controller_infos(self):
        iAdapterIndex = INT(self._adapter_index)

        res = []
        with ADL2_Main_Control_Create as context:
            for iThermalControllerIndex in range(10):
                termalControllerInfo = ADLThermalControllerInfo()
                termalControllerInfo.iSize = ctypes.sizeof(ADLThermalControllerInfo)

                err = _ADL2_Overdrive5_ThermalDevices_Enum(
                    context,
                    iAdapterIndex,
                    iThermalControllerIndex,
                    ctypes.byref(termalControllerInfo)
                )
                if err == ADL_WARNING_NO_DATA:
                    break

                res += [termalControllerInfo]
        return res

    @property
    def _temperatures(self):
        res = []
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            for i, termalControllerInfo in enumerate(self._thermal_controller_infos):
                if termalControllerInfo.iThermalDomain.value == ADL_DL_THERMAL_DOMAIN_GPU:
                    adlTemperature = ADLTemperature()
                    adlTemperature.iSize = ctypes.sizeof(ADLTemperature)
                    if _ADL2_Overdrive5_Temperature_Get(
                        context,
                        iAdapterIndex,
                        i,
                        ctypes.byref(adlTemperature)
                    ) == ADL_OK:
                        res += [adlTemperature.iTemperature.value / 1000.0]
        return res

    @property
    def is_power_control_supported(self):
        powerControlSupported = INT()
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive5_PowerControl_Caps(
                context,
                iAdapterIndex,
                ctypes.byref(powerControlSupported)
            ) == ADL_OK:
                return bool(powerControlSupported.value)

        return False

    @property
    def power_control(self):
        iAdapterIndex = INT(self._adapter_index)
        powerControlInfo = ADLPowerControlInfo()
        powerControlCurrent = INT()
        powerControlDefault = INT()

        with ADL2_Main_Control_Create as context:

            if _ADL2_Overdrive5_PowerControlInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(powerControlInfo)
            ) != ADL_OK:
                return

            if _ADL2_Overdrive5_PowerControl_Get(
                context,
                iAdapterIndex,
                ctypes.byref(powerControlCurrent),
                ctypes.byref(powerControlDefault)
            ) != ADL_OK:
                return

            min_power_threshold = powerControlInfo.iMinValue.value
            max_power_threshold = powerControlInfo.iMaxValue.value
            step_power_threshold = powerControlInfo.iStepValue.value
            current_power_threshold = powerControlCurrent.value

            class PThreshold(object):
                min_value = min_power_threshold
                max_value = max_power_threshold
                step = step_power_threshold

            power_threshold = PowerThreshold(current_power_threshold)
            power_threshold._set_object(PThreshold)

            return power_threshold

    @power_control.setter
    def power_control(self, value):

        if self.is_power_control_supported:
            power_control = self.power_control

            if value % power_control.step:
                return

            if power_control.min <= value <= power_control.max:
                iAdapterIndex = INT(self._adapter_index)

                with ADL2_Main_Control_Create as context:

                    _ADL2_Overdrive5_PowerControl_Set(
                        context,
                        iAdapterIndex,
                        value
                    )

    @property
    def _overdrive_parameters(self):
        overdriveParameters = ADLODParameters()
        overdriveParameters.iSize = ctypes.sizeof(ADLODParameters)
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive5_ODParameters_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(overdriveParameters)
            ) == ADL_OK:
                return overdriveParameters

    @property
    def performance_levels(self):
        return PerformanceLevels(self)

    @property
    def fan_speeds(self):
        return FanSpeeds(self)
