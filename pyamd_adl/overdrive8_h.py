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


ADL2_OVERDRIVE8_INIT_SETTING_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD8InitSetting)
)
ADL2_OVERDRIVE8_CURRENT_SETTING_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD8CurrentSetting)
)
ADL2_OVERDRIVE8_SETTING_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLOD8SetSetting),
    POINTER(ADLOD8CurrentSetting)
)
ADL2_NEW_QUERYPMLOGDATA_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPMLogDataOutput)
)
ADL2_OVERDRIVE8_INIT_SETTINGX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLOD8SingleInitSetting))
)
ADL2_OVERDRIVE8_CURRENT_SETTINGX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(INT))
)
ADL2_AUTOTUNINGRESULT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(BOOL)
)
ADL2_OVERDRIVE8_PMLOGSENSORRANGE_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLOD8SingleInitSetting))
)
ADL2_OVERDRIVE8_PMLOGSENSORTYPE_SUPPORT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(INT))
)
ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_SUPPORT = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    INT,
)
ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_START = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(INT),
    POINTER(ADL_D3DKMT_HANDLE),
    POINTER(POINTER(VOID)),
    INT
)
ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_READ = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(VOID)),
    POINTER(ADLPMLogDataOutput)
)
ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_STOP = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADL_D3DKMT_HANDLE)
)
ADL2_DEVICE_PMLOG_DEVICE_CREATE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADL_D3DKMT_HANDLE)
)
ADL2_DEVICE_PMLOG_DEVICE_DESTROY = _int(
    ADL_CONTEXT_HANDLE,
    ADL_D3DKMT_HANDLE
)
ADL2_OVERDRIVE8_CURRENT_SETTINGX3_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(INT)),
    INT
)


# Function to retrieve the Overdrive8 initial settings.
_ADL2_Overdrive8_Init_Setting_Get = ADL2_OVERDRIVE8_INIT_SETTING_GET

# Function to retrieve the Overdrive8 current settings.
_ADL2_Overdrive8_Current_Setting_Get = ADL2_OVERDRIVE8_CURRENT_SETTING_GET

# Function to set the Overdrive8 settings.
_ADL2_Overdrive8_Setting_Set = ADL2_OVERDRIVE8_SETTING_SET

# Function to retrieve the Overdrive8 current settings.
_ADL2_New_QueryPMLogData_Get = ADL2_NEW_QUERYPMLOGDATA_GET

# Function to retrieve the Overdrive8 current range settings.
# This is new versin of ADL2_Overdrive8_Init_Setting_Get.
# It supports new features and does not need to change the PAI.
_ADL2_Overdrive8_Init_SettingX2_Get = ADL2_OVERDRIVE8_INIT_SETTINGX2_GET

# Function to retrieve the Overdrive8 current settings.
# This is new versin of ADL2_Overdrive8_Current_SettingX2_Get.
# It supports new features and does not need to change the PAI.
_ADL2_Overdrive8_Current_SettingX2_Get = ADL2_OVERDRIVE8_CURRENT_SETTINGX2_GET

# Function to retrieve the current auto tuning state.
_ADL2_AutoTuningResult_Get = ADL2_AUTOTUNINGRESULT_GET

# Function to retrieve the PMLog sensor range value if the driver supports the sensor.
_ADL2_Overdrive8_PMLogSenorRange_Caps = ADL2_OVERDRIVE8_PMLOGSENSORRANGE_CAPS

# Function to retrieve the PMLog sensor real value reading support flag from the driver.
_ADL2_Overdrive8_PMLogSenorType_Support_Get = ADL2_OVERDRIVE8_PMLOGSENSORTYPE_SUPPORT_GET

# Function to retrieve the support flag, which indictates if the shared
# memoory way is avilable or not.
_ADL2_Overdrive8_PMLog_ShareMemory_Support = ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_SUPPORT

# Function to start a shared memory session.
_ADL2_Overdrive8_PMLog_ShareMemory_Start = ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_START

# Function to start a shared memory session.
_ADL2_Overdrive8_PMLog_ShareMemory_Read = ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_READ

# Function to stop a shared memory session.
_ADL2_Overdrive8_PMLog_ShareMemory_Stop = ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_STOP

# This function create the device. Adds MGPU support over legacy functions.
_ADL2_Device_PMLog_Device_Create = ADL2_DEVICE_PMLOG_DEVICE_CREATE

# This function destroy the device. Adds MGPU support over legacy functions.
_ADL2_Device_PMLog_Device_Destroy = ADL2_DEVICE_PMLOG_DEVICE_DESTROY

# Function to retrieve the Overdrive8 current settings. This is new versin
# of ADL2_Overdrive8_Current_SettingX3_Get. It supports the availablity of each item.
_ADL2_Overdrive8_Current_SettingX3_Get = ADL2_OVERDRIVE8_CURRENT_SETTINGX3_GET


def Init(hDLL):
    global _ADL2_Overdrive8_Init_Setting_Get
    global _ADL2_Overdrive8_Current_Setting_Get
    global _ADL2_Overdrive8_Setting_Set
    global _ADL2_New_QueryPMLogData_Get
    global _ADL2_Overdrive8_Init_SettingX2_Get
    global _ADL2_Overdrive8_Current_SettingX2_Get
    global _ADL2_AutoTuningResult_Get
    global _ADL2_Overdrive8_PMLogSenorRange_Caps
    global _ADL2_Overdrive8_PMLogSenorType_Support_Get
    global _ADL2_Overdrive8_PMLog_ShareMemory_Support
    global _ADL2_Overdrive8_PMLog_ShareMemory_Start
    global _ADL2_Overdrive8_PMLog_ShareMemory_Read
    global _ADL2_Overdrive8_PMLog_ShareMemory_Stop
    global _ADL2_Device_PMLog_Device_Create
    global _ADL2_Device_PMLog_Device_Destroy
    global _ADL2_Overdrive8_Current_SettingX3_Get

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
    _ADL2_AutoTuningResult_Get = ADL2_AUTOTUNINGRESULT_GET(
          GetProcAddress(hDLL, "ADL2_AutoTuningResult_Get")
    )
    _ADL2_Overdrive8_PMLogSenorRange_Caps = ADL2_OVERDRIVE8_PMLOGSENSORRANGE_CAPS(
          GetProcAddress(hDLL, "ADL2_Overdrive8_PMLogSenorRange_Caps")
    )
    _ADL2_Overdrive8_PMLogSenorType_Support_Get = ADL2_OVERDRIVE8_PMLOGSENSORTYPE_SUPPORT_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive8_PMLogSenorType_Support_Get")
    )
    _ADL2_Overdrive8_PMLog_ShareMemory_Support = ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_SUPPORT(
          GetProcAddress(hDLL, "ADL2_Overdrive8_PMLog_ShareMemory_Support")
    )
    _ADL2_Overdrive8_PMLog_ShareMemory_Start = ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_START(
          GetProcAddress(hDLL, "ADL2_Overdrive8_PMLog_ShareMemory_Start")
    )
    _ADL2_Overdrive8_PMLog_ShareMemory_Read = ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_READ(
          GetProcAddress(hDLL, "ADL2_Overdrive8_PMLog_ShareMemory_Read")
    )
    _ADL2_Overdrive8_PMLog_ShareMemory_Stop = ADL2_OVERDRIVE8_PMLOG_SHAREMEMORY_STOP(
          GetProcAddress(hDLL, "ADL2_Overdrive8_PMLog_ShareMemory_Stop")
    )
    _ADL2_Device_PMLog_Device_Create = ADL2_DEVICE_PMLOG_DEVICE_CREATE(
          GetProcAddress(hDLL, "ADL2_Device_PMLog_Device_Create")
    )
    _ADL2_Device_PMLog_Device_Destroy = ADL2_DEVICE_PMLOG_DEVICE_DESTROY(
          GetProcAddress(hDLL, "ADL2_Device_PMLog_Device_Destroy")
    )
    _ADL2_Overdrive8_Current_SettingX3_Get = ADL2_OVERDRIVE8_CURRENT_SETTINGX3_GET(
          GetProcAddress(hDLL, "ADL2_Overdrive8_Current_SettingX3_Get")
    )


__all__ = (
    '_ADL2_Overdrive8_Init_Setting_Get',
    '_ADL2_Overdrive8_Current_Setting_Get',
    '_ADL2_Overdrive8_Setting_Set',
    '_ADL2_New_QueryPMLogData_Get',
    '_ADL2_Overdrive8_Init_SettingX2_Get',
    '_ADL2_Overdrive8_Current_SettingX2_Get',
    '_ADL2_AutoTuningResult_Get',
    '_ADL2_Overdrive8_PMLogSenorRange_Caps',
    '_ADL2_Overdrive8_PMLogSenorType_Support_Get',
    '_ADL2_Overdrive8_PMLog_ShareMemory_Support',
    '_ADL2_Overdrive8_PMLog_ShareMemory_Start',
    '_ADL2_Overdrive8_PMLog_ShareMemory_Read',
    '_ADL2_Overdrive8_PMLog_ShareMemory_Stop',
    '_ADL2_Device_PMLog_Device_Create',
    '_ADL2_Device_PMLog_Device_Destroy',
    '_ADL2_Overdrive8_Current_SettingX3_Get',
    'OverDrive8'
)


from .adl_sdk_h import ADL2_Main_Control_Create, ADL_Main_Memory_Free # NOQA


def _set_overdrive_8(context, iAdapterIndex, initSetting, level, value):
    lpNumberOfFeatures = INT(OD8_COUNT)
    lppCurrentSettingList = (INT * OD8_COUNT)()
    odCurrentSetting = ADLOD8CurrentSetting()

    _ADL2_Overdrive8_Current_SettingX2_Get(
        context,
        iAdapterIndex,
        ctypes.byref(lpNumberOfFeatures),
        ctypes.byref(lppCurrentSettingList)
    )

    if lpNumberOfFeatures > OD8_COUNT:
        odCurrentSetting.count = OD8_COUNT
    else:
        odCurrentSetting.count = lpNumberOfFeatures

    for i in range(odCurrentSetting.count):
        odCurrentSetting.Od8SettingTable[i] = lppCurrentSettingList[i]

    ADL_Main_Memory_Free(lppCurrentSettingList)

    odlpDataOutput = ADLPMLogDataOutput()

    _ADL2_New_QueryPMLogData_Get(
        context,
        iAdapterIndex,
        ctypes.byref(odlpDataOutput),
    )

    odSetSetting = ADLOD8SetSetting()
    odSetSetting.count = OD8_COUNT

    max_val = initSetting.od8SettingTable[level].maxValue
    min_val = initSetting.od8SettingTable[level].minValue

    if max_val < value or min_val > value:
        return

    for i in range(OD8_GFXCLK_FREQ1, OD8_UCLK_FMAX + 1):
        odSetSetting.od8SettingTable[i].requested = 1
        odSetSetting.od8SettingTable[i].value = odCurrentSetting.Od8SettingTable[i]

    reset = True

    if OD8_FAN_CURVE_TEMPERATURE_1 <= level <= OD8_FAN_CURVE_SPEED_5:
        reset = False

    for i in range(OD8_FAN_CURVE_TEMPERATURE_1, OD8_FAN_CURVE_SPEED_5 + 1):
        odSetSetting.od8SettingTable[i].reset = reset
        odSetSetting.od8SettingTable[i].requested = 1
        odSetSetting.od8SettingTable[i].value = odCurrentSetting.Od8SettingTable[i]

    odSetSetting.od8SettingTable[level].requested = 1
    odSetSetting.od8SettingTable[level].value = value

    if OD8_GFXCLK_FMAX == level:
        odSetSetting.od8SettingTable[OD8_GFXCLK_FREQ3].value = value
    elif OD8_GFXCLK_FMIN == level:
        odSetSetting.od8SettingTable[OD8_GFXCLK_FREQ1].value = value

    if _ADL2_Overdrive8_Setting_Set(
            context,
            iAdapterIndex,
            ctypes.byref(odSetSetting),
            ctypes.byref(odCurrentSetting)
    ) == ADL_OK:
        return value


def _get_overdrive_8(context, iAdapterIndex, initSetting, *args):
    lpNumberOfFeatures = INT(OD8_COUNT)
    lppCurrentSettingList = (INT * OD8_COUNT)()
    odCurrentSetting = ADLOD8CurrentSetting()

    _ADL2_Overdrive8_Current_SettingX2_Get(
        context,
        iAdapterIndex,
        ctypes.byref(lpNumberOfFeatures),
        ctypes.byref(lppCurrentSettingList)
    )

    if lpNumberOfFeatures > OD8_COUNT:
        odCurrentSetting.count = OD8_COUNT
    else:
        odCurrentSetting.count = lpNumberOfFeatures

    for i in range(odCurrentSetting.count):
        odCurrentSetting.Od8SettingTable[i] = lppCurrentSettingList[i]

    ADL_Main_Memory_Free(lppCurrentSettingList)

    odlpDataOutput = ADLPMLogDataOutput()

    _ADL2_New_QueryPMLogData_Get(
        context,
        iAdapterIndex,
        ctypes.byref(odlpDataOutput),
    )

    for item, cap in args:
        if initSetting.overdrive8Capabilities & cap == cap:
            editable_val = True
        else:
            editable_val = False

        max_val = initSetting.od8SettingTable[item].maxValue
        min_val = initSetting.od8SettingTable[item].minValue
        default_val = initSetting.od8SettingTable[item].defaultValue
        current_val = odCurrentSetting.Od8SettingTable[item]

        class Values(object):
            min_value = min_val
            max_value = max_val
            default = default_val
            editable = editable_val
            current = current_val
            level = item

        yield Values


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
        self.real != self.default

    def activate(self):
        pass

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


@utils.instance_singleton
class CoreVoltages(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index
        self._core_voltages = None

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
        with ADL2_Main_Control_Create as context:
            lpNumberOfFeatures = INT(OD8_COUNT)
            lpOverdrive8Capabilities = INT(0)
            lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
            initSetting = ADLOD8InitSetting()

            _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpOverdrive8Capabilities),
                ctypes.byref(lpNumberOfFeatures),
                ctypes.byref(lppInitSettingList)
            )

            if (
                not lpOverdrive8Capabilities.value & ADL_OD8_GFXCLK_LIMITS == ADL_OD8_GFXCLK_LIMITS and
                not lpOverdrive8Capabilities.value & ADL_OD8_GFXCLK_CURVE == ADL_OD8_GFXCLK_CURVE
            ):
                return

            initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

            if lpNumberOfFeatures > OD8_COUNT:
                initSetting.count = OD8_COUNT
            else:
                initSetting.count = lpNumberOfFeatures

            for i in range(initSetting.count):
                initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

            ADL_Main_Memory_Free(lppInitSettingList)

            return _set_overdrive_8(context, iAdapterIndex, initSetting, level, value)

    def __iter__(self):
        if self._core_voltages is None:
            self._core_voltages = []

            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if (
                    lpOverdrive8Capabilities.value & ADL_OD8_GFXCLK_LIMITS == ADL_OD8_GFXCLK_LIMITS or
                    lpOverdrive8Capabilities.value & ADL_OD8_GFXCLK_CURVE == ADL_OD8_GFXCLK_CURVE
                ):

                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    for cls in _get_overdrive_8(
                        context,
                        iAdapterIndex,
                        initSetting,
                        [OD8_GFXCLK_VOLTAGE1, ADL_OD8_GFXCLK_CURVE],
                        [OD8_GFXCLK_VOLTAGE2, ADL_OD8_GFXCLK_CURVE],
                        [OD8_GFXCLK_VOLTAGE3, ADL_OD8_GFXCLK_CURVE]
                    ):

                        value = CoreVoltage(cls.current)
                        value._obj = cls
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._core_voltages.append(value)

        return iter(self._core_voltages)


class CoreClock(IntValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        lpCoreClock = INT()
        lpMemoryClock = INT()

        from .adapter_h import _ADL2_Adapter_ObservedClockInfo_Get

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_ObservedClockInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpCoreClock),
                ctypes.byref(lpMemoryClock)
            )

            return lpCoreClock == self.real

    def activate(self):
        pass

    @property
    def editable(self):
        return self._obj.editable

    @property
    def step(self):
        return 0

    @property
    def default(self):
        return self._obj.default

    @property
    def min(self):
        return self._obj.min_value

    @property
    def unit_of_measure(self):
        return 'MHz'


@utils.instance_singleton
class CoreClocks(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index
        self._core_clocks = None

    def __getitem__(self, item):
        return list(self)[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += value - val.real

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpCoreClock = INT()
        lpMemoryClock = INT()

        from .adapter_h import _ADL2_Adapter_ObservedClockInfo_Get

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_ObservedClockInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpCoreClock),
                ctypes.byref(lpMemoryClock)
            )

            return CoreClock(lpCoreClock)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            lpNumberOfFeatures = INT(OD8_COUNT)
            lpOverdrive8Capabilities = INT(0)
            lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
            initSetting = ADLOD8InitSetting()

            _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpOverdrive8Capabilities),
                ctypes.byref(lpNumberOfFeatures),
                ctypes.byref(lppInitSettingList)
            )

            if (
                not lpOverdrive8Capabilities.value & ADL_OD8_GFXCLK_LIMITS == ADL_OD8_GFXCLK_LIMITS and
                not lpOverdrive8Capabilities.value & ADL_OD8_GFXCLK_CURVE == ADL_OD8_GFXCLK_CURVE
            ):
                return

            initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

            if lpNumberOfFeatures > OD8_COUNT:
                initSetting.count = OD8_COUNT
            else:
                initSetting.count = lpNumberOfFeatures

            for i in range(initSetting.count):
                initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

            ADL_Main_Memory_Free(lppInitSettingList)

            return _set_overdrive_8(context, iAdapterIndex, initSetting, level, value)

    def __iter__(self):
        if self._core_clocks is None:
            self._core_clocks = []

            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if (
                    lpOverdrive8Capabilities.value & ADL_OD8_GFXCLK_LIMITS == ADL_OD8_GFXCLK_LIMITS or
                    lpOverdrive8Capabilities.value & ADL_OD8_GFXCLK_CURVE == ADL_OD8_GFXCLK_CURVE
                ):

                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    for cls in _get_overdrive_8(
                            context,
                            iAdapterIndex,
                            initSetting,
                            [OD8_GFXCLK_FREQ1, ADL_OD8_GFXCLK_CURVE],
                            [OD8_GFXCLK_FREQ2, ADL_OD8_GFXCLK_CURVE],
                            [OD8_GFXCLK_FREQ3, ADL_OD8_GFXCLK_CURVE],
                            [OD8_GFXCLK_FMIN, ADL_OD8_GFXCLK_CURVE],
                            [OD8_GFXCLK_FMAX, ADL_OD8_GFXCLK_CURVE]
                    ):
                        value = CoreClock(cls.current)
                        value._obj = cls
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._core_clocks.append(value)

        return iter(self._core_clocks)


class MemoryVoltage(FloatValueWrapper):

    @property
    def is_active(self):
        return False

    def activate(self):
        pass

    @property
    def step(self):
        return 0

    @property
    def default(self):
        return 0

    @property
    def max(self):
        return 0

    @property
    def min(self):
        return 0

    @property
    def unit_of_measure(self):
        return 'VDC'


@utils.instance_singleton
class MemoryVoltages(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index
        self._memory_voltages = []

    def __getitem__(self, item):
        return list(self)[item]

    def __setitem__(self, key, value):
        pass

    @property
    def actual(self):
        return MemoryVoltage(0.0)

    @property
    def current(self):
        return MemoryVoltage(0.0)

    def _set_level(self, level, value):
        pass

    def __iter__(self):
        return iter(self._memory_voltages)


class MemoryClock(IntValueWrapper):

    @property
    def is_active(self):
        iAdapterIndex = INT(self._adapter_index)
        lpCoreClock = INT()
        lpMemoryClock = INT()

        from .adapter_h import _ADL2_Adapter_ObservedClockInfo_Get

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_ObservedClockInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpCoreClock),
                ctypes.byref(lpMemoryClock)
            )

            return lpMemoryClock == self.real

    def activate(self):
        pass

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


@utils.instance_singleton
class MemoryClocks(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index
        self._memory_clocks = None

    def __getitem__(self, item):
        return list(self)[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += value - val.real

    @property
    def actual(self):
        iAdapterIndex = INT(self._adapter_index)
        lpCoreClock = INT()
        lpMemoryClock = INT()

        from .adapter_h import _ADL2_Adapter_ObservedClockInfo_Get

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_ObservedClockInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpCoreClock),
                ctypes.byref(lpMemoryClock)
            )

            return MemoryClock(lpMemoryClock)

    @property
    def current(self):
        for value in self:
            if value.is_active:
                return value

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            lpNumberOfFeatures = INT(OD8_COUNT)
            lpOverdrive8Capabilities = INT(0)
            lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
            initSetting = ADLOD8InitSetting()

            _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpOverdrive8Capabilities),
                ctypes.byref(lpNumberOfFeatures),
                ctypes.byref(lppInitSettingList)
            )

            if not lpOverdrive8Capabilities.value & ADL_OD8_UCLK_MAX == ADL_OD8_UCLK_MAX:
                return

            initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

            if lpNumberOfFeatures > OD8_COUNT:
                initSetting.count = OD8_COUNT
            else:
                initSetting.count = lpNumberOfFeatures

            for i in range(initSetting.count):
                initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

            ADL_Main_Memory_Free(lppInitSettingList)

            return _set_overdrive_8(context, iAdapterIndex, initSetting, level, value)

    def __iter__(self):
        if self._memory_clocks is None:
            self._memory_clocks = []

            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if lpOverdrive8Capabilities.value & ADL_OD8_UCLK_MAX == ADL_OD8_UCLK_MAX:

                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    for cls in _get_overdrive_8(
                        context,
                        iAdapterIndex,
                        initSetting,
                        [OD8_UCLK_FMAX, ADL_OD8_UCLK_MAX]
                    ):
                        value = MemoryClock(cls.current)
                        value._obj = cls
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._memory_clocks.append(value)

            return iter(self._memory_clocks)


class MemoryTiming(IntValueWrapper):

    @property
    def unit_of_measure(self):
        return ''

    @property
    def min(self):
        return self._obj.min_value

    @property
    def step(self):
        return self._obj.step_value


@utils.instance_singleton
class MemoryTimings(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index
        self._memory_timings

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            lpNumberOfFeatures = INT(OD8_COUNT)
            lpOverdrive8Capabilities = INT(0)
            lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
            initSetting = ADLOD8InitSetting()

            _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpOverdrive8Capabilities),
                ctypes.byref(lpNumberOfFeatures),
                ctypes.byref(lppInitSettingList)
            )

            if not lpOverdrive8Capabilities.value &  ADL_OD8_MEMORY_TIMING_TUNE ==  ADL_OD8_MEMORY_TIMING_TUNE:
                return

            initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

            if lpNumberOfFeatures > OD8_COUNT:
                initSetting.count = OD8_COUNT
            else:
                initSetting.count = lpNumberOfFeatures

            for i in range(initSetting.count):
                initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

            ADL_Main_Memory_Free(lppInitSettingList)

            return _set_overdrive_8(context, iAdapterIndex, initSetting, level, value)

    def __iter__(self):
        if self._memory_timings is None:
            self._memory_timings = []
            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if lpOverdrive8Capabilities.value & ADL_OD8_MEMORY_TIMING_TUNE ==  ADL_OD8_MEMORY_TIMING_TUNE:

                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    for cls in _get_overdrive_8(
                        context,
                        iAdapterIndex,
                        initSetting,
                        [OD8_AC_TIMING, ADL_OD8_MEMORY_TIMING_TUNE],
                    ):
                        value = MemoryTiming(cls.current)
                        value._obj = cls
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._memory_timings.append(value)

        return iter(self._memory_timings)

    def __getitem__(self, item):
        timings = list(self)
        return timings[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += value - val.real


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


@utils.instance_singleton
class FanSpeeds(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index
        self._fan_speeds = None

    @property
    def zero_controls(self):
        return ZeroFanControls(self._adapter_index)

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            lpNumberOfFeatures = INT(OD8_COUNT)
            lpOverdrive8Capabilities = INT(0)
            lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
            initSetting = ADLOD8InitSetting()

            _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpOverdrive8Capabilities),
                ctypes.byref(lpNumberOfFeatures),
                ctypes.byref(lppInitSettingList)
            )

            if (
                not lpOverdrive8Capabilities.value & ADL_OD8_ACOUSTIC_LIMIT_SCLK == ADL_OD8_ACOUSTIC_LIMIT_SCLK and
                not lpOverdrive8Capabilities.value & ADL_OD8_FAN_SPEED_MIN == ADL_OD8_FAN_SPEED_MIN
            ):
                return

            initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

            if lpNumberOfFeatures > OD8_COUNT:
                initSetting.count = OD8_COUNT
            else:
                initSetting.count = lpNumberOfFeatures

            for i in range(initSetting.count):
                initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

            ADL_Main_Memory_Free(lppInitSettingList)

            return _set_overdrive_8(context, iAdapterIndex, initSetting, level, value)

    def __iter__(self):
        if self._fan_speeds is None:
            self._fan_speeds = []
            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if (
                    lpOverdrive8Capabilities.value & ADL_OD8_ACOUSTIC_LIMIT_SCLK == ADL_OD8_ACOUSTIC_LIMIT_SCLK or
                    lpOverdrive8Capabilities.value & ADL_OD8_FAN_SPEED_MIN == ADL_OD8_FAN_SPEED_MIN
                ):

                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    for cls in _get_overdrive_8(
                        context,
                        iAdapterIndex,
                        initSetting,
                        [OD8_FAN_MIN_SPEED, ADL_OD8_FAN_SPEED_MIN],
                        [OD8_FAN_ACOUSTIC_LIMIT, ADL_OD8_ACOUSTIC_LIMIT_SCLK]

                    ):
                        value = FanSpeed(cls.current)
                        value._obj = cls
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._fan_speeds.append(value)

        return iter(self._fan_speeds)

    def __getitem__(self, item):
        speeds = list(self)
        return speeds[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += value - val.real


class ZeroFanControl(IntValueWrapper):

    @property
    def unit_of_measure(self):
        return ''

    @property
    def min(self):
        return self._obj.min_value


@utils.instance_singleton
class ZeroFanControls(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index
        self._fan_controls = None

    def _set_level(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            lpNumberOfFeatures = INT(OD8_COUNT)
            lpOverdrive8Capabilities = INT(0)
            lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
            initSetting = ADLOD8InitSetting()

            _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpOverdrive8Capabilities),
                ctypes.byref(lpNumberOfFeatures),
                ctypes.byref(lppInitSettingList)
            )

            if (
                not lpOverdrive8Capabilities.value & ADL_OD8_FAN_ZERO_RPM_CONTROL == ADL_OD8_FAN_ZERO_RPM_CONTROL
            ):
                return

            initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

            if lpNumberOfFeatures > OD8_COUNT:
                initSetting.count = OD8_COUNT
            else:
                initSetting.count = lpNumberOfFeatures

            for i in range(initSetting.count):
                initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

            ADL_Main_Memory_Free(lppInitSettingList)

            return _set_overdrive_8(context, iAdapterIndex, initSetting, level, value)

    def __iter__(self):
        if self._fan_controls is None:
            self._fan_controls = []
            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if (
                    lpOverdrive8Capabilities.value & ADL_OD8_FAN_ZERO_RPM_CONTROL == ADL_OD8_FAN_ZERO_RPM_CONTROL
                ):

                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    for cls in _get_overdrive_8(
                        context,
                        iAdapterIndex,
                        initSetting,
                        [OD8_FAN_ZERORPM_CONTROL, ADL_OD8_FAN_ZERO_RPM_CONTROL]
                    ):
                        value = ZeroFanControl(cls.current)
                        value._obj = cls
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._fan_controls.append(value)

        return iter(self._fan_controls)

    def __getitem__(self, item):
        speeds = list(self)
        return speeds[item]

    def __setitem__(self, key, value):
        values = list(self)
        val = values[key]
        val += value - val.real


class PowerThreshold(IntValueWrapper):

    @property
    def unit_of_measure(self):
        return ''

    @property
    def min(self):
        return self._obj.min_value

    @property
    def default(self):
        return self._obj.default

    @property
    def editable(self):
        return self._obj.editable


class Temperature(FloatValueWrapper):

    @property
    def unit_of_measure(self):
        return ''

    @property
    def min(self):
        return self._obj.min_value

    @property
    def default(self):
        return self._obj.default

    @property
    def editable(self):
        return self._obj.editable


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


class AutoOC(IntValueWrapper):

    @property
    def unit_of_measure(self):
        return ''

    @property
    def min(self):
        return self._obj.min_value

    @property
    def default(self):
        return self._obj.default

    @property
    def editable(self):
        return self._obj.editable


@utils.instance_singleton
class OverDrive8(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index
        self. _power_threshold = []
        self._temperatures = None
        self._auto_oc_uv = None
        self._auto_oc_core = None
        self._auto_oc_memory = None

    @property
    def _activity(self):
        iAdapterIndex = INT(self._adapter_index)
        lpActivity = ADLPMActivity()
        lpActivity.iSize = ctypes.sizeof(ADLPMActivity)

        from .overdrive5_h import _ADL2_Overdrive5_CurrentActivity_Get

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
        return Load(lpActivity.iGPUActivityPercent / 10.0)

    @property
    def temperatures(self):
        if self._temperatures is None:
            self._temperatures = []
            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if (
                    lpOverdrive8Capabilities.value & ADL_OD8_TEMPERATURE_SYSTEM == ADL_OD8_TEMPERATURE_SYSTEM or
                    lpOverdrive8Capabilities.value & ADL_OD8_TEMPERATURE_FAN == ADL_OD8_TEMPERATURE_FAN or
                    lpOverdrive8Capabilities.value & ADL_OD8_POWER_LIMIT == ADL_OD8_POWER_LIMIT
                ):
                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    def _set(level, val):
                        with ADL2_Main_Control_Create as _context:
                            _lpNumberOfFeatures = INT(OD8_COUNT)
                            _lpOverdrive8Capabilities = INT(0)
                            _lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                            _initSetting = ADLOD8InitSetting()

                            _ADL2_Overdrive8_Init_SettingX2_Get(
                                _context,
                                iAdapterIndex,
                                ctypes.byref(_lpOverdrive8Capabilities),
                                ctypes.byref(_lpNumberOfFeatures),
                                ctypes.byref(_lppInitSettingList)
                            )

                            if (
                                not _lpOverdrive8Capabilities.value & ADL_OD8_TEMPERATURE_SYSTEM == ADL_OD8_TEMPERATURE_SYSTEM and
                                not _lpOverdrive8Capabilities.value & ADL_OD8_TEMPERATURE_FAN == ADL_OD8_TEMPERATURE_FAN and
                                not _lpOverdrive8Capabilities.value & ADL_OD8_POWER_LIMIT == ADL_OD8_POWER_LIMIT
                            ):
                                return

                            _initSetting.overdrive8Capabilities = _lpOverdrive8Capabilities

                            if _lpNumberOfFeatures > OD8_COUNT:
                                initSetting.count = OD8_COUNT
                            else:
                                _initSetting.count = _lpNumberOfFeatures

                            for j in range(initSetting.count):
                                _initSetting.od8SettingTable[j].defaultValue = _lppInitSettingList[j].defaultValue
                                _initSetting.od8SettingTable[j].featureID = _lppInitSettingList[j].featureID
                                _initSetting.od8SettingTable[j].maxValue = _lppInitSettingList[j].maxValue
                                _initSetting.od8SettingTable[j].minValue = _lppInitSettingList[j].minValue

                            ADL_Main_Memory_Free(_lppInitSettingList)

                            return _set_overdrive_8(_context, iAdapterIndex, _initSetting, level, val)

                    for cls in _get_overdrive_8(
                            context,
                            iAdapterIndex,
                            initSetting,
                            [OD8_OPERATING_TEMP_MAX, ADL_OD8_TEMPERATURE_SYSTEM],
                            [OD8_FAN_TARGET_TEMP, ADL_OD8_TEMPERATURE_FAN],
                            [OD8_POWER_PERCENTAGE, ADL_OD8_POWER_LIMIT]
                    ):
                        value = Temperature(cls.current)
                        value._obj = cls
                        value._set = _set
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._temperatures.append(value)

        return self._temperatures

    @property
    def is_power_control_supported(self):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            lpNumberOfFeatures = INT(OD8_COUNT)
            lpOverdrive8Capabilities = INT(0)
            lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
            initSetting = ADLOD8InitSetting()

            _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpOverdrive8Capabilities),
                ctypes.byref(lpNumberOfFeatures),
                ctypes.byref(lppInitSettingList)
            )
            initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

            return lpOverdrive8Capabilities.value & ADL_OD8_POWER_GAUGE == ADL_OD8_POWER_GAUGE

    def _set_value(self, level, value):
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            lpNumberOfFeatures = INT(OD8_COUNT)
            lpOverdrive8Capabilities = INT(0)
            lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
            initSetting = ADLOD8InitSetting()

            _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpOverdrive8Capabilities),
                ctypes.byref(lpNumberOfFeatures),
                ctypes.byref(lppInitSettingList)
            )

            if not lpOverdrive8Capabilities.value & ADL_OD8_POWER_GAUGE == ADL_OD8_POWER_GAUGE:
                return

            initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

            if lpNumberOfFeatures > OD8_COUNT:
                initSetting.count = OD8_COUNT
            else:
                initSetting.count = lpNumberOfFeatures

            for i in range(initSetting.count):
                initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

            ADL_Main_Memory_Free(lppInitSettingList)

            return _set_overdrive_8(context, iAdapterIndex, initSetting, level, value)

    @property
    def auto_oc_uv(self):
        if self._auto_oc_uv is None:
            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if not lpOverdrive8Capabilities.value & ADL_OD8_AUTO_UV_ENGINE == ADL_OD8_AUTO_UV_ENGINE:
                    class Value(object):
                        min_val = 0
                        max_val = 0
                        default = 0

                    value = AutoOC(0)
                    value._obj = Value
                    self._auto_oc_uv = value

                else:
                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    def _set(level, val):
                        with ADL2_Main_Control_Create as _context:
                            _lpNumberOfFeatures = INT(OD8_COUNT)
                            _lpOverdrive8Capabilities = INT(0)
                            _lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                            _initSetting = ADLOD8InitSetting()

                            _ADL2_Overdrive8_Init_SettingX2_Get(
                                _context,
                                iAdapterIndex,
                                ctypes.byref(_lpOverdrive8Capabilities),
                                ctypes.byref(_lpNumberOfFeatures),
                                ctypes.byref(_lppInitSettingList)
                            )

                            if not lpOverdrive8Capabilities.value & ADL_OD8_AUTO_UV_ENGINE == ADL_OD8_AUTO_UV_ENGINE:
                                return

                            _initSetting.overdrive8Capabilities = _lpOverdrive8Capabilities

                            if _lpNumberOfFeatures > OD8_COUNT:
                                initSetting.count = OD8_COUNT
                            else:
                                _initSetting.count = _lpNumberOfFeatures

                            for j in range(initSetting.count):
                                _initSetting.od8SettingTable[j].defaultValue = _lppInitSettingList[j].defaultValue
                                _initSetting.od8SettingTable[j].featureID = _lppInitSettingList[j].featureID
                                _initSetting.od8SettingTable[j].maxValue = _lppInitSettingList[j].maxValue
                                _initSetting.od8SettingTable[j].minValue = _lppInitSettingList[j].minValue

                            ADL_Main_Memory_Free(_lppInitSettingList)

                            return _set_overdrive_8(_context, iAdapterIndex, _initSetting, level, val)

                    for cls in _get_overdrive_8(
                        context,
                        iAdapterIndex,
                        initSetting,
                        [OD8_AUTO_UV_ENGINE_CONTROL, ADL_OD8_AUTO_UV_ENGINE]
                    ):
                        value = AutoOC(cls.current)
                        value._obj = cls
                        value._set = _set
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._auto_oc_uv = value

        return self._auto_oc_uv

    @property
    def auto_oc_core(self):
        if self._auto_oc_core is None:
            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if not lpOverdrive8Capabilities.value & ADL_OD8_AUTO_OC_ENGINE == ADL_OD8_AUTO_OC_ENGINE:
                    class Value(object):
                        min_val = 0
                        max_val = 0
                        default = 0

                    value = AutoOC(0)
                    value._obj = Value
                    self._auto_oc_core = value

                else:
                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    def _set(level, val):
                        with ADL2_Main_Control_Create as _context:
                            _lpNumberOfFeatures = INT(OD8_COUNT)
                            _lpOverdrive8Capabilities = INT(0)
                            _lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                            _initSetting = ADLOD8InitSetting()

                            _ADL2_Overdrive8_Init_SettingX2_Get(
                                _context,
                                iAdapterIndex,
                                ctypes.byref(_lpOverdrive8Capabilities),
                                ctypes.byref(_lpNumberOfFeatures),
                                ctypes.byref(_lppInitSettingList)
                            )

                            if not lpOverdrive8Capabilities.value & ADL_OD8_AUTO_OC_ENGINE == ADL_OD8_AUTO_OC_ENGINE:
                                return

                            _initSetting.overdrive8Capabilities = _lpOverdrive8Capabilities

                            if _lpNumberOfFeatures > OD8_COUNT:
                                initSetting.count = OD8_COUNT
                            else:
                                _initSetting.count = _lpNumberOfFeatures

                            for j in range(initSetting.count):
                                _initSetting.od8SettingTable[j].defaultValue = _lppInitSettingList[j].defaultValue
                                _initSetting.od8SettingTable[j].featureID = _lppInitSettingList[j].featureID
                                _initSetting.od8SettingTable[j].maxValue = _lppInitSettingList[j].maxValue
                                _initSetting.od8SettingTable[j].minValue = _lppInitSettingList[j].minValue

                            ADL_Main_Memory_Free(_lppInitSettingList)

                            return _set_overdrive_8(_context, iAdapterIndex, _initSetting, level, val)

                    for cls in _get_overdrive_8(
                            context,
                            iAdapterIndex,
                            initSetting,
                            [OD8_AUTO_OC_ENGINE_CONTROL, ADL_OD8_AUTO_OC_ENGINE]
                    ):
                        value = AutoOC(cls.current)
                        value._obj = cls
                        value._set = _set
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._auto_oc_core = value

        return self._auto_oc_core

    @property
    def auto_oc_memory(self):
        if self._auto_oc_memory is None:
            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if not lpOverdrive8Capabilities.value & ADL_OD8_AUTO_OC_MEMORY == ADL_OD8_AUTO_OC_MEMORY:
                    class Value(object):
                        min_val = 0
                        max_val = 0
                        default = 0

                    value = AutoOC(0)
                    value._obj = Value
                    self._auto_oc_memory = value

                else:
                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    def _set(level, val):
                        with ADL2_Main_Control_Create as _context:
                            _lpNumberOfFeatures = INT(OD8_COUNT)
                            _lpOverdrive8Capabilities = INT(0)
                            _lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                            _initSetting = ADLOD8InitSetting()

                            _ADL2_Overdrive8_Init_SettingX2_Get(
                                _context,
                                iAdapterIndex,
                                ctypes.byref(_lpOverdrive8Capabilities),
                                ctypes.byref(_lpNumberOfFeatures),
                                ctypes.byref(_lppInitSettingList)
                            )

                            if not lpOverdrive8Capabilities.value & ADL_OD8_AUTO_OC_MEMORY == ADL_OD8_AUTO_OC_MEMORY:
                                return

                            _initSetting.overdrive8Capabilities = _lpOverdrive8Capabilities

                            if _lpNumberOfFeatures > OD8_COUNT:
                                initSetting.count = OD8_COUNT
                            else:
                                _initSetting.count = _lpNumberOfFeatures

                            for j in range(initSetting.count):
                                _initSetting.od8SettingTable[j].defaultValue = _lppInitSettingList[j].defaultValue
                                _initSetting.od8SettingTable[j].featureID = _lppInitSettingList[j].featureID
                                _initSetting.od8SettingTable[j].maxValue = _lppInitSettingList[j].maxValue
                                _initSetting.od8SettingTable[j].minValue = _lppInitSettingList[j].minValue

                            ADL_Main_Memory_Free(_lppInitSettingList)

                            return _set_overdrive_8(_context, iAdapterIndex, _initSetting, level, val)

                    for cls in _get_overdrive_8(
                            context,
                            iAdapterIndex,
                            initSetting,
                            [OD8_AUTO_OC_MEMORY_CONTROL, ADL_OD8_AUTO_OC_MEMORY]
                    ):
                        value = AutoOC(cls.current)
                        value._obj = cls
                        value._set = _set
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._auto_oc_memory = value

        return self._auto_oc_memory

    @property
    def power_control(self):
        if not self._power_threshold:
            iAdapterIndex = INT(self._adapter_index)

            with ADL2_Main_Control_Create as context:
                lpNumberOfFeatures = INT(OD8_COUNT)
                lpOverdrive8Capabilities = INT(0)
                lppInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()
                initSetting = ADLOD8InitSetting()

                _ADL2_Overdrive8_Init_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpOverdrive8Capabilities),
                    ctypes.byref(lpNumberOfFeatures),
                    ctypes.byref(lppInitSettingList)
                )
                initSetting.overdrive8Capabilities = lpOverdrive8Capabilities

                if lpOverdrive8Capabilities.value & ADL_OD8_POWER_GAUGE == ADL_OD8_POWER_GAUGE:

                    if lpNumberOfFeatures > OD8_COUNT:
                        initSetting.count = OD8_COUNT
                    else:
                        initSetting.count = lpNumberOfFeatures

                    for i in range(initSetting.count):
                        initSetting.od8SettingTable[i].defaultValue = lppInitSettingList[i].defaultValue
                        initSetting.od8SettingTable[i].featureID = lppInitSettingList[i].featureID
                        initSetting.od8SettingTable[i].maxValue = lppInitSettingList[i].maxValue
                        initSetting.od8SettingTable[i].minValue = lppInitSettingList[i].minValue

                    ADL_Main_Memory_Free(lppInitSettingList)

                    for cls in _get_overdrive_8(
                            context,
                            iAdapterIndex,
                            initSetting,
                            [OD8_POWER_GAUGE, ADL_OD8_POWER_GAUGE]
                    ):
                        value = ZeroFanControl(cls.current)
                        value._obj = cls
                        value._adapter_index = self._adapter_index
                        value._level = cls.level
                        self._power_threshold.append(value)

        return iter(self._power_threshold)

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
    def memory_timings(self):
        return MemoryTimings(self._adapter_index)

    @property
    def fan_speeds(self):
        return FanSpeeds(self._adapter_index)

