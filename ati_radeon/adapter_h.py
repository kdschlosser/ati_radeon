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






