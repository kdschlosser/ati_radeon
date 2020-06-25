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


ADL2_OVERDRIVEN_CAPABILITIES_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNCapabilities)
)
ADL2_OVERDRIVEN_CAPABILITIESX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNCapabilitiesX2)
)
ADL2_OVERDRIVEN_SYSTEMCLOCKS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceLevels)
)
ADL2_OVERDRIVEN_SYSTEMCLOCKS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceLevels)
)
ADL2_OVERDRIVEN_SYSTEMCLOCKSX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceLevelsX2)
)
ADL2_OVERDRIVEN_SYSTEMCLOCKSX2_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceLevelsX2)
)
ADL2_OVERDRIVEN_MEMORYCLOCKSX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceLevelsX2)
)
ADL2_OVERDRIVEN_MEMORYCLOCKSX2_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceLevelsX2)
)
ADL2_OVERDRIVEN_MEMORYCLOCKS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceLevels)
)
ADL2_OVERDRIVEN_MEMORYCLOCKS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceLevels)
)
ADL2_OVERDRIVEN_FANCONTROL_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNFanControl)
)
ADL2_OVERDRIVEN_FANCONTROL_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNFanControl)
)
ADL2_OVERDRIVEN_POWERLIMIT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPowerLimitSetting)
)
ADL2_OVERDRIVEN_POWERLIMIT_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPowerLimitSetting)
)
ADL2_OVERDRIVEN_TEMPERATURE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL2_OVERDRIVEN_PERFORMANCESTATUS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNPerformanceStatus)
)
ADL2_CUSTOMFAN_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL2_CUSTOMFAN_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNFanControl)
)
ADL2_CUSTOMFAN_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLODNFanControl)
)
ADL2_OVERDRIVEN_MEMORYTIMINGLEVEL_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(INT))
)
ADL2_OVERDRIVEN_MEMORYTIMINGLEVEL_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL2_OVERDRIVEN_ZERORPMFAN_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_OVERDRIVEN_ZERORPMFAN_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL2_OVERDRIVEN_SETTINGSEXT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLODNExtSingleInitSetting)),
    POINTER(POINTER(INT))
)
ADL2_OVERDRIVEN_SETTINGSEXT_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)


# Function to retrieve the OverdriveN capabilities.
_ADL2_OverdriveN_Capabilities_Get = ADL2_OVERDRIVEN_CAPABILITIES_GET

# Function to retrieve the OverdriveN capabilities.
_ADL2_OverdriveN_CapabilitiesX2_Get = ADL2_OVERDRIVEN_CAPABILITIESX2_GET

# Function to retrieve the current GPU clocks settings.
_ADL2_OverdriveN_SystemClocks_Get = ADL2_OVERDRIVEN_SYSTEMCLOCKS_GET

# Function to sets the current GPU clocks settings.
_ADL2_OverdriveN_SystemClocks_Set = ADL2_OVERDRIVEN_SYSTEMCLOCKS_SET

# Function to retrieve the current GPU clocks settings.
_ADL2_OverdriveN_SystemClocksX2_Get = ADL2_OVERDRIVEN_SYSTEMCLOCKSX2_GET

# Function to sets the current GPU clocks settings.
_ADL2_OverdriveN_SystemClocksX2_Set = ADL2_OVERDRIVEN_SYSTEMCLOCKSX2_SET

# Function to retrieve the current memory clocks settings.
_ADL2_OverdriveN_MemoryClocksX2_Get = ADL2_OVERDRIVEN_MEMORYCLOCKSX2_GET

# Function to sets the current memory clocks settings.
_ADL2_OverdriveN_MemoryClocksX2_Set = ADL2_OVERDRIVEN_MEMORYCLOCKSX2_SET

# Function to retrieve the current memory clocks settings.
_ADL2_OverdriveN_MemoryClocks_Get = ADL2_OVERDRIVEN_MEMORYCLOCKS_GET

# Function to sets the current memory clocks settings.
_ADL2_OverdriveN_MemoryClocks_Set = ADL2_OVERDRIVEN_MEMORYCLOCKS_SET

# Function to retrieve the current Fan control settings.
_ADL2_OverdriveN_FanControl_Get = ADL2_OVERDRIVEN_FANCONTROL_GET

# Function to set the current Fan controls settings.
_ADL2_OverdriveN_FanControl_Set = ADL2_OVERDRIVEN_FANCONTROL_SET

# Function to retrieve the current power limit settings.
_ADL2_OverdriveN_PowerLimit_Get = ADL2_OVERDRIVEN_POWERLIMIT_GET

# Function to sets the current power limit settings.
_ADL2_OverdriveN_PowerLimit_Set = ADL2_OVERDRIVEN_POWERLIMIT_SET

# Function to retrieve the current temperture.
_ADL2_OverdriveN_Temperature_Get = ADL2_OVERDRIVEN_TEMPERATURE_GET

# Function to retrieve the current OD performance status.
_ADL2_OverdriveN_PerformanceStatus_Get = ADL2_OVERDRIVEN_PERFORMANCESTATUS_GET

# Function to retrieve the Custom Fan support.
_ADL2_CustomFan_Caps = ADL2_CUSTOMFAN_CAPS

# Function to retrieve the Custom Fan current status.
_ADL2_CustomFan_Get = ADL2_CUSTOMFAN_GET

# Function to set the Custom Fan status.
_ADL2_CustomFan_Set = ADL2_CUSTOMFAN_SET

_ADL2_OverdriveN_MemoryTimingLevel_Get = ADL2_OVERDRIVEN_MEMORYTIMINGLEVEL_GET

# Function to change memory timing levels.
_ADL2_OverdriveN_MemoryTimingLevel_Set = ADL2_OVERDRIVEN_MEMORYTIMINGLEVEL_SET

# Function to get zero RPM fan control info.
_ADL2_OverdriveN_ZeroRPMFan_Get = ADL2_OVERDRIVEN_ZERORPMFAN_GET

# Function to change Zero RPM cntrol levels.
_ADL2_OverdriveN_ZeroRPMFan_Set = ADL2_OVERDRIVEN_ZERORPMFAN_SET

# Function to get Fan curve info.
_ADL2_OverdriveN_SettingsExt_Get = ADL2_OVERDRIVEN_SETTINGSEXT_GET

# Function to set fan curve (temperature and speed).
_ADL2_OverdriveN_SettingsExt_Set = ADL2_OVERDRIVEN_SETTINGSEXT_SET


def Init(hDLL):
    global _ADL2_OverdriveN_Capabilities_Get
    global _ADL2_OverdriveN_CapabilitiesX2_Get
    global _ADL2_OverdriveN_SystemClocks_Get
    global _ADL2_OverdriveN_SystemClocks_Set
    global _ADL2_OverdriveN_SystemClocksX2_Get
    global _ADL2_OverdriveN_SystemClocksX2_Set
    global _ADL2_OverdriveN_MemoryClocksX2_Get
    global _ADL2_OverdriveN_MemoryClocksX2_Set
    global _ADL2_OverdriveN_MemoryClocks_Get
    global _ADL2_OverdriveN_MemoryClocks_Set
    global _ADL2_OverdriveN_FanControl_Get
    global _ADL2_OverdriveN_FanControl_Set
    global _ADL2_OverdriveN_PowerLimit_Get
    global _ADL2_OverdriveN_PowerLimit_Set
    global _ADL2_OverdriveN_Temperature_Get
    global _ADL2_OverdriveN_PerformanceStatus_Get
    global _ADL2_CustomFan_Caps
    global _ADL2_CustomFan_Get
    global _ADL2_CustomFan_Set
    global _ADL2_OverdriveN_MemoryTimingLevel_Get
    global _ADL2_OverdriveN_MemoryTimingLevel_Set
    global _ADL2_OverdriveN_ZeroRPMFan_Get
    global _ADL2_OverdriveN_ZeroRPMFan_Set
    global _ADL2_OverdriveN_SettingsExt_Get
    global _ADL2_OverdriveN_SettingsExt_Set

    _ADL2_OverdriveN_Capabilities_Get = ADL2_OVERDRIVEN_CAPABILITIES_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_Capabilities_Get")
    )
    _ADL2_OverdriveN_CapabilitiesX2_Get = ADL2_OVERDRIVEN_CAPABILITIESX2_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_CapabilitiesX2_Get")
    )
    _ADL2_OverdriveN_SystemClocks_Get = ADL2_OVERDRIVEN_SYSTEMCLOCKS_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_SystemClocks_Get")
    )
    _ADL2_OverdriveN_SystemClocks_Set = ADL2_OVERDRIVEN_SYSTEMCLOCKS_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_SystemClocks_Set")
    )
    _ADL2_OverdriveN_SystemClocksX2_Get = ADL2_OVERDRIVEN_SYSTEMCLOCKSX2_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_SystemClocksX2_Get")
    )
    _ADL2_OverdriveN_SystemClocksX2_Set = ADL2_OVERDRIVEN_SYSTEMCLOCKSX2_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_SystemClocksX2_Set")
    )
    _ADL2_OverdriveN_MemoryClocksX2_Get = ADL2_OVERDRIVEN_MEMORYCLOCKSX2_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_MemoryClocksX2_Get")
    )
    _ADL2_OverdriveN_MemoryClocksX2_Set = ADL2_OVERDRIVEN_MEMORYCLOCKSX2_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_MemoryClocksX2_Set")
    )
    _ADL2_OverdriveN_MemoryClocks_Get = ADL2_OVERDRIVEN_MEMORYCLOCKS_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_MemoryClocks_Get")
    )
    _ADL2_OverdriveN_MemoryClocks_Set = ADL2_OVERDRIVEN_MEMORYCLOCKS_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_MemoryClocks_Set")
    )
    _ADL2_OverdriveN_FanControl_Get = ADL2_OVERDRIVEN_FANCONTROL_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_FanControl_Get")
    )
    _ADL2_OverdriveN_FanControl_Set = ADL2_OVERDRIVEN_FANCONTROL_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_FanControl_Set")
    )
    _ADL2_OverdriveN_PowerLimit_Get = ADL2_OVERDRIVEN_POWERLIMIT_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_PowerLimit_Get")
    )
    _ADL2_OverdriveN_PowerLimit_Set = ADL2_OVERDRIVEN_POWERLIMIT_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_PowerLimit_Set")
    )
    _ADL2_OverdriveN_Temperature_Get = ADL2_OVERDRIVEN_TEMPERATURE_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_Temperature_Get")
    )
    _ADL2_OverdriveN_PerformanceStatus_Get = ADL2_OVERDRIVEN_PERFORMANCESTATUS_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_PerformanceStatus_Get")
    )
    _ADL2_CustomFan_Caps = ADL2_CUSTOMFAN_CAPS(
          GetProcAddress(hDLL, "ADL2_CustomFan_Caps")
    )
    _ADL2_CustomFan_Get = ADL2_CUSTOMFAN_GET(
          GetProcAddress(hDLL, "ADL2_CustomFan_Get")
    )
    _ADL2_CustomFan_Set = ADL2_CUSTOMFAN_SET(
          GetProcAddress(hDLL, "ADL2_CustomFan_Set")
    )
    _ADL2_OverdriveN_MemoryTimingLevel_Get = ADL2_OVERDRIVEN_MEMORYTIMINGLEVEL_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_MemoryTimingLevel_Get")
    )
    _ADL2_OverdriveN_MemoryTimingLevel_Set = ADL2_OVERDRIVEN_MEMORYTIMINGLEVEL_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_MemoryTimingLevel_Set")
    )
    _ADL2_OverdriveN_ZeroRPMFan_Get = ADL2_OVERDRIVEN_ZERORPMFAN_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_ZeroRPMFan_Get")
    )
    _ADL2_OverdriveN_ZeroRPMFan_Set = ADL2_OVERDRIVEN_ZERORPMFAN_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_ZeroRPMFan_Set")
    )
    _ADL2_OverdriveN_SettingsExt_Get = ADL2_OVERDRIVEN_SETTINGSEXT_GET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_SettingsExt_Get")
    )
    _ADL2_OverdriveN_SettingsExt_Set = ADL2_OVERDRIVEN_SETTINGSEXT_SET(
          GetProcAddress(hDLL, "ADL2_OverdriveN_SettingsExt_Set")
    )


__all__ = (
    '_ADL2_OverdriveN_Capabilities_Get',
    '_ADL2_OverdriveN_CapabilitiesX2_Get',
    '_ADL2_OverdriveN_SystemClocks_Get',
    '_ADL2_OverdriveN_SystemClocks_Set',
    '_ADL2_OverdriveN_SystemClocksX2_Get',
    '_ADL2_OverdriveN_SystemClocksX2_Set',
    '_ADL2_OverdriveN_MemoryClocksX2_Get',
    '_ADL2_OverdriveN_MemoryClocksX2_Set',
    '_ADL2_OverdriveN_MemoryClocks_Get',
    '_ADL2_OverdriveN_MemoryClocks_Set',
    '_ADL2_OverdriveN_FanControl_Get',
    '_ADL2_OverdriveN_FanControl_Set',
    '_ADL2_OverdriveN_PowerLimit_Get',
    '_ADL2_OverdriveN_PowerLimit_Set',
    '_ADL2_OverdriveN_Temperature_Get',
    '_ADL2_OverdriveN_PerformanceStatus_Get',
    '_ADL2_CustomFan_Caps',
    '_ADL2_CustomFan_Get',
    '_ADL2_CustomFan_Set',
    '_ADL2_OverdriveN_MemoryTimingLevel_Get',
    '_ADL2_OverdriveN_MemoryTimingLevel_Set',
    '_ADL2_OverdriveN_ZeroRPMFan_Get',
    '_ADL2_OverdriveN_ZeroRPMFan_Set',
    '_ADL2_OverdriveN_SettingsExt_Get',
    '_ADL2_OverdriveN_SettingsExt_Set',
    'OverDriveN'

)


from .adl_sdk_h import ADL2_Main_Control_Create  # NOQA


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
        self._set = None
        self._get_automatic = None
        self._set_automatic = None

    def __set_value(self, value):
        if self._set is None and None in (self._parent, self._level):
            return self

        if self._set is None:
            # noinspection PyProtectedMember
            value = self._parent._set_value(self._level, value)
        else:
            value = self._set(value)

        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent
        cls._set = self._set

        # noinspection PyMethodFirstArgAssignment
        self = cls

        return self

    def __idiv__(self, other):
        return self.__ifloordiv__(other)

    def __itruediv__(self, other):
        return self.__idiv__(other)

    def __ifloordiv__(self, other):
        value = self.real // other
        return self.__set_value(value)

    def __imul__(self, other):
        value = self.real * other
        return self.__set_value(value)

    def __iadd__(self, other):
        value = self.real + other
        return self.__set_value(value)

    def __isub__(self, other):
        value = self.real - other
        return self.__set_value(value)

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
        self._set = None

    def __set_value(self, value):
        if self._set is None and None in (self._parent, self._level):
            return self

        if self._set is None:
            # noinspection PyProtectedMember
            value = self._parent._set_value(self._level, value)
        else:
            value = self._set(value)

        if value is None:
            return self

        cls = self.__class__(value)
        cls._adapter_index = self._adapter_index
        cls._level = self._level
        cls._obj = self._obj
        cls._parent = self._parent
        cls._set = self._set

        # noinspection PyMethodFirstArgAssignment
        self = cls

        return self

    def __idiv__(self, other):
        value = self.real / other
        return self.__set_value(value)

    def __itruediv__(self, other):
        return self.__idiv__(other)

    def __ifloordiv__(self, other):
        return self

    def __imul__(self, other):
        value = self.real * other
        return self.__set_value(value)

    def __iadd__(self, other):
        value = self.real + other
        return self.__set_value(value)

    def __isub__(self, other):
        value = self.real - other
        return self.__set_value(value)

    @property
    def max(self):
        return self._obj.max_value


class CoreVoltage(FloatValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        # noinspection PyProtectedMember
        lpODCapabilities = self._parent._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_SystemClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_SystemClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[self._level]
            return bool(performanceLevel.iEnabled)

    def activate(self):
        iAdapterIndex = INT(self._adapter_index)
        # noinspection PyProtectedMember
        lpODCapabilities = self._parent._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_SystemClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]
        _ADL2_OverdriveN_SystemClocksX2_Set.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_SystemClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[self._level]
            performanceLevel.iEnabled = 1
            performanceLevels.iMode = ADLODNControlType.ODNControlType_Manual

            _ADL2_OverdriveN_SystemClocksX2_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

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
        val += value - val.real

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODPerformanceStatus = ADLODNPerformanceStatus()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_PerformanceStatus_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODPerformanceStatus)
            )

        try:
            return CoreVoltage(lpODPerformanceStatus.iVDDC / 1000.0)
        except ZeroDivisionError:
            return CoreVoltage(0.0)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = self._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        if iNumberOfPerformanceLevels <= level or 0 > level:
            return

        min_val = lpODCapabilities.svddcRange.iMin / 1000.0
        max_val = lpODCapabilities.svddcRange.iMax / 1000.0
        step_val = lpODCapabilities.svddcRange.iStep / 1000.0
        value -= value % step_val

        if max_val < value or min_val > value:
            return

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_SystemClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]
        _ADL2_OverdriveN_SystemClocksX2_Set.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_SystemClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[level]

            if not performanceLevel.iControl & ADLODNDPMMaskType.ADL_ODN_DPM_VDDC == ADLODNDPMMaskType.ADL_ODN_DPM_VDDC:
                return

            performanceLevel.iVddc = int(value * 1000)
            performanceLevels.iMode = ADLODNControlType.ODNControlType_Manual

            _ADL2_OverdriveN_SystemClocksX2_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            return value

    @property
    def _capabilities(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = ADLODNCapabilitiesX2()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_CapabilitiesX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODCapabilities)
            )

        return lpODCapabilities

    def __iter__(self):
        if CoreVoltages._core_voltages is None:
            CoreVoltages._core_voltages = []

            iAdapterIndex = INT(self._adapter_index)

            lpODCapabilities = self._capabilities

            with ADL2_Main_Control_Create as context:
                iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

                class _ADLODNPerformanceLevelsX2(ctypes.Structure):
                    _fields_ = [
                        ('iSize', INT),
                        ('iMode', INT),
                        ('iNumberOfPerformanceLevels', INT),
                        ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
                    ]

                _ADL2_OverdriveN_SystemClocksX2_Get.argtypes = [
                    ADL_CONTEXT_HANDLE,
                    INT,
                    POINTER(_ADLODNPerformanceLevelsX2)
                ]

                size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
                performanceLevels = _ADLODNPerformanceLevelsX2()
                performanceLevels.iSize = size
                performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

                defaultPerformanceLevels = _ADLODNPerformanceLevelsX2()
                defaultPerformanceLevels.iSize = size
                defaultPerformanceLevels.iMode = ADLODNControlType.ODNControlType_Default

                _ADL2_OverdriveN_SystemClocksX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(performanceLevels)
                )

                _ADL2_OverdriveN_SystemClocksX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(defaultPerformanceLevels)
                )

            if lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
                for i in range(iNumberOfPerformanceLevels):
                    performanceLevel = performanceLevels.aLevels[i]
                    defaultPerformanceLevel = defaultPerformanceLevels.aLevels[i]

                    min_val = lpODCapabilities.svddcRange.iMin / 1000.0
                    max_val = lpODCapabilities.svddcRange.iMax / 1000.0
                    step_val = lpODCapabilities.svddcRange.iStep / 1000.0
                    default_val = defaultPerformanceLevel.iVddc / 1000.0
                    current_val = performanceLevel.iVddc / 1000.0
                    editable_val = performanceLevel.iControl & ADL_ODN_DPM_VDDC == ADL_ODN_DPM_VDDC

                    class Values(object):
                        min_value = min_val
                        max_value = max_val
                        step = step_val
                        default = default_val
                        editable = editable_val

                    value = CoreVoltage(current_val)
                    value._obj = Values
                    value._adapter_index = self._adapter_index
                    value._level = i
                    CoreVoltages._core_voltages.append(value)

        return iter(CoreVoltages._core_voltages)


class CoreClock(IntValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        # noinspection PyProtectedMember
        lpODCapabilities = self._parent._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_SystemClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_SystemClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[self._level]
            return bool(performanceLevel.iEnabled)

    def activate(self):
        iAdapterIndex = INT(self._adapter_index)
        # noinspection PyProtectedMember
        lpODCapabilities = self._parent._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_SystemClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]
        _ADL2_OverdriveN_SystemClocksX2_Set.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_SystemClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[self._level]
            performanceLevel.iEnabled = 1
            performanceLevels.iMode = ADLODNControlType.ODNControlType_Manual

            _ADL2_OverdriveN_SystemClocksX2_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

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


class CoreClocks(object):
    _core_clocks = None

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    def __getitem__(self, item):
        return list(self)[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += value - val.real

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODPerformanceStatus = ADLODNPerformanceStatus()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_PerformanceStatus_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODPerformanceStatus)
            )

        try:
            return CoreClock(lpODPerformanceStatus.iCoreClock // 100)
        except ZeroDivisionError:
            return CoreClock(0)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = self._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_DPM == ADL_ODN_SCLK_DPM:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        if iNumberOfPerformanceLevels <= level or 0 > level:
            return

        min_val = lpODCapabilities.sEngineClockRange.iMin // 100
        max_val = lpODCapabilities.sEngineClockRange.iMax // 100
        step_val = lpODCapabilities.sEngineClockRange.iStep // 100
        value -= value % step_val

        if max_val < value or min_val > value:
            return

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_SystemClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]
        _ADL2_OverdriveN_SystemClocksX2_Set.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_SystemClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[level]

            if not performanceLevel.iControl & ADL_ODN_DPM_CLOCK == ADL_ODN_DPM_CLOCK:
                return

            performanceLevel.iClock = value * 100
            performanceLevels.iMode = ADLODNControlType.ODNControlType_Manual

            _ADL2_OverdriveN_SystemClocksX2_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            return value

    @property
    def _capabilities(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = ADLODNCapabilitiesX2()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_CapabilitiesX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODCapabilities)
            )

        return lpODCapabilities

    def __iter__(self):
        if CoreClocks._core_clocks is None:
            CoreClocks._core_clocks = []

            iAdapterIndex = INT(self._adapter_index)
            lpODCapabilities = self._capabilities

            with ADL2_Main_Control_Create as context:
                iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

                class _ADLODNPerformanceLevelsX2(ctypes.Structure):
                    _fields_ = [
                        ('iSize', INT),
                        ('iMode', INT),
                        ('iNumberOfPerformanceLevels', INT),
                        ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
                    ]

                _ADL2_OverdriveN_SystemClocksX2_Get.argtypes = [
                    ADL_CONTEXT_HANDLE,
                    INT,
                    POINTER(_ADLODNPerformanceLevelsX2)
                ]

                size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
                performanceLevels = _ADLODNPerformanceLevelsX2()
                performanceLevels.iSize = size
                performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

                defaultPerformanceLevels = _ADLODNPerformanceLevelsX2()
                defaultPerformanceLevels.iSize = size
                defaultPerformanceLevels.iMode = ADLODNControlType.ODNControlType_Default

                _ADL2_OverdriveN_SystemClocksX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(performanceLevels)
                )

                _ADL2_OverdriveN_SystemClocksX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(defaultPerformanceLevels)
                )

            if lpODCapabilities.iFlags & ADL_ODN_SCLK_DPM == ADL_ODN_SCLK_DPM:
                for i in range(iNumberOfPerformanceLevels):
                    performanceLevel = performanceLevels.aLevels[i]
                    defaultPerformanceLevel = defaultPerformanceLevels.aLevels[i]

                    min_val = lpODCapabilities.sEngineClockRange.iMin // 100
                    max_val = lpODCapabilities.sEngineClockRange.iMax // 100
                    step_val = lpODCapabilities.sEngineClockRange.iStep // 100
                    default_val = defaultPerformanceLevel.iClock // 100
                    current_val = performanceLevel.iClock // 100
                    editable_val = performanceLevel.iControl & ADL_ODN_DPM_CLOCK == ADL_ODN_DPM_CLOCK

                    class Values(object):
                        min_value = min_val
                        max_value = max_val
                        step = step_val
                        default = default_val
                        editable = editable_val

                    value = CoreClock(current_val)
                    value._obj = Values
                    value._adapter_index = self._adapter_index
                    value._level = i
                    CoreClocks._core_clocks.append(value)

        return iter(CoreClocks._core_clocks)


class MemoryVoltage(FloatValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        # noinspection PyProtectedMember
        lpODCapabilities = self._parent._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_MemoryClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_MemoryClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[self._level]
            return bool(performanceLevel.iEnabled)

    def activate(self):
        iAdapterIndex = INT(self._adapter_index)
        # noinspection PyProtectedMember
        lpODCapabilities = self._parent._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_MemoryClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        _ADL2_OverdriveN_MemoryClocksX2_Set.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_MemoryClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[self._level]
            performanceLevel.iEnabled = 1
            performanceLevels.iMode = ADLODNControlType.ODNControlType_Manual

            _ADL2_OverdriveN_MemoryClocksX2_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

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


class MemoryVoltages(object):
    _memory_voltages = None

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    def __getitem__(self, item):
        return list(self)[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += value - val.real

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODPerformanceStatus = ADLODNPerformanceStatus()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_PerformanceStatus_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODPerformanceStatus)
            )

        try:
            return MemoryVoltage(lpODPerformanceStatus.iVDDCI / 1000.0)
        except ZeroDivisionError:
            return MemoryVoltage(0.0)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = self._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_MCLK_VDD == ADL_ODN_MCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        if iNumberOfPerformanceLevels <= level or 0 > level:
            return

        min_val = lpODCapabilities.svddcRange.iMin / 1000.0
        max_val = lpODCapabilities.svddcRange.iMax / 1000.0
        step_val = lpODCapabilities.svddcRange.iStep / 1000.0
        value -= value % step_val

        if max_val < value or min_val > value:
            return

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_MemoryClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]
        _ADL2_OverdriveN_MemoryClocksX2_Set.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_MemoryClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[level]

            if not performanceLevel.iControl & ADLODNDPMMaskType.ADL_ODN_DPM_VDDC == ADLODNDPMMaskType.ADL_ODN_DPM_VDDC:
                return

            performanceLevel.iVddc = int(value * 1000)
            performanceLevels.iMode = ADLODNControlType.ODNControlType_Manual

            _ADL2_OverdriveN_MemoryClocksX2_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            return value

    @property
    def _capabilities(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = ADLODNCapabilitiesX2()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_CapabilitiesX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODCapabilities)
            )

        return lpODCapabilities

    def __iter__(self):
        if MemoryVoltages._memory_voltages is None:
            MemoryVoltages._memory_voltages = []

            iAdapterIndex = INT(self._adapter_index)

            lpODCapabilities = self._capabilities

            with ADL2_Main_Control_Create as context:
                iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

                class _ADLODNPerformanceLevelsX2(ctypes.Structure):
                    _fields_ = [
                        ('iSize', INT),
                        ('iMode', INT),
                        ('iNumberOfPerformanceLevels', INT),
                        ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
                    ]

                _ADL2_OverdriveN_MemoryClocksX2_Get.argtypes = [
                    ADL_CONTEXT_HANDLE,
                    INT,
                    POINTER(_ADLODNPerformanceLevelsX2)
                ]

                size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
                performanceLevels = _ADLODNPerformanceLevelsX2()
                performanceLevels.iSize = size
                performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

                defaultPerformanceLevels = _ADLODNPerformanceLevelsX2()
                defaultPerformanceLevels.iSize = size
                defaultPerformanceLevels.iMode = ADLODNControlType.ODNControlType_Default

                _ADL2_OverdriveN_MemoryClocksX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(performanceLevels)
                )

                _ADL2_OverdriveN_MemoryClocksX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(defaultPerformanceLevels)
                )

            if lpODCapabilities.iFlags & ADL_ODN_MCLK_VDD == ADL_ODN_MCLK_VDD:
                for i in range(iNumberOfPerformanceLevels):
                    performanceLevel = performanceLevels.aLevels[i]
                    defaultPerformanceLevel = defaultPerformanceLevels.aLevels[i]

                    min_val = lpODCapabilities.svddcRange.iMin / 1000.0
                    max_val = lpODCapabilities.svddcRange.iMax / 1000.0
                    step_val = lpODCapabilities.svddcRange.iStep / 1000.0
                    default_val = defaultPerformanceLevel.iVddc / 1000.0
                    current_val = performanceLevel.iVddc / 1000.0
                    editable_val = performanceLevel.iControl & ADL_ODN_DPM_VDDC == ADL_ODN_DPM_VDDC

                    class Values(object):
                        min_value = min_val
                        max_value = max_val
                        step = step_val
                        default = default_val
                        editable = editable_val

                    value = MemoryVoltage(current_val)
                    value._obj = Values
                    value._adapter_index = self._adapter_index
                    value._level = i
                    MemoryVoltages._memory_voltages.append(value)

        return iter(MemoryVoltages._memory_voltages)


class MemoryClock(IntValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        # noinspection PyProtectedMember
        lpODCapabilities = self._parent._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_MemoryClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_MemoryClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[self._level]
            return bool(performanceLevel.iEnabled)

    def activate(self):
        iAdapterIndex = INT(self._adapter_index)
        # noinspection PyProtectedMember
        lpODCapabilities = self._parent._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_SCLK_VDD == ADL_ODN_SCLK_VDD:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_MemoryClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        _ADL2_OverdriveN_MemoryClocksX2_Set.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_MemoryClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[self._level]
            performanceLevel.iEnabled = 1
            performanceLevels.iMode = ADLODNControlType.ODNControlType_Manual

            _ADL2_OverdriveN_MemoryClocksX2_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

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
    def editable(self):
        return self._obj.editable

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
        val += value - val.real

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODPerformanceStatus = ADLODNPerformanceStatus()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_PerformanceStatus_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODPerformanceStatus)
            )

        try:
            return MemoryClock(lpODPerformanceStatus.iMemoryClock // 100)
        except ZeroDivisionError:
            return MemoryClock(0)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = self._capabilities

        if not lpODCapabilities.iFlags & ADL_ODN_MCLK_DPM == ADL_ODN_MCLK_DPM:
            return

        iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

        if iNumberOfPerformanceLevels <= level or 0 > level:
            return

        min_val = lpODCapabilities.sMemoryClock.iMin // 100
        max_val = lpODCapabilities.sMemoryClock.iMax // 100
        step_val = lpODCapabilities.sMemoryClock.iStep // 100
        value -= value % step_val

        if max_val < value or min_val > value:
            return

        class _ADLODNPerformanceLevelsX2(ctypes.Structure):
            _fields_ = [
                ('iSize', INT),
                ('iMode', INT),
                ('iNumberOfPerformanceLevels', INT),
                ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
            ]

        _ADL2_OverdriveN_MemoryClocksX2_Get.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]
        _ADL2_OverdriveN_MemoryClocksX2_Set.argtypes = [
            ADL_CONTEXT_HANDLE,
            INT,
            POINTER(_ADLODNPerformanceLevelsX2)
        ]

        size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
        performanceLevels = _ADLODNPerformanceLevelsX2()
        performanceLevels.iSize = size
        performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_MemoryClocksX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            performanceLevel = performanceLevels.aLevels[level]

            if not performanceLevel.iControl & ADL_ODN_DPM_CLOCK == ADL_ODN_DPM_CLOCK:
                return

            performanceLevel.iClock = value * 100
            performanceLevels.iMode = ADLODNControlType.ODNControlType_Manual

            _ADL2_OverdriveN_MemoryClocksX2_Set(
                context,
                iAdapterIndex,
                ctypes.byref(performanceLevels)
            )

            return value

    @property
    def _capabilities(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = ADLODNCapabilitiesX2()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_CapabilitiesX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODCapabilities)
            )

        return lpODCapabilities

    def __iter__(self):
        if MemoryClocks._memory_clocks is None:
            MemoryClocks._memory_clocks = []

            iAdapterIndex = INT(self._adapter_index)
            lpODCapabilities = self._capabilities

            with ADL2_Main_Control_Create as context:
                iNumberOfPerformanceLevels = lpODCapabilities.iNumberOfPerformanceLevels

                class _ADLODNPerformanceLevelsX2(ctypes.Structure):
                    _fields_ = [
                        ('iSize', INT),
                        ('iMode', INT),
                        ('iNumberOfPerformanceLevels', INT),
                        ('aLevels', ADLODNPerformanceLevelX2 * iNumberOfPerformanceLevels),
                    ]

                _ADL2_OverdriveN_MemoryClocksX2_Get.argtypes = [
                    ADL_CONTEXT_HANDLE,
                    INT,
                    POINTER(_ADLODNPerformanceLevelsX2)
                ]

                size = ctypes.sizeof(_ADLODNPerformanceLevelsX2)
                performanceLevels = _ADLODNPerformanceLevelsX2()
                performanceLevels.iSize = size
                performanceLevels.iMode = ADLODNControlType.ODNControlType_Current

                defaultPerformanceLevels = _ADLODNPerformanceLevelsX2()
                defaultPerformanceLevels.iSize = size
                defaultPerformanceLevels.iMode = ADLODNControlType.ODNControlType_Default

                _ADL2_OverdriveN_MemoryClocksX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(performanceLevels)
                )

                _ADL2_OverdriveN_MemoryClocksX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(defaultPerformanceLevels)
                )

            if lpODCapabilities.iFlags & ADL_ODN_MCLK_DPM == ADL_ODN_MCLK_DPM:
                for i in range(iNumberOfPerformanceLevels):
                    performanceLevel = performanceLevels.aLevels[i]
                    defaultPerformanceLevel = defaultPerformanceLevels.aLevels[i]

                    min_val = lpODCapabilities.sMemoryClock.iMin // 100
                    max_val = lpODCapabilities.sMemoryClock.iMax // 100
                    step_val = lpODCapabilities.sMemoryClock.iStep // 100
                    default_val = defaultPerformanceLevel.iClock // 100
                    current_val = performanceLevel.iClock // 100
                    editable_val = performanceLevel.iControl & ADL_ODN_DPM_CLOCK == ADL_ODN_DPM_CLOCK

                    class Values(object):
                        min_value = min_val
                        max_value = max_val
                        step = step_val
                        default = default_val
                        editable = editable_val

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
    def step(self):
        return self._obj.step_value

    @property
    def automatic(self):
        return self._get_automatic()

    @automatic.setter
    def automatic(self, value):
        if value is True:
            value = ODNControlType_Auto
        elif value is False:
            value = ODNControlType_Manual
        else:
            return

        if value is True:
            self._set_automatic(self.real, value)


class FanSpeeds(object):
    _fan_speeds = None

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def _capabilities(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = ADLODNCapabilitiesX2()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_CapabilitiesX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODCapabilities)
            )

        return lpODCapabilities

    def __iter__(self):

        if FanSpeeds._fan_speeds is None:
            FanSpeeds._fan_speeds = []
            iAdapterIndex = INT(self._adapter_index)

            def _dummy():
                def _set_auto(_, __):
                    pass

                def _set_val(_):
                    pass

                class FanSpeedMetrics(object):
                    min_value = 0
                    max_value = 0
                    step_value = 0
                    unit = 'Unsupported'

                value = FanSpeed(0)
                value._obj = FanSpeedMetrics
                value._adapter_index = self._adapter_index
                value._parent = self
                value._set = _set_val
                value._get_automatic = _get_automatic
                value._set_automatic = _set_auto

                return value

            def _do():
                class FanSpeedMetrics(object):
                    min_value = min_val
                    max_value = max_val
                    step_value = step_val
                    unit = uom

                value = FanSpeed(current_val)
                value._obj = FanSpeedMetrics
                value._adapter_index = self._adapter_index
                value._parent = self
                value._set = _set
                value._get_automatic = _get_automatic
                value._set_automatic = _set_automatic

                return value

            def _get_automatic():
                _lpODFanSpeed = ADLODNFanControl()
                with ADL2_Main_Control_Create as _context:
                    _ADL2_OverdriveN_FanControl_Get(
                        _context,
                        iAdapterIndex,
                        ctypes.byref(_lpODFanSpeed)
                    )

                    return _lpODFanSpeed.iMode == ODNControlType_Auto

            lpODCapabilities = self._capabilities
            lpODFanSpeed = ADLODNFanControl()

            with ADL2_Main_Control_Create as context:
                _ADL2_OverdriveN_FanControl_Get(
                        context,
                        iAdapterIndex,
                        ctypes.byref(lpODFanSpeed)
                )

            if lpODCapabilities.iFlags & ADL_ODN_FAN_SPEED_MIN == ADL_ODN_FAN_SPEED_MIN:
                min_val = lpODCapabilities.fanSpeed.iMin
                max_val = lpODCapabilities.fanSpeed.iMax
                step_val = lpODCapabilities.fanSpeed.iStep
                current_val = lpODFanSpeed.iMinFanLimit
                uom = 'RPM'

                def _set(value):
                    value -= value % lpODCapabilities.fanSpeed.iStep

                    if value < lpODCapabilities.fanSpeed.iMin:
                        return
                    elif value > lpODCapabilities.fanSpeed.iMax:
                        return

                    _lpODFanSpeed = ADLODNFanControl()
                    _lpODFanSpeed.iMinFanLimit = value
                    _lpODFanSpeed.iMode = ODNControlType_Manual

                    with ADL2_Main_Control_Create as _context:
                        if ADL_OK == _ADL2_OverdriveN_FanControl_Set(
                            _context,
                            iAdapterIndex,
                            ctypes.byref(_lpODFanSpeed)
                        ):
                            return value

                def _set_automatic(value, mode):
                    _lpODFanSpeed = ADLODNFanControl()
                    _lpODFanSpeed.iMinFanLimit = value
                    _lpODFanSpeed.iMode = mode

                    with ADL2_Main_Control_Create as _context:
                        if ADL_OK == _ADL2_OverdriveN_FanControl_Set(
                            _context,
                            iAdapterIndex,
                            ctypes.byref(_lpODFanSpeed)
                        ):
                            return value

                FanSpeeds._fan_speeds += [_do()]

            else:
                FanSpeeds._fan_speeds += [_dummy()]

            if lpODCapabilities.iFlags & ADL_ODN_FAN_SPEED_TARGET == ADL_ODN_FAN_SPEED_TARGET:
                min_val = lpODCapabilities.fanSpeed.iMin
                max_val = lpODCapabilities.fanSpeed.iMax
                step_val = lpODCapabilities.fanSpeed.iStep
                current_val = lpODFanSpeed.iTargetFanSpeed
                uom = 'RPM'

                def _set(value):
                    value -= value % lpODCapabilities.fanSpeed.iStep

                    if value < lpODCapabilities.fanSpeed.iMin:
                        return
                    elif value > lpODCapabilities.fanSpeed.iMax:
                        return

                    _lpODFanSpeed = ADLODNFanControl()
                    _lpODFanSpeed.iTargetFanSpeed = value
                    _lpODFanSpeed.iMode = ODNControlType_Manual

                    with ADL2_Main_Control_Create as _context:
                        if ADL_OK == _ADL2_OverdriveN_FanControl_Set(
                            _context,
                            iAdapterIndex,
                            ctypes.byref(_lpODFanSpeed)
                        ):
                            return value

                def _set_automatic(value, mode):
                    _lpODFanSpeed = ADLODNFanControl()
                    _lpODFanSpeed.iTargetFanSpeed = value
                    _lpODFanSpeed.iMode = mode

                    with ADL2_Main_Control_Create as _context:
                        if ADL_OK == _ADL2_OverdriveN_FanControl_Set(
                            _context,
                            iAdapterIndex,
                            ctypes.byref(_lpODFanSpeed)
                        ):
                            return value

                FanSpeeds._fan_speeds += [_do()]

            else:
                FanSpeeds._fan_speeds += [_dummy()]

            if lpODCapabilities.iFlags & ADL_ODN_ACOUSTIC_LIMIT_SCLK == ADL_ODN_ACOUSTIC_LIMIT_SCLK:
                min_val = lpODCapabilities.minimumPerformanceClock.iMin
                max_val = lpODCapabilities.minimumPerformanceClock.iMax
                step_val = lpODCapabilities.minimumPerformanceClock.iStep
                current_val = lpODFanSpeed.iMinPerformanceClock
                uom = 'mhz'

                def _set(value):
                    value -= value % lpODCapabilities.minimumPerformanceClock.iStep

                    if value < lpODCapabilities.minimumPerformanceClock.iMin:
                        return
                    elif value > lpODCapabilities.minimumPerformanceClock.iMax:
                        return

                    _lpODFanSpeed = ADLODNFanControl()
                    _lpODFanSpeed.iMinPerformanceClock = value
                    _lpODFanSpeed.iMode = ODNControlType_Manual

                    with ADL2_Main_Control_Create as _context:
                        if ADL_OK == _ADL2_OverdriveN_FanControl_Set(
                            _context,
                            iAdapterIndex,
                            ctypes.byref(_lpODFanSpeed)
                        ):
                            return value

                def _set_automatic(value, mode):
                    _lpODFanSpeed = ADLODNFanControl()
                    _lpODFanSpeed.iMinFanLimit = value
                    _lpODFanSpeed.iMode = mode

                    with ADL2_Main_Control_Create as _context:
                        if ADL_OK == _ADL2_OverdriveN_FanControl_Set(
                            _context,
                            iAdapterIndex,
                            ctypes.byref(_lpODFanSpeed)
                        ):
                            return value

                FanSpeeds._fan_speeds += [_do()]

            else:
                FanSpeeds._fan_speeds += [_dummy()]

            if lpODCapabilities.iFlags & ADL_ODN_TEMPERATURE_FAN_MAX == ADL_ODN_TEMPERATURE_FAN_MAX:
                min_val = lpODCapabilities.fanTemperature.iMin
                max_val = lpODCapabilities.fanTemperature.iMax
                step_val = lpODCapabilities.fanTemperature.iStep
                current_val = lpODFanSpeed.iTargetTemperature
                uom = 'degrees'

                def _set(value):
                    value -= value % lpODCapabilities.fanTemperature.iStep

                    if value < lpODCapabilities.fanTemperature.iMin:
                        return
                    elif value > lpODCapabilities.fanTemperature.iMax:
                        return

                    _lpODFanSpeed = ADLODNFanControl()
                    _lpODFanSpeed.iTargetTemperature = value
                    _lpODFanSpeed.iMode = ODNControlType_Manual

                    with ADL2_Main_Control_Create as _context:
                        if ADL_OK == _ADL2_OverdriveN_FanControl_Set(
                            _context,
                            iAdapterIndex,
                            ctypes.byref(_lpODFanSpeed)
                        ):
                            return value

                def _set_automatic(value, mode):
                    _lpODFanSpeed = ADLODNFanControl()
                    _lpODFanSpeed.iTargetTemperature = value
                    _lpODFanSpeed.iMode = mode

                    with ADL2_Main_Control_Create as _context:
                        if ADL_OK == _ADL2_OverdriveN_FanControl_Set(
                            _context,
                            iAdapterIndex,
                            ctypes.byref(_lpODFanSpeed)
                        ):
                            return value

                FanSpeeds._fan_speeds += [_do()]

            else:
                FanSpeeds._fan_speeds += [_dummy()]

        return iter(FanSpeeds._fan_speeds)

    def __getitem__(self, item):
        speeds = list(self)
        return speeds[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += value - val.real


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


class OverDriveN(object):
    _power_threshold = []

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def _capabilities(self):
        iAdapterIndex = INT(self._adapter_index)
        lpODCapabilities = ADLODNCapabilitiesX2()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_CapabilitiesX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODCapabilities)
            )

        return lpODCapabilities

    @property
    def _activity(self):
        iAdapterIndex = INT(self._adapter_index)
        odNPerformanceStatus = ADLODNPerformanceStatus()

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_PerformanceStatus_Get(
                context,
                iAdapterIndex,
                ctypes.byref(odNPerformanceStatus)
            )
            return odNPerformanceStatus

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
        return Load(lpActivity.iGPUActivityPercent / 10.0)

    @property
    def temperatures(self):
        iAdapterIndex = INT(self._adapter_index)

        iTemperatureType = INT(1)
        iTemperature = INT(-1)

        with ADL2_Main_Control_Create as context:

            _ADL2_OverdriveN_Temperature_Get(
                context,
                iAdapterIndex,
                iTemperatureType,
                ctypes.byref(iTemperature)
            )

        return [Temperature(iTemperature.value / 1000.0)]

    @property
    def is_power_control_supported(self):
        lpODCapabilities = self._capabilities

        return lpODCapabilities.iFlags & ADL_ODN_POWER_LIMIT == ADL_ODN_POWER_LIMIT

    def _set_value(self, level, value):
        if not self.is_power_control_supported:
            return

        lpODCapabilities = self._capabilities

        iAdapterIndex = INT(self._adapter_index)
        lpODPowerLimit = ADLODNPowerLimitSetting()
        lpODPowerLimit.iMode = ODNControlType_Current

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_PowerLimit_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpODPowerLimit)
            )

            if level == 1:
                min_val = lpODCapabilities.powerTuneTemperature.iMin
                max_val = lpODCapabilities.powerTuneTemperature.iMax
                step_val = lpODCapabilities.powerTuneTemperature.iStep
            elif level == 2:
                min_val = lpODCapabilities.power.iMin
                max_val = lpODCapabilities.power.iMax
                step_val = lpODCapabilities.power.iStep
            else:
                return

            value -= value % step_val

            if min_val > value or max_val < value:
                return

            if level == 1:
                lpODPowerLimit.iMaxOperatingTemperature = value
            else:
                lpODPowerLimit.iTDPLimit = value

            lpODPowerLimit.iMode = ODNControlType_Manual

            _ADL2_OverdriveN_PowerLimit_Set(
                context,
                iAdapterIndex,
                ctypes.byref(lpODPowerLimit)
            )

            return value

    @property
    def power_control(self):
        if not OverDriveN._power_threshold:
            def _do():
                class Values(object):
                    min_value = min_val
                    max_value = max_val
                    step = step_val
                    default = None

                value = PowerThreshold(current_val)
                value._obj = Values
                value._parent = self
                value._level = level
                value._adapter_index = self._adapter_index
                return value

            if self.is_power_control_supported:
                lpODCapabilities = self._capabilities

                iAdapterIndex = INT(self._adapter_index)
                lpODPowerLimit = ADLODNPowerLimitSetting()
                lpODPowerLimit.iMode = ODNControlType_Current

                with ADL2_Main_Control_Create as context:
                    _ADL2_OverdriveN_PowerLimit_Get(
                        context,
                        iAdapterIndex,
                        ctypes.byref(lpODPowerLimit)
                    )

                    min_val = lpODCapabilities.powerTuneTemperature.iMin
                    max_val = lpODCapabilities.powerTuneTemperature.iMax
                    step_val = lpODCapabilities.powerTuneTemperature.iStep
                    current_val = lpODPowerLimit.iMaxOperatingTemperature
                    level = 1

                    OverDriveN._power_threshold += [_do()]

                    min_val = lpODCapabilities.power.iMin
                    max_val = lpODCapabilities.power.iMax
                    step_val = lpODCapabilities.power.iStep
                    current_val = lpODPowerLimit.iTDPLimit
                    level = 2
                    OverDriveN._power_threshold += [_do()]

            else:
                min_val = 0
                max_val = 0
                step_val = 0
                current_val = 0
                level = 1
                OverDriveN._power_threshold += [_do()]

                level = 2
                OverDriveN._power_threshold += [_do()]

        return iter(OverDriveN._power_threshold)

    @property
    def engine_clocks(self):
        return CoreClocks(self._adapter_index)

    @property
    def memory_clocks(self):
        return MemoryClocks(self._adapter_index)

    @property
    def core_voltages(self):
        return CoreVoltages(self._adapter_index)

    @property
    def memory_voltages(self):
        return MemoryVoltages(self._adapter_index)

    @property
    def fan_speeds(self):
        return FanSpeeds(self._adapter_index)
