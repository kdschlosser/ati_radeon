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


class OverDriveN(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def _capabilities(self):
        """Function to retrieve the OverdriveN capabilities."""
        lpODCapabilities = ADLODNCapabilitiesX2()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_OverdriveN_CapabilitiesX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpODCapabilities)
            ) == ADL_OK:
                return lpODCapabilities

    @property
    def gpu(self):
        caps = self._capabilities
        num_levels = caps.iMaximumNumberOfPerformanceLevels.value

        for i in range(num_levels):
            yield GPUPerformanceLevel(self, i)

    @property
    def memory(self):
        caps = self._capabilities
        num_levels = caps.iMaximumNumberOfPerformanceLevels.value

        for i in range(num_levels):
            yield MemoryPerformanceLevel(self, i)

    @property
    def fan_speed(self):
        return FanSpeed(self)

    @property
    def temperature_limits(self):
        return TemperatureLimits(self)

    @property
    def memory_timings(self):
        return MemoryTimingLevels(self)

    @property
    def zero_rpm_fan(self):
        return ZeroRPMFan(self)

    @property
    def _performance_stats(self):
        lpODPerformanceStatus = ADLODNPerformanceStatus()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_OverdriveN_PerformanceStatus_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpODPerformanceStatus)
            ) == ADL_OK:
                return lpODPerformanceStatus

    @property
    def core_clock(self):
        return self._performance_stats.iCoreClock.value

    @property
    def bus_lanes(self):
        return self._performance_stats.iCurrentBusLanes.value

    @property
    def bus_speed(self):
        return self._performance_stats.iCurrentBusSpeed.value

    @property
    def core_performance_level(self):
        return self._performance_stats.iCurrentCorePerformanceLevel.value

    @property
    def dcef_performance_level(self):
        return self._performance_stats.iCurrentDCEFPerformanceLevel.value

    @property
    def gfx_performance_level(self):
        return self._performance_stats.iCurrentGFXPerformanceLevel.value

    @property
    def memory_performance_level(self):
        return self._performance_stats.iCurrentMemoryPerformanceLevel.value

    @property
    def dcef_clock(self):
        return self._performance_stats.iDCEFClock.value

    @property
    def gfx_clock(self):
        return self._performance_stats.iGFXClock.value

    @property
    def gpu_activity(self):
        return self._performance_stats.iGPUActivityPercent.value

    @property
    def maximum_bus_lanes(self):
        return self._performance_stats.iMaximumBusLanes.value

    @property
    def memory_clock(self):
        return self._performance_stats.iMemoryClock.value

    @property
    def uvd_clock(self):
        return self._performance_stats.iUVDClock.value

    @property
    def uvd_performance_level(self):
        return self._performance_stats.iUVDPerformanceLevel.value

    @property
    def vce_clock(self):
        return self._performance_stats.iVCEClock.value

    @property
    def vce_performance_level(self):
        return self._performance_stats.iVCEPerformanceLevel.value

    @property
    def vddc(self):
        return self._performance_stats.iVDDC.value

    @property
    def vddci(self):
        return self._performance_stats.iVDDCI.value

    def reset(self):
        overdriveCapabilities = self._capabilities

        num_levels = overdriveCapabilities.iMaximumNumberOfPerformanceLevels.value

        size = (
            ctypes.sizeof(ADLODNPerformanceLevelsX2) +
            ctypes.sizeof(ADLODNPerformanceLevelX2) *
            (num_levels - 1)
        )

        performanceLevelsBuffer = (CHAR * size)()
        ctypes.memset(performanceLevelsBuffer, 0, size)

        odPerformanceLevels = ctypes.cast(performanceLevelsBuffer, POINTER(ADLODNPerformanceLevelsX2))
        odPerformanceLevels.iSize = size
        odPerformanceLevels.iMode = ODNControlType_Default
        odPerformanceLevels.iNumberOfPerformanceLevels = num_levels

        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            return _ADL2_OverdriveN_SystemClocksX2_Set(
                context,
                iAdapterIndex,
                odPerformanceLevels
            ) == ADL_OK


# noinspection PyUnresolvedReferences
class ParameterRange(int):

    def __init__(self, value=None):
        if value is None:
            super(ParameterRange, self).__init__()
        else:
            try:
                super(ParameterRange, self).__init__(value)
            except TypeError:
                super(ParameterRange, self).__init__()

        self.__obj = None

    def _set_object(self, obj):
        self.__obj = obj

    @property
    def min(self):
        return self.__obj.iMin.value

    @property
    def max(self):
        return self.__obj.iMax.value

    @property
    def step(self):
        return self.__obj.iStep.value


# noinspection PyProtectedMember
class ZeroRPMFan(object):
    def __init__(self, parent):
        self._parent = parent

    @property
    def _get(self):
        iAdapterIndex = INT(self._parent._adapter_index)
        support = INT()
        currentValue = INT()
        defaultValue = INT()

        with ADL2_Main_Control_Create as context:
            if _ADL2_OverdriveN_ZeroRPMFan_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(support),
                    ctypes.byref(currentValue),
                    ctypes.byref(defaultValue)
            ) == ADL_OK:
                return support.value, currentValue.value, defaultValue.value

    @property
    def value(self):
        return self._get[1]

    @value.setter
    def value(self, value):
        value = INT(value)
        value = INT(value)
        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_ZeroRPMFan_Set(
                context,
                iAdapterIndex,
                value
            )

    @property
    def support(self):
        return self._get[0]

    @property
    def default(self):
        return self._get[2]


# noinspection PyProtectedMember
class MemoryTimingLevels(object):

    def __init__(self, parent):
        self._parent = parent

    def __getitem__(self, item):
        return list(self)[item]

    @property
    def support(self):
        return self._get[0]

    def __len__(self):
        return self._get[3]

    @property
    def value(self):
        return self._get[1]

    @value.setter
    def value(self, value):
        value = INT(value)
        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_MemoryTimingLevel_Set(
                    context,
                    iAdapterIndex,
                    value
            )

    @property
    def default(self):
        return self._get[2]

    @property
    def _get(self):
        iAdapterIndex = INT(self._parent._adapter_index)
        support = INT()
        currentValue = INT()
        defaultValue = INT()
        numberLevels = INT()
        levelList = (INT * 1)()

        with ADL2_Main_Control_Create as context:
            if _ADL2_OverdriveN_MemoryTimingLevel_Get(
                context,
                iAdapterIndex,
                ctypes.byref(support),
                ctypes.byref(currentValue),
                ctypes.byref(defaultValue),
                ctypes.byref(numberLevels),
                ctypes.byref(levelList)
            ) == ADL_OK:

                levelList = list(levelList[i].value for i in range(numberLevels.value))
                return support.value, currentValue.value, defaultValue.value, numberLevels.value, levelList

    def __iter__(self):
        return iter(self._get[4])


# noinspection PyProtectedMember
class TemperatureLimits(object):

    def __init__(self, parent):
        self._parent = parent

    @property
    def mode(self):
        settings = self._power_limit_settings
        return settings.iMode.value

    @property
    def _power_limit_settings(self):
        odNPowerControl = ADLODNPowerLimitSetting()
        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_OverdriveN_PowerLimit_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(odNPowerControl)
            ) == ADL_OK:
                return odNPowerControl

    @property
    def max_operating_temperature(self):
        caps = self._parent._capabilities
        settings = self._power_limit_settings

        max_operating_temperature = ParameterRange(settings.iMaxOperatingTemperature.value)
        max_operating_temperature._set_object(caps.powerTuneTemperature)
        return max_operating_temperature

    @max_operating_temperature.setter
    def max_operating_temperature(self, value):

        max_operating_temperature = self.max_operating_temperature

        if not max_operating_temperature.max >= value >= max_operating_temperature.min:
            return

        if not value % max_operating_temperature.step:
            return

        odNPowerControl = self._power_limit_settings
        odNPowerControl.iMode = ODNControlType_Manual
        odNPowerControl.iMaxOperatingTemperature = value

        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_PowerLimit_Set(
                context,
                iAdapterIndex,
                ctypes.byref(odNPowerControl)
            )

    @property
    def tdp_limit(self):
        caps = self._parent._capabilities
        settings = self._power_limit_settings

        tdp_limit = ParameterRange(settings.iTDPLimit.value)
        tdp_limit._set_object(caps.power)
        return tdp_limit

    @tdp_limit.setter
    def tdp_limit(self, value):
        tdp_limit = self.tdp_limit

        if not tdp_limit.max >= value >= tdp_limit.min:
            return

        if not value % tdp_limit.step:
            return

        odNPowerControl = self._power_limit_settings
        odNPowerControl.iMode = ODNControlType_Manual
        odNPowerControl.iTDPLimit = value

        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_OverdriveN_PowerLimit_Set(
                    context,
                    iAdapterIndex,
                    ctypes.byref(odNPowerControl)
            )


# noinspection PyProtectedMember
class FanSpeed(object):

    def __init__(self, parent):
        self._parent = parent

    @property
    def _fan_control(self):
        odNFanControl = ADLODNFanControl()
        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            if ADL_OK == _ADL2_OverdriveN_FanControl_Get(
                context,
                iAdapterIndex,
                ctypes.byref(odNFanControl)
            ):
                return odNFanControl

    @property
    def min_limit(self):
        caps = self._parent._capabilities

        if not caps.iFlags.value & ADL_ODN_FAN_SPEED_MIN == ADL_ODN_FAN_SPEED_MIN:
            return

        fan_control = self._fan_control
        min_limit = ParameterRange(fan_control.iMinFanLimit.value)
        min_limit._set_object(caps.fanSpeed)
        return min_limit

    @min_limit.setter
    def min_limit(self, value):
        caps = self._parent._capabilities
        if caps.iFlags.value & ADL_ODN_FAN_SPEED_MIN == ADL_ODN_FAN_SPEED_MIN:
            min_limit = self.min_limit

            if not min_limit.max >= value >= min_limit.min:
                return

            if value % min_limit.step:
                return

            iAdapterIndex = INT(self._parent._adapter_index)

            odNFanControl = self._fan_control
            odNFanControl.iMode = ODNControlType_Manual
            odNFanControl.iMinFanLimit = value

            with ADL2_Main_Control_Create as context:
                _ADL2_OverdriveN_FanControl_Set(context, iAdapterIndex, ctypes.byref(odNFanControl))

    @property
    def control_mode(self):
        fan_control = self._fan_control
        return fan_control.iFanControlMode.value

    @property
    def target(self):
        caps = self._parent._capabilities

        if not caps.iFlags.value & ADL_ODN_FAN_SPEED_TARGET == ADL_ODN_FAN_SPEED_TARGET:
            return

        fan_control = self._fan_control
        target = ParameterRange(fan_control.iTargetFanSpeed.value)
        target._set_object(caps.fanSpeed)
        return target

    @target.setter
    def target(self, value):
        caps = self._parent._capabilities
        if caps.iFlags.value & ADL_ODN_FAN_SPEED_TARGET == ADL_ODN_FAN_SPEED_TARGET:
            target = self.target

            if not target.max >= value >= target.min:
                return

            if value % target.step:
                return

            iAdapterIndex = INT(self._parent._adapter_index)
            odNFanControl = self._fan_control
            odNFanControl.iMode = ODNControlType_Manual
            odNFanControl.iTargetFanSpeed = value

            with ADL2_Main_Control_Create as context:
                _ADL2_OverdriveN_FanControl_Set(context, iAdapterIndex, ctypes.byref(odNFanControl))

    @property
    def min_performance_clock(self):
        caps = self._parent._capabilities

        if not caps.iFlags.value & ADL_ODN_ACOUSTIC_LIMIT_SCLK == ADL_ODN_ACOUSTIC_LIMIT_SCLK:
            return

        fan_control = self._fan_control

        min_performance_clock = ParameterRange(fan_control.iMinPerformanceClock.value)
        min_performance_clock._set_object(caps.minimumPerformanceClock)

        return min_performance_clock

    @min_performance_clock.setter
    def min_performance_clock(self, value):
        caps = self._parent._capabilities
        if caps.iFlags.value & ADL_ODN_ACOUSTIC_LIMIT_SCLK == ADL_ODN_ACOUSTIC_LIMIT_SCLK:
            min_performance_clock = self.min_performance_clock

            if not min_performance_clock.max >= value >= min_performance_clock.min:
                return

            if value % min_performance_clock.step:
                return

            iAdapterIndex = INT(self._parent._adapter_index)
            odNFanControl = self._fan_control
            odNFanControl.iMode = ODNControlType_Manual
            odNFanControl.iMinPerformanceClock = value

            with ADL2_Main_Control_Create as context:
                _ADL2_OverdriveN_FanControl_Set(context, iAdapterIndex, ctypes.byref(odNFanControl))

    @property
    def target_temperature(self):
        caps = self._parent._capabilities

        if not caps.iFlags.value & ADL_ODN_TEMPERATURE_FAN_MAX == ADL_ODN_TEMPERATURE_FAN_MAX:
            return

        fan_control = self._fan_control
        target_temperature = ParameterRange(fan_control.iTargetTemperature.value)
        target_temperature._set_object(caps.fanTemperature)

        return target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        caps = self._parent._capabilities
        if caps.iFlags.value & ADL_ODN_TEMPERATURE_FAN_MAX == ADL_ODN_TEMPERATURE_FAN_MAX:
            target_temperature = self.target_temperature

            if not target_temperature.max >= value >= target_temperature.min:
                return

            if value % target_temperature.step:
                return

            iAdapterIndex = INT(self._parent._adapter_index)
            odNFanControl = self._fan_control
            odNFanControl.iMode = ODNControlType_Manual
            odNFanControl.iTargetTemperature = value

            with ADL2_Main_Control_Create as context:
                _ADL2_OverdriveN_FanControl_Set(context, iAdapterIndex, ctypes.byref(odNFanControl))

    @property
    def fan_speed(self):
        fan_control = self._fan_control
        return fan_control.iCurrentFanSpeed.value

    @property
    def fan_speed_mode(self):
        fan_control = self._fan_control
        return fan_control.iCurrentFanSpeedMode.value


# noinspection PyProtectedMember
class GPUPerformanceLevel(object):

    # noinspection PyShadowingBuiltins
    def __init__(self, parent, id):
        self._id = id
        self._parent = parent

    @property
    def id(self):
        return self._id

    @property
    def _level(self):
        overdriveCapabilities = self._parent._capabilities

        num_levels = overdriveCapabilities.iMaximumNumberOfPerformanceLevels.value

        size = (
                ctypes.sizeof(ADLODNPerformanceLevelsX2) +
                ctypes.sizeof(ADLODNPerformanceLevelX2) *
                (num_levels - 1)
        )

        performanceLevelsBuffer = (CHAR * size)()
        ctypes.memset(performanceLevelsBuffer, 0, size)
        odPerformanceLevels = ctypes.cast(
            performanceLevelsBuffer,
            ctypes.POINTER(ADLODNPerformanceLevelsX2)
        )
        odPerformanceLevels.iSize = size
        odPerformanceLevels.iNumberOfPerformanceLevels = num_levels

        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            if ADL_OK == _ADL2_OverdriveN_SystemClocksX2_Get(
                context,
                iAdapterIndex,
                odPerformanceLevels
            ):
                # noinspection PyUnresolvedReferences
                return odPerformanceLevels.content.aLevels[self._id]

    @property
    def clock(self):
        caps = self._parent._capabilities
        level = self._level

        value = ParameterRange(level.iClock.value)
        value._set_object(caps.sEngineClockRange)
        return value

    @clock.setter
    def clock(self, value):
        if not self.is_clock_editable:
            return

        old_value = self.clock
        if not old_value.max >= value >= old_value.min:
            return

        if value % old_value.step:
            return

        # TODO: finish setting

    @property
    def is_clock_editable(self):
        level = self._level
        return level.iControl & ADL_ODN_DPM_CLOCK == ADL_ODN_DPM_CLOCK

    @property
    def is_vdcc_editable(self):
        level = self._level
        return level.iControl & ADL_ODN_DPM_VDDC == ADL_ODN_DPM_VDDC

    @property
    def vdcc(self):
        caps = self._parent._capabilities
        level = self._level
        value = ParameterRange(level.iVddc.value)
        value._set_object(caps.svddcRange)
        return value

    @vdcc.setter
    def vdcc(self, value):
        if not self.is_vdcc_editable:
            return

        old_value = self.vdcc
        if not old_value.max >= value >= old_value.min:
            return

        if value % old_value.step:
            return

        # TODO: finish setting

    @property
    def dpm_state(self):
        level = self._level
        return bool(level.iEnabled.value)

    @dpm_state.setter
    def dpm_state(self, value):
        if self.is_dpm_state_editable:
            # TODO: finish setting
            pass

    @property
    def is_dpm_state_editable(self):
        level = self._level
        caps = self._parent._capabilities

        return (
            level.iControl & ADL_ODN_DPM_MASK == ADL_ODN_DPM_MASK and
            caps.iFlags & ADL_ODN_MCLK_DPM_MASK_ENABLE == ADL_ODN_MCLK_DPM_MASK_ENABLE
        )


# noinspection PyProtectedMember
class MemoryPerformanceLevel(GPUPerformanceLevel):

    @property
    def _defaults(self):
        overdriveCapabilities = self._parent._capabilities

        num_levels = overdriveCapabilities.iMaximumNumberOfPerformanceLevels.value

        size = (
                ctypes.sizeof(ADLODNPerformanceLevelsX2) +
                ctypes.sizeof(ADLODNPerformanceLevelX2) *
                (num_levels - 1)
        )

        performanceLevelsBuffer_default = (CHAR * size)()
        ctypes.memset(performanceLevelsBuffer_default, 0, size)

        odPerformanceLevels_default = ctypes.cast(performanceLevelsBuffer_default, POINTER(ADLODNPerformanceLevelsX2))
        odPerformanceLevels_default.iSize = size
        odPerformanceLevels_default.iMode = 1  # DEFAULTS
        odPerformanceLevels_default.iNumberOfPerformanceLevels = num_levels

        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            if ADL_OK == _ADL2_OverdriveN_MemoryClocksX2_Get(
                    context,
                    iAdapterIndex,
                    odPerformanceLevels_default
            ):
                # noinspection PyUnresolvedReferences
                return odPerformanceLevels_default.content.aLevels[self._id]

    @property
    def _level(self):
        overdriveCapabilities = self._parent._capabilities

        num_levels = overdriveCapabilities.iMaximumNumberOfPerformanceLevels.value

        size = (
                ctypes.sizeof(ADLODNPerformanceLevelsX2) +
                ctypes.sizeof(ADLODNPerformanceLevelX2) *
                (num_levels - 1)
        )

        performanceLevelsBuffer = (CHAR * size)()
        ctypes.memset(performanceLevelsBuffer, 0, size)
        odPerformanceLevels = ctypes.cast(
            performanceLevelsBuffer,
            ctypes.POINTER(ADLODNPerformanceLevelsX2)
        )
        odPerformanceLevels.iSize = size
        odPerformanceLevels.iMode = 0
        odPerformanceLevels.iNumberOfPerformanceLevels = num_levels

        iAdapterIndex = INT(self._parent._adapter_index)

        with ADL2_Main_Control_Create as context:
            if ADL_OK == _ADL2_OverdriveN_MemoryClocksX2_Get(
                    context,
                    iAdapterIndex,
                    odPerformanceLevels
            ):
                # noinspection PyUnresolvedReferences
                return odPerformanceLevels.content.aLevels[self._id]

    @property
    def clock(self):
        caps = self._parent._capabilities
        level = self._level
        odPerformanceLevels_default = self._defaults

        if not caps.iFlags.value & ADL_ODN_MCLK_UNDERCLOCK_ENABLE == ADL_ODN_MCLK_UNDERCLOCK_ENABLE:
            caps.sMemoryClockRange.iMin = odPerformanceLevels_default.iClock

        value = ParameterRange(level.iClock.value)
        value._set_object(caps.sMemoryClockRange)
        return value

    @clock.setter
    def clock(self, value):
        if not self.is_clock_editable:
            return

        old_value = self.clock
        if not old_value.max >= value >= old_value.min:
            return

        if value % old_value.step:
            return

        # TODO: finish setting
