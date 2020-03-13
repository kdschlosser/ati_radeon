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
    'OverDrive8'
)


from .adl_sdk_h import ADL2_Main_Control_Create  # NOQA


class ValueWrapper(int):

    def __init__(self, value=None):
        if value is None:
            super(ValueWrapper, self).__init__(self)
        else:
            try:
                super(ValueWrapper, self).__init__(value)
            except TypeError:
                super(ValueWrapper, self).__init__()

        self.__obj = None

    def _set_object(self, obj):
        self.__obj = obj

    @property
    def min(self):
        return self.__obj.minValue.value

    @property
    def max(self):
        return self.__obj.maxValue.value

    @property
    def default(self):
        return self.__obj.defaultValue.value


def _get_value(item_id, feature_id, odInitSetting, odCurrentSetting):
    if item_id in (
        OD8_GFXCLK_FMIN,
        OD8_GFXCLK_FMAX,
        OD8_UCLK_FMAX,
        OD8_AC_TIMING,
        OD8_FAN_ZERORPM_CONTROL,
        OD8_AUTO_UV_ENGINE_CONTROL,
        OD8_AUTO_OC_ENGINE_CONTROL,
        OD8_AUTO_OC_MEMORY_CONTROL
    ):
        visible = True
    else:
        visible = odInitSetting.overdrive8Capabilities & feature_id == feature_id

    if visible:
        res = ValueWrapper(odCurrentSetting.Od8SettingTable[item_id].value)
        res._set_object(odInitSetting.od8SettingTable[item_id])
        return res


class OverDrive8(object):
    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def _current_settings(self):
        iAdapterIndex = INT(self._adapter_index)
        odCurrentSetting = ADLOD8CurrentSetting()
        ctypes.memset(ctypes.byref(odCurrentSetting), 0, ctypes.sizeof(ADLOD8CurrentSetting))

        odCurrentSetting.count = OD8_COUNT

        numberOfFeaturesCurrent = INT(OD8_COUNT)
        lpCurrentSettingList = (INT * OD8_COUNT)()
        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive8_Current_SettingX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(numberOfFeaturesCurrent),
                    ctypes.byref(lpCurrentSettingList)
            ) == ADL_OK:
                if numberOfFeaturesCurrent.value > OD8_COUNT:
                    odCurrentSetting.count = OD8_COUNT
                else:
                    odCurrentSetting.count = numberOfFeaturesCurrent

                for i in range(odCurrentSetting.count.value):
                    odCurrentSetting.Od8SettingTable[i] = lpCurrentSettingList[i]

                return odCurrentSetting

    @property
    def _init_settings(self):
        iAdapterIndex = INT(self._adapter_index)

        odInitSetting = ADLOD8InitSetting()
        ctypes.memset(ctypes.byref(odInitSetting), 0, ctypes.sizeof(ADLOD8InitSetting))

        odInitSetting.count = OD8_COUNT
        overdrive8Capabilities = INT()
        numberOfFeatures = INT(OD8_COUNT)
        lpInitSettingList = (ADLOD8SingleInitSetting * OD8_COUNT)()

        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive8_Init_SettingX2_Get(
                context,
                iAdapterIndex,
                ctypes.byref(overdrive8Capabilities),
                ctypes.byref(numberOfFeatures),
                ctypes.byref(lpInitSettingList)
            ) == ADL_OK:
                if numberOfFeatures.value > OD8_COUNT:
                    odInitSetting.count = OD8_COUNT
                else:
                    odInitSetting.count = numberOfFeatures

                odInitSetting.overdrive8Capabilities = overdrive8Capabilities

                for i in range(odInitSetting.count.value):
                    odInitSetting.od8SettingTable[i].defaultValue = lpInitSettingList[i].defaultValue.value
                    odInitSetting.od8SettingTable[i].featureID = lpInitSettingList[i].featureID.value
                    odInitSetting.od8SettingTable[i].maxValue = lpInitSettingList[i].maxValue.value
                    odInitSetting.od8SettingTable[i].minValue = lpInitSettingList[i].minValue.value

                return odInitSetting

    @property
    def _pm_log(self):
        iAdapterIndex = INT(self._adapter_index)
        odlpDataOutput = ADLPMLogDataOutput()
        ctypes.memset(ctypes.byref(odlpDataOutput), 0, ctypes.sizeof(ADLPMLogDataOutput))

        with ADL2_Main_Control_Create as context:
            if _ADL2_New_QueryPMLogData_Get(
                context,
                iAdapterIndex,
                ctypes.byref(odlpDataOutput)
            ) == ADL_OK:
                return odlpDataOutput

    @property
    def is_gfx_clock_limits_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_GFXCLK_LIMITS == ADL_OD8_GFXCLK_LIMITS

    @property
    def is_gfx_clock_curve_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_GFXCLK_CURVE == ADL_OD8_GFXCLK_CURVE

    @property
    def is_memory_clock_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_UCLK_MAX == ADL_OD8_UCLK_MAX

    @property
    def is_power_percentage_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_POWER_LIMIT == ADL_OD8_POWER_LIMIT

    @property
    def is_fan_acoustic_limit_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_ACOUSTIC_LIMIT_SCLK == ADL_OD8_ACOUSTIC_LIMIT_SCLK

    @property
    def is_minimum_fan_speed_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_FAN_SPEED_MIN == ADL_OD8_FAN_SPEED_MIN

    @property
    def is_fan_target_temperature_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_TEMPERATURE_FAN == ADL_OD8_TEMPERATURE_FAN

    @property
    def is_system_temperature_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_TEMPERATURE_SYSTEM == ADL_OD8_TEMPERATURE_SYSTEM

    @property
    def is_ac_timing_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_MEMORY_TIMING_TUNE == ADL_OD8_MEMORY_TIMING_TUNE

    @property
    def is_zero_rpm_fan_control_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_FAN_ZERO_RPM_CONTROL == ADL_OD8_FAN_ZERO_RPM_CONTROL

    @property
    def is_auto_uv_engine_control_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_AUTO_UV_ENGINE == ADL_OD8_AUTO_UV_ENGINE

    @property
    def is_auto_oc_engine_control_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_AUTO_OC_ENGINE == ADL_OD8_AUTO_OC_ENGINE

    @property
    def is_auto_oc_memory_control_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_AUTO_OC_MEMORY == ADL_OD8_AUTO_OC_MEMORY

    @property
    def is_fan_curve_supported(self):
        odInitSetting = self._init_settings
        return odInitSetting.overdrive8Capabilities.value & ADL_OD8_FAN_CURVE == ADL_OD8_FAN_CURVE

    @property
    def gfx_clock_frequency_1(self):
        if self.is_gfx_clock_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_GFXCLK_FREQ1, ADL_OD8_GFXCLK_CURVE, odInitSetting, odCurrentSetting)

    @gfx_clock_frequency_1.setter
    def gfx_clock_frequency_1(self, value):
        if self.is_gfx_clock_curve_supported:
            self.__set(OD8_GFXCLK_FREQ1, value)

    @property
    def gfx_clock_frequency_2(self):
        if self.is_gfx_clock_curve_supported or self.is_gfx_clock_limits_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_GFXCLK_FREQ2, ADL_OD8_GFXCLK_CURVE, odInitSetting, odCurrentSetting)

    @gfx_clock_frequency_2.setter
    def gfx_clock_frequency_2(self, value):
        if self.is_gfx_clock_curve_supported or self.is_gfx_clock_limits_supported:
            self.__set(OD8_GFXCLK_FREQ2, value)

    @property
    def gfx_clock_frequency_3(self):
        if self.is_gfx_clock_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_GFXCLK_FREQ3, ADL_OD8_GFXCLK_CURVE, odInitSetting, odCurrentSetting)

    @gfx_clock_frequency_3.setter
    def gfx_clock_frequency_3(self, value):
        if self.is_gfx_clock_curve_supported:
            self.__set(OD8_GFXCLK_FREQ3, value)

    @property
    def gfx_clock_f_min(self):
        if self.is_gfx_clock_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_GFXCLK_FMIN, ADL_OD8_GFXCLK_CURVE, odInitSetting, odCurrentSetting)

    @gfx_clock_f_min.setter
    def gfx_clock_f_min(self, value):
        if self.is_gfx_clock_curve_supported:
            self.__set(OD8_GFXCLK_FMIN, value)

    @property
    def gfx_clock_f_max(self):
        if self.is_gfx_clock_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_GFXCLK_FMAX, ADL_OD8_GFXCLK_CURVE, odInitSetting, odCurrentSetting)

    @gfx_clock_f_max.setter
    def gfx_clock_f_max(self, value):
        if self.is_gfx_clock_curve_supported:
            self.__set(OD8_GFXCLK_FMAX, value)

    @property
    def is_gfx_clock_sensor_supported(self):
        odlpDataOutput = self._pm_log
        return bool(odlpDataOutput.sensors[PMLOG_CLK_GFXCLK].supported.value)

    @property
    def gfx_clock_sensor(self):
        odlpDataOutput = self._pm_log

        if odlpDataOutput.sensors[PMLOG_CLK_GFXCLK].supported.value:
            return odlpDataOutput.sensors[PMLOG_CLK_GFXCLK].value.value

    @property
    def gfx_clock_voltage_1(self):
        if self.is_gfx_clock_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_GFXCLK_VOLTAGE1, ADL_OD8_GFXCLK_CURVE, odInitSetting, odCurrentSetting)

    @gfx_clock_voltage_1.setter
    def gfx_clock_voltage_1(self, value):
        if self.is_gfx_clock_curve_supported:
            self.__set(OD8_GFXCLK_VOLTAGE1, value)

    @property
    def gfx_clock_voltage_2(self):
        if self.is_gfx_clock_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_GFXCLK_VOLTAGE2, ADL_OD8_GFXCLK_CURVE, odInitSetting, odCurrentSetting)

    @gfx_clock_voltage_2.setter
    def gfx_clock_voltage_2(self, value):
        if self.is_gfx_clock_curve_supported:
            self.__set(OD8_GFXCLK_VOLTAGE2, value)

    @property
    def gfx_clock_voltage_3(self):
        if self.is_gfx_clock_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_GFXCLK_VOLTAGE3, ADL_OD8_GFXCLK_CURVE, odInitSetting, odCurrentSetting)

    @gfx_clock_voltage_3.setter
    def gfx_clock_voltage_3(self, value):
        if self.is_gfx_clock_curve_supported:
            self.__set(OD8_GFXCLK_VOLTAGE3, value)

    @property
    def memory_clock(self):

        if self.is_memory_clock_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_UCLK_FMAX, ADL_OD8_UCLK_MAX, odInitSetting, odCurrentSetting)

    @memory_clock.setter
    def memory_clock(self, value):

        if self.is_memory_clock_supported:
            self.__set(OD8_UCLK_FMAX, value)

    @property
    def is_memory_clock_sensor_supported(self):
        odlpDataOutput = self._pm_log
        return bool(odlpDataOutput.sensors[PMLOG_CLK_MEMCLK].supported.value)

    @property
    def memory_clock_sensor(self):
        odlpDataOutput = self._pm_log

        if odlpDataOutput.sensors[PMLOG_CLK_MEMCLK].supported.value:
            return odlpDataOutput.sensors[PMLOG_CLK_MEMCLK].value.value

    @property
    def system_temperature(self):
        if self.is_system_temperature_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_OPERATING_TEMP_MAX, ADL_OD8_TEMPERATURE_SYSTEM, odInitSetting, odCurrentSetting)

    @system_temperature.setter
    def system_temperature(self, value):
        if self.is_system_temperature_supported:
            self.__set(OD8_OPERATING_TEMP_MAX, value)

    @property
    def fan_target_temperature(self):
        if self.is_fan_target_temperature_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_TARGET_TEMP, ADL_OD8_TEMPERATURE_FAN, odInitSetting, odCurrentSetting)

    @fan_target_temperature.setter
    def fan_target_temperature(self, value):
        if self.is_fan_target_temperature_supported:
            self.__set(OD8_FAN_TARGET_TEMP, value)

    @property
    def power_percentage(self):
        if self.is_power_percentage_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_POWER_PERCENTAGE, ADL_OD8_POWER_LIMIT, odInitSetting, odCurrentSetting)

    @power_percentage.setter
    def power_percentage(self, value):
        if self.is_power_percentage_supported:
            self.__set(OD8_POWER_PERCENTAGE, value)

    @property
    def is_temperature_edge_sensor_supported(self):
        odlpDataOutput = self._pm_log
        return bool(odlpDataOutput.sensors[PMLOG_TEMPERATURE_EDGE].supported.value)

    @property
    def temperature_edge_sensor(self):
        odlpDataOutput = self._pm_log

        if odlpDataOutput.sensors[PMLOG_TEMPERATURE_EDGE].supported.value:
            return odlpDataOutput.sensors[PMLOG_TEMPERATURE_EDGE].value.value

    @property
    def is_temperature_hotspot_sensor_supported(self):
        odlpDataOutput = self._pm_log
        return bool(odlpDataOutput.sensors[PMLOG_TEMPERATURE_HOTSPOT].supported.value)

    @property
    def temperature_hotspot_sensor(self):
        odlpDataOutput = self._pm_log

        if odlpDataOutput.sensors[PMLOG_TEMPERATURE_HOTSPOT].supported.value:
            return odlpDataOutput.sensors[PMLOG_TEMPERATURE_HOTSPOT].value.value

    @property
    def minimum_fan_speed(self):
        if self.is_minimum_fan_speed_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_MIN_SPEED, ADL_OD8_FAN_SPEED_MIN, odInitSetting, odCurrentSetting)

    @minimum_fan_speed.setter
    def minimum_fan_speed(self, value):
        if self.is_minimum_fan_speed_supported:
            self.__set(OD8_FAN_MIN_SPEED, value)

    @property
    def fan_acoustic_limit(self):
        if self.is_fan_acoustic_limit_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_ACOUSTIC_LIMIT, ADL_OD8_ACOUSTIC_LIMIT_SCLK, odInitSetting, odCurrentSetting)

    @fan_acoustic_limit.setter
    def fan_acoustic_limit(self, value):
        if self.is_fan_acoustic_limit_supported:
            self.__set(OD8_FAN_ACOUSTIC_LIMIT, value)

    @property
    def is_fan_rpm_sensor_supported(self):
        odlpDataOutput = self._pm_log
        return bool(odlpDataOutput.sensors[PMLOG_FAN_RPM].supported.value)

    @property
    def fan_rpm_sensor(self):
        odlpDataOutput = self._pm_log

        if odlpDataOutput.sensors[PMLOG_FAN_RPM].supported.value:
            return odlpDataOutput.sensors[PMLOG_FAN_RPM].value.value

    @property
    def ac_timing(self):
        if self.is_ac_timing_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_AC_TIMING, ADL_OD8_MEMORY_TIMING_TUNE, odInitSetting, odCurrentSetting)

    @ac_timing.setter
    def ac_timing(self, value):
        if self.is_ac_timing_supported:
            self.__set(OD8_AC_TIMING, value)

    @property
    def zero_rpm_fan_control(self):
        if self.is_zero_rpm_fan_control_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_ZERORPM_CONTROL, ADL_OD8_FAN_ZERO_RPM_CONTROL, odInitSetting, odCurrentSetting)

    @zero_rpm_fan_control.setter
    def zero_rpm_fan_control(self, value):
        if self.is_zero_rpm_fan_control_supported:
            self.__set(OD8_FAN_ZERORPM_CONTROL, value)

    @property
    def auto_uv_engine_control(self):
        if self.is_auto_uv_engine_control_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_AUTO_UV_ENGINE_CONTROL, ADL_OD8_AUTO_UV_ENGINE, odInitSetting, odCurrentSetting)

    @auto_uv_engine_control.setter
    def auto_uv_engine_control(self, value):
        if self.is_auto_uv_engine_control_supported:
            self.__set(OD8_AUTO_UV_ENGINE_CONTROL, value)

    @property
    def auto_oc_engine_control(self):
        if self.is_auto_oc_engine_control_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_AUTO_OC_ENGINE_CONTROL, ADL_OD8_AUTO_OC_ENGINE, odInitSetting, odCurrentSetting)

    @auto_oc_engine_control.setter
    def auto_oc_engine_control(self, value):
        if self.is_auto_oc_engine_control_supported:
            self.__set(OD8_AUTO_OC_ENGINE_CONTROL, value)

    @property
    def auto_oc_memory_control(self):
        if self.is_auto_oc_memory_control_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_AUTO_OC_MEMORY_CONTROL, ADL_OD8_AUTO_OC_MEMORY, odInitSetting, odCurrentSetting)

    @auto_oc_memory_control.setter
    def auto_oc_memory_control(self, value):
        if self.is_auto_oc_memory_control_supported:
            self.__set(OD8_AUTO_OC_MEMORY_CONTROL, value)

    @property
    def fan_curve_temperature_1(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_TEMPERATURE_1, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_temperature_1.setter
    def fan_curve_temperature_1(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_TEMPERATURE_1, value)

    @property
    def fan_curve_speed_1(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_SPEED_1, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_speed_1.setter
    def fan_curve_speed_1(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_SPEED_1, value)

    @property
    def fan_curve_temperature_2(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_TEMPERATURE_2, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_temperature_2.setter
    def fan_curve_temperature_2(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_TEMPERATURE_2, value)

    @property
    def fan_curve_speed_2(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_SPEED_2, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_speed_2.setter
    def fan_curve_speed_2(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_SPEED_2, value)

    @property
    def fan_curve_temperature_3(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_TEMPERATURE_3, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_temperature_3.setter
    def fan_curve_temperature_3(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_TEMPERATURE_3, value)

    @property
    def fan_curve_speed_3(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_SPEED_3, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_speed_3.setter
    def fan_curve_speed_3(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_SPEED_3, value)

    @property
    def fan_curve_temperature_4(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_TEMPERATURE_4, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_temperature_4.setter
    def fan_curve_temperature_4(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_TEMPERATURE_4, value)

    @property
    def fan_curve_speed_4(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_SPEED_4, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_speed_4.setter
    def fan_curve_speed_4(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_SPEED_4, value)

    @property
    def fan_curve_temperature_5(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_TEMPERATURE_5, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_temperature_5.setter
    def fan_curve_temperature_5(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_TEMPERATURE_5, value)

    @property
    def fan_curve_speed_5(self):
        if self.is_fan_curve_supported:
            odCurrentSetting = self._current_settings
            odInitSetting = self._init_settings

            return _get_value(OD8_FAN_CURVE_SPEED_5, ADL_OD8_FAN_CURVE, odInitSetting, odCurrentSetting)

    @fan_curve_speed_5.setter
    def fan_curve_speed_5(self, value):
        if self.is_fan_curve_supported:
            self.__set(OD8_FAN_CURVE_SPEED_5, value)

    def __set(self, setting_id, value):
        iAdapterIndex = INT(self._adapter_index)
        odCurrentSetting = self._current_settings
        odInitSetting = self._init_settings

        odSetSetting = ADLOD8SetSetting()
        ctypes.memset(ctypes.byref(odSetSetting), 0, ctypes.sizeof(ADLOD8SetSetting))
        odSetSetting.count = OD8_COUNT
        for i in range(OD8_GFXCLK_FREQ1, OD8_UCLK_FMAX):
            odSetSetting.od8SettingTable[i].requested = 1
            odSetSetting.od8SettingTable[i].value = odCurrentSetting.Od8SettingTable[i]

        if OD8_FAN_CURVE_SPEED_5 >= setting_id >= OD8_FAN_CURVE_TEMPERATURE_1:
            reset = False
        else:
            reset = True

        for i in range(OD8_FAN_CURVE_TEMPERATURE_1, OD8_FAN_CURVE_SPEED_5):
            odSetSetting.od8SettingTable[i].reset = reset
            odSetSetting.od8SettingTable[i].requested = 1
            odSetSetting.od8SettingTable[i].value = odCurrentSetting.Od8SettingTable[i]

        odSetSetting.od8SettingTable[setting_id].requested = 1

        if odInitSetting.od8SettingTable[setting_id].minValue.value > value:
            return False

        if odInitSetting.od8SettingTable[setting_id].maxValue.value < value:
            return False

        odSetSetting.od8SettingTable[setting_id].value = value
        if OD8_GFXCLK_FMAX == setting_id:
            odSetSetting.od8SettingTable[OD8_GFXCLK_FREQ3].value = value
        elif OD8_GFXCLK_FMIN == setting_id:
            odSetSetting.od8SettingTable[OD8_GFXCLK_FREQ1].value = value

        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive8_Setting_Set(
                    context,
                    iAdapterIndex,
                    ctypes.byref(odSetSetting),
                    ctypes.byref(odCurrentSetting)
            ) == ADL_OK:
                return True

        return False
