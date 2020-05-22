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
from . import utils

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


# ==============================================================================
# These 2 classes are wrapper classes, one subclasses int and the other float
# The purpose for these classes is to extend the default behavior of int and float
# so we can use right hand operations to set the value.
# //=, /=, *=, +=, -=
#
# I have also added properties to these classes.
# default, min, max, step, is_active, unit_of_measure
# not all properties will be available. it depends on what the class is
# being used for.
# ==============================================================================
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
        self._adapter_index = None
        self._level = None
        self._parent = None

    def __idiv__(self, other):
        return self.__ifloordiv__(other)

    def __itruediv__(self, other):
        return self.__idiv__(other)

    def __ifloordiv__(self, other):
        value = self.real // other

        if None in (self._parent, self._level):
            return self

        value = self._parent._set_value(self._level, value)
        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent

        self = cls

        return self

    def __imul__(self, other):
        value = self.real * other

        if None in (self._parent, self._level):
            return self

        value = self._parent._set_value(self._level, value)
        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent
        self = cls

        return self

    def __iadd__(self, other):
        value = self.real + other

        if None in (self._parent, self._level):
            return self

        value = self._parent._set_value(self._level, value)
        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent

        self = cls

        return self

    def __isub__(self, other):
        value = self.real - other

        if None in (self._parent, self._level):
            return self

        value = self._parent._set_value(self._level, value)
        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent

        self = cls

        return self

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
        self._adapter_index = None
        self._level = None
        self._parent = None

    def __idiv__(self, other):
        value = self.real / other

        if None in (self._parent, self._level):
            return self

        value = self._parent._set_value(self._level, value)
        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent

        self = cls

        return self

    def __itruediv__(self, other):
        return self.__idiv__(other)

    def __ifloordiv__(self, other):
        return self

    def __imul__(self, other):
        value = self.real * other

        if None in (self._parent, self._level):
            return self

        value = self._parent._set_value(self._level, value)
        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent
        self = cls

        return self

    def __iadd__(self, other):
        value = self.real + other

        if None in (self._parent, self._level):
            return self

        value = self._parent._set_value(self._level, value)
        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent

        self = cls

        return self

    def __isub__(self, other):
        value = self.real - other

        if None in (self._parent, self._level):
            return self

        value = self._parent._set_value(self._level, value)
        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent

        self = cls

        return self

    @property
    def max(self):
        return self._obj.max_value

# ==============================================================================


class CoreVoltage(FloatValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        currentActivity = ADLPMActivity()
        currentActivity.iSize = ctypes.sizeof(ADLPMActivity)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_CurrentActivity_Get(
                context,
                iAdapterIndex,
                ctypes.byref(currentActivity)
            )
            return currentActivity.iCurrentPerformanceLevel == self._level

    @property
    def step(self):
        return self._obj.step

    @property
    def default(self):
        return self._obj.default

    @property
    def min(self):
        return self._obj.min_value

    @property
    def unit_of_measure(self):
        return 'VDC'


class CoreVoltages(object):
    _core_voltages = None

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    def __getitem__(self, item):
        return list(self)[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += val.real - value

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpActivity = ADLPMActivity()
        lpActivity.iSize = ctypes.sizeof(ADLPMActivity)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_CurrentActivity_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpActivity)
            )
            try:
                return CoreVoltage(lpActivity.iVddc / 1000.0)
            except ZeroDivisionError:
                return CoreVoltage(0)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)

        overdriveParameters = ADLODParameters()
        overdriveParameters.iSize = ctypes.sizeof(ADLODParameters)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_ODParameters_Get(
                context,
                iAdapterIndex,
                ctypes.byref(overdriveParameters)
            )

            iNumberOfPerformanceLevels = overdriveParameters.iNumberOfPerformanceLevels

            if iNumberOfPerformanceLevels <= level or 0 > level:
                return

            min_val = overdriveParameters.sVddc.iMin / 1000.0
            max_val = overdriveParameters.sVddc.iMax / 1000.0
            step_val = overdriveParameters.sVddc.iStep / 1000.0
            value -= value % step_val

            if max_val < value or min_val > value:
                return

            class _ADLODPerformanceLevels(ctypes.Structure):
                _fields_ = [
                    ('iSize', INT),
                    ('iReserved', INT),
                    ('aLevels', ADLODPerformanceLevel * iNumberOfPerformanceLevels),
                ]

            _ADL2_Overdrive5_ODPerformanceLevels_Get.argtypes = [
                ADL_CONTEXT_HANDLE,
                INT,
                INT,
                POINTER(_ADLODPerformanceLevels)
            ]

            _ADL2_Overdrive5_ODPerformanceLevels_Set.argtypes = [
                ADL_CONTEXT_HANDLE,
                INT,
                POINTER(_ADLODPerformanceLevels)
            ]

            size = ctypes.sizeof(_ADLODPerformanceLevels)
            performanceLevels = _ADLODPerformanceLevels()
            performanceLevels.iSize = size

            _ADL2_Overdrive5_ODPerformanceLevels_Get(
                context,
                iAdapterIndex,
                0,
                ctypes.byref(performanceLevels)
            )

            performanceLevels.aLevels[level].iVddc = int(value * 1000)

            _ADL2_Overdrive5_ODPerformanceLevels_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            return value

    def __iter__(self):
        if CoreVoltages._core_voltages is None:
            CoreVoltages._core_voltages = []

            iAdapterIndex = INT(self._adapter_index)

            overdriveParameters = ADLODParameters()
            overdriveParameters.iSize = ctypes.sizeof(ADLODParameters)

            with ADL2_Main_Control_Create as context:
                _ADL2_Overdrive5_ODParameters_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(overdriveParameters)
                )

                iNumberOfPerformanceLevels = overdriveParameters.iNumberOfPerformanceLevels

                class _ADLODPerformanceLevels(ctypes.Structure):
                    _fields_ = [
                        ('iSize', INT),
                        ('iReserved', INT),
                        ('aLevels', ADLODPerformanceLevel * iNumberOfPerformanceLevels),
                    ]

                _ADL2_Overdrive5_ODPerformanceLevels_Get.argtypes = [
                    ADL_CONTEXT_HANDLE,
                    INT,
                    INT,
                    POINTER(_ADLODPerformanceLevels)
                ]

                size = ctypes.sizeof(_ADLODPerformanceLevels)
                performanceLevels = _ADLODPerformanceLevels()
                performanceLevels.iSize = size

                defaultPerformanceLevels = _ADLODPerformanceLevels()
                defaultPerformanceLevels.iSize = size

                currentActivity = ADLPMActivity()
                currentActivity.iSize = ctypes.sizeof(ADLPMActivity)

                _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    0,
                    ctypes.byref(performanceLevels)
                )

                _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    1,
                    ctypes.byref(defaultPerformanceLevels)
                )

            for i in range(iNumberOfPerformanceLevels):
                defaultPerformanceLevel = defaultPerformanceLevels.aLevels[i]
                performanceLevel = performanceLevels.aLevels[i]

                min_val = overdriveParameters.sVddc.iMin / 1000.0
                max_val = overdriveParameters.sVddc.iMax / 1000.0
                step_val = overdriveParameters.sVddc.iStep / 1000.0
                default_val = defaultPerformanceLevel.iVddc / 1000.0
                current_val = performanceLevel.iVddc / 1000.0

                class Values(object):
                    min_value = min_val
                    max_value = max_val
                    step = step_val
                    default = default_val

                value = CoreVoltage(current_val)
                value._obj = Values
                value._adapter_index = self._adapter_index
                value._level = i
                CoreVoltages._core_voltages.append(value)

        return iter(CoreVoltages._core_voltages)


class EngineClock(IntValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        currentActivity = ADLPMActivity()
        currentActivity.iSize = ctypes.sizeof(ADLPMActivity)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_CurrentActivity_Get(
                context,
                iAdapterIndex,
                ctypes.byref(currentActivity)
            )
            return currentActivity.iCurrentPerformanceLevel == self._level

    @property
    def step(self):
        return self._obj.step

    @property
    def default(self):
        return self._obj.default

    @property
    def min(self):
        return self._obj.min_value

    @property
    def unit_of_measure(self):
        return 'MHz'


class EngineClocks(object):
    _engine_clocks = None

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    def __getitem__(self, item):
        return list(self)[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += val.real - value

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpActivity = ADLPMActivity()
        lpActivity.iSize = ctypes.sizeof(ADLPMActivity)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_CurrentActivity_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpActivity)
            )
            try:
                return EngineClock(lpActivity.iEngineClock // 100)
            except ZeroDivisionError:
                return EngineClock(0)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)

        overdriveParameters = ADLODParameters()
        overdriveParameters.iSize = ctypes.sizeof(ADLODParameters)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_ODParameters_Get(
                context,
                iAdapterIndex,
                ctypes.byref(overdriveParameters)
            )

            iNumberOfPerformanceLevels = overdriveParameters.iNumberOfPerformanceLevels

            if iNumberOfPerformanceLevels <= level or 0 > level:
                return

            min_val = overdriveParameters.sEngineClock.iMin // 100
            max_val = overdriveParameters.sEngineClock.iMax // 100
            step_val = overdriveParameters.sEngineClock.iStep // 100
            value -= value % step_val

            if max_val < value or min_val > value:
                return

            class _ADLODPerformanceLevels(ctypes.Structure):
                _fields_ = [
                    ('iSize', INT),
                    ('iReserved', INT),
                    ('aLevels', ADLODPerformanceLevel * iNumberOfPerformanceLevels),
                ]

            _ADL2_Overdrive5_ODPerformanceLevels_Get.argtypes = [
                ADL_CONTEXT_HANDLE,
                INT,
                INT,
                POINTER(_ADLODPerformanceLevels)
            ]

            _ADL2_Overdrive5_ODPerformanceLevels_Set.argtypes = [
                ADL_CONTEXT_HANDLE,
                INT,
                POINTER(_ADLODPerformanceLevels)
            ]

            size = ctypes.sizeof(_ADLODPerformanceLevels)
            performanceLevels = _ADLODPerformanceLevels()
            performanceLevels.iSize = size

            _ADL2_Overdrive5_ODPerformanceLevels_Get(
                context,
                iAdapterIndex,
                0,
                ctypes.byref(performanceLevels)
            )

            performanceLevels.aLevels[level].iEngineClock = value * 100

            _ADL2_Overdrive5_ODPerformanceLevels_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            return value

    def __iter__(self):
        if EngineClocks._engine_clocks is None:
            EngineClocks._engine_clocks = []

            iAdapterIndex = INT(self._adapter_index)

            overdriveParameters = ADLODParameters()
            overdriveParameters.iSize = ctypes.sizeof(ADLODParameters)

            with ADL2_Main_Control_Create as context:
                _ADL2_Overdrive5_ODParameters_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(overdriveParameters)
                )

                iNumberOfPerformanceLevels = overdriveParameters.iNumberOfPerformanceLevels

                class _ADLODPerformanceLevels(ctypes.Structure):
                    _fields_ = [
                        ('iSize', INT),
                        ('iReserved', INT),
                        ('aLevels', ADLODPerformanceLevel * iNumberOfPerformanceLevels),
                    ]

                _ADL2_Overdrive5_ODPerformanceLevels_Get.argtypes = [
                    ADL_CONTEXT_HANDLE,
                    INT,
                    INT,
                    POINTER(_ADLODPerformanceLevels)
                ]

                size = ctypes.sizeof(_ADLODPerformanceLevels)
                performanceLevels = _ADLODPerformanceLevels()
                performanceLevels.iSize = size

                defaultPerformanceLevels = _ADLODPerformanceLevels()
                defaultPerformanceLevels.iSize = size

                currentActivity = ADLPMActivity()
                currentActivity.iSize = ctypes.sizeof(ADLPMActivity)

                _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    0,
                    ctypes.byref(performanceLevels)
                )

                _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    1,
                    ctypes.byref(defaultPerformanceLevels)
                )

            for i in range(iNumberOfPerformanceLevels):
                defaultPerformanceLevel = defaultPerformanceLevels.aLevels[i]
                performanceLevel = performanceLevels.aLevels[i]

                min_val = overdriveParameters.sEngineClock.iMin // 100
                max_val = overdriveParameters.sEngineClock.iMax // 100
                step_val = overdriveParameters.sEngineClock.iStep // 100
                default_val = defaultPerformanceLevel.iEngineClock // 100
                current_val = performanceLevel.iEngineClock // 100

                class Values(object):
                    min_value = min_val
                    max_value = max_val
                    step = step_val
                    default = default_val

                value = EngineClock(current_val)
                value._obj = Values
                value._adapter_index = self._adapter_index
                value._level = i
                EngineClocks._engine_clocks.append(value)

        return iter(EngineClocks._engine_clocks)


class MemoryClock(IntValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        currentActivity = ADLPMActivity()
        currentActivity.iSize = ctypes.sizeof(ADLPMActivity)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_CurrentActivity_Get(
                context,
                iAdapterIndex,
                ctypes.byref(currentActivity)
            )
            return currentActivity.iCurrentPerformanceLevel == self._level

    @property
    def step(self):
        return self._obj.step

    @property
    def default(self):
        return self._obj.default

    @property
    def min(self):
        return self._obj.min_value

    @property
    def unit_of_measure(self):
        return 'MHz'


class MemoryClocks(object):
    _memory_clocks = None

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    def __getitem__(self, item):
        return list(self)[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += val.real - value

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpActivity = ADLPMActivity()
        lpActivity.iSize = ctypes.sizeof(ADLPMActivity)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_CurrentActivity_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpActivity)
            )
            try:
                return MemoryClock(lpActivity.iMemoryClock // 100)
            except ZeroDivisionError:
                return MemoryClock(0)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)

        overdriveParameters = ADLODParameters()
        overdriveParameters.iSize = ctypes.sizeof(ADLODParameters)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_ODParameters_Get(
                context,
                iAdapterIndex,
                ctypes.byref(overdriveParameters)
            )

            iNumberOfPerformanceLevels = overdriveParameters.iNumberOfPerformanceLevels

            if iNumberOfPerformanceLevels <= level or 0 > level:
                return

            min_val = overdriveParameters.sMemoryClock.iMin // 100
            max_val = overdriveParameters.sMemoryClock.iMax // 100
            step_val = overdriveParameters.sMemoryClock.iStep // 100
            value -= value % step_val

            if max_val < value or min_val > value:
                return

            class _ADLODPerformanceLevels(ctypes.Structure):
                _fields_ = [
                    ('iSize', INT),
                    ('iReserved', INT),
                    ('aLevels', ADLODPerformanceLevel * iNumberOfPerformanceLevels),
                ]

            _ADL2_Overdrive5_ODPerformanceLevels_Get.argtypes = [
                ADL_CONTEXT_HANDLE,
                INT,
                INT,
                POINTER(_ADLODPerformanceLevels)
            ]

            _ADL2_Overdrive5_ODPerformanceLevels_Set.argtypes = [
                ADL_CONTEXT_HANDLE,
                INT,
                POINTER(_ADLODPerformanceLevels)
            ]

            size = ctypes.sizeof(_ADLODPerformanceLevels)
            performanceLevels = _ADLODPerformanceLevels()
            performanceLevels.iSize = size

            _ADL2_Overdrive5_ODPerformanceLevels_Get(
                context,
                iAdapterIndex,
                0,
                ctypes.byref(performanceLevels)
            )

            performanceLevels.aLevels[level].iMemoryClock = value * 100

            _ADL2_Overdrive5_ODPerformanceLevels_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            return value

    def __iter__(self):
        if MemoryClocks._memory_clocks is None:
            MemoryClocks._memory_clocks = []

            iAdapterIndex = INT(self._adapter_index)

            overdriveParameters = ADLODParameters()
            overdriveParameters.iSize = ctypes.sizeof(ADLODParameters)

            with ADL2_Main_Control_Create as context:
                _ADL2_Overdrive5_ODParameters_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(overdriveParameters)
                )

                iNumberOfPerformanceLevels = overdriveParameters.iNumberOfPerformanceLevels

                class _ADLODPerformanceLevels(ctypes.Structure):
                    _fields_ = [
                        ('iSize', INT),
                        ('iReserved', INT),
                        ('aLevels', ADLODPerformanceLevel * iNumberOfPerformanceLevels),
                    ]

                _ADL2_Overdrive5_ODPerformanceLevels_Get.argtypes = [
                    ADL_CONTEXT_HANDLE,
                    INT,
                    INT,
                    POINTER(_ADLODPerformanceLevels)
                ]

                size = ctypes.sizeof(_ADLODPerformanceLevels)
                performanceLevels = _ADLODPerformanceLevels()
                performanceLevels.iSize = size

                defaultPerformanceLevels = _ADLODPerformanceLevels()
                defaultPerformanceLevels.iSize = size

                currentActivity = ADLPMActivity()
                currentActivity.iSize = ctypes.sizeof(ADLPMActivity)

                _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    0,
                    ctypes.byref(performanceLevels)
                )

                _ADL2_Overdrive5_ODPerformanceLevels_Get(
                    context,
                    iAdapterIndex,
                    1,
                    ctypes.byref(defaultPerformanceLevels)
                )

            for i in range(iNumberOfPerformanceLevels):
                defaultPerformanceLevel = defaultPerformanceLevels.aLevels[i]
                performanceLevel = performanceLevels.aLevels[i]

                min_val = overdriveParameters.sMemoryClock.iMin // 100
                max_val = overdriveParameters.sMemoryClock.iMax // 100
                step_val = overdriveParameters.sMemoryClock.iStep // 100
                default_val = defaultPerformanceLevel.iMemoryClock // 100
                current_val = performanceLevel.iMemoryClock // 100

                class Values(object):
                    min_value = min_val
                    max_value = max_val
                    step = step_val
                    default = default_val

                value = MemoryClock(current_val)
                value._obj = Values
                value._adapter_index = self._adapter_index
                value._level = i
                MemoryClocks._memory_clocks.append(value)

        return iter(MemoryClocks._memory_clocks)


class FanSpeed(IntValueWrapper):

    @property
    def unit_of_measure(self):
        return self._obj.unit

    @property
    def min(self):
        return self._obj.min_value

    @property
    def automatic(self):
        return self._parent._get_automatic(self._level)

    @automatic.setter
    def automatic(self, value):
        if value is True:
            self._parent._set_automatic(self._level)


class FanSpeeds(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    def __iter__(self):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            iThermalControllerIndex = 0
            while True:
                termalControllerInfo = ADLThermalControllerInfo()
                termalControllerInfo.iSize = ctypes.sizeof(ADLThermalControllerInfo)

                fanSpeedInfo = ADLFanSpeedInfo()
                fanSpeedInfo.iSize = ctypes.sizeof(ADLFanSpeedInfo)

                fanSpeedValue = ADLFanSpeedValue()

                if _ADL2_Overdrive5_ThermalDevices_Enum(
                    context,
                    iAdapterIndex,
                    iThermalControllerIndex,
                    ctypes.byref(termalControllerInfo)
                ) == ADL_WARNING_NO_DATA:
                    break

                iFlags = termalControllerInfo.iFlags

                # if iFlags | ADL_DL_THERMAL_FLAG_FANCONTROL != iFlags:
                #     iThermalControllerIndex += 1
                #     continue

                _ADL2_Overdrive5_FanSpeedInfo_Get(
                    context,
                    iAdapterIndex,
                    iThermalControllerIndex,
                    ctypes.byref(fanSpeedInfo)
                )

                iFlags = fanSpeedInfo.iFlags

                if iFlags | ADL_DL_FANCTRL_SUPPORTS_RPM_READ == iFlags:
                    fanSpeedReportingMethod = ADL_DL_FANCTRL_SPEED_TYPE_RPM
                    min_val = fanSpeedInfo.iMinRPM
                    max_val = fanSpeedInfo.iMaxRPM
                    uom = 'RPM'
                else:
                    fanSpeedReportingMethod = ADL_DL_FANCTRL_SPEED_TYPE_PERCENT
                    min_val = fanSpeedInfo.iMinPercent
                    max_val = fanSpeedInfo.iMaxPercent
                    uom = '%'

                fanSpeedValue.iSpeedType = fanSpeedReportingMethod

                _ADL2_Overdrive5_FanSpeed_Get(
                    context,
                    iAdapterIndex,
                    iThermalControllerIndex,
                    ctypes.byref(fanSpeedValue)
                )

                class FanSpeedMetrics(object):
                    min_value = min_val
                    max_value = max_val
                    unit = uom

                current_val = fanSpeedValue.iFanSpeed

                value = FanSpeed(current_val)
                value._obj = FanSpeedMetrics
                value._level = iThermalControllerIndex
                value._adapter_index = self._adapter_index
                value._parent = self

                yield value
                iThermalControllerIndex += 1

    def _get_automatic(self, level):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            termalControllerInfo = ADLThermalControllerInfo()
            termalControllerInfo.iSize = ctypes.sizeof(ADLThermalControllerInfo)

            fanSpeedInfo = ADLFanSpeedInfo()
            fanSpeedInfo.iSize = ctypes.sizeof(ADLFanSpeedInfo)

            fanSpeedValue = ADLFanSpeedValue()

            if _ADL2_Overdrive5_ThermalDevices_Enum(
                context,
                iAdapterIndex,
                level,
                ctypes.byref(termalControllerInfo)
            ) == ADL_WARNING_NO_DATA:
                return True

            iFlags = termalControllerInfo.iFlags

            if iFlags | ADL_DL_THERMAL_FLAG_FANCONTROL != iFlags:
                return True

            _ADL2_Overdrive5_FanSpeedInfo_Get(
                context,
                iAdapterIndex,
                level,
                ctypes.byref(fanSpeedInfo)
            )

            iFlags = fanSpeedInfo.iFlags

            if iFlags | ADL_DL_FANCTRL_SUPPORTS_RPM_READ == iFlags:
                fanSpeedValue.iSpeedType = ADL_DL_FANCTRL_SPEED_TYPE_RPM
            else:
                fanSpeedValue.iSpeedType = ADL_DL_FANCTRL_SPEED_TYPE_PERCENT

            _ADL2_Overdrive5_FanSpeed_Get(
                context,
                iAdapterIndex,
                level,
                ctypes.byref(fanSpeedValue)
            )

            return not (fanSpeedValue.iFlags == ADL_DL_FANCTRL_FLAG_USER_DEFINED_SPEED)

    def _set_automatic(self, level):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_FanSpeedToDefault_Set(
                context,
                iAdapterIndex,
                level
            )
        
    def _set_value(self, level, value):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            termalControllerInfo = ADLThermalControllerInfo()
            termalControllerInfo.iSize = ctypes.sizeof(ADLThermalControllerInfo)

            fanSpeedInfo = ADLFanSpeedInfo()
            fanSpeedInfo.iSize = ctypes.sizeof(ADLFanSpeedInfo)

            fanSpeedValue = ADLFanSpeedValue()

            if _ADL2_Overdrive5_ThermalDevices_Enum(
                    context,
                    iAdapterIndex,
                    level,
                    ctypes.byref(termalControllerInfo)
            ) == ADL_WARNING_NO_DATA:
                return

            iFlags = termalControllerInfo.iFlags

            if iFlags | ADL_DL_THERMAL_FLAG_FANCONTROL != iFlags:
                return

            _ADL2_Overdrive5_FanSpeedInfo_Get(
                context,
                iAdapterIndex,
                level,
                ctypes.byref(fanSpeedInfo)
            )

            iFlags = fanSpeedInfo.iFlags

            if iFlags | ADL_DL_FANCTRL_SUPPORTS_RPM_WRITE == iFlags:
                fanSpeedReportingMethod = ADL_DL_FANCTRL_SPEED_TYPE_RPM
                min_val = fanSpeedInfo.iMinRPM
                max_val = fanSpeedInfo.iMaxRPM
            elif iFlags | ADL_DL_FANCTRL_SUPPORTS_PERCENT_WRITE == iFlags:
                fanSpeedReportingMethod = ADL_DL_FANCTRL_SPEED_TYPE_PERCENT
                min_val = fanSpeedInfo.iMinPercent
                max_val = fanSpeedInfo.iMaxPercent
            else:
                return

            if min_val > value or max_val < value:
                return

            fanSpeedValue.iSpeedType = fanSpeedReportingMethod
            fanSpeedValue.iFanSpeed = value
            fanSpeedValue.iFlags = ADL_DL_FANCTRL_FLAG_USER_DEFINED_SPEED

            _ADL2_Overdrive5_FanSpeed_Set(
                context,
                iAdapterIndex,
                level,
                ctypes.byref(fanSpeedValue)
            )

            return value

    def __getitem__(self, item):
        speeds = list(self)

        if isinstance(item, FanSpeed):
            for speed in speeds:
                if speed._level == item._level:
                    return speed
            else:
                raise KeyError('Unable to locate fan speed')

        return speeds[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += val.real - value


class PowerThreshold(IntValueWrapper):

    @property
    def step(self):
        return self._obj.step

    @property
    def default(self):
        return self._obj.default

    @property
    def min(self):
        return self._obj.min_value


class Temperature(FloatValueWrapper):

    @property
    def unit_of_measure(self):
        return 'C'


class Load(FloatValueWrapper):

    @property
    def unit_of_measure(self):
        return '%'

    @property
    def min(self):
        return 0.0

    @property
    def max(self):
        return 100.0


class OverDrive5(object):
    _power_threshold = None

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def _activity(self):
        iAdapterIndex = INT(self._adapter_index)
        lpActivity = ADLPMActivity()
        lpActivity.iSize = ctypes.sizeof(ADLPMActivity)

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_CurrentActivity_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpActivity)
            )
            return lpActivity

    @property
    def bus_speed(self):
        lpActivity = self._activity
        return lpActivity.iCurrentBusSpeed // 100

    @property
    def bus_lanes(self):
        lpActivity = self._activity

        class BusLanes(object):
            max_value = lpActivity.iMaximumBusLanes

        bus_lanes = IntValueWrapper(lpActivity.iCurrentBusLanes)
        bus_lanes._obj = BusLanes

        return bus_lanes

    @property
    def load(self):
        lpActivity = self._activity
        return Load(lpActivity.iActivityPercent / 10.0)

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
    def temperatures(self):
        res = []
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            for i, termalControllerInfo in enumerate(self._thermal_controller_infos):
                if termalControllerInfo.iThermalDomain == ADL_DL_THERMAL_DOMAIN_GPU:
                    adlTemperature = ADLTemperature()
                    adlTemperature.iSize = ctypes.sizeof(ADLTemperature)
                    if _ADL2_Overdrive5_Temperature_Get(
                        context,
                        iAdapterIndex,
                        i,
                        ctypes.byref(adlTemperature)
                    ) == ADL_OK:
                        res += [Temperature(adlTemperature.iTemperature / 1000.0)]
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

    def _set_value(self, _, value):
        if not self.is_power_control_supported:
            return

        iAdapterIndex = INT(self._adapter_index)
        powerControlInfo = ADLPowerControlInfo()
        powerControlCurrent = INT()
        powerControlDefault = INT()

        with ADL2_Main_Control_Create as context:
            _ADL2_Overdrive5_PowerControlInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(powerControlInfo)
            )
            _ADL2_Overdrive5_PowerControl_Get(
                context,
                iAdapterIndex,
                ctypes.byref(powerControlCurrent),
                ctypes.byref(powerControlDefault)
            )

            min_val = powerControlInfo.iMinValue
            max_val = powerControlInfo.iMaxValue
            step_val = powerControlInfo.iStepValue

            value -= value % step_val

            if min_val > value or max_val < value:
                return

            _ADL2_Overdrive5_PowerControl_Set(
                context,
                iAdapterIndex,
                value
            )
            return value

    @property
    def power_control(self):
        if OverDrive5._power_threshold is None:
            if self.is_power_control_supported:
                iAdapterIndex = INT(self._adapter_index)
                powerControlInfo = ADLPowerControlInfo()
                powerControlCurrent = INT()
                powerControlDefault = INT()

                with ADL2_Main_Control_Create as context:
                    _ADL2_Overdrive5_PowerControlInfo_Get(
                        context,
                        iAdapterIndex,
                        ctypes.byref(powerControlInfo)
                    )
                    _ADL2_Overdrive5_PowerControl_Get(
                        context,
                        iAdapterIndex,
                        ctypes.byref(powerControlCurrent),
                        ctypes.byref(powerControlDefault)
                    )

                    min_val = powerControlInfo.iMinValue
                    max_val = powerControlInfo.iMaxValue
                    step_val = powerControlInfo.iStepValue
                    current_val = powerControlCurrent.value
                    default_val = powerControlDefault.value

            else:
                min_val = 0
                max_val = 0
                step_val = 0
                default_val = 0
                current_val = 0

            class Values(object):
                min_value = min_val
                max_value = max_val
                step = step_val
                default = default_val

            value = PowerThreshold(current_val)
            value._obj = Values
            value._parent = self
            value._level = 0
            value._adapter_index = self._adapter_index

            OverDrive5._power_threshold = value

        return OverDrive5._power_threshold

    @power_control.setter
    def power_control(self, value):
        val = self.power_control
        val += val.real - value

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
    def engine_clocks(self):
        return EngineClocks(self._adapter_index)

    @property
    def memory_clocks(self):
        return MemoryClocks(self._adapter_index)

    @property
    def core_voltages(self):
        return CoreVoltages(self._adapter_index)

    @property
    def fan_speeds(self):
        return FanSpeeds(self._adapter_index)
