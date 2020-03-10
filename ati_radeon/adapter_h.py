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


ADL2_ADAPTER_ACTIVE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_ACTIVE_GET = int(
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_ASPECTS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(CHAR),
    INT
)
ADL_ADAPTER_ASPECTS_GET = int(
    INT,
    POINTER(CHAR),
    INT
)
ADL2_ADAPTER_NUMBEROFADAPTERS_GET = int(
    ADL_CONTEXT_HANDLE,
    POINTER(INT)
)
ADL_ADAPTER_NUMBEROFADAPTERS_GET = int(
    POINTER(INT)
)
ADL2_FLUSH_DRIVER_DATA = int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_FLUSH_DRIVER_DATA = int(
    INT
)
ADL2_ADAPTER_ADAPTERINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    LPAdapterInfo,
    INT
)
ADL_ADAPTER_ADAPTERINFO_GET = int(
    LPAdapterInfo,
    INT
)
ADL2_ADAPTER_ADAPTERINFOX2_GET = int(
    ADL_CONTEXT_HANDLE,
    POINTER(POINTER(AdapterInfo))
)
ADL_ADAPTER_ADAPTERINFOX2_GET = int(
    POINTER(POINTER(AdapterInfo))
)
ADL2_ADAPTER_ASICFAMILYTYPE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_ASICFAMILYTYPE_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_SPEED_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_SPEED_CAPS = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_SPEED_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_SPEED_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_SPEED_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_ADAPTER_SPEED_SET = int(
    INT,
    INT
)
ADL2_ADAPTER_ACCESSIBILITY_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_ACCESSIBILITY_GET = int(
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_VIDEOBIOSINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLBiosInfo)
)
ADL_ADAPTER_VIDEOBIOSINFO_GET = int(
    INT,
    POINTER(ADLBiosInfo)
)
ADL2_ADAPTER_ID_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_ID_GET = int(
    INT,
    POINTER(INT)
)
ADL2_ADAPTERX2_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLAdapterCapsX2)
)
ADL_ADAPTERX2_CAPS = int(
    INT,
    POINTER(ADLAdapterCapsX2)
)
ADL2_ADAPTER_CROSSFIRE_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLCrossfireComb))
)
ADL_ADAPTER_CROSSFIRE_CAPS = int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLCrossfireComb))
)
ADL2_ADAPTER_CROSSFIRE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLCrossfireComb),
    POINTER(ADLCrossfireInfo)
)
ADL_ADAPTER_CROSSFIRE_GET = int(
    INT,
    POINTER(ADLCrossfireComb),
    POINTER(ADLCrossfireInfo)
)
ADL2_ADAPTER_CROSSFIRE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLCrossfireComb)
)
ADL_ADAPTER_CROSSFIRE_SET = int(
    INT,
    POINTER(ADLCrossfireComb)
)
ADL2_ADAPTER_MVPU_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL2_ADAPTER_MEMORYINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLMemoryInfo)
)
ADL_ADAPTER_MEMORYINFO_GET = int(
    INT,
    POINTER(ADLMemoryInfo)
)
ADL2_ADAPTER_CONFIGMEMORY_GET = int(
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
ADL_ADAPTER_CONFIGMEMORY_GET = int(
    INT,
    INT,
    INT,
    INT,
    INT,
    POINTER(ADLMemoryDisplayFeatures),
    POINTER(INT),
    POINTER(POINTER(ADLMemoryRequired))
)
ADL2_ADAPTER_OBSERVEDCLOCKINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_ADAPTER_OBSERVEDCLOCKINFO_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_ADAPTER_BOARDLAYOUT_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLBracketSlotInfo)),
    POINTER(INT),
    POINTER(POINTER(ADLConnectorInfo))
)
ADL_ADAPTER_BOARDLAYOUT_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLBracketSlotInfo)),
    POINTER(INT),
    POINTER(POINTER(ADLConnectorInfo))
)
ADL2_ADAPTER_SUPPORTEDCONNECTIONS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    POINTER(ADLSupportedConnections)
)
ADL_ADAPTER_SUPPORTEDCONNECTIONS_GET = int(
    INT,
    ADLDevicePort,
    POINTER(ADLSupportedConnections)
)
ADL2_ADAPTER_CONNECTIONSTATE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    POINTER(ADLConnectionState)
)
ADL_ADAPTER_CONNECTIONSTATE_GET = int(
    INT,
    ADLDevicePort,
    POINTER(ADLConnectionState)
)
ADL2_ADAPTER_EMULATIONMODE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    INT
)
ADL_ADAPTER_EMULATIONMODE_SET = int(
    INT,
    ADLDevicePort,
    INT
)
ADL2_ADAPTER_CONNECTIONDATA_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    ADLConnectionData
)
ADL_ADAPTER_CONNECTIONDATA_SET = int(
    INT,
    ADLDevicePort,
    ADLConnectionData
)
ADL2_ADAPTER_CONNECTIONDATA_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort,
    INT,
    POINTER(ADLConnectionData)
)
ADL_ADAPTER_CONNECTIONDATA_GET = int(
    INT,
    ADLDevicePort,
    INT,
    POINTER(ADLConnectionData)
)
ADL2_ADAPTER_CONNECTIONDATA_REMOVE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDevicePort
)
ADL_ADAPTER_CONNECTIONDATA_REMOVE = int(
    INT,
    ADLDevicePort
)
ADL2_ADAPTER_EDIDMANAGEMENT_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_EDIDMANAGEMENT_CAPS = int(
    INT,
    POINTER(INT)
)
ADL2_WORKSTATION_GLOBALEDIDPERSISTENCE_GET = int(
    ADL_CONTEXT_HANDLE,
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_GLOBALEDIDPERSISTENCE_GET = int(
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_GLOBALEDIDPERSISTENCE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_WORKSTATION_GLOBALEDIDPERSISTENCE_SET = int(
    INT
)
ADL2_FPS_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_FPS_SETTINGS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLFPSSettingsOutput)
)
ADL2_FPS_SETTINGS_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLFPSSettingsInput
)
ADL2_FPS_SETTINGS_RESET = int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL2_ADAPTER_CLOCKINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLClockInfo)
)
ADL_ADAPTER_CLOCKINFO_GET = int(
    INT,
    POINTER(ADLClockInfo)
)
ADL2_DISPLAY_ADAPTERID_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_ADAPTERID_GET = int(
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_EDC_ERRORRECORDS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(ADLErrorRecord)
)
ADL2_ADAPTER_EDC_ERRORINJECTION_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLErrorInjection)
)
ADL2_ADAPTER_GRAPHIC_CORE_INFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLGraphicCoreInfo)
)
ADL2_ADAPTER_PMLOG_SUPPORT_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPMLogSupportInfo)
)
ADL2_ADAPTER_PMLOG_START = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLPMLogStartInput),
    POINTER(ADLPMLogStartOutput),
    ADL_D3DKMT_HANDLE
)
ADL2_ADAPTER_PMLOG_STOP = int(
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
from .adl_sdk_h import ADL2_Main_Control_Create, AdapterBase  # NOQA
from .display_h import Display, _ADL2_Display_NumberOfDisplays_Get  # NOQA
from .crossdisplay_h import CrossDisplay  # NOQA

#
# _ADL2_Adapter_NumberOfAdapters_Get
#
# _ADL2_Adapter_MVPU_Set # crossfire
#
# _ADL2_Adapter_EmulationMode_Set
# _ADL2_Adapter_ConnectionData_Set
# _ADL2_Adapter_ConnectionData_Remove
# _ADL2_Adapter_EDIDManagement_Caps
#
#
# _ADL2_Workstation_GlobalEDIDPersistence_Get
# _ADL2_Workstation_GlobalEDIDPersistence_Set
#
#
# _ADL2_FPS_Caps
# _ADL2_FPS_Settings_Get
# _ADL2_FPS_Settings_Set
# _ADL2_FPS_Settings_Reset
#
#
#
#
#

# _ADL2_Adapter_Graphic_Core_Info_Get



class PortConnector(object):

    def __init__(
            self,
            name,
            adapter_index,
            device_port,
            type
    ):
        self.name = name
        self._adapter_index = adapter_index
        self._device_port = device_port
        self._type = type

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
            if _ADL2_Adapter_ConnectionData_Get(
                    context,
                    iAdapterIndex,
                    devicePort,
                    ADL_QUERY_CURRENT_DATA,
                    ctypes.byref(connectionData)
            ) == ADL_OK:
                return connectionData

    @property
    def is_connected(self):
        connectionData = self._connection_data
        return connectionData.iConnectionType.value == self._type

    @property
    def bitrate(self):
        connectionData = self._connection_data
        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_BITRATE == ADL_CONNECTION_PROPERTY_BITRATE:
            bitrate = connectionData.aConnectionProperties.iBitrate.value

            if bitrate == ADL_LINK_BITRATE_1_62_GHZ:
                return '1.62GHz'
            if bitrate == ADL_LINK_BITRATE_2_7_GHZ:
                return '2.7GHz'
            if bitrate == ADL_LINK_BTIRATE_3_24_GHZ:
                return '3.24GHz'
            if bitrate == ADL_LINK_BITRATE_5_4_GHZ:
                return '5.4GHz'

        return 'Unknown'

    @property
    def number_of_lanes(self):
        connectionData = self._connection_data
        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_NUMBER_OF_LANES == ADL_CONNECTION_PROPERTY_NUMBER_OF_LANES:
            return connectionData.aConnectionProperties.iNumberOfLanes.value

    @property
    def three_d_caps(self):
        connectionData = self._connection_data
        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_3DCAPS == ADL_CONNECTION_PROPERTY_3DCAPS:
            caps = connectionData.aConnectionProperties.iStereo3DCaps.value

            if caps & ADL_CONNPROP_S3D_ALTERNATE_TO_FRAME_PACK == ADL_CONNPROP_S3D_ALTERNATE_TO_FRAME_PACK:
                return True

        return False

    @property
    def output_bandwidth(self):
        connectionData = self._connection_data
        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_OUTPUT_BANDWIDTH == ADL_CONNECTION_PROPERTY_OUTPUT_BANDWIDTH:
            output_bandwidth = connectionData.aConnectionProperties.iOutputBandwidth.value

            if output_bandwidth == ADL_LINK_BITRATE_1_62_GHZ:
                return '1.62GHz'
            if output_bandwidth == ADL_LINK_BITRATE_2_7_GHZ:
                return '2.7GHz'
            if output_bandwidth == ADL_LINK_BTIRATE_3_24_GHZ:
                return '3.24GHz'
            if output_bandwidth == ADL_LINK_BITRATE_5_4_GHZ:
                return '5.4GHz'

        return 'Unknown'

    @property
    def color_depth(self):
        connectionData = self._connection_data
        valid_properties = connectionData.aConnectionProperties.iValidProperties.value

        if valid_properties & ADL_CONNECTION_PROPERTY_COLORDEPTH == ADL_CONNECTION_PROPERTY_COLORDEPTH:
            color_depth = connectionData.aConnectionProperties.iColorDepth.value

            if color_depth == ADL_COLORDEPTH_666:
                return '6bit'
            if color_depth == ADL_COLORDEPTH_888:
                return '8bit'
            if color_depth == ADL_COLORDEPTH_101010:
                return '10bit'
            if color_depth == ADL_COLORDEPTH_121212:
                return '12bit'
            if color_depth == ADL_COLORDEPTH_141414:
                return '14bit'
            if color_depth == ADL_COLORDEPTH_161616:
                return '16bit'

            return 'Unknown'


class AdapterPort(object):

    def __init__(self, adapter_index, id):
        self._adapter_index = adapter_index
        self.id = id

    @property
    def active_connector(self):
        for connector in self.supported_connections:
            if connector.is_connected:
                return connector

    @property
    def supported_connections(self):
        iAdapterIndex = INT(self._adapter_index)
        supportedConnections = ADLSupportedConnections()

        devicePort = ADLDevicePort()
        devicePort.iConnectorIndex = INT(self.id)
        devicePort.aMSTRad.iLinkNumber = INT(1)
        devicePort.aMSTRad.rad[0] = INT(0)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_SupportedConnections_Get(
                    context,
                    iAdapterIndex,
                    devicePort,
                    ctypes.byref(supportedConnections)
            ) != ADL_OK:
                return []

        res = []
        for i in range(14):
            if (supportedConnections.iSupportedConnections.value & (1 << i)) != (1 << i):
                continue

            if i == ADL_CONNECTION_TYPE_VGA:
                res += [PortConnector('VGA', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_DVI:
                res += [PortConnector('DVI-D', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_DVI_SL:
                res += [PortConnector('DVI-I', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_HDMI:
                res += [PortConnector('HDMI', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_DISPLAY_PORT:
                res += [PortConnector('DisplayPort', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_SL:
                res += [PortConnector('DisplayPort --> DVI-I (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_DL:
                res += [PortConnector('DisplayPort --> DVI-D (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_HDMI:
                res += [PortConnector('DisplayPort --> HDMI (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_VGA:
                res += [PortConnector('DisplayPort --> VGA (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_HDMI:
                res += [PortConnector('DisplayPort --> HDMI (Passive)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_DVI:
                res += [PortConnector('DisplayPort --> DVI (Passive)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_MST:
                res += [PortConnector('Display Branch', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE:
                res += [PortConnector('DisplayPort (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_VIRTUAL:
                res += [PortConnector('Virtual', self._adapter_index, devicePort, i)]

        return res

    @property
    def _connection_state(self):
        connectionState = ADLConnectionState()
        iAdapterIndex = INT(self._adapter_index)

        devicePort = ADLDevicePort()
        devicePort.iConnectorIndex = INT(self.id)
        devicePort.aMSTRad.iLinkNumber = INT(1)
        devicePort.aMSTRad.rad[0] = INT(0)

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

        if connectionState.iDisplayIndex.value == -1:
            return ''

        status = connectionState.iEmulationStatus.value

        if (
            status & ADL_EMUL_STATUS_REAL_DEVICE_CONNECTED ==
            ADL_EMUL_STATUS_REAL_DEVICE_CONNECTED
        ):
            return 'Real Display'

        if (
            status & ADL_EMUL_STATUS_EMULATED_DEVICE_USED ==
            ADL_EMUL_STATUS_EMULATED_DEVICE_USED
        ):
            return 'Emulated Display'
        if (
            status & ADL_EMUL_STATUS_LAST_ACTIVE_DEVICE_USED ==
            ADL_EMUL_STATUS_LAST_ACTIVE_DEVICE_USED
        ):
            return 'Last Active Display'

        return 'No Display'

    @property
    def emulation_mode(self):
        connectionState = self._connection_state
        mode = connectionState.iEmulationMode.value
        if mode == ADL_EMUL_MODE_OFF:
            return 'Off'
        if mode == ADL_EMUL_MODE_ON_CONNECTED:
            return 'When Display connected'
        if mode == ADL_EMUL_MODE_ON_DISCONNECTED:
            return 'When Display Disconnected'
        if mode == ADL_EMUL_MODE_ALWAYS:
            return 'Always'

    @property
    def device_present(self):
        connectionState = self._connection_state
        status = connectionState.iEmulationStatus.value
        return status & ADL_EMUL_STATUS_EMULATED_DEVICE_PRESENT == ADL_EMUL_STATUS_EMULATED_DEVICE_PRESENT

    @property
    def mhl_ports(self):
        iAdapterIndex = INT(self._adapter_index)

        connectionData = ADLConnectionData()
        connectionData.iActiveConnections = INT(0)
        connectionData.iNumberofPorts = INT(0)

        parentDevicePort = ADLDevicePort()
        parentDevicePort.iConnectorIndex = INT(self.id)
        parentDevicePort.aMSTRad.iLinkNumber = INT(1)
        parentDevicePort.aMSTRad.rad[0] = INT(0)

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
        devicePort.aMSTRad.iLinkNumber = INT(self._parent_device_port.aMSTRad.iLinkNumber.value + 1)
        ctypes.memset(devicePort.aMSTRad.rad, 0, ADL_MAX_RAD_LINK_COUNT)
        ctypes.memmove(
            devicePort.aMSTRad.rad, 
            self._parent_device_port.aMSTRad.rad, 
            devicePort.aMSTRad.iLinkNumber.value
        )
        devicePort.aMSTRad.rad[self._parent_device_port.aMSTRad.iLinkNumber.value] = CHAR(active_bit + 1)

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
        for i in range(14):
            if (supportedConnections.iSupportedConnections.value & (1 << i)) != (1 << i):
                continue

            if i == ADL_CONNECTION_TYPE_VGA:
                res += [PortConnector('VGA', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_DVI:
                res += [PortConnector('DVI-D', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_DVI_SL:
                res += [PortConnector('DVI-I', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_HDMI:
                res += [PortConnector('HDMI', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_DISPLAY_PORT:
                res += [PortConnector('DisplayPort', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_SL:
                res += [PortConnector('DisplayPort --> DVI-I (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_DL:
                res += [PortConnector('DisplayPort --> DVI-D (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_HDMI:
                res += [PortConnector('DisplayPort --> HDMI (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_VGA:
                res += [PortConnector('DisplayPort --> VGA (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_HDMI:
                res += [PortConnector('DisplayPort --> HDMI (Passive)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_DVI:
                res += [PortConnector('DisplayPort --> DVI (Passive)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_MST:
                res += [PortConnector('Display Branch', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_ACTIVE_DONGLE:
                res += [PortConnector('DisplayPort (Active)', self._adapter_index, devicePort, i)]
            elif i == ADL_CONNECTION_TYPE_VIRTUAL:
                res += [PortConnector('Virtual', self._adapter_index, devicePort, i)]

        return res


class Connector(object):
    def __init__(self, slot, index, id, type, offset, length):
        self.slot = slot
        self.index = index
        self.id = id
        self._type = type
        self.offset = offset
        self.length = length

    @property
    def type(self):
        if self._type == ADL_CONNECTOR_TYPE_UNKNOWN:
            return 'Unknown'
        if self._type == ADL_CONNECTOR_TYPE_VGA:
            return 'VGA'
        if self._type == ADL_CONNECTOR_TYPE_DVI_D:
            return 'DVI-D'
        if self._type == ADL_CONNECTOR_TYPE_DVI_I:
            return 'DVI-I'
        if self._type == ADL_CONNECTOR_TYPE_ATICVDONGLE_NA:
            return 'Active Dongle-NA'
        if self._type == ADL_CONNECTOR_TYPE_ATICVDONGLE_JP:
            return 'Active Dongle-JP'
        if self._type == ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C:
            return 'Active Dongle-NONI2C'
        if self._type == ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C_D:
            return 'Active Dongle-NONI2C-D'
        if self._type == ADL_CONNECTOR_TYPE_HDMI_TYPE_A:
            return 'HDMI (type A)'
        if self._type == ADL_CONNECTOR_TYPE_HDMI_TYPE_B:
            return 'HDMI (type B)'
        if self._type == ADL_CONNECTOR_TYPE_DISPLAYPORT:
            return 'DisplayPort'
        if self._type == ADL_CONNECTOR_TYPE_EDP:
            return 'EDP'
        if self._type == ADL_CONNECTOR_TYPE_MINI_DISPLAYPORT:
            return 'DisplayPort (Mini)'
        if self._type == ADL_CONNECTOR_TYPE_VIRTUAL:
            return 'Virtual'


class Slot(object):

    def __init__(self, index, length, width, connectors):

        self.index = index
        self.length = length
        self.width = width
        self._connectors = connectors

    @property
    def connectors(self):
        for connector in self._connectors:
            yield Connector(
                self,
                connector.iConnectorIndex.value,
                connector.iConnectorId.value,
                connector.iType.value,
                connector.iOffset.value,
                connector.iLength.value
            )


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

        with ADL2_Main_Control_Create as context:
            if _ADL2_FPS_Settings_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpFPSSettings),
            ) == ADL_OK:
                return lpFPSSettings

    @property
    def monitor_power(self):
        lpFPSSettings = self._fps_settings

        if lpFPSSettings.bACFPSEnabled.value:
            return 'AC'

        elif lpFPSSettings.bDCFPSEnabled.value:
            return 'DC'

        return ''

    @property
    def is_enabled(self):
        lpFPSSettings = self._fps_settings

        return bool(lpFPSSettings.bACFPSEnabled.value) or bool(lpFPSSettings.bDCFPSEnabled.value)

    @property
    def value(self):
        lpFPSSettings = self._fps_settings

        if lpFPSSettings.bACFPSEnabled.value:
            return lpFPSSettings.ulACFPSCurrent.value

        elif lpFPSSettings.bDCFPSEnabled.value:
            return lpFPSSettings.ulDCFPSCurrent.value

    @property
    def maximum(self):
        lpFPSSettings = self._fps_settings

        if lpFPSSettings.bACFPSEnabled.value:
            return lpFPSSettings.ulACFPSMaximum.value

        elif lpFPSSettings.bDCFPSEnabled.value:
            return lpFPSSettings.ulDCFPSMaximum.value

    @property
    def minimum(self):
        lpFPSSettings = self._fps_settings

        if lpFPSSettings.bACFPSEnabled.value:
            return lpFPSSettings.ulACFPSMinimum.value

        elif lpFPSSettings.bDCFPSEnabled.value:
            return lpFPSSettings.ulDCFPSMinimum.value


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
    def is_location_vlid(self):
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


class Adapter(AdapterBase):

    @property
    def error_records(self):
        iAdapterIndex = INT(self._adapter_index)
        errorRecords = (ADLErrorRecord * ADL_MAX_ERROR_RECORDS_COUNT)()
        pErrorrecordCount = INT()

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_AdapterID_Get(
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

    # _ADL2_Adapter_PMLog_Support_Get
    # _ADL2_Adapter_PMLog_Start
    # _ADL2_Adapter_PMLog_Stop

    @property
    def adapter_id(self):
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
    def core_clock(self):
        iAdapterIndex = INT(self._adapter_index)
        lpClockInfo = ADLClockInfo()

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ClockInfo_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpClockInfo),
            ) == ADL_OK:
                return lpClockInfo.iCoreClock.value

    @property
    def memory_clock(self):
        iAdapterIndex = INT(self._adapter_index)
        lpClockInfo = ADLClockInfo()

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_ClockInfo_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpClockInfo),
            ) == ADL_OK:
                return lpClockInfo.iMemoryClock.value

    @property
    def fps(self):
        return FPS(self._adapter_index)

    @property
    def ports(self):
        pAdapterCaps = ADLAdapterCapsX2()
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_AdapterX2_Caps(
                    context,
                    iAdapterIndex,
                    ctypes.byref(pAdapterCaps)
            ) != ADL_OK:
                return []
            
        res = []

        for i in range(pAdapterCaps.iNumConnectors.value):
            res += [AdapterPort(self._adapter_index, i)]
        
        return res

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
                ctypes.byref(lppBracketSlot),
                ctypes.byref(lpNumberConnector),
                ctypes.byref(lppConnector),
            ):

                connectors = {}
                for i in range(lpNumberConnector.value):
                    connector = lppConnector[i]
                    slot_index = connector.iSlotIndex.value

                    if slot_index not in connectors:
                        connectors[slot_index] = []

                    connectors[slot_index] += [connector]

                for i in range(lpNumberSlots.value):
                    slot = lppBracketSlot[i]
                    slot_index = slot.iSlotIndex.value
                    yield Slot(
                        slot_index,
                        slot.iLength.value,
                        slot.iWidth.value,
                        connectors.get(slot_index, [])
                    )

    @property
    def aspects(self):
        iSize = INT(ADL_MAX_CHAR)
        lpAspects = ctypes.create_string_buffer(ADL_MAX_CHAR)
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Adapter_Aspects_Get(context, iAdapterIndex, lpAspects, iSize)

        return lpAspects

    @property
    def memory(self):
        return Memory(self._adapter_index)

    @property
    def crossfire(self):
        return CrossFire(self._adapter_index)

    @property
    def firmware(self):
        return Firmware(self._adapter_index)

    @property
    def crossdisplay(self):
        return CrossDisplay(self._adapter_index)

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
                return lpAdapterID

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
    def supported_aspect_ratios(self):
        iSize = INT(256)
        lpAspects = (CHAR * 256)
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL_Adapter_Aspects_Get(context, iAdapterIndex, lpAspects, iSize) == ADL_OK:
                return self._get_string(lpAspects)

    @property
    def _adapter_info(self):
        lpInfo = AdapterInfo()
        lpInfo.iSize = ctypes.sizeof(AdapterInfo)
        iInputSize = INT(ctypes.sizeof(AdapterInfo))
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_AdapterInfoX2_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpInfo),
                    iInputSize
            ) == ADL_OK:
                return lpInfo

    @property
    def udid(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strUDID)

    @property
    def bus_number(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iBusNumber

    @property
    def device_number(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iDeviceNumber

    @property
    def function_number(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iFunctionNumber

    @property
    def vendor_id(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iVendorID

    @property
    def adapter_name(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strAdapterName)

    @property
    def display_name(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strDisplayName)

    @property
    def is_present(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iPresent == 1

    @property
    def exists(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iExist == 1

    @property
    def driver_path(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strDriverPath)

    @property
    def driver_path_ext(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strDriverPathExt)

    @property
    def upnp_path(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strPNPString)

    @property
    def display_index(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iOSDisplayIndex

    @property
    def driver_index(self):
        lpInfo = self._adapter_info
        if lpInfo is not None:
            return lpInfo.iDrvIndex

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
                asic_mapping = {
                    ADL_ASIC_UNDEFINED: 'Undefined',
                    ADL_ASIC_DISCRETE: 'Discrete',
                    ADL_ASIC_INTEGRATED: 'Integrated',
                    ADL_ASIC_FIREGL: 'FireGL',
                    ADL_ASIC_FIREMV: 'FireMV',
                    ADL_ASIC_XGP: 'XGP',
                    ADL_ASIC_FUSION: 'Fusion',
                    ADL_ASIC_FIRESTREAM: 'Firestream',
                    ADL_ASIC_EMBEDDED: 'Embedded'
                }

                return asic_mapping[lpAsicTypes]

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
            if _ADL_Adapter_Speed_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault)
            ) == ADL_OK:
                # not sure what to do with the values

                speed_mapping = {
                    ADL_CONTEXT_SPEED_UNFORCED: 'Unforced',
                    ADL_CONTEXT_SPEED_FORCEHIGH: 'Force High',
                    ADL_CONTEXT_SPEED_FORCELOW: 'Force_low',

                }

                return speed_mapping[lpCurrent]

            return 'Unsupported'

    @speed.setter
    def speed(self, value):

        if not isinstance(value, int):
            if value not in ('Unforced', 'Force High'):
                return

            if value == 'Force High':
                value = ADL_CONTEXT_SPEED_FORCEHIGH
            else:
                value = ADL_CONTEXT_SPEED_UNFORCED

        else:
            if value not in (
                    ADL_CONTEXT_SPEED_FORCEHIGH,
                    ADL_CONTEXT_SPEED_UNFORCED
            ):
                return

        iSpeed = INT(value)
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            _ADL_Adapter_Speed_Set(
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
            if _ADL_Adapter_Speed_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault)
            ) == ADL_OK:
                # not sure what to do with the values

                speed_mapping = {
                    ADL_CONTEXT_SPEED_UNFORCED: 'Unforced',
                    ADL_CONTEXT_SPEED_FORCEHIGH: 'Force High',
                    ADL_CONTEXT_SPEED_FORCELOW: 'Force_low',

                }

                return speed_mapping[lpDefault]

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

    @property
    def core_clock(self):
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


class CrossFire(AdapterBase):

    @property
    def is_prefered_adapter(self):
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

            return lpCrossfireInfo.iState

    @property
    def __crossfire_info(self):
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

                for i in range(lpNumComb.value):
                    lpCrossfireComb = ppCrossfireComb[i]

                    for j in range(lpCrossfireComb.iNumLinkAdapter.value):
                        adapter_index = lpCrossfireComb.iAdaptLink[j]
                        if adapter_index == self._adapter_index:
                            break
                    else:
                        continue

                    break
                else:
                    return ADL_XFIREX_STATE_ERRORGETTINGSTATUS

                lpCrossfireInfo = ADLCrossfireInfo()
                if _ADL2_Adapter_Crossfire_Get(
                        context,
                        iAdapterIndex,
                        ctypes.byref(lpCrossfireComb),
                        ctypes.byref(lpCrossfireInfo)
                ) == ADL_OK:
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


class Firmware(AdapterBase):

    @property
    def __bios_info(self):
        lpBiosInfo = AdapterInfo()
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
            return self._get_string(lpBiosInfo.strDate)

    @property
    def part_number(self):
        lpBiosInfo = self.__bios_info
        if lpBiosInfo is not None:
            return self._get_string(lpBiosInfo.strPartNumber)

    @property
    def version(self):
        lpBiosInfo = self.__bios_info
        if lpBiosInfo is not None:
            return self._get_string(lpBiosInfo.strVersion)


class Memory(AdapterBase):

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
            return lpMemoryInfo.iMemorySize.value

    @property
    def type(self):
        lpMemoryInfo = self.__memory_info
        if lpMemoryInfo is not None:
            return self._get_string(lpMemoryInfo.strMemoryType)

    @property
    def bandwidth(self):
        lpMemoryInfo = self.__memory_info
        if lpMemoryInfo is not None:
            return lpMemoryInfo.iMemoryBandwidth.value

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
                return lpMemoryClock.value
