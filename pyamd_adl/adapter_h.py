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


ADL2_ADAPTER_ACTIVE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_ACTIVE_GET = _int(
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_ASPECTS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(CHAR),
    INT
)
ADL_ADAPTER_ASPECTS_GET = _int(
    INT,
    POINTER(CHAR),
    INT
)
ADL2_ADAPTER_NUMBEROFADAPTERS_GET = _int(
    ADL_CONTEXT_HANDLE,
    POINTER(INT)
)
ADL_ADAPTER_NUMBEROFADAPTERS_GET = _int(
    POINTER(INT)
)
ADL2_FLUSH_DRIVER_DATA = _int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_FLUSH_DRIVER_DATA = _int(
    INT
)
ADL2_ADAPTER_ADAPTERINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    LPAdapterInfo,
    INT
)
ADL_ADAPTER_ADAPTERINFO_GET = _int(
    LPAdapterInfo,
    INT
)
ADL2_ADAPTER_ADAPTERINFOX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    POINTER(POINTER(AdapterInfo))
)
ADL_ADAPTER_ADAPTERINFOX2_GET = _int(
    POINTER(POINTER(AdapterInfo))
)
ADL2_ADAPTER_REGVALUESTRING_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(CHAR),
    POINTER(CHAR),
    INT,
    POINTER(CHAR)
)
ADL_ADAPTER_REGVALUESTRING_GET = _int(
    INT,
    INT,
    POINTER(CHAR),
    POINTER(CHAR),
    INT,
    POINTER(CHAR)
)
ADL2_ADAPTER_REGVALUESTRING_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(CHAR),
    POINTER(CHAR),
    INT,
    POINTER(CHAR)
)
ADL_ADAPTER_REGVALUESTRING_SET = _int(
    INT,
    INT,
    POINTER(CHAR),
    POINTER(CHAR),
    INT,
    POINTER(CHAR)
)
ADL2_ADAPTER_ASICFAMILYTYPE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_ASICFAMILYTYPE_GET = _int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_SPEED_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_SPEED_CAPS = _int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_SPEED_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_SPEED_GET = _int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_SPEED_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_ADAPTER_SPEED_SET = _int(
    INT,
    INT
)
ADL2_ADAPTER_ACCESSIBILITY_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_ACCESSIBILITY_GET = _int(
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_VIDEOBIOSINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLBiosInfo)
)
ADL_ADAPTER_VIDEOBIOSINFO_GET = _int(
    INT,
    POINTER(ADLBiosInfo)
)
ADL2_ADAPTER_ID_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_ID_GET = _int(
    INT,
    POINTER(INT)
)
ADL2_ADAPTERX2_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLAdapterCapsX2)
)
ADL_ADAPTERX2_CAPS = _int(
    INT,
    POINTER(ADLAdapterCapsX2)
)
ADL2_ADAPTER_CROSSFIRE_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLCrossfireComb))
)
ADL_ADAPTER_CROSSFIRE_CAPS = _int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLCrossfireComb))
)
ADL2_ADAPTER_CROSSFIRE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLCrossfireComb),
    POINTER(ADLCrossfireInfo)
)
ADL_ADAPTER_CROSSFIRE_GET = _int(
    INT,
    POINTER(ADLCrossfireComb),
    POINTER(ADLCrossfireInfo)
)
ADL2_ADAPTER_CROSSFIRE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLCrossfireComb)
)
ADL_ADAPTER_CROSSFIRE_SET = _int(
    INT,
    POINTER(ADLCrossfireComb)
)
ADL2_ADAPTER_MVPU_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL2_ADAPTER_MEMORYINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLMemoryInfo)
)
ADL_ADAPTER_MEMORYINFO_GET = _int(
    INT,
    POINTER(ADLMemoryInfo)
)
ADL2_ADAPTER_CONFIGMEMORY_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT,
    INT,
    POINTER(ADLMemoryDisplayFeatures),
    POINTER(INT),
    POINTER(POINTER(ADLMemoryRequired))
)
ADL_ADAPTER_CONFIGMEMORY_GET = _int(
    INT,
    INT,
    INT,
    INT,
    INT,
    POINTER(ADLMemoryDisplayFeatures),
    POINTER(INT),
    POINTER(POINTER(ADLMemoryRequired))
)
ADL2_ADAPTER_OBSERVEDCLOCKINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_OBSERVEDCLOCKINFO_GET = _int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_BOARDLAYOUT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLBracketSlotInfo)),
    POINTER(INT),
    POINTER(POINTER(ADLConnectorInfo))
)
ADL_ADAPTER_BOARDLAYOUT_GET = _int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLBracketSlotInfo)),
    POINTER(INT),
    POINTER(POINTER(ADLConnectorInfo))
)
ADL2_ADAPTER_SUPPORTEDCONNECTIONS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    POINTER(ADLSupportedConnections)
)
ADL_ADAPTER_SUPPORTEDCONNECTIONS_GET = _int(
    INT,
    ADLDevicePort,
    POINTER(ADLSupportedConnections)
)
ADL2_ADAPTER_CONNECTIONSTATE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    POINTER(ADLConnectionState)
)
ADL_ADAPTER_CONNECTIONSTATE_GET = _int(
    INT,
    ADLDevicePort,
    POINTER(ADLConnectionState)
)
ADL2_ADAPTER_EMULATIONMODE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    INT
)
ADL_ADAPTER_EMULATIONMODE_SET = _int(
    INT,
    ADLDevicePort,
    INT
)
ADL2_ADAPTER_CONNECTIONDATA_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    ADLConnectionData
)
ADL_ADAPTER_CONNECTIONDATA_SET = _int(
    INT,
    ADLDevicePort,
    ADLConnectionData
)
ADL2_ADAPTER_CONNECTIONDATA_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    INT,
    POINTER(ADLConnectionData)
)
ADL_ADAPTER_CONNECTIONDATA_GET = _int(
    INT,
    ADLDevicePort,
    INT,
    POINTER(ADLConnectionData)
)
ADL2_ADAPTER_CONNECTIONDATA_REMOVE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort
)
ADL_ADAPTER_CONNECTIONDATA_REMOVE = _int(
    INT,
    ADLDevicePort
)
ADL2_ADAPTER_EDIDMANAGEMENT_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_EDIDMANAGEMENT_CAPS = _int(
    INT,
    POINTER(INT)
)
ADL2_WORKSTATION_GLOBALEDIDPERSISTENCE_GET = _int(
    ADL_CONTEXT_HANDLE,
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_GLOBALEDIDPERSISTENCE_GET = _int(
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_GLOBALEDIDPERSISTENCE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_WORKSTATION_GLOBALEDIDPERSISTENCE_SET = _int(
    INT
)
ADL2_FPS_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_FPS_SETTINGS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLFPSSettingsOutput)
)
ADL2_FPS_SETTINGS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLFPSSettingsInput
)
ADL2_FPS_SETTINGS_RESET = _int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL2_RIS_SETTINGS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADL_RIS_SETTINGS,
    ADL_RIS_NOTFICATION_REASON
)
ADL2_RIS_SETTINGS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADL_RIS_SETTINGS)
)
ADL2_CHILL_SETTINGSX2_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADL_CHILL_SETTINGS,
    ADL_CHILL_NOTFICATION_REASON,
    POINTER(ADL_ERROR_REASON)
)
ADL2_CHILL_SETTINGSX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADL_CHILL_SETTINGS)
)
ADL2_DELAG_SETTINGS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADL_DELAG_SETTINGS,
    ADL_DELAG_NOTFICATION_REASON,
    POINTER(ADL_ERROR_REASON)
)
ADL2_DELAG_SETTINGS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADL_DELAG_SETTINGS)
)
ADL2_BOOST_SETTINGS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADL_BOOST_SETTINGS,
    ADL_BOOST_NOTFICATION_REASON,
    POINTER(ADL_ERROR_REASON)
)
ADL2_BOOST_SETTINGS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADL_BOOST_SETTINGS)
)
ADL2_ADAPTER_CLOCKINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLClockInfo)
)
ADL_ADAPTER_CLOCKINFO_GET = _int(
    INT,
    POINTER(ADLClockInfo)
)
ADL2_DISPLAY_ADAPTERID_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_ADAPTERID_GET = _int(
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_EDC_ERRORRECORDS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(ADLErrorRecord)
)
ADL2_ADAPTER_EDC_ERRORINJECTION_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLErrorInjection)
)
ADL2_ADAPTER_GRAPHIC_CORE_INFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLGraphicCoreInfo)
)
ADL2_ADAPTER_PMLOG_SUPPORT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPMLogSupportInfo)
)
ADL2_ADAPTER_PMLOG_START = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPMLogStartInput),
    POINTER(ADLPMLogStartOutput),
    ADL_D3DKMT_HANDLE
)
ADL2_ADAPTER_PMLOG_STOP = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADL_D3DKMT_HANDLE
)


# Function to determine if the adapter is active or not.
_ADL2_Adapter_Active_Get = ADL2_ADAPTER_ACTIVE_GET

# Function to determine if the adapter is active or not.
_ADL_Adapter_Active_Get = ADL_ADAPTER_ACTIVE_GET

# ADL local interface. Function to retrieve the supported aspects list.
_ADL2_Adapter_Aspects_Get = ADL2_ADAPTER_ASPECTS_GET

# ADL local interface. Function to retrieve the supported aspects list.
_ADL_Adapter_Aspects_Get = ADL_ADAPTER_ASPECTS_GET

# Function to retrieve the number of OS-known adapters.
_ADL2_Adapter_NumberOfAdapters_Get = ADL2_ADAPTER_NUMBEROFADAPTERS_GET

# Function to retrieve the number of OS-known adapters.
_ADL_Adapter_NumberOfAdapters_Get = ADL_ADAPTER_NUMBEROFADAPTERS_GET

# Function to save driver data.
_ADL2_Flush_Driver_Data = ADL2_FLUSH_DRIVER_DATA

# Function to save driver data.
_ADL_Flush_Driver_Data = ADL_FLUSH_DRIVER_DATA

# Retrieves all OS-known adapter information.
_ADL2_Adapter_AdapterInfo_Get = ADL2_ADAPTER_ADAPTERINFO_GET

# Retrieves all OS-known adapter information.
_ADL_Adapter_AdapterInfo_Get = ADL_ADAPTER_ADAPTERINFO_GET

# Retrieves all OS-known adapter information.
_ADL2_Adapter_AdapterInfoX2_Get = ADL2_ADAPTER_ADAPTERINFOX2_GET

# Retrieves all OS-known adapter information.
_ADL_Adapter_AdapterInfoX2_Get = ADL_ADAPTER_ADAPTERINFOX2_GET

# ADL local interface. Function to query a string registry value set by driver.
_ADL2_Adapter_RegValueString_Get = ADL2_ADAPTER_REGVALUESTRING_GET

# ADL local interface. Function to query a string registry value set by driver.
_ADL_Adapter_RegValueString_Get = ADL_ADAPTER_REGVALUESTRING_GET

# ADL local interface. Function to set a driver registry string value.
_ADL2_Adapter_RegValueString_Set = ADL2_ADAPTER_REGVALUESTRING_SET

# ADL local interface. Function to set a driver registry string value.
_ADL_Adapter_RegValueString_Set = ADL_ADAPTER_REGVALUESTRING_SET

# Function to get the ASICFamilyType from the adapter.
_ADL2_Adapter_ASICFamilyType_Get = ADL2_ADAPTER_ASICFAMILYTYPE_GET

# Function to get the ASICFamilyType from the adapter.
_ADL_Adapter_ASICFamilyType_Get = ADL_ADAPTER_ASICFAMILYTYPE_GET

# Function to get the current Force3DClock setting from the adapter.
_ADL2_Adapter_Speed_Caps = ADL2_ADAPTER_SPEED_CAPS

# Function to get the current Force3DClock setting from the adapter.
_ADL_Adapter_Speed_Caps = ADL_ADAPTER_SPEED_CAPS

# Function to get the current Speed setting from the adapter.
_ADL2_Adapter_Speed_Get = ADL2_ADAPTER_SPEED_GET

# Function to get the current Speed setting from the adapter.
_ADL_Adapter_Speed_Get = ADL_ADAPTER_SPEED_GET

# Function to set the current Speed setting from the adapter.
_ADL2_Adapter_Speed_Set = ADL2_ADAPTER_SPEED_SET

# Function to set the current Speed setting from the adapter.
_ADL_Adapter_Speed_Set = ADL_ADAPTER_SPEED_SET

# Function to check if the GPU is accessible or not at the time of this call.
_ADL2_Adapter_Accessibility_Get = ADL2_ADAPTER_ACCESSIBILITY_GET

# Function to check if the GPU is accessible or not at the time of this call.
_ADL_Adapter_Accessibility_Get = ADL_ADAPTER_ACCESSIBILITY_GET

# ADL local interface. Function to retrieve BIOS information.
_ADL2_Adapter_VideoBiosInfo_Get = ADL2_ADAPTER_VIDEOBIOSINFO_GET

# ADL local interface. Function to retrieve BIOS information.
_ADL_Adapter_VideoBiosInfo_Get = ADL_ADAPTER_VIDEOBIOSINFO_GET

# Function to get the unique identifier of an adapter.
_ADL2_Adapter_ID_Get = ADL2_ADAPTER_ID_GET

# Function to get the unique identifier of an adapter.
_ADL_Adapter_ID_Get = ADL_ADAPTER_ID_GET

# Function to retrieve adapter caps information.
_ADL2_AdapterX2_Caps = ADL2_ADAPTERX2_CAPS

# Function to retrieve adapter caps information.
_ADL_AdapterX2_Caps = ADL_ADAPTERX2_CAPS

# Function to retrieve CrossfireX capabilities of the system.
_ADL2_Adapter_Crossfire_Caps = ADL2_ADAPTER_CROSSFIRE_CAPS

# Function to retrieve CrossfireX capabilities of the system.
_ADL_Adapter_Crossfire_Caps = ADL_ADAPTER_CROSSFIRE_CAPS

# Function to get current CrossfireX combination settings.
_ADL2_Adapter_Crossfire_Get = ADL2_ADAPTER_CROSSFIRE_GET

# Function to get current CrossfireX combination settings.
_ADL_Adapter_Crossfire_Get = ADL_ADAPTER_CROSSFIRE_GET

# Function to set CrossfireX combination settings.
_ADL2_Adapter_Crossfire_Set = ADL2_ADAPTER_CROSSFIRE_SET

# Function to set CrossfireX combination settings.
_ADL_Adapter_Crossfire_Set = ADL_ADAPTER_CROSSFIRE_SET

# Function to set CrossfireX status.
_ADL2_Adapter_MVPU_Set = ADL2_ADAPTER_MVPU_SET

# Function to retrieve memory information from the adapter.
_ADL2_Adapter_MemoryInfo_Get = ADL2_ADAPTER_MEMORYINFO_GET

# Function to retrieve memory information from the adapter.
_ADL_Adapter_MemoryInfo_Get = ADL_ADAPTER_MEMORYINFO_GET

# Function to get the memory configuration of an adapter.
_ADL2_Adapter_ConfigMemory_Get = ADL2_ADAPTER_CONFIGMEMORY_GET

# Function to get the memory configuration of an adapter.
_ADL_Adapter_ConfigMemory_Get = ADL_ADAPTER_CONFIGMEMORY_GET

# Function to get the core and memory clock info of an adapter.
# This is the clock displayed on CCC information center.
# Specific logic is used to select appropriate clock for display in current configuration.
_ADL2_Adapter_ObservedClockInfo_Get = ADL2_ADAPTER_OBSERVEDCLOCKINFO_GET

# Function to get the core and memory clock info of an adapter.
# This is the clock displayed on CCC information center.
# Specific logic is used to select appropriate clock for display in current configuration.
_ADL_Adapter_ObservedClockInfo_Get = ADL_ADAPTER_OBSERVEDCLOCKINFO_GET

# Function to get the board layout information.
_ADL2_Adapter_BoardLayout_Get = ADL2_ADAPTER_BOARDLAYOUT_GET

# Function to get the board layout information.
_ADL_Adapter_BoardLayout_Get = ADL_ADAPTER_BOARDLAYOUT_GET

# Function to get the supported connection types of given connector.
_ADL2_Adapter_SupportedConnections_Get = ADL2_ADAPTER_SUPPORTEDCONNECTIONS_GET

# Function to get the supported connection types of given connector.
_ADL_Adapter_SupportedConnections_Get = ADL_ADAPTER_SUPPORTEDCONNECTIONS_GET

# Function to get the current emulation state of a given connector.
_ADL2_Adapter_ConnectionState_Get = ADL2_ADAPTER_CONNECTIONSTATE_GET

# Function to get the current emulation state of a given connector.
_ADL_Adapter_ConnectionState_Get = ADL_ADAPTER_CONNECTIONSTATE_GET

# Function to sets the emulation mode of given connector.
_ADL2_Adapter_EmulationMode_Set = ADL2_ADAPTER_EMULATIONMODE_SET

# Function to sets the emulation mode of given connector.
_ADL_Adapter_EmulationMode_Set = ADL_ADAPTER_EMULATIONMODE_SET

# Function to set the emulation data to on specified connector.
_ADL2_Adapter_ConnectionData_Set = ADL2_ADAPTER_CONNECTIONDATA_SET

# Function to set the emulation data to on specified connector.
_ADL_Adapter_ConnectionData_Set = ADL_ADAPTER_CONNECTIONDATA_SET

# Function to gets the emulation data on specified connector.
_ADL2_Adapter_ConnectionData_Get = ADL2_ADAPTER_CONNECTIONDATA_GET

# Function to gets the emulation data on specified connector.
_ADL_Adapter_ConnectionData_Get = ADL_ADAPTER_CONNECTIONDATA_GET

# Function to remove emulation on specified connector.
_ADL2_Adapter_ConnectionData_Remove = ADL2_ADAPTER_CONNECTIONDATA_REMOVE

# Function to remove emulation on specified connector.
_ADL_Adapter_ConnectionData_Remove = ADL_ADAPTER_CONNECTIONDATA_REMOVE

# Function to retrieve EDID management feature support.
_ADL2_Adapter_EDIDManagement_Caps = ADL2_ADAPTER_EDIDMANAGEMENT_CAPS

# Function to retrieve EDID management feature support.
_ADL_Adapter_EDIDManagement_Caps = ADL_ADAPTER_EDIDMANAGEMENT_CAPS

# Function to get the EDID Persistence state of the system.
_ADL2_Workstation_GlobalEDIDPersistence_Get = ADL2_WORKSTATION_GLOBALEDIDPERSISTENCE_GET

# Function to get the EDID Persistence state of the system.
_ADL_Workstation_GlobalEDIDPersistence_Get = ADL_WORKSTATION_GLOBALEDIDPERSISTENCE_GET

# Function to set the EDID Persistence state of the system.
_ADL2_Workstation_GlobalEDIDPersistence_Set = ADL2_WORKSTATION_GLOBALEDIDPERSISTENCE_SET

# Function to set the EDID Persistence state of the system.
_ADL_Workstation_GlobalEDIDPersistence_Set = ADL_WORKSTATION_GLOBALEDIDPERSISTENCE_SET

# Function to retrieve FPS Global Setting Capability.
_ADL2_FPS_Caps = ADL2_FPS_CAPS

# Function to retrieve FPS Global Settings.
_ADL2_FPS_Settings_Get = ADL2_FPS_SETTINGS_GET

# Function to update FPS Global Settings.
_ADL2_FPS_Settings_Set = ADL2_FPS_SETTINGS_SET

# Function to reset FPS Global Settings.
_ADL2_FPS_Settings_Reset = ADL2_FPS_SETTINGS_RESET

# Function to set RIS settings This function sets the user input values to
# RIS feature.
_ADL2_RIS_Settings_Set = ADL2_RIS_SETTINGS_SET

# Function to get the RIS settings This function retrieves the RIS settings
# for a specified display adapter.
_ADL2_RIS_Settings_Get = ADL2_RIS_SETTINGS_GET

# Function to set CHILL settings This function sets the user input values
# to CHILL feature.
_ADL2_CHILL_SettingsX2_Set = ADL2_CHILL_SETTINGSX2_SET

# Function to get the CHILL settings This function retrieves the CHILL settings
# for a specified display adapter.
_ADL2_CHILL_SettingsX2_Get = ADL2_CHILL_SETTINGSX2_GET

# Function to set DELAG settings This function sets the user input values to
# DELAG feature.
_ADL2_DELAG_Settings_Set = ADL2_DELAG_SETTINGS_SET

# Function to get the DELAG settings This function retrieves the DELAG settings
# for a specified display adapter.
_ADL2_DELAG_Settings_Get = ADL2_DELAG_SETTINGS_GET

# Function to set BOOST settings This function sets the user input values
# to BOOST feature.
_ADL2_BOOST_Settings_Set = ADL2_BOOST_SETTINGS_SET

# Function to get the BOOST settings This function retrieves the BOOST settings
# for a specified display adapter.
_ADL2_BOOST_Settings_Get = ADL2_BOOST_SETTINGS_GET

# Function to retrieve clock information for an adapter.
_ADL2_Adapter_ClockInfo_Get = ADL2_ADAPTER_CLOCKINFO_GET

# Function to retrieve clock information for an adapter.
_ADL_Adapter_ClockInfo_Get = ADL_ADAPTER_CLOCKINFO_GET

# Function to get the unique identifier of an adapter. Will be removed! Use ADL_Adapter_ID_Get().
_ADL2_Display_AdapterID_Get = ADL2_DISPLAY_ADAPTERID_GET

# Function to get the unique identifier of an adapter. Will be removed! Use ADL_Adapter_ID_Get().
_ADL_Display_AdapterID_Get = ADL_DISPLAY_ADAPTERID_GET

# Function to retrieve Gfx EDC Error Log.
_ADL2_Adapter_EDC_ErrorRecords_Get = ADL2_ADAPTER_EDC_ERRORRECORDS_GET

# Function to inject Gfx EDC Error .
_ADL2_Adapter_EDC_ErrorInjection_Set = ADL2_ADAPTER_EDC_ERRORINJECTION_SET

# Function to retrieve Graphic Core Info.
_ADL2_Adapter_Graphic_Core_Info_Get = ADL2_ADAPTER_GRAPHIC_CORE_INFO_GET

# Function to retrieve power management logging support.
_ADL2_Adapter_PMLog_Support_Get = ADL2_ADAPTER_PMLOG_SUPPORT_GET

# Function to start power management logging.
_ADL2_Adapter_PMLog_Start = ADL2_ADAPTER_PMLOG_START

# Function to stop power management logging.
_ADL2_Adapter_PMLog_Stop = ADL2_ADAPTER_PMLOG_STOP


def Init(hDLL):
    global _ADL2_Adapter_Active_Get
    global _ADL_Adapter_Active_Get
    global _ADL2_Adapter_Aspects_Get
    global _ADL_Adapter_Aspects_Get
    global _ADL2_Adapter_NumberOfAdapters_Get
    global _ADL_Adapter_NumberOfAdapters_Get
    global _ADL2_Flush_Driver_Data
    global _ADL_Flush_Driver_Data
    global _ADL2_Adapter_AdapterInfo_Get
    global _ADL_Adapter_AdapterInfo_Get
    global _ADL2_Adapter_AdapterInfoX2_Get
    global _ADL_Adapter_AdapterInfoX2_Get
    global _ADL2_Adapter_RegValueString_Get
    global _ADL_Adapter_RegValueString_Get
    global _ADL2_Adapter_RegValueString_Set
    global _ADL_Adapter_RegValueString_Set
    global _ADL2_Adapter_ASICFamilyType_Get
    global _ADL_Adapter_ASICFamilyType_Get
    global _ADL2_Adapter_Speed_Caps
    global _ADL_Adapter_Speed_Caps
    global _ADL2_Adapter_Speed_Get
    global _ADL_Adapter_Speed_Get
    global _ADL2_Adapter_Speed_Set
    global _ADL_Adapter_Speed_Set
    global _ADL2_Adapter_Accessibility_Get
    global _ADL_Adapter_Accessibility_Get
    global _ADL2_Adapter_VideoBiosInfo_Get
    global _ADL_Adapter_VideoBiosInfo_Get
    global _ADL2_Adapter_ID_Get
    global _ADL_Adapter_ID_Get
    global _ADL2_AdapterX2_Caps
    global _ADL_AdapterX2_Caps
    global _ADL2_Adapter_Crossfire_Caps
    global _ADL_Adapter_Crossfire_Caps
    global _ADL2_Adapter_Crossfire_Get
    global _ADL_Adapter_Crossfire_Get
    global _ADL2_Adapter_Crossfire_Set
    global _ADL_Adapter_Crossfire_Set
    global _ADL2_Adapter_MVPU_Set
    global _ADL2_Adapter_MemoryInfo_Get
    global _ADL_Adapter_MemoryInfo_Get
    global _ADL2_Adapter_ConfigMemory_Get
    global _ADL_Adapter_ConfigMemory_Get
    global _ADL2_Adapter_ObservedClockInfo_Get
    global _ADL_Adapter_ObservedClockInfo_Get
    global _ADL2_Adapter_BoardLayout_Get
    global _ADL_Adapter_BoardLayout_Get
    global _ADL2_Adapter_SupportedConnections_Get
    global _ADL_Adapter_SupportedConnections_Get
    global _ADL2_Adapter_ConnectionState_Get
    global _ADL_Adapter_ConnectionState_Get
    global _ADL2_Adapter_EmulationMode_Set
    global _ADL_Adapter_EmulationMode_Set
    global _ADL2_Adapter_ConnectionData_Set
    global _ADL_Adapter_ConnectionData_Set
    global _ADL2_Adapter_ConnectionData_Get
    global _ADL_Adapter_ConnectionData_Get
    global _ADL2_Adapter_ConnectionData_Remove
    global _ADL_Adapter_ConnectionData_Remove
    global _ADL2_Adapter_EDIDManagement_Caps
    global _ADL_Adapter_EDIDManagement_Caps
    global _ADL2_Workstation_GlobalEDIDPersistence_Get
    global _ADL_Workstation_GlobalEDIDPersistence_Get
    global _ADL2_Workstation_GlobalEDIDPersistence_Set
    global _ADL_Workstation_GlobalEDIDPersistence_Set
    global _ADL2_FPS_Caps
    global _ADL2_FPS_Settings_Get
    global _ADL2_FPS_Settings_Set
    global _ADL2_FPS_Settings_Reset
    global _ADL2_RIS_Settings_Set
    global _ADL2_RIS_Settings_Get
    global _ADL2_CHILL_SettingsX2_Set
    global _ADL2_CHILL_SettingsX2_Get
    global _ADL2_DELAG_Settings_Set
    global _ADL2_DELAG_Settings_Get
    global _ADL2_BOOST_Settings_Set
    global _ADL2_BOOST_Settings_Get
    global _ADL2_Adapter_ClockInfo_Get
    global _ADL_Adapter_ClockInfo_Get
    global _ADL2_Display_AdapterID_Get
    global _ADL_Display_AdapterID_Get
    global _ADL2_Adapter_EDC_ErrorRecords_Get
    global _ADL2_Adapter_EDC_ErrorInjection_Set
    global _ADL2_Adapter_Graphic_Core_Info_Get
    global _ADL2_Adapter_PMLog_Support_Get
    global _ADL2_Adapter_PMLog_Start
    global _ADL2_Adapter_PMLog_Stop

    _ADL2_Adapter_Active_Get = ADL2_ADAPTER_ACTIVE_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_Active_Get")
    )
    _ADL_Adapter_Active_Get = ADL_ADAPTER_ACTIVE_GET(
          GetProcAddress(hDLL, "ADL_Adapter_Active_Get")
    )
    _ADL2_Adapter_Aspects_Get = ADL2_ADAPTER_ASPECTS_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_Aspects_Get")
    )
    _ADL_Adapter_Aspects_Get = ADL_ADAPTER_ASPECTS_GET(
          GetProcAddress(hDLL, "ADL_Adapter_Aspects_Get")
    )
    _ADL2_Adapter_NumberOfAdapters_Get = ADL2_ADAPTER_NUMBEROFADAPTERS_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_NumberOfAdapters_Get")
    )
    _ADL_Adapter_NumberOfAdapters_Get = ADL_ADAPTER_NUMBEROFADAPTERS_GET(
          GetProcAddress(hDLL, "ADL_Adapter_NumberOfAdapters_Get")
    )
    _ADL2_Flush_Driver_Data = ADL2_FLUSH_DRIVER_DATA(
          GetProcAddress(hDLL, "ADL2_Flush_Driver_Data")
    )
    _ADL_Flush_Driver_Data = ADL_FLUSH_DRIVER_DATA(
          GetProcAddress(hDLL, "ADL_Flush_Driver_Data")
    )
    _ADL2_Adapter_AdapterInfo_Get = ADL2_ADAPTER_ADAPTERINFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_AdapterInfo_Get")
    )
    _ADL_Adapter_AdapterInfo_Get = ADL_ADAPTER_ADAPTERINFO_GET(
          GetProcAddress(hDLL, "ADL_Adapter_AdapterInfo_Get")
    )
    _ADL2_Adapter_AdapterInfoX2_Get = ADL2_ADAPTER_ADAPTERINFOX2_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_AdapterInfoX2_Get")
    )
    _ADL_Adapter_AdapterInfoX2_Get = ADL_ADAPTER_ADAPTERINFOX2_GET(
          GetProcAddress(hDLL, "ADL_Adapter_AdapterInfoX2_Get")
    )
    _ADL2_Adapter_RegValueString_Get = ADL2_ADAPTER_REGVALUESTRING_GET(
        GetProcAddress(hDLL, "ADL2_Adapter_RegValueString_Get")
    )
    _ADL_Adapter_RegValueString_Get = ADL_ADAPTER_REGVALUESTRING_GET(
        GetProcAddress(hDLL, "ADL_Adapter_RegValueString_Get")
    )

    _ADL2_Adapter_RegValueString_Set = ADL2_ADAPTER_REGVALUESTRING_SET(
        GetProcAddress(hDLL, "ADL2_Adapter_RegValueString_Set")
    )
    _ADL_Adapter_RegValueString_Set = ADL_ADAPTER_REGVALUESTRING_SET(
        GetProcAddress(hDLL, "ADL_Adapter_RegValueString_Set")
    )
    _ADL2_Adapter_ASICFamilyType_Get = ADL2_ADAPTER_ASICFAMILYTYPE_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_ASICFamilyType_Get")
    )
    _ADL_Adapter_ASICFamilyType_Get = ADL_ADAPTER_ASICFAMILYTYPE_GET(
          GetProcAddress(hDLL, "ADL_Adapter_ASICFamilyType_Get")
    )
    _ADL2_Adapter_Speed_Caps = ADL2_ADAPTER_SPEED_CAPS(
          GetProcAddress(hDLL, "ADL2_Adapter_Speed_Caps")
    )
    _ADL_Adapter_Speed_Caps = ADL_ADAPTER_SPEED_CAPS(
          GetProcAddress(hDLL, "ADL_Adapter_Speed_Caps")
    )
    _ADL2_Adapter_Speed_Get = ADL2_ADAPTER_SPEED_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_Speed_Get")
    )
    _ADL_Adapter_Speed_Get = ADL_ADAPTER_SPEED_GET(
          GetProcAddress(hDLL, "ADL_Adapter_Speed_Get")
    )
    _ADL2_Adapter_Speed_Set = ADL2_ADAPTER_SPEED_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_Speed_Set")
    )
    _ADL_Adapter_Speed_Set = ADL_ADAPTER_SPEED_SET(
          GetProcAddress(hDLL, "ADL_Adapter_Speed_Set")
    )
    _ADL2_Adapter_Accessibility_Get = ADL2_ADAPTER_ACCESSIBILITY_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_Accessibility_Get")
    )
    _ADL_Adapter_Accessibility_Get = ADL_ADAPTER_ACCESSIBILITY_GET(
          GetProcAddress(hDLL, "ADL_Adapter_Accessibility_Get")
    )
    _ADL2_Adapter_VideoBiosInfo_Get = ADL2_ADAPTER_VIDEOBIOSINFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_VideoBiosInfo_Get")
    )
    _ADL_Adapter_VideoBiosInfo_Get = ADL_ADAPTER_VIDEOBIOSINFO_GET(
          GetProcAddress(hDLL, "ADL_Adapter_VideoBiosInfo_Get")
    )
    _ADL2_Adapter_ID_Get = ADL2_ADAPTER_ID_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_ID_Get")
    )
    _ADL_Adapter_ID_Get = ADL_ADAPTER_ID_GET(
          GetProcAddress(hDLL, "ADL_Adapter_ID_Get")
    )
    _ADL2_AdapterX2_Caps = ADL2_ADAPTERX2_CAPS(
          GetProcAddress(hDLL, "ADL2_AdapterX2_Caps")
    )
    _ADL_AdapterX2_Caps = ADL_ADAPTERX2_CAPS(
          GetProcAddress(hDLL, "ADL_AdapterX2_Caps")
    )
    _ADL2_Adapter_Crossfire_Caps = ADL2_ADAPTER_CROSSFIRE_CAPS(
          GetProcAddress(hDLL, "ADL2_Adapter_Crossfire_Caps")
    )
    _ADL_Adapter_Crossfire_Caps = ADL_ADAPTER_CROSSFIRE_CAPS(
          GetProcAddress(hDLL, "ADL_Adapter_Crossfire_Caps")
    )
    _ADL2_Adapter_Crossfire_Get = ADL2_ADAPTER_CROSSFIRE_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_Crossfire_Get")
    )
    _ADL_Adapter_Crossfire_Get = ADL_ADAPTER_CROSSFIRE_GET(
          GetProcAddress(hDLL, "ADL_Adapter_Crossfire_Get")
    )
    _ADL2_Adapter_Crossfire_Set = ADL2_ADAPTER_CROSSFIRE_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_Crossfire_Set")
    )
    _ADL_Adapter_Crossfire_Set = ADL_ADAPTER_CROSSFIRE_SET(
          GetProcAddress(hDLL, "ADL_Adapter_Crossfire_Set")
    )
    _ADL2_Adapter_MVPU_Set = ADL2_ADAPTER_MVPU_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_MVPU_Set")
    )
    _ADL2_Adapter_MemoryInfo_Get = ADL2_ADAPTER_MEMORYINFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_MemoryInfo_Get")
    )
    _ADL_Adapter_MemoryInfo_Get = ADL_ADAPTER_MEMORYINFO_GET(
          GetProcAddress(hDLL, "ADL_Adapter_MemoryInfo_Get")
    )
    _ADL2_Adapter_ConfigMemory_Get = ADL2_ADAPTER_CONFIGMEMORY_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_ConfigMemory_Get")
    )
    _ADL_Adapter_ConfigMemory_Get = ADL_ADAPTER_CONFIGMEMORY_GET(
          GetProcAddress(hDLL, "ADL_Adapter_ConfigMemory_Get")
    )
    _ADL2_Adapter_ObservedClockInfo_Get = ADL2_ADAPTER_OBSERVEDCLOCKINFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_ObservedClockInfo_Get")
    )
    _ADL_Adapter_ObservedClockInfo_Get = ADL_ADAPTER_OBSERVEDCLOCKINFO_GET(
          GetProcAddress(hDLL, "ADL_Adapter_ObservedClockInfo_Get")
    )
    _ADL2_Adapter_BoardLayout_Get = ADL2_ADAPTER_BOARDLAYOUT_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_BoardLayout_Get")
    )
    _ADL_Adapter_BoardLayout_Get = ADL_ADAPTER_BOARDLAYOUT_GET(
          GetProcAddress(hDLL, "ADL_Adapter_BoardLayout_Get")
    )
    _ADL2_Adapter_SupportedConnections_Get = ADL2_ADAPTER_SUPPORTEDCONNECTIONS_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_SupportedConnections_Get")
    )
    _ADL_Adapter_SupportedConnections_Get = ADL_ADAPTER_SUPPORTEDCONNECTIONS_GET(
          GetProcAddress(hDLL, "ADL_Adapter_SupportedConnections_Get")
    )
    _ADL2_Adapter_ConnectionState_Get = ADL2_ADAPTER_CONNECTIONSTATE_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_ConnectionState_Get")
    )
    _ADL_Adapter_ConnectionState_Get = ADL_ADAPTER_CONNECTIONSTATE_GET(
          GetProcAddress(hDLL, "ADL_Adapter_ConnectionState_Get")
    )
    _ADL2_Adapter_EmulationMode_Set = ADL2_ADAPTER_EMULATIONMODE_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_EmulationMode_Set")
    )
    _ADL_Adapter_EmulationMode_Set = ADL_ADAPTER_EMULATIONMODE_SET(
          GetProcAddress(hDLL, "ADL_Adapter_EmulationMode_Set")
    )
    _ADL2_Adapter_ConnectionData_Set = ADL2_ADAPTER_CONNECTIONDATA_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_ConnectionData_Set")
    )
    _ADL_Adapter_ConnectionData_Set = ADL_ADAPTER_CONNECTIONDATA_SET(
          GetProcAddress(hDLL, "ADL_Adapter_ConnectionData_Set")
    )
    _ADL2_Adapter_ConnectionData_Get = ADL2_ADAPTER_CONNECTIONDATA_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_ConnectionData_Get")
    )
    _ADL_Adapter_ConnectionData_Get = ADL_ADAPTER_CONNECTIONDATA_GET(
          GetProcAddress(hDLL, "ADL_Adapter_ConnectionData_Get")
    )
    _ADL2_Adapter_ConnectionData_Remove = ADL2_ADAPTER_CONNECTIONDATA_REMOVE(
          GetProcAddress(hDLL, "ADL2_Adapter_ConnectionData_Remove")
    )
    _ADL_Adapter_ConnectionData_Remove = ADL_ADAPTER_CONNECTIONDATA_REMOVE(
          GetProcAddress(hDLL, "ADL_Adapter_ConnectionData_Remove")
    )
    _ADL2_Adapter_EDIDManagement_Caps = ADL2_ADAPTER_EDIDMANAGEMENT_CAPS(
          GetProcAddress(hDLL, "ADL2_Adapter_EDIDManagement_Caps")
    )
    _ADL_Adapter_EDIDManagement_Caps = ADL_ADAPTER_EDIDMANAGEMENT_CAPS(
          GetProcAddress(hDLL, "ADL_Adapter_EDIDManagement_Caps")
    )
    _ADL2_Workstation_GlobalEDIDPersistence_Get = ADL2_WORKSTATION_GLOBALEDIDPERSISTENCE_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_GlobalEDIDPersistence_Get")
    )
    _ADL_Workstation_GlobalEDIDPersistence_Get = ADL_WORKSTATION_GLOBALEDIDPERSISTENCE_GET(
          GetProcAddress(hDLL, "ADL_Workstation_GlobalEDIDPersistence_Get")
    )
    _ADL2_Workstation_GlobalEDIDPersistence_Set = ADL2_WORKSTATION_GLOBALEDIDPERSISTENCE_SET(
          GetProcAddress(hDLL, "ADL2_Workstation_GlobalEDIDPersistence_Set")
    )
    _ADL_Workstation_GlobalEDIDPersistence_Set = ADL_WORKSTATION_GLOBALEDIDPERSISTENCE_SET(
          GetProcAddress(hDLL, "ADL_Workstation_GlobalEDIDPersistence_Set")
    )
    _ADL2_FPS_Caps = ADL2_FPS_CAPS(
          GetProcAddress(hDLL, "ADL2_FPS_Caps")
    )
    _ADL2_FPS_Settings_Get = ADL2_FPS_SETTINGS_GET(
          GetProcAddress(hDLL, "ADL2_FPS_Settings_Get")
    )
    _ADL2_FPS_Settings_Set = ADL2_FPS_SETTINGS_SET(
          GetProcAddress(hDLL, "ADL2_FPS_Settings_Set")
    )
    _ADL2_FPS_Settings_Reset = ADL2_FPS_SETTINGS_RESET(
          GetProcAddress(hDLL, "ADL2_FPS_Settings_Reset")
    )
    _ADL2_RIS_Settings_Set = ADL2_RIS_SETTINGS_SET(
        GetProcAddress(hDLL, "ADL2_RIS_Settings_Set")
    )
    _ADL2_RIS_Settings_Get = ADL2_RIS_SETTINGS_GET(
        GetProcAddress(hDLL, "ADL2_RIS_Settings_Get")
    )
    _ADL2_CHILL_SettingsX2_Set = ADL2_CHILL_SETTINGSX2_SET(
        GetProcAddress(hDLL, "ADL2_CHILL_SettingsX2_Set")
    )
    _ADL2_CHILL_SettingsX2_Get = ADL2_CHILL_SETTINGSX2_GET(
        GetProcAddress(hDLL, "ADL2_CHILL_SettingsX2_Get")
    )
    _ADL2_DELAG_Settings_Set = ADL2_DELAG_SETTINGS_SET(
        GetProcAddress(hDLL, "ADL2_DELAG_Settings_Set")
    )
    _ADL2_DELAG_Settings_Get = ADL2_DELAG_SETTINGS_GET(
        GetProcAddress(hDLL, "ADL2_DELAG_Settings_Get")
    )
    _ADL2_BOOST_Settings_Set = ADL2_BOOST_SETTINGS_SET(
        GetProcAddress(hDLL, "ADL2_BOOST_Settings_Set")
    )
    _ADL2_BOOST_Settings_Get = ADL2_BOOST_SETTINGS_GET(
        GetProcAddress(hDLL, "ADL2_BOOST_Settings_Get")
    )
    _ADL2_Adapter_ClockInfo_Get = ADL2_ADAPTER_CLOCKINFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_ClockInfo_Get")
    )
    _ADL_Adapter_ClockInfo_Get = ADL_ADAPTER_CLOCKINFO_GET(
          GetProcAddress(hDLL, "ADL_Adapter_ClockInfo_Get")
    )
    _ADL2_Display_AdapterID_Get = ADL2_DISPLAY_ADAPTERID_GET(
          GetProcAddress(hDLL, "ADL2_Display_AdapterID_Get")
    )
    _ADL_Display_AdapterID_Get = ADL_DISPLAY_ADAPTERID_GET(
          GetProcAddress(hDLL, "ADL_Display_AdapterID_Get")
    )
    _ADL2_Adapter_EDC_ErrorRecords_Get = ADL2_ADAPTER_EDC_ERRORRECORDS_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_EDC_ErrorRecords_Get")
    )
    _ADL2_Adapter_EDC_ErrorInjection_Set = ADL2_ADAPTER_EDC_ERRORINJECTION_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_EDC_ErrorInjection_Set")
    )
    _ADL2_Adapter_Graphic_Core_Info_Get = ADL2_ADAPTER_GRAPHIC_CORE_INFO_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_Graphic_Core_Info_Get")
    )
    _ADL2_Adapter_PMLog_Support_Get = ADL2_ADAPTER_PMLOG_SUPPORT_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_PMLog_Support_Get")
    )
    _ADL2_Adapter_PMLog_Start = ADL2_ADAPTER_PMLOG_START(
          GetProcAddress(hDLL, "ADL2_Adapter_PMLog_Start")
    )
    _ADL2_Adapter_PMLog_Stop = ADL2_ADAPTER_PMLOG_STOP(
          GetProcAddress(hDLL, "ADL2_Adapter_PMLog_Stop")
    )


__all__ = (
    '_ADL2_Adapter_Active_Get',
    '_ADL_Adapter_Active_Get',
    '_ADL2_Adapter_Aspects_Get',
    '_ADL_Adapter_Aspects_Get',
    '_ADL2_Adapter_NumberOfAdapters_Get',
    '_ADL_Adapter_NumberOfAdapters_Get',
    '_ADL2_Flush_Driver_Data',
    '_ADL_Flush_Driver_Data',
    '_ADL2_Adapter_AdapterInfo_Get',
    '_ADL_Adapter_AdapterInfo_Get',
    '_ADL2_Adapter_AdapterInfoX2_Get',
    '_ADL_Adapter_AdapterInfoX2_Get',
    '_ADL2_Adapter_RegValueString_Get',
    '_ADL_Adapter_RegValueString_Get',
    '_ADL2_Adapter_RegValueString_Set',
    '_ADL_Adapter_RegValueString_Set',
    '_ADL2_Adapter_ASICFamilyType_Get',
    '_ADL_Adapter_ASICFamilyType_Get',
    '_ADL2_Adapter_Speed_Caps',
    '_ADL_Adapter_Speed_Caps',
    '_ADL2_Adapter_Speed_Get',
    '_ADL_Adapter_Speed_Get',
    '_ADL2_Adapter_Speed_Set',
    '_ADL_Adapter_Speed_Set',
    '_ADL2_Adapter_Accessibility_Get',
    '_ADL_Adapter_Accessibility_Get',
    '_ADL2_Adapter_VideoBiosInfo_Get',
    '_ADL_Adapter_VideoBiosInfo_Get',
    '_ADL2_Adapter_ID_Get',
    '_ADL_Adapter_ID_Get',
    '_ADL2_AdapterX2_Caps',
    '_ADL_AdapterX2_Caps',
    '_ADL2_Adapter_Crossfire_Caps',
    '_ADL_Adapter_Crossfire_Caps',
    '_ADL2_Adapter_Crossfire_Get',
    '_ADL_Adapter_Crossfire_Get',
    '_ADL2_Adapter_Crossfire_Set',
    '_ADL_Adapter_Crossfire_Set',
    '_ADL2_Adapter_MVPU_Set',
    '_ADL2_Adapter_MemoryInfo_Get',
    '_ADL_Adapter_MemoryInfo_Get',
    '_ADL2_Adapter_ConfigMemory_Get',
    '_ADL_Adapter_ConfigMemory_Get',
    '_ADL2_Adapter_ObservedClockInfo_Get',
    '_ADL_Adapter_ObservedClockInfo_Get',
    '_ADL2_Adapter_BoardLayout_Get',
    '_ADL_Adapter_BoardLayout_Get',
    '_ADL2_Adapter_SupportedConnections_Get',
    '_ADL_Adapter_SupportedConnections_Get',
    '_ADL2_Adapter_ConnectionState_Get',
    '_ADL_Adapter_ConnectionState_Get',
    '_ADL2_Adapter_EmulationMode_Set',
    '_ADL_Adapter_EmulationMode_Set',
    '_ADL2_Adapter_ConnectionData_Set',
    '_ADL_Adapter_ConnectionData_Set',
    '_ADL2_Adapter_ConnectionData_Get',
    '_ADL_Adapter_ConnectionData_Get',
    '_ADL2_Adapter_ConnectionData_Remove',
    '_ADL_Adapter_ConnectionData_Remove',
    '_ADL2_Adapter_EDIDManagement_Caps',
    '_ADL_Adapter_EDIDManagement_Caps',
    '_ADL2_Workstation_GlobalEDIDPersistence_Get',
    '_ADL_Workstation_GlobalEDIDPersistence_Get',
    '_ADL2_Workstation_GlobalEDIDPersistence_Set',
    '_ADL_Workstation_GlobalEDIDPersistence_Set',
    '_ADL2_FPS_Caps',
    '_ADL2_FPS_Settings_Get',
    '_ADL2_FPS_Settings_Set',
    '_ADL2_FPS_Settings_Reset',
    '_ADL2_RIS_Settings_Set',
    '_ADL2_RIS_Settings_Get',
    '_ADL2_CHILL_SettingsX2_Set',
    '_ADL2_CHILL_SettingsX2_Get',
    '_ADL2_DELAG_Settings_Set',
    '_ADL2_DELAG_Settings_Get',
    '_ADL2_BOOST_Settings_Set',
    '_ADL2_BOOST_Settings_Get',
    '_ADL2_Adapter_ClockInfo_Get',
    '_ADL_Adapter_ClockInfo_Get',
    '_ADL2_Display_AdapterID_Get',
    '_ADL_Display_AdapterID_Get',
    '_ADL2_Adapter_EDC_ErrorRecords_Get',
    '_ADL2_Adapter_EDC_ErrorInjection_Set',
    '_ADL2_Adapter_Graphic_Core_Info_Get',
    '_ADL2_Adapter_PMLog_Support_Get',
    '_ADL2_Adapter_PMLog_Start',
    '_ADL2_Adapter_PMLog_Stop',
)


from .displaysmanager_h import *  # NOQA
from .adl_sdk_h import ADL2_Main_Control_Create  # NOQA
from .display_h import Display, _ADL2_Display_NumberOfDisplays_Get  # NOQA
from .crossdisplay_h import CrossDisplay  # NOQA


class PortConnector(object):

    def __init__(
            self,
            type_,
            parent_type,
            adapter_index,
            device_port,
    ):
        self.name = str(type_)
        self._adapter_index = adapter_index
        self._device_port = device_port
        self._type = type_
        self._parent_type = parent_type

    @property
    def _properties(self):
        iAdapterIndex = INT(self._adapter_index)
        supportedConnections = ADLSupportedConnections()

        devicePort = self._device_port

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_SupportedConnections_Get(
                context,
                iAdapterIndex,
                devicePort,
                ctypes.byref(supportedConnections)
            ) == ADL_OK:
                return supportedConnections.iSupportedProperties[self._type]

    @property
    def supports_bitrate(self):
        properties = self._properties
        return properties & ADL_CONNECTION_PROPERTY_BITRATE == ADL_CONNECTION_PROPERTY_BITRATE

    @property
    def supports_number_of_lanes(self):
        properties = self._properties
        return properties & ADL_CONNECTION_PROPERTY_NUMBER_OF_LANES == ADL_CONNECTION_PROPERTY_NUMBER_OF_LANES

    @property
    def supports_three_d_caps(self):
        properties = self._properties
        return properties & ADL_CONNECTION_PROPERTY_3DCAPS == ADL_CONNECTION_PROPERTY_3DCAPS

    @property
    def supports_output_bandwidth(self):
        properties = self._properties
        return properties & ADL_CONNECTION_PROPERTY_OUTPUT_BANDWIDTH == ADL_CONNECTION_PROPERTY_OUTPUT_BANDWIDTH

    @property
    def supports_color_depth(self):
        properties = self._properties
        return properties & ADL_CONNECTION_PROPERTY_COLORDEPTH == ADL_CONNECTION_PROPERTY_COLORDEPTH

    @property
    def _connection_data(self):
        iAdapterIndex = INT(self._adapter_index)

        connectionData = ADLConnectionData()
        connectionData.iActiveConnections = INT(0)
        connectionData.iNumberofPorts = INT(0)

        devicePort = self._device_port

        with ADL2_Main_Control_Create as context:
            res = _ADL2_Adapter_ConnectionData_Get(
                context,
                iAdapterIndex,
                devicePort,
                ADL_QUERY_REAL_DATA,
                ctypes.byref(connectionData)
            )

            if res == ADL_OK:
                return connectionData

    @property
    def is_connected(self):
        mapping = {
            ADL_DISPLAY_CONTYPE_UNKNOWN: ADL_CONNECTOR_TYPE_UNKNOWN,
            ADL_DISPLAY_CONTYPE_VGA: ADL_CONNECTOR_TYPE_VGA,
            ADL_DISPLAY_CONTYPE_DVI_D: ADL_CONNECTOR_TYPE_DVI_D,
            ADL_DISPLAY_CONTYPE_DVI_I: ADL_CONNECTOR_TYPE_DVI_I,
            ADL_DISPLAY_CONTYPE_ATICVDONGLE_NTSC: ADL_CONNECTOR_TYPE_ATICVDONGLE_NA,
            ADL_DISPLAY_CONTYPE_ATICVDONGLE_JPN: ADL_CONNECTOR_TYPE_ATICVDONGLE_JP,
            ADL_DISPLAY_CONTYPE_ATICVDONGLE_NONI2C_JPN: ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C,
            ADL_DISPLAY_CONTYPE_ATICVDONGLE_NONI2C_NTSC: ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C_D,
            ADL_DISPLAY_CONTYPE_HDMI_TYPE_A: ADL_CONNECTOR_TYPE_HDMI_TYPE_A,
            ADL_DISPLAY_CONTYPE_HDMI_TYPE_B: ADL_CONNECTOR_TYPE_HDMI_TYPE_B,
            ADL_DISPLAY_CONTYPE_DISPLAYPORT: ADL_CONNECTOR_TYPE_DISPLAYPORT,
            ADL_DISPLAY_CONTYPE_EDP: ADL_CONNECTOR_TYPE_EDP,
            ADL_DISPLAY_CONTYPE_WIRELESSDISPLAY: ADL_CONNECTOR_TYPE_VIRTUAL
        }

        from .display_h import _ADL2_Display_DisplayInfo_Get, _ADL2_Display_ConnectedDisplays_Get
        iAdapterIndex = INT(self._adapter_index)
        lpConnections = INT()

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ConnectedDisplays_Get(context, iAdapterIndex, ctypes.byref(lpConnections))
            lpNumDisplays = INT()
            lppInfo = LPADLDisplayInfo()
            iForceDetect = INT(1)

            _ADL2_Display_DisplayInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpNumDisplays),
                ctypes.byref(lppInfo),
                iForceDetect
            )
            for i in range(lpNumDisplays.value):
                bitmask = lppInfo[i].iDisplayInfoValue

                if bitmask | ADL_DISPLAY_DISPLAYINFO_DISPLAYCONNECTED == bitmask:
                    info = lppInfo[i]

                    if info.iDisplayConnector not in mapping:
                        continue

                    value = mapping[info.iDisplayConnector]

                    if value == self._parent_type and value == self._type:
                        return True

            return False

    @property
    def bitrate(self):
        connectionData = self._connection_data
        if connectionData is None:
            return

        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_BITRATE == ADL_CONNECTION_PROPERTY_BITRATE:
            bitrate = connectionData.aConnectionProperties.iBitrate.value

            mapping = [
                ADL_LINK_BITRATE_1_62_GHZ,
                ADL_LINK_BITRATE_2_7_GHZ,
                ADL_LINK_BTIRATE_3_24_GHZ,
                ADL_LINK_BITRATE_5_4_GHZ,
                ADL_LINK_BITRATE_UNKNOWN
            ]
            return mapping[mapping.index(bitrate)]

        return ADL_LINK_BITRATE_UNKNOWN

    @property
    def number_of_lanes(self):
        connectionData = self._connection_data
        if connectionData is None:
            return

        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_NUMBER_OF_LANES == ADL_CONNECTION_PROPERTY_NUMBER_OF_LANES:
            return connectionData.aConnectionProperties.iNumberOfLanes.value

    @property
    def three_d_caps(self):
        connectionData = self._connection_data
        if connectionData is None:
            return

        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_3DCAPS == ADL_CONNECTION_PROPERTY_3DCAPS:
            caps = connectionData.aConnectionProperties.iStereo3DCaps.value

            if caps & ADL_CONNPROP_S3D_ALTERNATE_TO_FRAME_PACK == ADL_CONNPROP_S3D_ALTERNATE_TO_FRAME_PACK:
                return ADL_CONNPROP_S3D_ALTERNATE_TO_FRAME_PACK

        return 'Off'

    @property
    def output_bandwidth(self):
        connectionData = self._connection_data
        if connectionData is None:
            return

        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_OUTPUT_BANDWIDTH == ADL_CONNECTION_PROPERTY_OUTPUT_BANDWIDTH:
            output_bandwidth = connectionData.aConnectionProperties.iOutputBandwidth.value
            mapping = [
                ADL_LINK_BITRATE_1_62_GHZ,
                ADL_LINK_BITRATE_2_7_GHZ,
                ADL_LINK_BTIRATE_3_24_GHZ,
                ADL_LINK_BITRATE_5_4_GHZ,
                ADL_LINK_BITRATE_UNKNOWN
            ]
            return mapping[mapping.index(output_bandwidth)]

        return ADL_LINK_BITRATE_UNKNOWN

    @property
    def color_depth(self):
        connectionData = self._connection_data
        if connectionData is None:
            return

        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_COLORDEPTH == ADL_CONNECTION_PROPERTY_COLORDEPTH:
            color_depth = connectionData.aConnectionProperties.iColorDepth.value

            mapping = [
                ADL_COLORDEPTH_UNKNOWN,
                ADL_COLORDEPTH_666,
                ADL_COLORDEPTH_888,
                ADL_COLORDEPTH_101010,
                ADL_COLORDEPTH_121212,
                ADL_COLORDEPTH_141414,
                ADL_COLORDEPTH_161616
            ]
            if color_depth in mapping:
                return mapping[mapping.index(color_depth)]

        return ADL_COLORDEPTH_UNKNOWN

    @property
    def _connection_state(self):
        connectionState = ADLConnectionState()
        iAdapterIndex = INT(self._adapter_index)
        devicePort = self._device_port

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ConnectionState_Get(
                context,
                iAdapterIndex,
                devicePort,
                ctypes.byref(connectionState)
            ) == ADL_OK:
                return connectionState

    @property
    def emulation_status(self):
        connectionState = self._connection_state

        if connectionState is None:
            return ''

        if connectionState.iDisplayIndex.value == -1:
            return ''

        status = connectionState.iEmulationStatus.value

        for item in (
            ADL_EMUL_STATUS_REAL_DEVICE_CONNECTED,
            ADL_EMUL_STATUS_EMULATED_DEVICE_USED,
            ADL_EMUL_STATUS_LAST_ACTIVE_DEVICE_USED,
            ADL_EMUL_STATUS_EMULATED_DEVICE_PRESENT
        ):
            if status & item == item:
                return item

    @property
    def emulation_mode(self):
        connectionState = self._connection_state
        if connectionState is None:
            return ''

        mode = connectionState.iEmulationMode.value

        mapping = [
            ADL_EMUL_MODE_OFF,
            ADL_EMUL_MODE_ON_CONNECTED,
            ADL_EMUL_MODE_ON_DISCONNECTED,
            ADL_EMUL_MODE_ALWAYS
        ]

        return mapping[mapping.index(mode)]

    @emulation_mode.setter
    def emulation_mode(self, value):
        for item in (
            ADL_EMUL_MODE_OFF,
            ADL_EMUL_MODE_ON_CONNECTED,
            ADL_EMUL_MODE_ON_DISCONNECTED,
            ADL_EMUL_MODE_ALWAYS
        ):
            if value == str(item):
                value = item
            if value == item:
                break

        else:
            return

        iEmulationMode = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        devicePort = self._device_port

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_EmulationMode_Set(
                    context,
                    iAdapterIndex,
                    devicePort,
                    ctypes.byref(iEmulationMode)
            )

    @property
    def device_present(self):
        connectionState = self._connection_state
        if connectionState is None:
            return False

        status = connectionState.iEmulationStatus.value
        return (
            status & ADL_EMUL_STATUS_EMULATED_DEVICE_PRESENT ==
            ADL_EMUL_STATUS_EMULATED_DEVICE_PRESENT
        )


class AdapterConnector(object):

    def __init__(self, adapter_index, connector_type, connector_index, connector_id):
        self._adapter_index = adapter_index
        self._connector_index = connector_index
        self._connector_type = connector_type
        self._connector_id = connector_id

    @property
    def type(self):
        return self._connector_type

    @property
    def label(self):
        return str(self._connector_type)

    @property
    def display(self):
        mapping = {
            ADL_DISPLAY_CONTYPE_UNKNOWN: ADL_CONNECTOR_TYPE_UNKNOWN,
            ADL_DISPLAY_CONTYPE_VGA: ADL_CONNECTOR_TYPE_VGA,
            ADL_DISPLAY_CONTYPE_DVI_D: ADL_CONNECTOR_TYPE_DVI_D,
            ADL_DISPLAY_CONTYPE_DVI_I: ADL_CONNECTOR_TYPE_DVI_I,
            ADL_DISPLAY_CONTYPE_ATICVDONGLE_NTSC: ADL_CONNECTOR_TYPE_ATICVDONGLE_NA,
            ADL_DISPLAY_CONTYPE_ATICVDONGLE_JPN: ADL_CONNECTOR_TYPE_ATICVDONGLE_JP,
            ADL_DISPLAY_CONTYPE_ATICVDONGLE_NONI2C_JPN: ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C,
            ADL_DISPLAY_CONTYPE_ATICVDONGLE_NONI2C_NTSC: ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C_D,
            ADL_DISPLAY_CONTYPE_HDMI_TYPE_A: ADL_CONNECTOR_TYPE_HDMI_TYPE_A,
            ADL_DISPLAY_CONTYPE_HDMI_TYPE_B: ADL_CONNECTOR_TYPE_HDMI_TYPE_B,
            ADL_DISPLAY_CONTYPE_DISPLAYPORT: ADL_CONNECTOR_TYPE_DISPLAYPORT,
            ADL_DISPLAY_CONTYPE_EDP: ADL_CONNECTOR_TYPE_EDP,
            ADL_DISPLAY_CONTYPE_WIRELESSDISPLAY: ADL_CONNECTOR_TYPE_VIRTUAL
        }

        dt_mapping = [
            ADL_DT_MONITOR,
            ADL_DT_TELEVISION,
            ADL_DT_LCD_PANEL,
            ADL_DT_DIGITAL_FLAT_PANEL,
            ADL_DT_COMPONENT_VIDEO,
            ADL_DT_PROJECTOR
        ]

        ot_mapping = [
            ADL_DOT_UNKNOWN,
            ADL_DOT_COMPOSITE,
            ADL_DOT_SVIDEO,
            ADL_DOT_ANALOG,
            ADL_DOT_DIGITAL
        ]

        from .display_h import _ADL2_Display_DisplayInfo_Get, _ADL2_Display_ConnectedDisplays_Get
        iAdapterIndex = INT(self._adapter_index)
        lpConnections = INT()

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ConnectedDisplays_Get(context, iAdapterIndex, ctypes.byref(lpConnections))
            lpNumDisplays = INT()
            lppInfo = LPADLDisplayInfo()
            iForceDetect = INT(1)

            _ADL2_Display_DisplayInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpNumDisplays),
                ctypes.byref(lppInfo),
                iForceDetect
            )
            for i in range(lpNumDisplays.value):
                bitmask = lppInfo[i].iDisplayInfoValue

                if bitmask | ADL_DISPLAY_DISPLAYINFO_DISPLAYCONNECTED == bitmask:
                    info = lppInfo[i]
                    display_id = info.displayID

                    for key, value in mapping.items():
                        if value != self.type:
                            continue
                        if key != info.iDisplayConnector:
                            continue

                        strDisplayName = utils.get_string(info.strDisplayName)
                        strDisplayManufacturerName = utils.get_string(info.strDisplayManufacturerName)
                        iDisplayType = dt_mapping[dt_mapping.index(info.iDisplayType)]
                        iDisplayOutputType = ot_mapping[ot_mapping.index(info.iDisplayOutputType)]
                        return Display(
                            self._adapter_index,
                            display_id,
                            strDisplayName,
                            strDisplayManufacturerName,
                            iDisplayType,
                            iDisplayOutputType
                        )

    @property
    def index(self):
        return self._connector_index

    @property
    def active_connector(self):
        for connector in self:
            if connector.is_connected:
                return connector

    def __iter__(self):
        iAdapterIndex = INT(self._adapter_index)
        supportedConnections = ADLSupportedConnections()

        devicePort = ADLDevicePort()
        devicePort.iConnectorIndex = INT(self._connector_index)
        devicePort.aMSTRad.iLinkNumber = INT(1)
        # devicePort.aMSTRad.rad = b'\x00'

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_SupportedConnections_Get(
                context,
                iAdapterIndex,
                devicePort,
                ctypes.byref(supportedConnections)
            ) == ADL_OK:

                mapping = [
                    ADL_CONNECTION_TYPE_VGA,
                    ADL_CONNECTION_TYPE_DVI,
                    ADL_CONNECTION_TYPE_DVI_SL,
                    ADL_CONNECTION_TYPE_HDMI,
                    ADL_CONNECTION_TYPE_DISPLAY_PORT,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_SL,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_DL,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_HDMI,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_VGA,
                    ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_HDMI,
                    ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_DVI,
                    ADL_CONNECTION_TYPE_MST,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE,
                    ADL_CONNECTION_TYPE_VIRTUAL
                ]
                for item in mapping:
                    if (supportedConnections.iSupportedConnections & (1 << item)) == (1 << item):
                        yield PortConnector(item, self._connector_type, self._adapter_index, devicePort)

    @property
    def _connection_data(self):
        lpConnectionData = ADLConnectionData()
        iAdapterIndex = INT(self._adapter_index)
        iQueryType = INT(ADL_QUERY_CURRENT_DATA)

        devicePort = ADLDevicePort()
        devicePort.iConnectorIndex = INT(self._connector_index)
        devicePort.aMSTRad.iLinkNumber = INT(1)
        # devicePort.aMSTRad.rad = b'\x00'
        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_ConnectionData_Get(
                context,
                iAdapterIndex,
                devicePort,
                iQueryType,
                ctypes.byref(lpConnectionData)
            )

            return lpConnectionData

    @property
    def child_ports(self):
        lpConnectionData = self._connection_data
        if lpConnectionData is None:
            return

        for i in range(lpConnectionData.iNumberofPorts):
            from .adl_sdk_h import libc

            active_bit = i
            active = False

            if (1 << i) & lpConnectionData.iActiveConnections.value == 1 << i:
                active = True

            else:
                if i + 1 == lpConnectionData.iNumberofPorts.value:
                    if (1 << 7) & lpConnectionData.iActiveConnections.value == 1 << 7:
                        active = True
                        active_bit = 7

            devicePort = ADLDevicePort()
            devicePort.iConnectorIndex = INT(self._connector_index)
            devicePort.aMSTRad.iLinkNumber = 2
            libc.memset(devicePort.aMSTRad.rad, 0, ADL_MAX_RAD_LINK_COUNT)
            libc.memcpy(devicePort.aMSTRad.rad, (CHAR * 2)(b'\x00'), devicePort.aMSTRad.iLinkNumber)
            devicePort.aMSTRad.rad[2] = CHAR(bytes(active_bit + 1))

            iAdapterIndex = INT(self._adapter_index)
            supportedConnections = ADLSupportedConnections()

            with ADL2_Main_Control_Create as context:
                if _ADL2_Adapter_SupportedConnections_Get(
                        context,
                        iAdapterIndex,
                        devicePort,
                        ctypes.byref(supportedConnections)
                ) != ADL_OK:
                    print('_ADL2_Adapter_SupportedConnections_Get failed')
                    return

                res = []

                mapping = [
                    ADL_CONNECTION_TYPE_VGA,
                    ADL_CONNECTION_TYPE_DVI,
                    ADL_CONNECTION_TYPE_DVI_SL,
                    ADL_CONNECTION_TYPE_HDMI,
                    ADL_CONNECTION_TYPE_DISPLAY_PORT,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_SL,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_DL,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_HDMI,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_VGA,
                    ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_HDMI,
                    ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_DVI,
                    ADL_CONNECTION_TYPE_MST,
                    ADL_CONNECTION_TYPE_ACTIVE_DONGLE,
                    ADL_CONNECTION_TYPE_VIRTUAL
                ]
                for item in mapping:
                    if (supportedConnections.iSupportedConnections & (1 << item)) == (1 << item):
                        res += [item]

            if active:
                print('Connection Active')
            else:
                print('Connection Inactive')

    @property
    def mhl_ports(self):
        iAdapterIndex = INT(self._adapter_index)

        connectionData = ADLConnectionData()
        connectionData.iActiveConnections = INT(0)
        connectionData.iNumberofPorts = INT(0)

        parentDevicePort = ADLDevicePort()
        parentDevicePort.iConnectorIndex = INT(self._connector_index)
        parentDevicePort.aMSTRad.iLinkNumber = INT(1)
        parentDevicePort.aMSTRad.rad = b'\x00'

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ConnectionData_Get(
                context,
                iAdapterIndex,
                parentDevicePort,
                ADL_QUERY_CURRENT_DATA,
                ctypes.byref(connectionData)
            ) != ADL_OK:
                return []

        num_ports = connectionData.iNumberofPorts.value
        
        res = []
        for i in range(num_ports):
            res += [MSTPort(self._adapter_index, i, parentDevicePort)]

        return res


class MSTPort(object):

    def __init__(self, adapter_index, port_num, parent_device_port):

        self._adapter_index = adapter_index
        self._port_num = port_num
        self._parent_device_port = parent_device_port

    @property
    def _connection_data(self):
        iAdapterIndex = INT(self._adapter_index)

        connectionData = ADLConnectionData()
        connectionData.iActiveConnections = INT(0)
        connectionData.iNumberofPorts = INT(0)

        parentDevicePort = self._parent_device_port

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ConnectionData_Get(
                context,
                iAdapterIndex,
                parentDevicePort,
                ADL_QUERY_CURRENT_DATA,
                ctypes.byref(connectionData)
            ) == ADL_OK:
                return connectionData

    @property
    def active_connector(self):
        for connector in self.supported_connections:
            if connector.is_connected:
                return connector

    @property
    def is_active(self):
        connectionData = self._connection_data
        active_connections = connectionData.iActiveConnections.value
        num_ports = connectionData.iNumberofPorts.value

        if (1 << self._port_num) & active_connections == (1 << self._port_num):
            return True

        # we have check, whether last bit is active. last bit can active when internal hub in use.
        elif (
                self._port_num + 1 == num_ports and
                (1 << 7) & active_connections == (1 << 7)
        ):
            return True

        return False

    @property
    def supported_connections(self):
        connectionData = self._connection_data
        active_connections = connectionData.iActiveConnections.value
        num_ports = connectionData.iNumberofPorts.value

        if (
            self._port_num + 1 == num_ports and
            (1 << 7) & active_connections == (1 << 7)
        ):
            active_bit = 7
        else:
            active_bit = self._port_num

        iAdapterIndex = INT(self._adapter_index)
        devicePort = ADLDevicePort()
        devicePort.iConnectorIndex = self._parent_device_port.iConnectorIndex
        devicePort.aMSTRad.iLinkNumber = INT(
            self._parent_device_port.aMSTRad.iLinkNumber.value + 1
        )
        ctypes.memset(devicePort.aMSTRad.rad, 0, ADL_MAX_RAD_LINK_COUNT)
        ctypes.memmove(
            devicePort.aMSTRad.rad, 
            self._parent_device_port.aMSTRad.rad, 
            devicePort.aMSTRad.iLinkNumber.value
        )
        devicePort.aMSTRad.rad[self._parent_device_port.aMSTRad.iLinkNumber.value] = (
            CHAR(active_bit + 1)
        )

        supportedConnections = ADLSupportedConnections()

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_SupportedConnections_Get(
                    context,
                    iAdapterIndex,
                    devicePort,
                    ctypes.byref(supportedConnections)
            ) != ADL_OK:
                return []

        res = []

        mapping = [
            ADL_CONNECTION_TYPE_VGA,
            ADL_CONNECTION_TYPE_DVI,
            ADL_CONNECTION_TYPE_DVI_SL,
            ADL_CONNECTION_TYPE_HDMI,
            ADL_CONNECTION_TYPE_DISPLAY_PORT,
            ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_SL,
            ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_DL,
            ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_HDMI,
            ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_VGA,
            ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_HDMI,
            ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_DVI,
            ADL_CONNECTION_TYPE_MST,
            ADL_CONNECTION_TYPE_ACTIVE_DONGLE,
            ADL_CONNECTION_TYPE_VIRTUAL
        ]
        for item in mapping:
            if (supportedConnections.iSupportedConnections.value & (1 << item)) == (1 << item):
                res += [PortConnector(item, self._adapter_index, devicePort)]

        return res


class Connector(object):
    def __init__(self, slot, index, id_, type_, offset, length):
        self.slot = slot
        self.index = index
        self.id = id_
        self._type = type_
        self.offset = offset
        self.length = length

    @property
    def type(self):
        return self._type


class Slot(object):

    def __init__(self, index, length, width, connectors):

        self.index = index
        self.length = length
        self.width = width
        self._connectors = connectors

    @property
    def connectors(self):
        mapping = [
            ADL_CONNECTOR_TYPE_UNKNOWN,
            ADL_CONNECTOR_TYPE_VGA,
            ADL_CONNECTOR_TYPE_DVI_D,
            ADL_CONNECTOR_TYPE_DVI_I,
            ADL_CONNECTOR_TYPE_ATICVDONGLE_NA,
            ADL_CONNECTOR_TYPE_ATICVDONGLE_JP,
            ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C,
            ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C_D,
            ADL_CONNECTOR_TYPE_HDMI_TYPE_A,
            ADL_CONNECTOR_TYPE_HDMI_TYPE_B,
            ADL_CONNECTOR_TYPE_DISPLAYPORT,
            ADL_CONNECTOR_TYPE_EDP,
            ADL_CONNECTOR_TYPE_MINI_DISPLAYPORT,
            ADL_CONNECTOR_TYPE_VIRTUAL
        ]
        for connector in self._connectors:
            yield Connector(
                self,
                connector.iConnectorIndex,
                connector.iConnectorId,
                mapping[connector.iType],
                connector.iOffset,
                connector.iLength
            )

    def __iter__(self):
        return self.connectors


class FPS(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def is_supported(self):
        iAdapterIndex = INT(self._adapter_index)
        lpSupported = INT()
        lpVersion = INT()

        with ADL2_Main_Control_Create as context:
            if _ADL2_FPS_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpSupported),
                    ctypes.byref(lpVersion)
            ) == ADL_OK:
                return bool(lpSupported.value)

        return False

    @property
    def version(self):
        iAdapterIndex = INT(self._adapter_index)
        lpSupported = INT()
        lpVersion = INT()

        with ADL2_Main_Control_Create as context:
            if _ADL2_FPS_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpSupported),
                    ctypes.byref(lpVersion)
            ) == ADL_OK:
                return lpVersion.value

    @property
    def _fps_settings(self):
        iAdapterIndex = INT(self._adapter_index)
        lpFPSSettings = ADLFPSSettingsOutput()
        lpFPSSettings.ulSize = ctypes.sizeof(ADLFPSSettingsOutput)

        with ADL2_Main_Control_Create as context:
            _ADL2_FPS_Settings_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpFPSSettings),
            )
            return lpFPSSettings

    @property
    def type(self):
        lpFPSSettings = self._fps_settings

        if lpFPSSettings.bACFPSEnabled:
            return 'AC'

        if lpFPSSettings.bDCFPSEnabled:
            return 'DC'

        return 'Not Enabled'

    @property
    def is_enabled(self):
        lpFPSSettings = self._fps_settings

        return bool(lpFPSSettings.bACFPSEnabled) or bool(lpFPSSettings.bDCFPSEnabled)

    @property
    def value(self):
        lpFPSSettings = self._fps_settings

        if lpFPSSettings.bACFPSEnabled:
            return lpFPSSettings.ulACFPSCurrent

        if lpFPSSettings.bDCFPSEnabled:
            return lpFPSSettings.ulDCFPSCurrent

        return -1

    @property
    def maximum(self):
        lpFPSSettings = self._fps_settings

        if lpFPSSettings.bACFPSEnabled:
            return lpFPSSettings.ulACFPSMaximum

        if lpFPSSettings.bDCFPSEnabled:
            return lpFPSSettings.ulDCFPSMaximum

        return -1

    @property
    def minimum(self):
        lpFPSSettings = self._fps_settings

        if lpFPSSettings.bACFPSEnabled:
            return lpFPSSettings.ulACFPSMinimum

        elif lpFPSSettings.bDCFPSEnabled:
            return lpFPSSettings.ulDCFPSMinimum

        return -1


class ErrorRecord(object):

    def __init__(self, record):
        self.__record = record

    @property
    def severity(self):
        # Severity
        return str(self.__record.Severity.value)

    @property
    def is_count_valid(self):
        # countValid
        return bool(self.__record.countValid.value)

    @property
    def count(self):
        # count
        return self.__record.count.value

    @property
    def is_location_valid(self):
        # locationValid
        return bool(self.__record.locationValid.value)

    @property
    def cu(self):
        # CU
        return self.__record.CU.value

    @property
    def location_name(self):
        # StructureName
        return self.__record.StructureName.value

    @property
    def timestamp(self):
        # tiestamp
        return self.__record.tiestamp.value


# noinspection PyUnresolvedReferences
class Adapter(object):

    def __init__(self, adapter_id, adapter_index):
        self._adapter_id = adapter_id
        self._adapter_index = adapter_index

    @property
    def _adapter_info(self):
        pNumAdapters = INT(-1)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_NumberOfAdapters_Get(
                    context,
                    ctypes.byref(pNumAdapters)
            ) != ADL_OK:
                raise RuntimeError('Unable to get adapter count')

            adapterInfoArray = (AdapterInfo * pNumAdapters.value)()

            if _ADL2_Adapter_AdapterInfo_Get(
                    context,
                    adapterInfoArray,
                    ctypes.sizeof(adapterInfoArray)
            ) != ADL_OK:
                raise RuntimeError("ADL2_Adapter_AdapterInfo_Get failed.")

            return adapterInfoArray[self._adapter_index]

    @property
    def supports_edid_management(self):
        lpSupported = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_EDIDManagement_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpSupported)
            ) != ADL_OK:
                return False

            return bool(lpSupported.value)

    @property
    def id(self):
        return self._adapter_id

    @property
    def index(self):
        return self._adapter_index

    @property
    def device_number(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iDeviceNumber

    @property
    def bus_number(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iBusNumber

    @property
    def vendor_id(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iVendorID

    @property
    def name(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return utils.get_string(lpInfo.strAdapterName)

    def __iter__(self):
        
        mapping = [
            ADL_CONNECTOR_TYPE_UNKNOWN,
            ADL_CONNECTOR_TYPE_VGA,
            ADL_CONNECTOR_TYPE_DVI_D,
            ADL_CONNECTOR_TYPE_DVI_I,
            ADL_CONNECTOR_TYPE_ATICVDONGLE_NA,
            ADL_CONNECTOR_TYPE_ATICVDONGLE_JP,
            ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C,
            ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C_D,
            ADL_CONNECTOR_TYPE_HDMI_TYPE_A,
            ADL_CONNECTOR_TYPE_HDMI_TYPE_B,
            ADL_CONNECTOR_TYPE_DISPLAYPORT,
            ADL_CONNECTOR_TYPE_EDP,
            ADL_CONNECTOR_TYPE_MINI_DISPLAYPORT,
            ADL_CONNECTOR_TYPE_VIRTUAL
        ]
        iAdapterIndex = INT(self._adapter_index)

        lpValidFlags = INT(-1)
        lpNumberSlots = INT(-1)
        lppBracketSlot = LPADLBracketSlotInfo()
        lpNumberConnector = INT(-1)
        lppConnector = LPADLConnectorInfo()

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_BoardLayout_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpValidFlags),
                ctypes.byref(lpNumberSlots),
                ctypes.byref(lppBracketSlot),
                ctypes.byref(lpNumberConnector),
                ctypes.byref(lppConnector),
            )
            for i in range(lpNumberConnector.value):
                iType = mapping[mapping.index(lppConnector[i].iType)]
                iConnectorIndex = lppConnector[i].iConnectorIndex
                iConnectorId = lppConnector[i].iConnectorId

                yield AdapterConnector(self._adapter_index, iType, iConnectorIndex, iConnectorId)

    @property
    def is_overdrive_enabled(self):
        iSupported = INT()
        iEnabled = INT()
        iVersion = INT()

        from .overdrive5_h import _ADL2_Overdrive_Caps

        # Repeat for all available adapters in the system
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive_Caps(
                context,
                iAdapterIndex,
                ctypes.byref(iSupported),
                ctypes.byref(iEnabled),
                ctypes.byref(iVersion)
            ) == ADL_OK:
                return bool(iEnabled.value)

    @property
    def is_overdrive_supported(self):
        iSupported = INT()
        iEnabled = INT()
        iVersion = INT()

        from .overdrive5_h import _ADL2_Overdrive_Caps

        # Repeat for all available adapters in the system
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(iSupported),
                    ctypes.byref(iEnabled),
                    ctypes.byref(iVersion)
            ) == ADL_OK:
                return bool(iSupported.value)

    @property
    def overdrive_version(self):
        iSupported = INT()
        iEnabled = INT()
        iVersion = INT()

        from .overdrive5_h import _ADL2_Overdrive_Caps

        # Repeat for all available adapters in the system
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(iSupported),
                    ctypes.byref(iEnabled),
                    ctypes.byref(iVersion)
            ) == ADL_OK:
                return iVersion.value

    @property
    def firmware(self):
        return Firmware(self._adapter_index)

    @property
    def fan_speeds(self):
        from .overdrive5_h import OverDrive5
        from .overdrive6_h import OverDrive6
        from .overdriven_h import OverDriveN
        from .overdrive8_h import OverDrive8

        overdrive = self._overdrive

        return overdrive.fan_speeds

    @property
    def core(self):
        return Core(self._adapter_index)

    @property
    def memory(self):
        return Memory(self._adapter_index)

    @property
    def crossfire(self):
        return CrossFire(self._adapter_index)

    @property
    def crossdisplay(self):
        return CrossDisplay(self._adapter_index)

    @property
    def error_records(self):
        iAdapterIndex = INT(self._adapter_index)
        errorRecords = (ADLErrorRecord * ADL_MAX_ERROR_RECORDS_COUNT)()
        pErrorrecordCount = INT()

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_EDC_ErrorRecords_Get(
                context,
                iAdapterIndex,
                ctypes.byref(pErrorrecordCount),
                errorRecords
            ) != ADL_OK:
                return []

        res = []
        for i in range(pErrorrecordCount.value):
            res += [ErrorRecord(errorRecords[i])]

        return res

    @property
    def fps(self):
        return FPS(self._adapter_index)

    @property
    def supported_aspects(self):
        iSize = INT(ADL_MAX_CHAR)
        lpAspects = (CHAR * ADL_MAX_CHAR)()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_Aspects_Get(context, iAdapterIndex, lpAspects, iSize) == ADL_OK:
                return utils.get_string(lpAspects).split(';')

        return []

    @property
    def udid(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return utils.get_string(lpInfo.strUDID)

    @property
    def function_number(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iFunctionNumber

    @property
    def is_present(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iPresent == 1

    @property
    def exists(self):
        if defined(_WIN32) or defined(_WIN64):
            lpInfo = self._adapter_info
            if lpInfo is not None:
                return lpInfo.iExist == 1

    @property
    def driver_path(self):
        if defined(_WIN32) or defined(_WIN64):
            lpInfo = self._adapter_info
            if lpInfo is not None:
                return utils.get_string(lpInfo.strDriverPath)

    @property
    def driver_path_ext(self):
        if defined(_WIN32) or defined(_WIN64):
            lpInfo = self._adapter_info
            if lpInfo is not None:
                return utils.get_string(lpInfo.strDriverPathExt)

    @property
    def upnp_path(self):
        if defined(_WIN32) or defined(_WIN64):
            lpInfo = self._adapter_info
            if lpInfo is not None:
                return utils.get_string(lpInfo.strPNPString)

    @property
    def display_index(self):
        if defined(_WIN32) or defined(_WIN64):
            lpInfo = self._adapter_info
            if lpInfo is not None:
                return lpInfo.iOSDisplayIndex

    @property
    def driver_index(self):
        if defined(LINUX):
            lpInfo = self._adapter_info
            if lpInfo is not None:
                return lpInfo.iDrvIndex

    @property
    def screen_config_name(self):
        if defined(LINUX):
            lpInfo = self._adapter_info
            if lpInfo is not None:
                return utils.get_string(lpInfo.strXScreenConfigName)

    @property
    def asic_family_type(self):
        lpAsicTypes = INT()
        lpValids = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ASICFamilyType_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpAsicTypes),
                    ctypes.byref(lpValids)
            ) == ADL_OK:
                # not sure what to do with the values
                mapping = [
                    ADL_ASIC_UNDEFINED,
                    ADL_ASIC_DISCRETE,
                    ADL_ASIC_INTEGRATED,
                    ADL_ASIC_FIREGL,
                    ADL_ASIC_FIREMV,
                    ADL_ASIC_XGP,
                    ADL_ASIC_FUSION,
                    ADL_ASIC_FIRESTREAM,
                    ADL_ASIC_EMBEDDED
                ]
                return mapping[mapping.index(lpAsicTypes.value)]

        return ADL_ASIC_UNDEFINED

    @property
    def can_change_speed(self):
        lpCaps = INT()
        lpValid = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_Speed_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpCaps),
                    ctypes.byref(lpValid)
            ) == ADL_OK:
                return ADL_ADAPTER_SPEEDCAPS_SUPPORTED == lpCaps

    @property
    def speed(self):
        lpCurrent = INT()
        lpDefault = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_Speed_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault)
            ) == ADL_OK:
                # not sure what to do with the values

                mapping = [
                    ADL_CONTEXT_SPEED_UNFORCED,
                    ADL_CONTEXT_SPEED_FORCEHIGH,
                    ADL_CONTEXT_SPEED_FORCELOW,
                    ADL_ADAPTER_SPEEDCAPS_SUPPORTED
                ]

                return mapping[lpCurrent.value]

            return 'Unsupported'

    @speed.setter
    def speed(self, value):
        if value not in (
                str(ADL_CONTEXT_SPEED_FORCEHIGH),
                ADL_CONTEXT_SPEED_FORCEHIGH,
                str(ADL_CONTEXT_SPEED_UNFORCED),
                ADL_CONTEXT_SPEED_UNFORCED
        ):
            return

        if not isinstance(value, int):
            if value == 'Force High':
                value = ADL_CONTEXT_SPEED_FORCEHIGH
            else:
                value = ADL_CONTEXT_SPEED_UNFORCED

        iSpeed = INT(value)
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_Speed_Set(
                context,
                iAdapterIndex,
                iSpeed,
            )

    @property
    def default_speed(self):
        lpCurrent = INT()
        lpDefault = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_Speed_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault)
            ) == ADL_OK:
                # not sure what to do with the values

                mapping = [
                    ADL_CONTEXT_SPEED_UNFORCED,
                    ADL_CONTEXT_SPEED_FORCEHIGH,
                    ADL_CONTEXT_SPEED_FORCELOW
                ]

                return mapping[mapping.index(lpDefault.value)]

            return 'Unsupported'

    @property
    def is_gpu_accessable(self):
        lpAccessibility = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_Accessibility_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpAccessibility),
            ) == ADL_OK:
                return lpAccessibility == 1

    def extended_desktop(self, value):
        lpNewlyActivate = INT()
        iStatus = INT(value)
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_Active_Set(
                context,
                iAdapterIndex,
                iStatus,
                ctypes.byref(lpNewlyActivate),
            )

    extended_desktop = property(fset=extended_desktop)

    @property
    def bus_speed(self):
        overdrive = self._overdrive
        return overdrive.bus_speed

    @property
    def bus_lanes(self):
        overdrive = self._overdrive
        return overdrive.bus_lanes

    @property
    def _overdrive(self):
        iSupported = INT()
        iEnabled = INT()
        iVersion = INT()

        from .overdrive5_h import _ADL2_Overdrive_Caps

        # Repeat for all available adapters in the system
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(iSupported),
                    ctypes.byref(iEnabled),
                    ctypes.byref(iVersion)
            ) == ADL_OK:
                if iVersion.value == 5:
                    from .overdrive5_h import OverDrive5
                    return OverDrive5(self._adapter_index)

                elif iVersion.value == 6:
                    from .overdrive6_h import OverDrive6
                    return OverDrive6(self._adapter_index)

                elif iVersion.value == 7:
                    from .overdriven_h import OverDriveN
                    return OverDriveN(self._adapter_index)

                elif iVersion.value == 8:
                    from .overdrive8_h import OverDrive8
                    return OverDrive8(self._adapter_index)

    @property
    def is_power_control_supported(self):
        overdrive = self._overdrive

        return overdrive.is_power_control_supported

    @property
    def power_control(self):
        overdrive = self._overdrive

        return overdrive.power_control

    @property
    def temperatures(self):
        overdrive = self._overdrive

        return overdrive.temperatures


class DisplayConnection(object):

    def __init__(self, adapter_index, display_index):
        self._adapter_index = adapter_index
        self._display_index = display_index

    @property
    def num_controllers(self):
        pAdapterCaps = self._adapter_caps_x2

        if pAdapterCaps is not None:
            return pAdapterCaps.iNumControllers

    @property
    def num_gl_sync_connectors(self):
        pAdapterCaps = self._adapter_caps_x2

        if pAdapterCaps is not None:
            return pAdapterCaps.iNumOfGLSyncConnectors

    @property
    def num_overlays(self):
        pAdapterCaps = self._adapter_caps_x2

        if pAdapterCaps is not None:
            return pAdapterCaps.iNumOverlays

    @property
    def num_connectors(self):
        pAdapterCaps = self._adapter_caps_x2

        if pAdapterCaps is not None:
            return pAdapterCaps.iNumConnectors

    @property
    def num_displays(self):
        pAdapterCaps = self._adapter_caps_x2

        if pAdapterCaps is not None:
            return pAdapterCaps.iNumDisplays

    @property
    def _adapter_caps_x2(self):
        pAdapterCaps = ADLAdapterCapsX2()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_AdapterX2_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(pAdapterCaps)
            ) == ADL_OK:
                return pAdapterCaps

    @property
    def ports(self):
        pAdapterCaps = self._adapter_caps_x2

        if pAdapterCaps is None:
            return []

        res = []

        for i in range(pAdapterCaps.iNumConnectors):
            res += [AdapterConnector(self._adapter_index, i)]

        return res

    @property
    def adapter_id(self):
        lpAdapterID = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ID_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpAdapterID),
            ) == ADL_OK:
                return lpAdapterID.value

    @property
    def display_adapter_id(self):
        iAdapterIndex = INT(self._adapter_index)
        lpAdapterID = INT()

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_AdapterID_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpAdapterID),
            ) == ADL_OK:
                return lpAdapterID.value

    @property
    def slots(self):
        lpValidFlags = INT()
        lpNumberSlots = INT()
        lpNumberConnector = INT()
        lppBracketSlot = (ADLBracketSlotInfo * ADL_ADAPTER_MAX_SLOTS)()
        lppConnector = (ADLConnectorInfo * ADL_ADAPTER_MAX_CONNECTORS)()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if ADL_OK == _ADL2_Adapter_BoardLayout_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpValidFlags),
                ctypes.byref(lpNumberSlots),
                ctypes.cast(lppBracketSlot, POINTER(POINTER(ADLBracketSlotInfo))),
                ctypes.byref(lpNumberConnector),
                ctypes.cast(lppConnector, POINTER(POINTER(ADLConnectorInfo))),
            ):

                for slot in lppBracketSlot:
                    if slot is None:
                        break

                for slot in lppConnector:
                    if slot is None:
                        break

                connectors = []
                for i in range(lpNumberConnector.value):
                    connector = lppConnector[i]
                    connectors += [connector]

                for i in range(lpNumberSlots.value):
                    slot = lppBracketSlot[i]
                    slot_index = slot.iSlotIndex
                    yield Slot(
                        slot_index,
                        slot.iLength,
                        slot.iWidth,
                        connectors
                    )

    @property
    def crossfire(self):
        return CrossFire(self._adapter_index)

    @property
    def is_active(self):
        lpStatus = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_Active_Get(context, iAdapterIndex, ctypes.byref(lpStatus)) == ADL_OK:
                return lpStatus != ADL_FALSE

    @property
    def is_primary(self):
        lpPrimaryAdapterIndex = INT()

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_Primary_Get(
                    context,
                    ctypes.byref(lpPrimaryAdapterIndex),
            ) == ADL_OK:
                return lpPrimaryAdapterIndex.value == self._adapter_index

    def make_primary(self):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            return _ADL2_Adapter_Primary_Set(
                context,
                iAdapterIndex,
            ) == ADL_OK

    def mode_switch(self):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            return _ADL2_Adapter_ModeSwitch(
                context,
                iAdapterIndex,
            ) == ADL_OK

    @property
    def displays(self):
        iAdapterIndex = INT(self._adapter_index)
        lpNumDisplays = INT()

        res = []

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_NumberOfDisplays_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpNumDisplays)
            ) == ADL_OK:
                for i in range(lpNumDisplays.value):
                    res += [Display(self._adapter_index, i)]

        return res

    def save(self):
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            return _ADL2_Flush_Driver_Data(context, iAdapterIndex) == ADL_OK

    @property
    def _adapter_info(self):
        num_adapters = INT(-1)

        with ADL2_Main_Control_Create as context:

            if _ADL2_Adapter_NumberOfAdapters_Get(
                context,
                ctypes.byref(num_adapters)
            ) != ADL_OK:
                raise RuntimeError('Unable to get adapter count')

            adapterInfoArray = (AdapterInfo * num_adapters.value)()

            if _ADL2_Adapter_AdapterInfo_Get(
                context,
                adapterInfoArray,
                ctypes.sizeof(adapterInfoArray)
            ) != ADL_OK:
                raise RuntimeError("ADL2_Adapter_AdapterInfo_Get failed.")

            for lpInfo in adapterInfoArray:
                if self._adapter_index == lpInfo.iAdapterIndex:
                    return lpInfo


class CrossFire(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def is_prefered_adapter(self):
        lpPreferred = INT()
        lpNumComb = INT()
        ppCrossfireComb = LPADLCrossfireComb()
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            res = _ADL2_Adapter_Crossfire_Caps(
                context,
                iAdapterIndex,
                ctypes.byref(lpPreferred),
                ctypes.byref(lpNumComb),
                ctypes.byref(ppCrossfireComb),
            )

            if res == ADL_OK:
                return lpPreferred.value == self._adapter_index

    @property
    def is_combination_supported(self):
        lpCrossfireInfo = self.__crossfire_info

        if lpCrossfireInfo is not None:
            return lpCrossfireInfo.iSupported == ADL_TRUE

    @property
    def state(self):
        """
        ADL_XFIREX_STATE_NOINTERCONNECT
        ADL_XFIREX_STATE_DOWNGRADEPIPES
        ADL_XFIREX_STATE_DOWNGRADEMEM
        ADL_XFIREX_STATE_REVERSERECOMMENDED
        ADL_XFIREX_STATE_3DACTIVE
        ADL_XFIREX_STATE_MASTERONSLAVE
        ADL_XFIREX_STATE_NODISPLAYCONNECT
        ADL_XFIREX_STATE_NOPRIMARYVIEW
        ADL_XFIREX_STATE_DOWNGRADEVISMEM
        ADL_XFIREX_STATE_LESSTHAN8LANE_MASTER
        ADL_XFIREX_STATE_LESSTHAN8LANE_SLAVE
        ADL_XFIREX_STATE_PEERTOPEERFAILED
        ADL_XFIREX_STATE_MEMISDOWNGRADED
        ADL_XFIREX_STATE_PIPESDOWNGRADED
        ADL_XFIREX_STATE_XFIREXACTIVE
        ADL_XFIREX_STATE_VISMEMISDOWNGRADED
        ADL_XFIREX_STATE_INVALIDINTERCONNECTION
        ADL_XFIREX_STATE_NONP2PMODE
        ADL_XFIREX_STATE_DOWNGRADEMEMBANKS
        ADL_XFIREX_STATE_MEMBANKSDOWNGRADED
        ADL_XFIREX_STATE_DUALDISPLAYSALLOWED
        ADL_XFIREX_STATE_P2P_APERTURE_MAPPING
        ADL_XFIREX_STATE_P2PFLUSH_REQUIRED
        ADL_XFIREX_STATE_XSP_CONNECTED
        ADL_XFIREX_STATE_ENABLE_CF_REBOOT_REQUIRED
        ADL_XFIREX_STATE_DISABLE_CF_REBOOT_REQUIRED
        ADL_XFIREX_STATE_DRV_HANDLE_DOWNGRADE_KEY
        ADL_XFIREX_STATE_CF_RECONFIG_REQUIRED
        ADL_XFIREX_STATE_ERRORGETTINGSTATUS
        """
        lpCrossfireInfo = self.__crossfire_info

        if lpCrossfireInfo is not None:
            if lpCrossfireInfo.iErrorCode:
                return lpCrossfireInfo.iErrorCode

            mapping = [
                ADL_XFIREX_STATE_NOINTERCONNECT,
                ADL_XFIREX_STATE_DOWNGRADEPIPES,
                ADL_XFIREX_STATE_DOWNGRADEMEM,
                ADL_XFIREX_STATE_REVERSERECOMMENDED,
                ADL_XFIREX_STATE_3DACTIVE,
                ADL_XFIREX_STATE_MASTERONSLAVE,
                ADL_XFIREX_STATE_NODISPLAYCONNECT,
                ADL_XFIREX_STATE_NOPRIMARYVIEW,
                ADL_XFIREX_STATE_DOWNGRADEVISMEM,
                ADL_XFIREX_STATE_LESSTHAN8LANE_MASTER,
                ADL_XFIREX_STATE_LESSTHAN8LANE_SLAVE,
                ADL_XFIREX_STATE_PEERTOPEERFAILED,
                ADL_XFIREX_STATE_MEMISDOWNGRADED,
                ADL_XFIREX_STATE_PIPESDOWNGRADED,
                ADL_XFIREX_STATE_XFIREXACTIVE,
                ADL_XFIREX_STATE_VISMEMISDOWNGRADED,
                ADL_XFIREX_STATE_INVALIDINTERCONNECTION,
                ADL_XFIREX_STATE_NONP2PMODE,
                ADL_XFIREX_STATE_DOWNGRADEMEMBANKS,
                ADL_XFIREX_STATE_MEMBANKSDOWNGRADED,
                ADL_XFIREX_STATE_DUALDISPLAYSALLOWED,
                ADL_XFIREX_STATE_P2P_APERTURE_MAPPING,
                ADL_XFIREX_STATE_P2PFLUSH_REQUIRED,
                ADL_XFIREX_STATE_XSP_CONNECTED,
                ADL_XFIREX_STATE_ENABLE_CF_REBOOT_REQUIRED,
                ADL_XFIREX_STATE_DISABLE_CF_REBOOT_REQUIRED,
                ADL_XFIREX_STATE_DRV_HANDLE_DOWNGRADE_KEY,
                ADL_XFIREX_STATE_CF_RECONFIG_REQUIRED,
                ADL_XFIREX_STATE_ERRORGETTINGSTATUS
            ]

            if lpCrossfireInfo.iState in mapping:
                return mapping[mapping.index(lpCrossfireInfo.iState)]

        return ADL_XFIREX_STATE_ERRORGETTINGSTATUS

    @property
    def __crossfire_info(self):
        lpCrossfireComb = ADLCrossfireComb()
        iAdapterIndex = INT(self._adapter_index)
        lpCrossfireInfo = ADLCrossfireInfo()

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_Crossfire_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpCrossfireComb),
                ctypes.byref(lpCrossfireInfo)
            )

            return lpCrossfireInfo

    @property
    def adapters(self):
        lpPreferred = INT()
        lpNumComb = INT()
        ppCrossfireComb = (ADLCrossfireComb * 3)()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_Crossfire_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpPreferred),
                    ctypes.byref(lpNumComb),
                    ctypes.byref(ppCrossfireComb),
            ) == ADL_OK:
                adapter_indexes = []

                for i in range(lpNumComb.value):
                    comb = ppCrossfireComb[i]

                    for j in range(comb.iNumLinkAdapter.value):
                        adapter_index = comb.iAdaptLink[j]
                        if (
                                adapter_index not in adapter_indexes and
                                adapter_index != self._adapter_index
                        ):
                            adapter_indexes += [Adapter(adapter_index)]

                return adapter_indexes

    @adapters.setter
    def adapters(self, value):
        """
        OK so this is the skinny on how I think this thing works..

        use the getter of this property it will return all adapters that are in the chain (excluding self)
        when you query for the state of the crossfire it is going to tell you if it is running or not.. the
        adapters returned from the getter of this property show a connection, it does not show if the connection
        is turned on or not that is what the state method does. you pass an adapter that has been returned from the
        getter tro the state to determine if the link is active between this adapter and the supplied adapter. and if
        the state of the connection reports as not active and you want it to be active pass that same adapyter to
        this property. or none if you weant to disable the connections to this adapter..

        card1 === card2 === card3

        If this adapter is card2 and you pass NULL it is going to turn oiff all crossfire connections. because it
        breaks the link between the 3 of them. if this card is card1 or card 3 and NULL is passed the other 2 cards
        will remain connected to each other.

        I am kind of bull shitting my way through this as I have never set up crossfire before.. I do have a spare
        card I will test it out with and see what happens.

        :param value: the adapter to enable the cross fire connection to
            or None if you want to disable crossfire for this adapter.

        """
        iAdapterIndex = INT(self._adapter_index)
        lpCrossfireComb = NULL

        if value is not None:
            lpPreferred = INT()
            lpNumComb = INT()
            ppCrossfireComb = (ADLCrossfireComb * 3)()

            with ADL2_Main_Control_Create as context:
                if _ADL2_Adapter_Crossfire_Caps(
                        context,
                        iAdapterIndex,
                        ctypes.byref(lpPreferred),
                        ctypes.byref(lpNumComb),
                        ctypes.byref(ppCrossfireComb),
                ) == ADL_OK:
                    for i in range(lpNumComb.value):
                        lpCrossfireComb = ppCrossfireComb[i]
                        adapter_indexes = []

                        for j in range(lpCrossfireComb.iNumLinkAdapter.value):
                            adapter_indexes += [lpCrossfireComb.iAdaptLink[j]]

                        # noinspection PyProtectedMember
                        if self._adapter_index in adapter_indexes and value._adapter_index in adapter_indexes:
                            break
                    else:
                        return

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_Crossfire_Set(
                context,
                iAdapterIndex,
                lpCrossfireComb
            )


class Firmware(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def __bios_info(self):
        lpBiosInfo = ADLBiosInfo()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_VideoBiosInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpBiosInfo),
            ) == ADL_OK:
                return lpBiosInfo

    @property
    def date(self):
        lpBiosInfo = self.__bios_info
        if lpBiosInfo is not None:
            return utils.get_string(lpBiosInfo.strDate)

    @property
    def part_number(self):
        lpBiosInfo = self.__bios_info
        if lpBiosInfo is not None:
            return utils.get_string(lpBiosInfo.strPartNumber)

    @property
    def version(self):
        lpBiosInfo = self.__bios_info
        if lpBiosInfo is not None:
            return utils.get_string(lpBiosInfo.strVersion)


class Memory(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def __memory_info(self):
        lpMemoryInfo = ADLMemoryInfo()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_MemoryInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpMemoryInfo),
            ) == ADL_OK:
                return lpMemoryInfo

    @property
    def size(self):
        lpMemoryInfo = self.__memory_info
        if lpMemoryInfo is not None:
            return lpMemoryInfo.iMemorySize

    @property
    def type(self):
        lpMemoryInfo = self.__memory_info
        if lpMemoryInfo is not None:
            return utils.get_string(lpMemoryInfo.strMemoryType)

    @property
    def bandwidth(self):
        lpMemoryInfo = self.__memory_info
        if lpMemoryInfo is not None:
            return lpMemoryInfo.iMemoryBandwidth

    @property
    def observed_clock(self):
        lpCoreClock = INT()
        lpMemoryClock = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ObservedClockInfo_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpCoreClock),
                    ctypes.byref(lpMemoryClock),
            ) == ADL_OK:
                return lpMemoryClock.value

    @property
    def voltages(self):
        overdrive = self._overdrive
        return overdrive.memory_voltages

    @property
    def clocks(self):
        overdrive = self._overdrive
        return overdrive.memory_clocks

    @property
    def _overdrive(self):
        iSupported = INT()
        iEnabled = INT()
        iVersion = INT()

        from .overdrive5_h import _ADL2_Overdrive_Caps

        # Repeat for all available adapters in the system
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(iSupported),
                    ctypes.byref(iEnabled),
                    ctypes.byref(iVersion)
            ) == ADL_OK:
                if iVersion.value == 5:
                    from .overdrive5_h import OverDrive5
                    return OverDrive5(self._adapter_index)

                elif iVersion.value == 6:
                    from .overdrive6_h import OverDrive6
                    return OverDrive6(self._adapter_index)

                elif iVersion.value == 7:
                    from .overdriven_h import OverDriveN
                    return OverDriveN(self._adapter_index)

                elif iVersion.value == 8:
                    from .overdrive8_h import OverDrive8
                    return OverDrive8(self._adapter_index)


class Core(object):

    def __init__(self, adapter_index):
        self._adapter_index = adapter_index

    @property
    def clock(self):
        lpCoreClock = INT()
        lpMemoryClock = INT()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ObservedClockInfo_Get(
                context,
                iAdapterIndex,
                ctypes.byref(lpCoreClock),
                ctypes.byref(lpMemoryClock),
            ) == ADL_OK:
                return lpCoreClock.value

    @property
    def _overdrive(self):
        iSupported = INT()
        iEnabled = INT()
        iVersion = INT()

        from .overdrive5_h import _ADL2_Overdrive_Caps

        # Repeat for all available adapters in the system
        iAdapterIndex = INT(self._adapter_index)
        with ADL2_Main_Control_Create as context:
            if _ADL2_Overdrive_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(iSupported),
                    ctypes.byref(iEnabled),
                    ctypes.byref(iVersion)
            ) == ADL_OK:
                if iVersion.value == 5:
                    from .overdrive5_h import OverDrive5
                    return OverDrive5(self._adapter_index)

                elif iVersion.value == 6:
                    from .overdrive6_h import OverDrive6
                    return OverDrive6(self._adapter_index)

                elif iVersion.value == 7:
                    from .overdriven_h import OverDriveN
                    return OverDriveN(self._adapter_index)

                elif iVersion.value == 8:
                    from .overdrive8_h import OverDrive8
                    return OverDrive8(self._adapter_index)

    @property
    def voltages(self):
        overdrive = self._overdrive

        return overdrive.core_voltages

    @property
    def clocks(self):
        overdrive = self._overdrive

        return overdrive.engine_clocks

    @property
    def load(self):
        overdrive = self._overdrive

        return overdrive.load
