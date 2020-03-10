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
from .adl_defines_h import *  # NOQA
from .adl_defines_h import _WIN32, _WIN64
import ctypes


class AdapterInfo(ctypes.Structure):
    pass


LPAdapterInfo = POINTER(AdapterInfo)


class XScreenInfo(ctypes.Structure):
    pass


LPXScreenInfo = POINTER(XScreenInfo)


class ADLMemoryInfo(ctypes.Structure):
    pass


LPADLMemoryInfo = POINTER(ADLMemoryInfo)


class ADLMemoryRequired(ctypes.Structure):
    pass


LPADLMemoryRequired = POINTER(ADLMemoryRequired)


class ADLMemoryDisplayFeatures(ctypes.Structure):
    pass


LPADLMemoryDisplayFeatures = POINTER(ADLMemoryDisplayFeatures)


class ADLDDCInfo(ctypes.Structure):
    pass


LPADLDDCInfo = POINTER(ADLDDCInfo)


class ADLDDCInfo2(ctypes.Structure):
    pass


LPADLDDCInfo2 = POINTER(ADLDDCInfo2)


class ADLGamma(ctypes.Structure):
    pass


LPADLGamma = POINTER(ADLGamma)


class ADLCustomMode(ctypes.Structure):
    pass


LPADLCustomMode = POINTER(ADLCustomMode)


class ADLGetClocksOUT(ctypes.Structure):
    pass


class ADLDisplayConfig(ctypes.Structure):
    pass


class ADLDisplayID(ctypes.Structure):
    pass


LPADLDisplayID = POINTER(ADLDisplayID)


class ADLDisplayInfo(ctypes.Structure):
    pass


LPADLDisplayInfo = POINTER(ADLDisplayInfo)


class ADLDisplayDPMSTInfo(ctypes.Structure):
    pass


LPADLDisplayDPMSTInfo = POINTER(ADLDisplayDPMSTInfo)


class ADLDisplayMode(ctypes.Structure):
    pass


class ADLDetailedTiming(ctypes.Structure):
    pass


class ADLDisplayModeInfo(ctypes.Structure):
    pass


class ADLDisplayProperty(ctypes.Structure):
    pass


class ADLClockInfo(ctypes.Structure):
    pass


LPADLClockInfo = POINTER(ADLClockInfo)


class ADLI2C(ctypes.Structure):
    pass


class ADLDisplayEDIDData(ctypes.Structure):
    pass


class ADLControllerOverlayInput(ctypes.Structure):
    pass


class ADLAdjustmentinfo(ctypes.Structure):
    pass


class ADLControllerOverlayInfo(ctypes.Structure):
    pass


class ADLGLSyncModuleID(ctypes.Structure):
    pass


LPADLGLSyncModuleID = POINTER(ADLGLSyncModuleID)


class ADLGLSyncPortCaps(ctypes.Structure):
    pass


LPADLGLSyncPortCaps = POINTER(ADLGLSyncPortCaps)


class ADLGLSyncGenlockConfig(ctypes.Structure):
    pass


LPADLGLSyncGenlockConfig = POINTER(ADLGLSyncGenlockConfig)


class ADLGlSyncPortInfo(ctypes.Structure):
    pass


LPADLGlSyncPortInfo = POINTER(ADLGlSyncPortInfo)


class ADLGlSyncPortControl(ctypes.Structure):
    pass


class ADLGlSyncMode(ctypes.Structure):
    pass


LPADLGlSyncMode = POINTER(ADLGlSyncMode)


class ADLGlSyncMode2(ctypes.Structure):
    pass


LPADLGlSyncMode2 = POINTER(ADLGlSyncMode2)


class ADLInfoPacket(ctypes.Structure):
    pass


class ADLAVIInfoPacket(ctypes.Structure):
    pass


class ADLODClockSetting(ctypes.Structure):
    pass


class ADLAdapterODClockInfo(ctypes.Structure):
    pass


class ADLAdapterODClockConfig(ctypes.Structure):
    pass


class ADLPMActivity(ctypes.Structure):
    pass


class ADLThermalControllerInfo(ctypes.Structure):
    pass


class ADLTemperature(ctypes.Structure):
    pass


class ADLFanSpeedInfo(ctypes.Structure):
    pass


class ADLFanSpeedValue(ctypes.Structure):
    pass


class ADLODParameterRange(ctypes.Structure):
    pass


class ADLODParameters(ctypes.Structure):
    pass


class ADLODPerformanceLevel(ctypes.Structure):
    pass


class ADLODPerformanceLevels(ctypes.Structure):
    pass


class ADLCrossfireComb(ctypes.Structure):
    pass


class ADLCrossfireInfo(ctypes.Structure):
    pass


class ADLBiosInfo(ctypes.Structure):
    pass


LPADLBiosInfo = POINTER(ADLBiosInfo)


class ADLAdapterLocation(ctypes.Structure):
    pass


ADLBdf = ADLAdapterLocation


class ADLVersionsInfo(ctypes.Structure):
    pass


LPADLVersionsInfo = POINTER(ADLVersionsInfo)


class ADLVersionsInfoX2(ctypes.Structure):
    pass


LPADLVersionsInfoX2 = POINTER(ADLVersionsInfoX2)


class ADLMVPUCaps(ctypes.Structure):
    pass


class ADLMVPUStatus(ctypes.Structure):
    pass


class ADLActivatableSource(ctypes.Structure):
    pass


LPADLActivatableSource = POINTER(ADLActivatableSource)


class ADLMode(ctypes.Structure):
    pass


LPADLMode = POINTER(ADLMode)


class ADLDisplayTarget(ctypes.Structure):
    pass


LPADLDisplayTarget = POINTER(ADLDisplayTarget)


class tagADLBezelTransientMode(ctypes.Structure):
    pass


ADLBezelTransientMode = tagADLBezelTransientMode
LPADLBezelTransientMode = POINTER(tagADLBezelTransientMode)


class ADLAdapterDisplayCap(ctypes.Structure):
    pass


LPADLAdapterDisplayCap = POINTER(ADLAdapterDisplayCap)


class ADLDisplayMap(ctypes.Structure):
    pass


LPADLDisplayMap = POINTER(ADLDisplayMap)


class ADLPossibleMap(ctypes.Structure):
    pass


LPADLPossibleMap = POINTER(ADLPossibleMap)


class ADLPossibleMapping(ctypes.Structure):
    pass


LPADLPossibleMapping = POINTER(ADLPossibleMapping)


class ADLPossibleMapResult(ctypes.Structure):
    pass


LPADLPossibleMapResult = POINTER(ADLPossibleMapResult)


class ADLSLSGrid(ctypes.Structure):
    pass


LPADLSLSGrid = POINTER(ADLSLSGrid)


class ADLSLSMap(ctypes.Structure):
    pass


LPADLSLSMap = POINTER(ADLSLSMap)


class ADLSLSOffset(ctypes.Structure):
    pass


LPADLSLSOffset = POINTER(ADLSLSOffset)


class ADLSLSMode(ctypes.Structure):
    pass


LPADLSLSMode = POINTER(ADLSLSMode)


class ADLPossibleSLSMap(ctypes.Structure):
    pass


LPADLPossibleSLSMap = POINTER(ADLPossibleSLSMap)


class ADLSLSTarget(ctypes.Structure):
    pass


LPADLSLSTarget = POINTER(ADLSLSTarget)


class ADLBezelOffsetSteppingSize(ctypes.Structure):
    pass


LPADLBezelOffsetSteppingSize = POINTER(ADLBezelOffsetSteppingSize)


class ADLSLSOverlappedMode(ctypes.Structure):
    pass


ADLSLSTargetOverlap = ADLSLSOverlappedMode
LPADLSLSTargetOverlap = POINTER(ADLSLSOverlappedMode)


class ADLPXConfigCaps(ctypes.Structure):
    pass


LPADLPXConfigCaps = POINTER(ADLPXConfigCaps)


class _ADLApplicationData(ctypes.Structure):
    pass


ADLApplicationData = _ADLApplicationData


class _ADLApplicationDataX2(ctypes.Structure):
    pass


ADLApplicationDataX2 = _ADLApplicationDataX2


class _ADLApplicationDataX3(ctypes.Structure):
    pass


ADLApplicationDataX3 = _ADLApplicationDataX3


class _PropertyRecord(ctypes.Structure):
    pass


PropertyRecord = _PropertyRecord


class _ADLApplicationProfile(ctypes.Structure):
    pass


ADLApplicationProfile = _ADLApplicationProfile


class ADLPowerControlInfo(ctypes.Structure):
    pass


class _ADLControllerMode(ctypes.Structure):
    pass


ADLControllerMode = _ADLControllerMode


class ADLDisplayIdentifier(ctypes.Structure):
    pass


class _ADLOD6ParameterRange(ctypes.Structure):
    pass


ADLOD6ParameterRange = _ADLOD6ParameterRange


class _ADLOD6Capabilities(ctypes.Structure):
    pass


ADLOD6Capabilities = _ADLOD6Capabilities


class _ADLOD6PerformanceLevel(ctypes.Structure):
    pass


ADLOD6PerformanceLevel = _ADLOD6PerformanceLevel


class _ADLOD6StateInfo(ctypes.Structure):
    pass


ADLOD6StateInfo = _ADLOD6StateInfo


class _ADLOD6CurrentStatus(ctypes.Structure):
    pass


ADLOD6CurrentStatus = _ADLOD6CurrentStatus


class _ADLOD6ThermalControllerCaps(ctypes.Structure):
    pass


ADLOD6ThermalControllerCaps = _ADLOD6ThermalControllerCaps


class _ADLOD6FanSpeedInfo(ctypes.Structure):
    pass


ADLOD6FanSpeedInfo = _ADLOD6FanSpeedInfo


class _ADLOD6FanSpeedValue(ctypes.Structure):
    pass


ADLOD6FanSpeedValue = _ADLOD6FanSpeedValue


class _ADLOD6PowerControlInfo(ctypes.Structure):
    pass


ADLOD6PowerControlInfo = _ADLOD6PowerControlInfo


class _ADLOD6VoltageControlInfo(ctypes.Structure):
    pass


ADLOD6VoltageControlInfo = _ADLOD6VoltageControlInfo


class _ADLECCData(ctypes.Structure):
    pass


ADLECCData = _ADLECCData


class ADLDisplayModeX2(ctypes.Structure):
    pass


class _ADLOD6CapabilitiesEx(ctypes.Structure):
    pass


ADLOD6CapabilitiesEx = _ADLOD6CapabilitiesEx


class _ADLOD6StateEx(ctypes.Structure):
    pass


ADLOD6StateEx = _ADLOD6StateEx


class _ADLOD6MaxClockAdjust(ctypes.Structure):
    pass


ADLOD6MaxClockAdjust = _ADLOD6MaxClockAdjust


class ADLConnectorInfo(ctypes.Structure):
    pass


class ADLBracketSlotInfo(ctypes.Structure):
    pass


class ADLMSTRad(ctypes.Structure):
    pass


class ADLDevicePort(ctypes.Structure):
    pass


class ADLSupportedConnections(ctypes.Structure):
    pass


class ADLConnectionState(ctypes.Structure):
    pass


class ADLConnectionProperties(ctypes.Structure):
    pass


class ADLConnectionData(ctypes.Structure):
    pass


class ADLAdapterCapsX2(ctypes.Structure):
    pass


class _ADL_ECC_EDC_FLAG(ctypes.Union):
    pass


ADL_ECC_EDC_FLAG = _ADL_ECC_EDC_FLAG


class ADLErrorRecord(ctypes.Structure):
    pass


class _ADL_ERROR_PATTERN(ctypes.Union):
    pass


ADL_ERROR_PATTERN = _ADL_ERROR_PATTERN


class _ADL_ERROR_INJECTION_DATA(ctypes.Structure):
    pass


ADL_ERROR_INJECTION_DATA = _ADL_ERROR_INJECTION_DATA


class ADLErrorInjection(ctypes.Structure):
    pass


class ADLErrorInjectionX2(ctypes.Structure):
    pass


class ADLFreeSyncCap(ctypes.Structure):
    pass


class _ADLDceSettings(ctypes.Structure):
    pass


ADLDceSettings = _ADLDceSettings


class ADLGraphicCoreInfo(ctypes.Structure):
    pass


class _ADLODNParameterRange(ctypes.Structure):
    pass


ADLODNParameterRange = _ADLODNParameterRange


class _ADLODNCapabilities(ctypes.Structure):
    pass


ADLODNCapabilities = _ADLODNCapabilities


class _ADLODNCapabilitiesX2(ctypes.Structure):
    pass


ADLODNCapabilitiesX2 = _ADLODNCapabilitiesX2


class ADLODNPerformanceLevel(ctypes.Structure):
    pass


class ADLODNPerformanceLevels(ctypes.Structure):
    pass


class ADLODNFanControl(ctypes.Structure):
    pass


class ADLODNPowerLimitSetting(ctypes.Structure):
    pass


class ADLODNPerformanceStatus(ctypes.Structure):
    pass


class ADLODNPerformanceLevelX2(ctypes.Structure):
    pass


class ADLODNPerformanceLevelsX2(ctypes.Structure):
    pass


class _ADLODNCurrentPowerParameters(ctypes.Structure):
    pass


ADLODNCurrentPowerParameters = _ADLODNCurrentPowerParameters


class _ADLODNExtSingleInitSetting(ctypes.Structure):
    pass


ADLODNExtSingleInitSetting = _ADLODNExtSingleInitSetting


class _ADLOD8SingleInitSetting(ctypes.Structure):
    pass


ADLOD8SingleInitSetting = _ADLOD8SingleInitSetting


class _ADLOD8InitSetting(ctypes.Structure):
    pass


ADLOD8InitSetting = _ADLOD8InitSetting


class _ADLOD8CurrentSetting(ctypes.Structure):
    pass


ADLOD8CurrentSetting = _ADLOD8CurrentSetting


class _ADLOD8SingleSetSetting(ctypes.Structure):
    pass


ADLOD8SingleSetSetting = _ADLOD8SingleSetSetting


class _ADLOD8SetSetting(ctypes.Structure):
    pass


ADLOD8SetSetting = _ADLOD8SetSetting


class _ADLSingleSensorData(ctypes.Structure):
    pass


ADLSingleSensorData = _ADLSingleSensorData


class _ADLPMLogDataOutput(ctypes.Structure):
    pass


ADLPMLogDataOutput = _ADLPMLogDataOutput


class ADLPPLogSettings(ctypes.Structure):
    pass


class _ADLFPSSettingsOutput(ctypes.Structure):
    pass


ADLFPSSettingsOutput = _ADLFPSSettingsOutput


class _ADLFPSSettingsInput(ctypes.Structure):
    pass


ADLFPSSettingsInput = _ADLFPSSettingsInput


class _ADLPMLogSupportInfo(ctypes.Structure):
    pass


ADLPMLogSupportInfo = _ADLPMLogSupportInfo


class _ADLPMLogStartInput(ctypes.Structure):
    pass


ADLPMLogStartInput = _ADLPMLogStartInput


class _ADLPMLogData(ctypes.Structure):
    pass


ADLPMLogData = _ADLPMLogData


class _ADLPMLogStartOutput(ctypes.Structure):
    pass


ADLPMLogStartOutput = _ADLPMLogStartOutput


class _ADLRASGetErrorCountsInput(ctypes.Structure):
    pass


ADLRASGetErrorCountsInput = _ADLRASGetErrorCountsInput


class _ADLRASGetErrorCountsOutput(ctypes.Structure):
    pass


ADLRASGetErrorCountsOutput = _ADLRASGetErrorCountsOutput


class _ADLRASGetErrorCounts(ctypes.Structure):
    pass


ADLRASGetErrorCounts = _ADLRASGetErrorCounts


class _ADLRASResetErrorCountsInput(ctypes.Structure):
    pass


ADLRASResetErrorCountsInput = _ADLRASResetErrorCountsInput


class _ADLRASResetErrorCountsOutput(ctypes.Structure):
    pass


ADLRASResetErrorCountsOutput = _ADLRASResetErrorCountsOutput


class _ADLRASResetErrorCounts(ctypes.Structure):
    pass


ADLRASResetErrorCounts = _ADLRASResetErrorCounts


class _ADLRASErrorInjectonInput(ctypes.Structure):
    pass


ADLRASErrorInjectonInput = _ADLRASErrorInjectonInput


class _ADLRASErrorInjectionOutput(ctypes.Structure):
    pass


ADLRASErrorInjectionOutput = _ADLRASErrorInjectionOutput


class _ADLRASErrorInjection(ctypes.Structure):
    pass


ADLRASErrorInjection = _ADLRASErrorInjection


class _ADLSGApplicationInfo(ctypes.Structure):
    pass


ADLSGApplicationInfo = _ADLSGApplicationInfo


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
# / \file adl_structures.h
# /\brief This file contains the structure declarations that are used by the
# public ADL interfaces for \ALL platforms.\n < b > Included in ADL SDK < /b >
# /
# / All data structures used in AMD Display Library (ADL) public interfaces
# should be defined in this header file.
# /


# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the graphics adapter.
# /
# / This structure is used to store various information about the graphics
# adapter. This
# / information can be returned to the user. Alternatively, it can be used
# to access various driver calls to set
# / or fetch various settings upon the user's request.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_TEMP_AdapterInfo = [
    # / Size of the structure.
    ('iSize', INT),
    # / The ADL index handle. One GPU may be associated with one or two
    # index handles
    ('iAdapterIndex', INT),
    # / The unique device ID associated with this adapter.
    ('strUDID', CHAR * ADL_MAX_PATH),
    # / The BUS number associated with this adapter.
    ('iBusNumber', INT),
    # / The driver number associated with this adapter.
    ('iDeviceNumber', INT),
    # / The function number.
    ('iFunctionNumber', INT),
    # / The vendor ID associated with this adapter.
    ('iVendorID', INT),
    # / Adapter name.
    ('strAdapterName', CHAR * ADL_MAX_PATH),
    # / Display name. For example, "\\\\Display0" for Windows or ":0:0"
    # for Linux.
    ('strDisplayName', CHAR * ADL_MAX_PATH),
    # / Present or not; 1 if present and 0 if not present.It the logical
    # adapter is present, the display name such as \\\\.\\Display1 can be
    # found from OS
    ('iPresent', INT),
]


if defined(_WIN32) or defined(_WIN64):
    _TEMP_AdapterInfo += [
        # / Exist or not; 1 is exist and 0 is not present.
        ('iExist', INT),
        # / Driver registry path.
        ('strDriverPath', CHAR * ADL_MAX_PATH),
        # / Driver registry path Ext for.
        ('strDriverPathExt', CHAR * ADL_MAX_PATH),
        # / PNP string from Windows.
        ('strPNPString', CHAR * ADL_MAX_PATH),
        # / It is generated from EnumDisplayDevices.
        ('iOSDisplayIndex', INT),
    ]
# END IF   (_WIN32) or (_WIN64)

if defined(LINUX):
    _TEMP_AdapterInfo += [
        # / Internal X screen number from GPUMapInfo
        # (DEPRICATED use XScreenInfo)
        ('iXScreenNum', INT),
        # / Internal driver index from GPUMapInfo
        ('iDrvIndex', INT),
        # / \deprecated Internal x config file screen identifier name. Use
        # XScreenInfo instead.
        ('strXScreenConfigName', CHAR * ADL_MAX_PATH),
    ]
# END IF   (LINUX)


AdapterInfo._fields_ = _TEMP_AdapterInfo

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the Linux X screen
# information.
# /
# / This structure is used to store the current screen number and
# xorg.conf ID name assoicated with an adapter index.
# / This structure is updated during ADL_Main_Control_Refresh or
# ADL_ScreenInfo_Update.
# / Note: This structure should be used in place of iXScreenNum and
# strXScreenConfigName in AdapterInfo as they will be
# / deprecated.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
if defined(LINUX):
    XScreenInfo._fields_ = [
        # / Internal X screen number from GPUMapInfo.
        ('iXScreenNum', INT),
        # / Internal x config file screen identifier name.
        ('strXScreenConfigName', CHAR * ADL_MAX_PATH),
    ]
# END IF  (LINUX)

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the ASIC memory.
# /
# / This structure is used to store various information about the ASIC
# memory. This
# / information can be returned to the user.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLMemoryInfo._fields_ = [
    # / Memory size in bytes.
    ('iMemorySize', LONGLONG),
    # / Memory type in string.
    ('strMemoryType', CHAR * ADL_MAX_PATH),
    # / Memory bandwidth in Mbytes/s.
    ('iMemoryBandwidth', LONGLONG),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about memory required by type
# /
# / This structure is returned by ADL_Adapter_ConfigMemory_Get, which
# given a desktop and display configuration
# / will return the Memory used.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLMemoryRequired._fields_ = [
    # / Memory in bytes required
    ('iMemoryReq', LONGLONG),
    # / Type of Memory \ref define_adl_validmemoryrequiredfields
    ('iType', INT),
    # / Display features \ref define_adl_visiblememoryfeatures that are
    # using this type of memory
    ('iDisplayFeatureValue', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the features associated
# with a display
# /
# / This structure is a parameter to ADL_Adapter_ConfigMemory_Get, which
# given a desktop and display configuration
# / will return the Memory used.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLMemoryDisplayFeatures._fields_ = [
    # / ADL Display index
    ('iDisplayIndex', INT),
    # / features that the display is using \ref
    # define_adl_visiblememoryfeatures
    ('iDisplayFeatureValue', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing DDC information.
# /
# / This structure is used to store various DDC information that can be
# returned to the user.
# / Note that all fields of type INT are actually defined as UINT types
# within the driver.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDDCInfo._fields_ = [
    # / Size of the structure
    ('ulSize', INT),
    # / Indicates whether the attached display supports DDC. If this field
    # is zero on return, no other DDC information fields will be used.
    ('ulSupportsDDC', INT),
    # / Returns the manufacturer ID of the display device. Should be
    # zeroed if this information is not available.
    ('ulManufacturerID', INT),
    # / Returns the product ID of the display device. Should be zeroed if
    # this information is not available.
    ('ulProductID', INT),
    # / Returns the name of the display device. Should be zeroed if this
    # information is not available.
    ('cDisplayName', CHAR * ADL_MAX_DISPLAY_NAME),
    # / Returns the maximum Horizontal supported resolution. Should be
    # zeroed if this information is not available.
    ('ulMaxHResolution', INT),
    # / Returns the maximum Vertical supported resolution. Should be
    # zeroed if this information is not available.
    ('ulMaxVResolution', INT),
    # / Returns the maximum supported refresh rate. Should be zeroed if
    # this information is not available.
    ('ulMaxRefresh', INT),
    # / Returns the display device preferred timing mode's horizontal
    # resolution.
    ('ulPTMCx', INT),
    # / Returns the display device preferred timing mode's vertical
    # resolution.
    ('ulPTMCy', INT),
    # / Returns the display device preferred timing mode's refresh rate.
    ('ulPTMRefreshRate', INT),
    # / Return EDID flags.
    ('ulDDCInfoFlag', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing DDC information.
# /
# / This structure is used to store various DDC information that can be
# returned to the user.
# / Note that all fields of type INT are actually defined as UINT types
# within the driver.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDDCInfo2._fields_ = [
    # / Size of the structure
    ('ulSize', INT),
    # / information fields will be used.
    ('ulSupportsDDC', INT),
    # / Returns the manufacturer ID of the display device. Should be
    # zeroed if this information is not available.
    ('ulManufacturerID', INT),
    # / Returns the product ID of the display device. Should be zeroed if
    # this information is not available.
    ('ulProductID', INT),
    # / Returns the name of the display device. Should be zeroed if this
    # information is not available.
    ('cDisplayName', CHAR * ADL_MAX_DISPLAY_NAME),
    # / Returns the maximum Horizontal supported resolution. Should be
    # zeroed if this information is not available.
    ('ulMaxHResolution', INT),
    # / Returns the maximum Vertical supported resolution. Should be
    # zeroed if this information is not available.
    ('ulMaxVResolution', INT),
    # / Returns the maximum supported refresh rate. Should be zeroed if
    # this information is not available.
    ('ulMaxRefresh', INT),
    # / Returns the display device preferred timing mode's horizontal
    # resolution.
    ('ulPTMCx', INT),
    # / Returns the display device preferred timing mode's vertical
    # resolution.
    ('ulPTMCy', INT),
    # / Returns the display device preferred timing mode's refresh rate.
    ('ulPTMRefreshRate', INT),
    # / Return EDID flags.
    ('ulDDCInfoFlag', INT),
    # / Returns 1 if the display supported packed pixel, 0 otherwise
    ('bPackedPixelSupported', INT),
    # / Returns the Pixel formats the display supports \ref
    # define_ddcinfo_pixelformats
    ('iPanelPixelFormat', INT),
    # / Return EDID serial ID.
    ('ulSerialID', INT),
    # / Return minimum monitor luminance data
    ('ulMinLuminanceData', INT),
    # / Return average monitor luminance data
    ('ulAvgLuminanceData', INT),
    # / Return maximum monitor luminance data
    ('ulMaxLuminanceData', INT),
    # / Bit vector of supported transfer functions \ref
    # define_source_content_TF
    ('iSupportedTransferFunction', INT),
    # / Bit vector of supported color spaces \ref define_source_content_CS
    ('iSupportedColorSpace', INT),
    # / Display Red Chromaticity X coordinate multiplied by 10000
    ('iNativeDisplayChromaticityRedX', INT),
    # / Display Red Chromaticity Y coordinate multiplied by 10000
    ('iNativeDisplayChromaticityRedY', INT),
    # / Display Green Chromaticity X coordinate multiplied by 10000
    ('iNativeDisplayChromaticityGreenX', INT),
    # / Display Green Chromaticity Y coordinate multiplied by 10000
    ('iNativeDisplayChromaticityGreenY', INT),
    # / Display Blue Chromaticity X coordinate multiplied by 10000
    ('iNativeDisplayChromaticityBlueX', INT),
    # / Display Blue Chromaticity Y coordinate multiplied by 10000
    ('iNativeDisplayChromaticityBlueY', INT),
    # / Display White Point X coordinate multiplied by 10000
    ('iNativeDisplayChromaticityWhitePointX', INT),
    # / Display White Point Y coordinate multiplied by 10000
    ('iNativeDisplayChromaticityWhitePointY', INT),
    # / Display diffuse screen reflectance 0-1 (100%) in units of 0.01
    ('iDiffuseScreenReflectance', INT),
    # / Display specular screen reflectance 0-1 (100%) in units of 0.01
    ('iSpecularScreenReflectance', INT),
    # / Bit vector of supported color spaces \ref define_HDR_support
    ('iSupportedHDR', INT),
    # / Bit vector for freesync flags
    ('iFreesyncFlags', INT),
    # / Return minimum monitor luminance without dimming data
    ('ulMinLuminanceNoDimmingData', INT),
    ('ulMaxBacklightMaxLuminanceData', INT),
    ('ulMinBacklightMaxLuminanceData', INT),
    ('ulMaxBacklightMinLuminanceData', INT),
    ('ulMinBacklightMinLuminanceData', INT),
    # Reserved for future use
    ('iReserved', INT * 4),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information controller Gamma settings.
# /
# / This structure is used to store the red, green and blue color channel
# information for the.
# / controller gamma setting. This information is returned by ADL, and it
# can also be used to
# / set the controller gamma setting.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGamma._fields_ = [
    # / Red color channel gamma value.
    ('fRed', FLOAT),
    # / Green color channel gamma value.
    ('fGreen', FLOAT),
    # / Blue color channel gamma value.
    ('fBlue', FLOAT),
]


# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about component video custom
# modes.
# /
# / This structure is used to store the component video custom mode.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLCustomMode._fields_ = [
    # / Custom mode flags. They are returned by the ADL driver.
    ('iFlags', INT),
    # / Custom mode width.
    ('iModeWidth', INT),
    # / Custom mode height.
    ('iModeHeight', INT),
    # / Custom mode base width.
    ('iBaseModeWidth', INT),
    # / Custom mode base height.
    ('iBaseModeHeight', INT),
    # / Custom mode refresh rate.
    ('iRefreshRate', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing Clock information for OD5 calls.
# /
# / This structure is used to retrieve clock information for OD5 calls.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGetClocksOUT._fields_ = [
    ('ulHighCoreClock', LONG),
    ('ulHighMemoryClock', LONG),
    ('ulHighVddc', LONG),
    ('ulCoreMin', LONG),
    ('ulCoreMax', LONG),
    ('ulMemoryMin', LONG),
    ('ulMemoryMax', LONG),
    ('ulActivityPercent', LONG),
    ('ulCurrentCoreClock', LONG),
    ('ulCurrentMemoryClock', LONG),
    ('ulReserved', LONG),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing HDTV information for display calls.
# /
# / This structure is used to retrieve HDTV information information for
# display calls.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayConfig._fields_ = [
    # / Size of the structure
    ('ulSize', LONG),
    # / HDTV connector type.
    ('ulConnectorType', LONG),
    # / HDTV capabilities.
    ('ulDeviceData', LONG),
    # / Overridden HDTV capabilities.
    ('ulOverridedDeviceData', LONG),
    # / Reserved field
    ('ulReserved', LONG),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display device.
# /
# / This structure is used to store display device information
# / such as display index, type, name, connection status, mapped adapter
# and controller indexes,
# / whether or not multiple VPUs are supported, local display connections
# or not (through Lasso), etc.
# / This information can be returned to the user. Alternatively, it can be
# used to access various driver calls to set
# / or fetch various display device related settings upon the user's
# request.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayID._fields_ = [
    # / The logical display index belonging to this adapter.
    ('iDisplayLogicalIndex', INT),
    # / index is still 2.
    ('iDisplayPhysicalIndex', INT),
    # / The persistent logical adapter index for the display.
    ('iDisplayLogicalAdapterIndex', INT),
    # / the Display Non Local flag is set inside DisplayInfoValue.
    ('iDisplayPhysicalAdapterIndex', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display device.
# /
# / This structure is used to store various information about the display
# device. This
# / information can be returned to the user, or used to access various
# driver calls to set
# / or fetch various display-device-related settings upon the user's
# request
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayInfo._fields_ = [
    # / The DisplayID structure
    ('displayID', ADLDisplayID),
    # /\deprecated The controller index to which the display is mapped.\n
    # Will not be used in the future\n
    ('iDisplayControllerIndex', INT),
    # / The display's EDID name.
    ('strDisplayName', CHAR * ADL_MAX_PATH),
    # / The display's manufacturer name.
    ('strDisplayManufacturerName', CHAR * ADL_MAX_PATH),
    # / The Display type. For example: CRT, TV, CV, DFP.
    ('iDisplayType', INT),
    # / The display output type. For example: HDMI, SVIDEO, COMPONMNET
    # VIDEO.
    ('iDisplayOutputType', INT),
    # / The connector type for the device.
    ('iDisplayConnector', INT),
    # / It will be the sum all the bit definitions in
    # ADL_DISPLAY_DISPLAYINFO_xxx.
    ('iDisplayInfoMask', INT),
    # / The bit mask identifies the display status. \ref
    # define_displayinfomask
    ('iDisplayInfoValue', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display port MST
# device.
# /
# / This structure is used to store various MST information about the
# display port device. This
# / information can be returned to the user, or used to access various
# driver calls to
# / fetch various display-device-related settings upon the user's request
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayDPMSTInfo._fields_ = [
    # / The ADLDisplayID structure
    ('displayID', ADLDisplayID),
    # / total bandwidth available on the DP connector
    ('iTotalAvailableBandwidthInMpbs', INT),
    # / bandwidth allocated to this display
    ('iAllocatedBandwidthInMbps', INT),
    # / string identifier for the display
    ('strGlobalUniqueIdentifier', CHAR * ADL_MAX_PATH),
    # / The link count of relative address, rad[0] upto rad[linkCount] are
    # valid
    ('radLinkCount', INT),
    # / The physical connector ID, used to identify the physical DP port
    ('iPhysicalConnectorID', INT),
    # / Relative address, address scheme starts from source side
    ('rad', CHAR * ADL_MAX_RAD_LINK_COUNT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the display mode definition used per
# controller.
# /
# / This structure is used to store the display mode definition used per
# controller.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayMode._fields_ = [
    # / Vertical resolution (in pixels).
    ('iPelsHeight', INT),
    # / Horizontal resolution (in pixels).
    ('iPelsWidth', INT),
    # / Color depth.
    ('iBitsPerPel', INT),
    # / Refresh rate.
    ('iDisplayFrequency', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing detailed timing parameters.
# /
# / This structure is used to store the detailed timing parameters.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDetailedTiming._fields_ = [
    # / Size of the structure.
    ('iSize', INT),
    # / Timing flags. \ref define_detailed_timing_flags
    ('sTimingFlags', SHORT),
    # / Total width (columns).
    ('sHTotal', SHORT),
    # / Displayed width.
    ('sHDisplay', SHORT),
    # / Horizontal sync signal offset.
    ('sHSyncStart', SHORT),
    # / Horizontal sync signal width.
    ('sHSyncWidth', SHORT),
    # / Total height (rows).
    ('sVTotal', SHORT),
    # / Displayed height.
    ('sVDisplay', SHORT),
    # / Vertical sync signal offset.
    ('sVSyncStart', SHORT),
    # / Vertical sync signal width.
    ('sVSyncWidth', SHORT),
    # / Pixel clock value.
    ('sPixelClock', SHORT),
    # / Overscan right.
    ('sHOverscanRight', SHORT),
    # / Overscan left.
    ('sHOverscanLeft', SHORT),
    # / Overscan bottom.
    ('sVOverscanBottom', SHORT),
    # / Overscan top.
    ('sVOverscanTop', SHORT),
    ('sOverscan8B', SHORT),
    ('sOverscanGR', SHORT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing display mode information.
# /
# / This structure is used to store the display mode information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayModeInfo._fields_ = [
    # / Timing standard of the current mode. \ref
    # define_modetiming_standard
    ('iTimingStandard', INT),
    # / Applicable timing standards for the current mode.
    ('iPossibleStandard', INT),
    # / Refresh rate factor.
    ('iRefreshRate', INT),
    # / Num of pixels in a row.
    ('iPelsWidth', INT),
    # / Num of pixels in a column.
    ('iPelsHeight', INT),
    # / Detailed timing parameters.
    ('sDetailedTiming', ADLDetailedTiming),
]

# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about display property.
# /
# / This structure is used to store the display property for the current
# adapter.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayProperty._fields_ = [
    # / Must be set to (ctypes.sizeof the structure
    ('iSize', INT),
    # / Must be set to \ref ADL_DL_DISPLAYPROPERTY_TYPE_EXPANSIONMODE or
    # \ref ADL_DL_DISPLAYPROPERTY_TYPE_USEUNDERSCANSCALING
    ('iPropertyType', INT),
    # / Get or Set \ref ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_CENTER or
    # \ref ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_FULLSCREEN or \ref
    # ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_ASPECTRATIO or \ref
    # ADL_DL_DISPLAYPROPERTY_TYPE_ITCFLAGENABLE
    ('iExpansionMode', INT),
    # / Display Property supported? 1: Supported, 0: Not supported
    ('iSupport', INT),
    # / Display Property current value
    ('iCurrent', INT),
    # / Display Property Default value
    ('iDefault', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Clock.
# /
# / This structure is used to store the clock information for the current
# adapter
# / such as core clock and memory clock info.
# /\nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLClockInfo._fields_ = [
    # / Core clock in 10 KHz.
    ('iCoreClock', INT),
    # / Memory clock in 10 KHz.
    ('iMemoryClock', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about I2C.
# /
# / This structure is used to store the I2C information for the current
# adapter.
# / This structure is used by the ADL_Display_WriteAndReadI2C() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLI2C._fields_ = [
    # / Size of the structure
    ('iSize', INT),
    # / Numerical value representing hardware I2C.
    ('iLine', INT),
    # / The 7-bit I2C slave device address, shifted one bit to the left.
    ('iAddress', INT),
    # / The offset of the data from the address.
    ('iOffset', INT),
    # / Read from or write to slave device. \ref ADL_DL_I2C_ACTIONREAD or
    # \ref ADL_DL_I2C_ACTIONWRITE or \ref
    # ADL_DL_I2C_ACTIONREAD_REPEATEDSTART
    ('iAction', INT),
    # / I2C clock speed in KHz.
    ('iSpeed', INT),
    # / A numerical value representing the number of bytes to be sent or
    # received on the I2C bus.
    ('iDataSize', INT),
    # / Address of the characters which are to be sent or received on the
    # I2C bus.
    ('pcData', POINTER(CHAR)),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about EDID data.
# /
# / This structure is used to store the information about EDID data for
# the adapter.
# / This structure is used by the ADL_Display_EdidData_Get() and
# ADL_Display_EdidData_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayEDIDData._fields_ = [
    # / Size of the structure
    ('iSize', INT),
    # / Set to 0
    ('iFlag', INT),
    # / Size of cEDIDData. Set by ADL_Display_EdidData_Get() upon return
    ('iEDIDSize', INT),
    # / 0, 1 or 2. If set to 3 or above an error ADL_ERR_INVALID_PARAM is
    # generated
    ('iBlockIndex', INT),
    # / EDID data
    ('cEDIDData', CHAR * ADL_MAX_EDIDDATA_SIZE),
    # / Reserved
    ('iReserved', INT * 4),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about input of controller
# overlay adjustment.
# /
# / This structure is used to store the information about input of
# controller overlay adjustment for the adapter.
# / This structure is used by the
# ADL_Display_ControllerOverlayAdjustmentCaps_Get,
# ADL_Display_ControllerOverlayAdjustmentData_Get, and
# / ADL_Display_ControllerOverlayAdjustmentData_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLControllerOverlayInput._fields_ = [
    # / Should be set to the (ctypes.sizeof the structure
    ('iSize', INT),
    # /\ref ADL_DL_CONTROLLER_OVERLAY_ALPHA or \ref
    # ADL_DL_CONTROLLER_OVERLAY_ALPHAPERPIX
    ('iOverlayAdjust', INT),
    # / Data.
    ('iValue', INT),
    # / Should be 0.
    ('iReserved', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about overlay adjustment.
# /
# / This structure is used to store the information about overlay
# adjustment for the adapter.
# / This structure is used by the ADLControllerOverlayInfo() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLAdjustmentinfo._fields_ = [
    # / Default value
    ('iDefault', INT),
    # / Minimum value
    ('iMin', INT),
    # / Maximum Value
    ('iMax', INT),
    # / Step value
    ('iStep', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about controller overlay
# information.
# /
# / This structure is used to store information about controller overlay
# info for the adapter.
# / This structure is used by the
# ADL_Display_ControllerOverlayAdjustmentCaps_Get() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLControllerOverlayInfo._fields_ = [
    # / Should be set to the (ctypes.sizeof the structure
    ('iSize', INT),
    # / Data.
    ('sOverlayInfo', ADLAdjustmentinfo),
    # / Should be 0.
    ('iReserved', INT * 3),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing GL-Sync module information.
# /
# / This structure is used to retrieve GL-Sync module information for
# / Workstation Framelock/Genlock.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGLSyncModuleID._fields_ = [
    # / Unique GL-Sync module ID.
    ('iModuleID', INT),
    # / GL-Sync GPU port index
    # (to be passed into ADLGLSyncGenlockConfig.lSignalSource and ADLGlSyncPortControl.lSignalSource).
    # 
    ('iGlSyncGPUPort', INT),
    # / GL-Sync module firmware version of Boot Sector.
    ('iFWBootSectorVersion', INT),
    # / GL-Sync module firmware version of User Sector.
    ('iFWUserSectorVersion', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing GL-Sync ports capabilities.
# /
# / This structure is used to retrieve hardware capabilities for the ports
# of the GL-Sync module
# / for Workstation Framelock/Genlock
# (such as port type and number of associated LEDs).
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGLSyncPortCaps._fields_ = [
    # / Port type. Bitfield of ADL_GLSYNC_PORTTYPE_* \ref define_glsync
    ('iPortType', INT),
    # / Number of LEDs associated for this port.
    ('iNumOfLEDs', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing GL-Sync Genlock settings.
# /
# / This structure is used to get and set genlock settings for the GPU
# ports of the GL-Sync module
# / for Workstation Framelock/Genlock.\n
# / \see define_glsync
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGLSyncGenlockConfig._fields_ = [
    # / Specifies what fields in this structure are valid \ref
    # define_glsync
    ('iValidMask', INT),
    # / Delay (ms) generating a sync signal.
    ('iSyncDelay', INT),
    # / Vector of framelock control bits. Bitfield of
    # ADL_GLSYNC_FRAMELOCKCNTL_* \ref define_glsync
    ('iFramelockCntlVector', INT),
    # / Source of the sync signal. Either GL_Sync GPU Port index or
    # ADL_GLSYNC_SIGNALSOURCE_* \ref define_glsync
    ('iSignalSource', INT),
    # / Use sampled sync signal. A value of 0 specifies no sampling.
    ('iSampleRate', INT),
    # / For interlaced sync signals, the value can be
    # ADL_GLSYNC_SYNCFIELD_1 or *_BOTH \ref define_glsync
    ('iSyncField', INT),
    # / The signal edge that should trigger synchronization.
    # ADL_GLSYNC_TRIGGEREDGE_* \ref define_glsync
    ('iTriggerEdge', INT),
    # / Scan rate multiplier applied to the sync signal.
    # ADL_GLSYNC_SCANRATECOEFF_* \ref define_glsync
    ('iScanRateCoeff', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing GL-Sync port information.
# /
# / This structure is used to get status of the GL-Sync ports
# (BNC or RJ45s)
# / for Workstation Framelock/Genlock.
# / \see define_glsync
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGlSyncPortInfo._fields_ = [
    # / Type of GL-Sync port (ADL_GLSYNC_PORT_*).
    ('iPortType', INT),
    # / The number of LEDs for this port. It's also filled within
    # ADLGLSyncPortCaps.
    ('iNumOfLEDs', INT),
    # / Port state ADL_GLSYNC_PORTSTATE_* \ref define_glsync
    ('iPortState', INT),
    # / Scanned frequency for this port
    # (vertical refresh rate in milliHz; 60000 means 60 Hz).
    ('iFrequency', INT),
    # / Used for ADL_GLSYNC_PORT_BNC. It is ADL_GLSYNC_SIGNALTYPE_* \ref
    # define_glsync
    ('iSignalType', INT),
    # / Used for ADL_GLSYNC_PORT_RJ45PORT*. It is GL_Sync GPU Port index
    # or ADL_GLSYNC_SIGNALSOURCE_*. \ref define_glsync
    ('iSignalSource', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing GL-Sync port control settings.
# /
# / This structure is used to configure the GL-Sync ports (RJ45s only)
# / for Workstation Framelock/Genlock.
# / \see define_glsync
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGlSyncPortControl._fields_ = [
    # / Port to control ADL_GLSYNC_PORT_RJ45PORT1 or
    # ADL_GLSYNC_PORT_RJ45PORT2 \ref define_glsync
    ('iPortType', INT),
    # / Port control data ADL_GLSYNC_PORTCNTL_* \ref define_glsync
    ('iControlVector', INT),
    # / Source of the sync signal. Either GL_Sync GPU Port index or
    # ADL_GLSYNC_SIGNALSOURCE_* \ref define_glsync
    ('iSignalSource', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing GL-Sync mode of a display.
# /
# / This structure is used to get and set GL-Sync mode settings for a
# display connected to
# / an adapter attached to a GL-Sync module for Workstation
# Framelock/Genlock.
# / \see define_glsync
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGlSyncMode._fields_ = [
    # / Mode control vector. Bitfield of ADL_GLSYNC_MODECNTL_* \ref
    # define_glsync
    ('iControlVector', INT),
    # / Mode status vector. Bitfield of ADL_GLSYNC_MODECNTL_STATUS_* \ref
    # define_glsync
    ('iStatusVector', INT),
    # / Index of GL-Sync connector used to genlock the display/controller.
    ('iGLSyncConnectorIndex', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing GL-Sync mode of a display.
# /
# / This structure is used to get and set GL-Sync mode settings for a
# display connected to
# / an adapter attached to a GL-Sync module for Workstation
# Framelock/Genlock.
# / \see define_glsync
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGlSyncMode2._fields_ = [
    # / Mode control vector. Bitfield of ADL_GLSYNC_MODECNTL_* \ref
    # define_glsync
    ('iControlVector', INT),
    # / Mode status vector. Bitfield of ADL_GLSYNC_MODECNTL_STATUS_* \ref
    # define_glsync
    ('iStatusVector', INT),
    # / Index of GL-Sync connector used to genlock the display/controller.
    ('iGLSyncConnectorIndex', INT),
    # / Index of the display to which this GLSync applies to.
    ('iDisplayIndex', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the packet info of a display.
# /
# / This structure is used to get and set the packet information of a
# display.
# / This structure is used by ADLDisplayDataPacket.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLInfoPacket._fields_ = [
    ('hb0', CHAR),
    ('hb1', CHAR),
    ('hb2', CHAR),
    # / sb0~sb27
    ('sb', CHAR * 28),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the AVI packet info of a display.
# /
# / This structure is used to get and set AVI the packet info of a display.
# / This structure is used by ADLDisplayDataPacket.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLAVIInfoPacket._fields_ = [
    # / byte 3, bit 7
    ('bPB3_ITC', CHAR),
    # / byte 5, bit [7:4].
    ('bPB5', CHAR),
]
# Overdrive clock setting structure definition.
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the Overdrive clock setting.
# /
# / This structure is used to get the Overdrive clock setting.
# / This structure is used by ADLAdapterODClockInfo.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODClockSetting._fields_ = [
    # / Deafult clock
    ('iDefaultClock', INT),
    # / Current clock
    ('iCurrentClock', INT),
    # / Maximum clcok
    ('iMaxClock', INT),
    # / Minimum clock
    ('iMinClock', INT),
    # / Requested clcock
    ('iRequestedClock', INT),
    # / Step
    ('iStepClock', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the Overdrive clock information.
# /
# / This structure is used to get the Overdrive clock information.
# / This structure is used by the ADL_Display_ODClockInfo_Get() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLAdapterODClockInfo._fields_ = [
    # / Size of the structure
    ('iSize', INT),
    # / Flag \ref define_clockinfo_flags
    ('iFlags', INT),
    # / Memory Clock
    ('sMemoryClock', ADLODClockSetting),
    # / Engine Clock
    ('sEngineClock', ADLODClockSetting),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the Overdrive clock configuration.
# /
# / This structure is used to set the Overdrive clock configuration.
# / This structure is used by the ADL_Display_ODClockConfig_Set() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLAdapterODClockConfig._fields_ = [
    # / Size of the structure
    ('iSize', INT),
    # / Flag \ref define_clockinfo_flags
    ('iFlags', INT),
    # / Memory Clock
    ('iMemoryClock', INT),
    # / Engine Clock
    ('iEngineClock', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about current power management
# related activity.
# /
# / This structure is used to store information about current power
# management related activity.
# / This structure (Overdrive 5 interfaces) is used by the
# ADL_PM_CurrentActivity_Get() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLPMActivity._fields_ = [
    # / Must be set to the size of the structure
    ('iSize', INT),
    # / Current engine clock.
    ('iEngineClock', INT),
    # / Current memory clock.
    ('iMemoryClock', INT),
    # / Current core voltage.
    ('iVddc', INT),
    # / GPU utilization.
    ('iActivityPercent', INT),
    # / Performance level index.
    ('iCurrentPerformanceLevel', INT),
    # / Current PCIE bus speed.
    ('iCurrentBusSpeed', INT),
    # / Number of PCIE bus lanes.
    ('iCurrentBusLanes', INT),
    # / Maximum number of PCIE bus lanes.
    ('iMaximumBusLanes', INT),
    # / Reserved for future purposes.
    ('iReserved', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about thermal controller.
# /
# / This structure is used to store information about thermal controller.
# / This structure is used by ADL_PM_ThermalDevices_Enum.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLThermalControllerInfo._fields_ = [
    # / Must be set to the size of the structure
    ('iSize', INT),
    # / Possible valies: \ref ADL_DL_THERMAL_DOMAIN_OTHER or \ref
    # ADL_DL_THERMAL_DOMAIN_GPU.
    ('iThermalDomain', INT),
    # / GPU 0, 1, etc.
    ('iDomainIndex', INT),
    # / Possible valies: \ref ADL_DL_THERMAL_FLAG_INTERRUPT or \ref
    # ADL_DL_THERMAL_FLAG_FANCONTROL
    ('iFlags', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about thermal controller
# temperature.
# /
# / This structure is used to store information about thermal controller
# temperature.
# / This structure is used by the ADL_PM_Temperature_Get() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLTemperature._fields_ = [
    # / Must be set to the size of the structure
    ('iSize', INT),
    # / Temperature in millidegrees Celsius.
    ('iTemperature', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about thermal controller fan
# speed.
# /
# / This structure is used to store information about thermal controller
# fan speed.
# / This structure is used by the ADL_PM_FanSpeedInfo_Get() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLFanSpeedInfo._fields_ = [
    # / Must be set to the size of the structure
    ('iSize', INT),
    # / \ref define_fanctrl
    ('iFlags', INT),
    # / Minimum possible fan speed value in percents.
    ('iMinPercent', INT),
    # / Maximum possible fan speed value in percents.
    ('iMaxPercent', INT),
    # / Minimum possible fan speed value in RPM.
    ('iMinRPM', INT),
    # / Maximum possible fan speed value in RPM.
    ('iMaxRPM', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about fan speed reported by
# thermal controller.
# /
# / This structure is used to store information about fan speed reported
# by thermal controller.
# / This structure is used by the ADL_Overdrive5_FanSpeed_Get() and
# ADL_Overdrive5_FanSpeed_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLFanSpeedValue._fields_ = [
    # / Must be set to the size of the structure
    ('iSize', INT),
    # / Possible valies: \ref ADL_DL_FANCTRL_SPEED_TYPE_PERCENT or \ref
    # ADL_DL_FANCTRL_SPEED_TYPE_RPM
    ('iSpeedType', INT),
    # / Fan speed value
    ('iFanSpeed', INT),
    # / The only flag for now is: \ref
    # ADL_DL_FANCTRL_FLAG_USER_DEFINED_SPEED
    ('iFlags', INT),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the range of Overdrive parameter.
# /
# / This structure is used to store information about the range of
# Overdrive parameter.
# / This structure is used by ADLODParameters.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODParameterRange._fields_ = [
    # / Minimum parameter value.
    ('iMin', INT),
    # / Maximum parameter value.
    ('iMax', INT),
    # / Parameter step value.
    ('iStep', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive parameters.
# /
# / This structure is used to store information about Overdrive parameters.
# / This structure is used by the ADL_Overdrive5_ODParameters_Get()
# function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODParameters._fields_ = [
    # / Must be set to the size of the structure
    ('iSize', INT),
    # / Number of standard performance states.
    ('iNumberOfPerformanceLevels', INT),
    # / Indicates whether the GPU is capable to measure its activity.
    ('iActivityReportingSupported', INT),
    # / Indicates whether the GPU supports discrete performance levels or
    # performance range.
    ('iDiscretePerformanceLevels', INT),
    # / Reserved for future use.
    ('iReserved', INT),
    # / Engine clock range.
    ('sEngineClock', ADLODParameterRange),
    # / Memory clock range.
    ('sMemoryClock', ADLODParameterRange),
    # / Core voltage range.
    ('sVddc', ADLODParameterRange),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive level.
# /
# / This structure is used to store information about Overdrive level.
# / This structure is used by ADLODPerformanceLevels.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODPerformanceLevel._fields_ = [
    # / Engine clock.
    ('iEngineClock', INT),
    # / Memory clock.
    ('iMemoryClock', INT),
    # / Core voltage.
    ('iVddc', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive performance
# levels.
# /
# / This structure is used to store information about Overdrive
# performance levels.
# / This structure is used by the ADL_Overdrive5_ODPerformanceLevels_Get()
# and ADL_Overdrive5_ODPerformanceLevels_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODPerformanceLevels._fields_ = [
    # / Must be set to
    # (ctypes.sizeof( \ref ADLODPerformanceLevels ) +
    # (ctypes.sizeof( \ref ADLODPerformanceLevel ) *
    # (ADLODParameters.iNumberOfPerformanceLevels - 1)
    # 
    ('iSize', INT),
    ('iReserved', INT),
    # / Array of performance state descriptors. Must have
    # ADLODParameters.iNumberOfPerformanceLevels elements.
    ('aLevels', ADLODPerformanceLevel * 1),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the proper CrossfireX
# chains combinations.
# /
# / This structure is used to store information about the CrossfireX
# chains combination for a particular adapter.
# / This structure is used by the ADL_Adapter_Crossfire_Caps(),
# ADL_Adapter_Crossfire_Get(), and ADL_Adapter_Crossfire_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLCrossfireComb._fields_ = [
    # / Number of adapters in this combination.
    ('iNumLinkAdapter', INT),
    # / A list of ADL indexes of the linked adapters in this combination.
    ('iAdaptLink', INT * 3),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing CrossfireX state and error information.
# /
# / This structure is used to store state and error information about a
# particular adapter CrossfireX combination.
# / This structure is used by the ADL_Adapter_Crossfire_Get() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLCrossfireInfo._fields_ = [
    # / Current error code of this CrossfireX combination.
    ('iErrorCode', INT),
    # / Current \ref define_crossfirestate
    ('iState', INT),
    # / If CrossfireX is supported by this combination. The value is
    # either \ref ADL_TRUE or \ref ADL_FALSE.
    ('iSupported', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about the BIOS.
# /
# / This structure is used to store various information about the Chipset.
# This
# / information can be returned to the user.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLBiosInfo._fields_ = [
    # / < Part number.
    ('strPartNumber', CHAR * ADL_MAX_PATH),
    # / < Version number.
    ('strVersion', CHAR * ADL_MAX_PATH),
    # / < BIOS date in yyyy/mm/dd hh:mm format.
    ('strDate', CHAR * ADL_MAX_PATH),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about adapter location.
# /
# / This structure is used to store information about adapter location.
# / This structure is used by ADLMVPUStatus.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLAdapterLocation._fields_ = [
    # / PCI Bus number : 8 bits
    ('iBus', INT),
    # / Device number : 5 bits
    ('iDevice', INT),
    # / Function number : 3 bits
    ('iFunction', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing version information
# /
# / This structure is used to store software version information,
# description of the display device and a web link to the latest installed
# Catalyst drivers.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLVersionsInfo._fields_ = [
    # / Driver Release (Packaging) Version (e.g. 8.71-100128n-094835E-ATI)
    ('strDriverVer', CHAR * ADL_MAX_PATH),
    # / Catalyst Version(e.g. "10.1").
    ('strCatalystVersion', CHAR * ADL_MAX_PATH),
    # ('Web link to an XML file with information about the latest AMD drivers and locations
    # (e.g. "http', /// * ADL_MAX_PATH, //www.amd.com/us/driverxml" ) CHAR strCatalystWebLink),
    ('strCatalystWebLink', CHAR * ADL_MAX_PATH)
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing version information
# /
# / This structure is used to store software version information,
# description of the display device and a web link to the latest installed
# Catalyst drivers.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLVersionsInfoX2._fields_ = [
    # / Driver Release (Packaging) Version
    # (e.g. "16.20.1035-160621a-303814C")
    ('strDriverVer', CHAR * ADL_MAX_PATH),
    # / Catalyst Version(e.g. "15.8").
    ('strCatalystVersion', CHAR * ADL_MAX_PATH),
    # / Crimson Version(e.g. "16.6.2").
    ('strCrimsonVersion', CHAR * ADL_MAX_PATH),
    # ('Web link to an XML file with information about the latest AMD drivers and locations
    # (e.g. "http', /// * ADL_MAX_PATH, //support.amd.com/drivers/xml/driver_09_us.xml" ) CHAR strCatalystWebLink),
    ('strCatalystWebLink', CHAR * ADL_MAX_PATH)
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about MultiVPU capabilities.
# /
# / This structure is used to store information about MultiVPU
# capabilities.
# / This structure is used by the ADL_Display_MVPUCaps_Get() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLMVPUCaps._fields_ = [
    # / Must be set to (ctypes.sizeof( ADLMVPUCaps ).
    ('iSize', INT),
    # / Number of adapters.
    ('iAdapterCount', INT),
    # / Bits set for all possible MVPU masters. \ref MVPU_ADAPTER_0 ..
    # \ref MVPU_ADAPTER_3
    ('iPossibleMVPUMasters', INT),
    # / Bits set for all possible MVPU slaves. \ref MVPU_ADAPTER_0 .. \ref
    # MVPU_ADAPTER_3
    ('iPossibleMVPUSlaves', INT),
    # / Registry path for each adapter.
    ('cAdapterPath', (CHAR * ADL_DL_MAX_MVPU_ADAPTERS)(CHAR * ADL_DL_MAX_REGISTRY_PATH)),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about MultiVPU status.
# /
# / This structure is used to store information about MultiVPU status.
# / Ths structure is used by the ADL_Display_MVPUStatus_Get() function.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLMVPUStatus._fields_ = [
    # / Must be set to (ctypes.sizeof( ADLMVPUStatus ).
    ('iSize', INT),
    # / Number of active adapters.
    ('iActiveAdapterCount', INT),
    # / MVPU status.
    ('iStatus', INT),
    # / PCI Bus/Device/Function for each active adapter participating in
    # MVPU.
    ('aAdapterLocation', ADLAdapterLocation * ADL_DL_MAX_MVPU_ADAPTERS),
]
# Displays Manager structures
# /////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about the activatable source.
# /
# / This structure is used to store activatable source information
# / This information can be returned to the user.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLActivatableSource._fields_ = [
    # / The Persistent logical Adapter Index.
    ('iAdapterIndex', INT),
    # / The number of Activatable Sources.
    ('iNumActivatableSources', INT),
    # / The bit mask identifies the number of bits ActivatableSourceValue
    # is using. (Not currnetly used)
    ('iActivatableSourceMask', INT),
    # / The bit mask identifies the status. (Not currnetly used)
    ('iActivatableSourceValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about display mode.
# /
# / This structure is used to store the display mode for the current
# adapter
# / such as X, Y positions, screen resolutions, orientation,
# / color depth, refresh rate, progressive or interlace mode, etc.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLMode._fields_ = [
    # / Adapter index.
    ('iAdapterIndex', INT),
    # / Display IDs.
    ('displayID', ADLDisplayID),
    # / Screen position X coordinate.
    ('iXPos', INT),
    # / Screen position Y coordinate.
    ('iYPos', INT),
    # / Screen resolution Width.
    ('iXRes', INT),
    # / Screen resolution Height.
    ('iYRes', INT),
    # / Screen Color Depth. E.g., 16, 32.
    ('iColourDepth', INT),
    # / Screen refresh rate. Could be fractional E.g. 59.97
    ('fRefreshRate', FLOAT),
    # / Screen orientation. E.g., 0, 90, 180, 270.
    ('iOrientation', INT),
    # / Vista mode flag indicating Progressive or Interlaced mode.
    ('iModeFlag', INT),
    # / The bit mask identifying the number of bits this Mode is currently
    # using. It is the sum of all the bit definitions defined in \ref
    # define_displaymode
    ('iModeMask', INT),
    # / The bit mask identifying the display status. The detailed
    # definition is in \ref define_displaymode
    ('iModeValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about display target
# information.
# /
# / This structure is used to store the display target information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayTarget._fields_ = [
    # / The Display ID.
    ('displayID', ADLDisplayID),
    # / The display map index identify this manner and the desktop surface.
    ('iDisplayMapIndex', INT),
    # / The bit mask identifies the number of bits DisplayTarget is
    # currently using. It is the sum of all the bit definitions defined in
    # \ref ADL_DISPLAY_DISPLAYTARGET_PREFERRED.
    ('iDisplayTargetMask', INT),
    # / The bit mask identifies the display status. The detailed
    # definition is in \ref ADL_DISPLAY_DISPLAYTARGET_PREFERRED.
    ('iDisplayTargetValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display SLS bezel
# Mode information.
# /
# / This structure is used to store the display SLS bezel Mode information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
tagADLBezelTransientMode._fields_ = [
    # / Adapter Index
    ('iAdapterIndex', INT),
    # / SLS Map Index
    ('iSLSMapIndex', INT),
    # / The mode index
    ('iSLSModeIndex', INT),
    # / The mode
    ('displayMode', ADLMode),
    # / The number of bezel offsets belongs to this map
    ('iNumBezelOffset', INT),
    # / The first bezel offset array index in the native mode array
    ('iFirstBezelOffsetArrayIndex', INT),
    # / The bit mask identifies the bits this structure is currently
    # using. It will be the total OR of all the bit definitions.
    ('iSLSBezelTransientModeMask', INT),
    # / The bit mask identifies the display status. The detail definition
    # is defined below.
    ('iSLSBezelTransientModeValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about the adapter display
# manner.
# /
# / This structure is used to store adapter display manner information
# / This information can be returned to the user. Alternatively, it can be
# used to access various driver calls to
# / fetch various display device related display manner settings upon the
# user's request.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLAdapterDisplayCap._fields_ = [
    # / The Persistent logical Adapter Index.
    ('iAdapterIndex', INT),
    # / The bit mask identifies the number of bits AdapterDisplayCap is
    # currently using. Sum all the bits defined in
    # ADL_ADAPTER_DISPLAYCAP_XXX
    ('iAdapterDisplayCapMask', INT),
    # / The bit mask identifies the status. Refer to
    # ADL_ADAPTER_DISPLAYCAP_XXX
    ('iAdapterDisplayCapValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about display mapping.
# /
# / This structure is used to store the display mapping data such as
# display manner.
# / For displays with horizontal or vertical stretch manner,
# / this structure also stores the display order, display row, and column
# data.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayMap._fields_ = [
    # / The current display map index. It is the OS desktop index. For
    # example, if the OS index 1 is showing clone mode, the display map
    # will be 1.
    ('iDisplayMapIndex', INT),
    # / The Display Mode for the current map
    ('displayMode', ADLMode),
    # / The number of display targets belongs to this map\n
    ('iNumDisplayTarget', INT),
    # / The first target array index in the Target array\n
    ('iFirstDisplayTargetArrayIndex', INT),
    # / The bit mask identifies the number of bits DisplayMap is currently
    # using. It is the sum of all the bit definitions defined in
    # ADL_DISPLAY_DISPLAYMAP_MANNER_xxx.
    ('iDisplayMapMask', INT),
    # /The bit mask identifies the display status. The detailed definition
    # is in ADL_DISPLAY_DISPLAYMAP_MANNER_xxx.
    ('iDisplayMapValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about the display device
# possible map for one GPU
# /
# / This structure is used to store the display device possible map
# / This information can be returned to the user.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLPossibleMap._fields_ = [
    # / The current PossibleMap index. Each PossibleMap is assigned an
    # index
    ('iIndex', INT),
    # / The adapter index identifying the GPU for which to validate these
    # Maps & Targets
    ('iAdapterIndex', INT),
    # / Number of display Maps for this GPU to be validated
    ('iNumDisplayMap', INT),
    # / The display Maps list to validate
    ('displayMap', POINTER(ADLDisplayMap)),
    # / the number of display Targets for these display Maps
    ('iNumDisplayTarget', INT),
    # / The display Targets list for these display Maps to be validated.
    ('displayTarget', POINTER(ADLDisplayTarget)),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about display possible mapping.
# /
# / This structure is used to store the display possible mapping's
# controller index for the current display.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLPossibleMapping._fields_ = [
    # / < The display index. Each display is assigned an index.
    ('iDisplayIndex', INT),
    # / < The controller index to which display is mapped.
    ('iDisplayControllerIndex', INT),
    # / < The supported display manner.
    ('iDisplayMannerSupported', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# / \brief Structure containing information about the validated display
# device possible map result.
# /
# / This structure is used to store the validated display device possible
# map result
# / This information can be returned to the user.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLPossibleMapResult._fields_ = [
    # / The current display map index. It is the OS Desktop index. For
    # example, OS Index 1 showing clone mode. The Display Map will be 1.
    ('iIndex', INT),
    # The bit mask identifies the number of bits PossibleMapResult is
    # currently using. It will be the sum all the bit definitions defined
    # in ADL_DISPLAY_POSSIBLEMAPRESULT_VALID.
    ('iPossibleMapResultMask', INT),
    # / The bit mask identifies the possible map result. The detail
    # definition is defined in ADL_DISPLAY_POSSIBLEMAPRESULT_XXX.
    ('iPossibleMapResultValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display SLS Grid
# information.
# /
# / This structure is used to store the display SLS Grid information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLSLSGrid._fields_ = [
    # / The Adapter index.
    ('iAdapterIndex', INT),
    # / The grid index.
    ('iSLSGridIndex', INT),
    # / The grid row.
    ('iSLSGridRow', INT),
    # / The grid column.
    ('iSLSGridColumn', INT),
    # / The grid bit mask identifies the number of bits DisplayMap is
    # currently using. Sum of all bits defined in
    # ADL_DISPLAY_SLSGRID_ORIENTATION_XXX
    ('iSLSGridMask', INT),
    # / The grid bit value identifies the display status. Refer to
    # ADL_DISPLAY_SLSGRID_ORIENTATION_XXX
    ('iSLSGridValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display SLS Map
# information.
# /
# / This structure is used to store the display SLS Map information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLSLSMap._fields_ = [
    # / The Adapter Index
    ('iAdapterIndex', INT),
    # / The current display map index. It is the OS Desktop index. For
    # example, OS Index 1 showing clone mode. The Display Map will be 1.
    ('iSLSMapIndex', INT),
    # / Indicate the current grid
    ('grid', ADLSLSGrid),
    # / OS surface index
    ('iSurfaceMapIndex', INT),
    # / Screen orientation. E.g., 0, 90, 180, 270
    ('iOrientation', INT),
    # / The number of display targets belongs to this map
    ('iNumSLSTarget', INT),
    # / The first target array index in the Target array
    ('iFirstSLSTargetArrayIndex', INT),
    # / The number of native modes belongs to this map
    ('iNumNativeMode', INT),
    # / The first native mode array index in the native mode array
    ('iFirstNativeModeArrayIndex', INT),
    # / The number of bezel modes belongs to this map
    ('iNumBezelMode', INT),
    # / The first bezel mode array index in the native mode array
    ('iFirstBezelModeArrayIndex', INT),
    # / The number of bezel offsets belongs to this map
    ('iNumBezelOffset', INT),
    # / The first bezel offset array index in the
    ('iFirstBezelOffsetArrayIndex', INT),
    # / The bit mask identifies the number of bits DisplayMap is currently
    # using. Sum all the bit definitions defined in ADL_DISPLAY_SLSMAP_XXX.
    ('iSLSMapMask', INT),
    # / The bit mask identifies the display map status. Refer to
    # ADL_DISPLAY_SLSMAP_XXX
    ('iSLSMapValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display SLS Offset
# information.
# /
# / This structure is used to store the display SLS Offset information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLSLSOffset._fields_ = [
    # / The Adapter Index
    ('iAdapterIndex', INT),
    # / The current display map index. It is the OS Desktop index. For
    # example, OS Index 1 showing clone mode. The Display Map will be 1.
    ('iSLSMapIndex', INT),
    # / The Display ID.
    ('displayID', ADLDisplayID),
    # / SLS Bezel Mode Index
    ('iBezelModeIndex', INT),
    # / SLS Bezel Offset X
    ('iBezelOffsetX', INT),
    # / SLS Bezel Offset Y
    ('iBezelOffsetY', INT),
    # / SLS Display Width
    ('iDisplayWidth', INT),
    # / SLS Display Height
    ('iDisplayHeight', INT),
    # / The bit mask identifies the number of bits Offset is currently
    # using.
    ('iBezelOffsetMask', INT),
    # / The bit mask identifies the display status.
    ('iBezelffsetValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display SLS Mode
# information.
# /
# / This structure is used to store the display SLS Mode information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLSLSMode._fields_ = [
    # / The Adapter Index
    ('iAdapterIndex', INT),
    # / The current display map index. It is the OS Desktop index. For
    # example, OS Index 1 showing clone mode. The Display Map will be 1.
    ('iSLSMapIndex', INT),
    # / The mode index
    ('iSLSModeIndex', INT),
    # / The mode for this map.
    ('displayMode', ADLMode),
    # / The bit mask identifies the number of bits Mode is currently using.
    ('iSLSNativeModeMask', INT),
    # / The bit mask identifies the display status.
    ('iSLSNativeModeValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the display Possible SLS
# Map information.
# /
# / This structure is used to store the display Possible SLS Map
# information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLPossibleSLSMap._fields_ = [
    # / For example, OS Index 1 showing clone mode. The Display Map will
    # be 1.
    ('iSLSMapIndex', INT),
    # / Number of display map to be validated.
    ('iNumSLSMap', INT),
    # / The display map list for validation
    ('lpSLSMap', POINTER(ADLSLSMap)),
    # / the number of display map config to be validated.
    ('iNumSLSTarget', INT),
    # / The display target list for validation.
    ('lpDisplayTarget', POINTER(ADLDisplayTarget)),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the SLS targets.
# /
# / This structure is used to store the SLS targets information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLSLSTarget._fields_ = [
    # / the logic adapter index
    ('iAdapterIndex', INT),
    # / The SLS map index
    ('iSLSMapIndex', INT),
    # / The target ID
    ('displayTarget', ADLDisplayTarget),
    # / Target postion X in SLS grid
    ('iSLSGridPositionX', INT),
    # / Target postion Y in SLS grid
    ('iSLSGridPositionY', INT),
    # / The view size width, height and rotation angle per SLS Target
    ('viewSize', ADLMode),
    # / The bit mask identifies the bits in iSLSTargetValue are currently
    # used
    ('iSLSTargetMask', INT),
    # / The bit mask identifies status info. It is for function extension
    # purpose
    ('iSLSTargetValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the Adapter offset
# stepping size.
# /
# / This structure is used to store the Adapter offset stepping size
# information.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLBezelOffsetSteppingSize._fields_ = [
    # / the logic adapter index
    ('iAdapterIndex', INT),
    # / The SLS map index
    ('iSLSMapIndex', INT),
    # / Bezel X stepping size offset
    ('iBezelOffsetSteppingSizeX', INT),
    # / Bezel Y stepping size offset
    ('iBezelOffsetSteppingSizeY', INT),
    # / Identifies the bits this structure is currently using. It will be
    # the total OR of all the bit definitions.
    ('iBezelOffsetSteppingSizeMask', INT),
    # / Bit mask identifies the display status.
    ('iBezelOffsetSteppingSizeValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about the overlap offset info
# for all the displays for each SLS mode.
# /
# / This structure is used to store the no. of overlapped modes for each
# SLS Mode once user finishes the configuration from Overlap Widget
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLSLSOverlappedMode._fields_ = [
    # / the SLS mode for which the overlap is configured
    ('SLSMode', ADLMode),
    # / the number of target displays in SLS.
    ('iNumSLSTarget', INT),
    # / the first target array index in the target array
    ('iFirstTargetArrayIndex', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about driver supported
# PowerExpress Config Caps
# /
# / This structure is used to store the driver supported PowerExpress
# Config Caps
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLPXConfigCaps._fields_ = [
    # / The Persistent logical Adapter Index.
    ('iAdapterIndex', INT),
    # / The bit mask identifies the number of bits PowerExpress Config
    # Caps is currently using. It is the sum of all the bit definitions
    # defined in ADL_PX_CONFIGCAPS_XXXX /ref define_powerxpress_constants.
    ('iPXConfigCapMask', INT),
    # / The bit mask identifies the PowerExpress Config Caps value. The
    # detailed definition is in ADL_PX_CONFIGCAPS_XXXX /ref
    # define_powerxpress_constants.
    ('iPXConfigCapValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about an application
# /
# / This structure is used to store basic information of an application
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLApplicationData._fields_ = [
    # / Path Name
    ('strPathName', CHAR * ADL_MAX_PATH),
    # / File Name
    ('strFileName', CHAR * ADL_APP_PROFILE_FILENAME_LENGTH),
    # / Creation timestamp
    ('strTimeStamp', CHAR * ADL_APP_PROFILE_TIMESTAMP_LENGTH),
    # / Version
    ('strVersion', CHAR * ADL_APP_PROFILE_VERSION_LENGTH),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about an application
# /
# / This structure is used to store basic information of an application
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLApplicationDataX2._fields_ = [
    # / Path Name
    ('strPathName', WCHAR * ADL_MAX_PATH),
    # / File Name
    ('strFileName', WCHAR * ADL_APP_PROFILE_FILENAME_LENGTH),
    # / Creation timestamp
    ('strTimeStamp', WCHAR * ADL_APP_PROFILE_TIMESTAMP_LENGTH),
    # / Version
    ('strVersion', WCHAR * ADL_APP_PROFILE_VERSION_LENGTH),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about an application
# /
# / This structure is used to store basic information of an application
# including process id
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLApplicationDataX3._fields_ = [
    # / Path Name
    ('strPathName', WCHAR * ADL_MAX_PATH),
    # / File Name
    ('strFileName', WCHAR * ADL_APP_PROFILE_FILENAME_LENGTH),
    # / Creation timestamp
    ('strTimeStamp', WCHAR * ADL_APP_PROFILE_TIMESTAMP_LENGTH),
    # / Version
    ('strVersion', WCHAR * ADL_APP_PROFILE_VERSION_LENGTH),
    # Application Process id
    ('iProcessId', UINT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information of a property of an application
# profile
# /
# / This structure is used to store property information of an application
# profile
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_PropertyRecord._fields_ = [
    # / Property Name
    ('strName', CHAR * ADL_APP_PROFILE_PROPERTY_LENGTH),
    # / Property Type
    ('eType', ADLProfilePropertyType),
    # / Data Size in bytes
    ('iDataSize', INT),
    # / Property Value, can be any data type
    ('uData', UCHAR * 1),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about an application profile
# /
# / This structure is used to store information of an application profile
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLApplicationProfile._fields_ = [
    # / Number of properties
    ('iCount', INT),
    # / Buffer to store all property records
    ('record', PropertyRecord * 1),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about an OD5 Power Control
# feature
# /
# / This structure is used to store information of an Power Control feature
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLPowerControlInfo._fields_ = [
    # / Minimum value.
    ('iMinValue', INT),
    # / Maximum value.
    ('iMaxValue', INT),
    # / The minimum change in between minValue and maxValue.
    ('iStepValue', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about an controller mode
# /
# / This structure is used to store information of an controller mode
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLControllerMode._fields_ = [
    # / ADL_CONTROLLERMODE_CM_MODIFIER_VIEW_PANLOCK and
    # ADL_CONTROLLERMODE_CM_MODIFIER_VIEW_SIZE
    ('iModifiers', INT),
    # / Horizontal view starting position
    ('iViewPositionCx', INT),
    # / Vertical view starting position
    ('iViewPositionCy', INT),
    # / Horizontal left panlock position
    ('iViewPanLockLeft', INT),
    # / Horizontal right panlock position
    ('iViewPanLockRight', INT),
    # / Vertical top panlock position
    ('iViewPanLockTop', INT),
    # / Vertical bottom panlock position
    ('iViewPanLockBottom', INT),
    # / View resolution in pixels (width)
    ('iViewResolutionCx', INT),
    # / View resolution in pixels (hight)
    ('iViewResolutionCy', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about a display
# /
# / This structure is used to store information about a display
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayIdentifier._fields_ = [
    # / ADL display index
    ('ulDisplayIndex', LONG),
    # / manufacturer ID of the display
    ('ulManufacturerId', LONG),
    # / product ID of the display
    ('ulProductId', LONG),
    # / serial number of the display
    ('ulSerialNo', LONG),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 clock range
# /
# / This structure is used to store information about Overdrive 6 clock
# range
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6ParameterRange._fields_ = [
    # / The starting value of the clock range
    ('iMin', INT),
    # / The ending value of the clock range
    ('iMax', INT),
    # / The minimum increment between clock values
    ('iStep', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 capabilities
# /
# / This structure is used to store information about Overdrive 6
# capabilities
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6Capabilities._fields_ = [
    # / \ref ADL_OD6_CAPABILITY_MCLK_CUSTOMIZATION, \ref
    # ADL_OD6_CAPABILITY_GPU_ACTIVITY_MONITOR
    ('iCapabilities', INT),
    # / is supported. Possible Values: \ref
    # ADL_OD6_SUPPORTEDSTATE_PERFORMANCE
    ('iSupportedStates', INT),
    # / indicates the maximum clocks.
    ('iNumberOfPerformanceLevels', INT),
    # / clocks cannot be set outside this range.
    ('sEngineClockRange', ADLOD6ParameterRange),
    # / clocks cannot be set outside this range.
    ('sMemoryClockRange', ADLOD6ParameterRange),
    # / Value for future extension
    ('iExtValue', INT),
    # / Mask for future extension
    ('iExtMask', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 clock values.
# /
# / This structure is used to store information about Overdrive 6 clock
# values.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6PerformanceLevel._fields_ = [
    # / Engine (core) clock.
    ('iEngineClock', INT),
    # / Memory clock.
    ('iMemoryClock', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 clocks.
# /
# / This structure is used to store information about Overdrive 6 clocks.
# This is a
# / variable-sized structure. iNumberOfPerformanceLevels indicate how many
# elements
# / are contained in the aLevels array.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6StateInfo._fields_ = [
    # / in the range. The 2nd level indicates the maximum clocks in the
    # range.
    ('iNumberOfPerformanceLevels', INT),
    # / Value for future extension
    ('iExtValue', INT),
    # / Mask for future extension
    ('iExtMask', INT),
    # / The number of elements in the array is specified by
    # iNumberofPerformanceLevels.
    ('aLevels', ADLOD6PerformanceLevel * 1),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about current Overdrive 6
# performance status.
# /
# / This structure is used to store information about current Overdrive 6
# performance status.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6CurrentStatus._fields_ = [
    # / Current engine clock in 10 KHz.
    ('iEngineClock', INT),
    # / Current memory clock in 10 KHz.
    ('iMemoryClock', INT),
    # / indicates how "busy" the GPU is.
    ('iActivityPercent', INT),
    # / Not used. Reserved for future use.
    ('iCurrentPerformanceLevel', INT),
    # / Current PCI-E bus speed
    ('iCurrentBusSpeed', INT),
    # / Current PCI-E bus of lanes
    ('iCurrentBusLanes', INT),
    # / Maximum possible PCI-E bus of lanes
    ('iMaximumBusLanes', INT),
    # / Value for future extension
    ('iExtValue', INT),
    # / Mask for future extension
    ('iExtMask', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 thermal
# contoller capabilities
# /
# / This structure is used to store information about Overdrive 6 thermal
# controller capabilities
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6ThermalControllerCaps._fields_ = [
    # / \ref ADL_OD6_TCCAPS_FANSPEED_PERCENT_READ, \ref
    # ADL_OD6_TCCAPS_FANSPEED_PERCENT_WRITE, \ref
    # ADL_OD6_TCCAPS_FANSPEED_RPM_READ, \ref
    # ADL_OD6_TCCAPS_FANSPEED_RPM_WRITE
    ('iCapabilities', INT),
    # / Minimum fan speed expressed as a percentage
    ('iFanMinPercent', INT),
    # / Maximum fan speed expressed as a percentage
    ('iFanMaxPercent', INT),
    # / Minimum fan speed expressed in revolutions-per-minute
    ('iFanMinRPM', INT),
    # / Maximum fan speed expressed in revolutions-per-minute
    ('iFanMaxRPM', INT),
    # / Value for future extension
    ('iExtValue', INT),
    # / Mask for future extension
    ('iExtMask', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 fan speed
# information
# /
# / This structure is used to store information about Overdrive 6 fan
# speed information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6FanSpeedInfo._fields_ = [
    # / Contains a bitmap of the valid fan speed type flags. Possible
    # values: \ref ADL_OD6_FANSPEED_TYPE_PERCENT, \ref
    # ADL_OD6_FANSPEED_TYPE_RPM, \ref ADL_OD6_FANSPEED_USER_DEFINED
    ('iSpeedType', INT),
    # / Contains current fan speed in percent
    # (if valid flag exists in iSpeedType)
    ('iFanSpeedPercent', INT),
    # / Contains current fan speed in RPM
    # (if valid flag exists in iSpeedType)
    ('iFanSpeedRPM', INT),
    # / Value for future extension
    ('iExtValue', INT),
    # / Mask for future extension
    ('iExtMask', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 fan speed
# value
# /
# / This structure is used to store information about Overdrive 6 fan
# speed value
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6FanSpeedValue._fields_ = [
    # / Indicates the units of the fan speed. Possible values: \ref
    # ADL_OD6_FANSPEED_TYPE_PERCENT, \ref ADL_OD6_FANSPEED_TYPE_RPM
    ('iSpeedType', INT),
    # / Fan speed value (units as indicated above)
    ('iFanSpeed', INT),
    # / Value for future extension
    ('iExtValue', INT),
    # / Mask for future extension
    ('iExtMask', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 PowerControl
# settings.
# /
# / This structure is used to store information about Overdrive 6
# PowerControl settings.
# / PowerControl is the feature which allows the performance
# characteristics of the GPU
# / to be adjusted by changing the PowerTune power limits.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6PowerControlInfo._fields_ = [
    # / The minimum PowerControl adjustment value
    ('iMinValue', INT),
    # / The maximum PowerControl adjustment value
    ('iMaxValue', INT),
    # / The minimum difference between PowerControl adjustment values
    ('iStepValue', INT),
    # / Value for future extension
    ('iExtValue', INT),
    # / Mask for future extension
    ('iExtMask', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 PowerControl
# settings.
# /
# / This structure is used to store information about Overdrive 6
# PowerControl settings.
# / PowerControl is the feature which allows the performance
# characteristics of the GPU
# / to be adjusted by changing the PowerTune power limits.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6VoltageControlInfo._fields_ = [
    # / The minimum VoltageControl adjustment value
    ('iMinValue', INT),
    # / The maximum VoltageControl adjustment value
    ('iMaxValue', INT),
    # / The minimum difference between VoltageControl adjustment values
    ('iStepValue', INT),
    # / Value for future extension
    ('iExtValue', INT),
    # / Mask for future extension
    ('iExtMask', INT),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing ECC statistics namely SEC counts and DED
# counts
# / Single error count - count of errors that can be corrected
# / Doubt Error Detect - count of errors that cannot be corrected
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLECCData._fields_ = [
    # Single error count - count of errors that can be corrected
    ('iSec', INT),
    # Double error detect - count of errors that cannot be corrected
    ('iDed', INT),
]
# / \brief Handle to ADL client context.
# /
# / ADL clients obtain context handle from initial call to \ref
# ADL2_Main_Control_Create.
# / Clients have to pass the handle to each subsequent ADL call and
# finally destroy
# / the context with call to \ref ADL2_Main_Control_Destroy
# / \nosubgrouping
ADL_CONTEXT_HANDLE = VOID
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the display mode definition used per
# controller.
# /
# / This structure is used to store the display mode definition used per
# controller.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDisplayModeX2._fields_ = [
    # / Horizontal resolution (in pixels).
    ('iWidth', INT),
    # / Vertical resolution (in lines).
    ('iHeight', INT),
    # / Interlaced/Progressive. The value will be set for Interlaced as
    # ADL_DL_TIMINGFLAG_INTERLACED. If not set it is progressive. Refer
    # define_detailed_timing_flags.
    ('iScanType', INT),
    # / Refresh rate.
    ('iRefreshRate', INT),
    # / Timing Standard. Refer define_modetiming_standard.
    ('iTimingStandard', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 extension
# capabilities
# /
# / This structure is used to store information about Overdrive 6
# extension capabilities
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6CapabilitiesEx._fields_ = [
    # // \ref ADL_OD6_CAPABILITY_THERMAL_LIMIT_UNLOCK
    ('iCapabilities', INT),
    # / Possible Values: \ref ADL_OD6_SUPPORTEDSTATE_PERFORMANCE
    ('iSupportedStates', INT),
    # / Returns the hard limits of the SCLK overdrive adjustment range.
    # Overdrive clocks should not be adjusted outside of this range. The
    # values are specified as + /- percentages.
    ('sEngineClockPercent', ADLOD6ParameterRange),
    # / Returns the hard limits of the MCLK overdrive adjustment range.
    # Overdrive clocks should not be adjusted outside of this range. The
    # values are specified as + /- percentages.
    ('sMemoryClockPercent', ADLOD6ParameterRange),
    # / Returns the hard limits of the Power Limit adjustment range. Power
    # limit should not be adjusted outside this range. The values are
    # specified as + /- percentages.
    ('sPowerControlPercent', ADLOD6ParameterRange),
    # / Reserved for future expansion of the structure.
    ('iExtValue', INT),
    # / Reserved for future expansion of the structure.
    ('iExtMask', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 extension
# state information
# /
# / This structure is used to store information about Overdrive 6
# extension state information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6StateEx._fields_ = [
    # / The current engine clock adjustment value, specified as a + /-
    # percent.
    ('iEngineClockPercent', INT),
    # / The current memory clock adjustment value, specified as a + /-
    # percent.
    ('iMemoryClockPercent', INT),
    # / The current power control adjustment value, specified as a + /-
    # percent.
    ('iPowerControlPercent', INT),
    # / Reserved for future expansion of the structure.
    ('iExtValue', INT),
    # / Reserved for future expansion of the structure.
    ('iExtMask', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive 6 extension
# recommended maximum clock adjustment values
# /
# / This structure is used to store information about Overdrive 6
# extension recommended maximum clock adjustment values
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD6MaxClockAdjust._fields_ = [
    # / The recommended maximum engine clock adjustment in percent, for
    # the specified power limit value.
    ('iEngineClockMax', INT),
    # / adjustment and Power Limit setting.
    ('iMemoryClockMax', INT),
    # / Reserved for future expansion of the structure.
    ('iExtValue', INT),
    # / Reserved for future expansion of the structure.
    ('iExtMask', INT),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the Connector information
# /
# / this structure is used to get the connector information like length,
# positions & etc.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLConnectorInfo._fields_ = [
    # /index of the connector(0-based)
    ('iConnectorIndex', INT),
    # /used for disply identification/ordering
    ('iConnectorId', INT),
    # /index of the slot, 0-based index.
    ('iSlotIndex', INT),
    # /Type of the connector. \ref define_connector_types
    ('iType', INT),
    # /Position of the connector(in millimeters), from the right side of
    # the slot.
    ('iOffset', INT),
    # /Length of the connector(in millimeters).
    ('iLength', INT),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing the slot information
# /
# / this structure is used to get the slot information like length of the
# slot, no of connectors on the slot & etc.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLBracketSlotInfo._fields_ = [
    # /index of the slot, 0-based index.
    ('iSlotIndex', INT),
    # /length of the slot(in millimeters).
    ('iLength', INT),
    # /width of the slot(in millimeters).
    ('iWidth', INT),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing MST branch information
# /
# / this structure is used to store the MST branch information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLMSTRad._fields_ = [
    # /depth of the link.
    ('iLinkNumber', INT),
    # / Relative address, address scheme starts from source side
    ('rad', CHAR * ADL_MAX_RAD_LINK_COUNT),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing port information
# /
# / this structure is used to get the display or MST branch information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLDevicePort._fields_ = [
    # /index of the connector.
    ('iConnectorIndex', INT),
    # /Relative MST address. If MST RAD contains 0 it means DP or Root of
    # the MST topology. For non DP connectors MST RAD is ignored.
    ('aMSTRad', ADLMSTRad),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing supported connection types and properties
# /
# / this structure is used to get the supported connection types and
# supported properties of given connector
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLSupportedConnections._fields_ = [
    # /Bit vector of supported connections. Bitmask is defined in
    # constants section. \ref define_connection_types
    ('iSupportedConnections', INT),
    # /Array of bitvectors. Each bit vector represents supported
    # properties for one connection type. Index of this array is
    # connection type (bit number in mask).
    ('iSupportedProperties', INT * ADL_MAX_CONNECTION_TYPES),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing connection state of the connector
# /
# / this structure is used to get the current Emulation status and mode of
# the given connector
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLConnectionState._fields_ = [
    # /The value is bit vector. Each bit represents status. See masks
    # constants for details. \ref define_emulation_status
    ('iEmulationStatus', INT),
    # /It contains information about current emulation mode. See constants
    # for details. \ref define_emulation_mode
    ('iEmulationMode', INT),
    # /If connection is active it will contain display id, otherwise
    # CWDDEDI_INVALID_DISPLAY_INDEX
    ('iDisplayIndex', INT),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing connection properties information
# /
# / this structure is used to retrieve the properties of connection type
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLConnectionProperties._fields_ = [
    # Bit vector. Represents actual properties. Supported properties for
    # specific connection type. \ref define_connection_properties
    ('iValidProperties', INT),
    # Bitrate(in MHz). Could be used for MST branch, DP or DP active
    # dongle. \ref define_linkrate_constants
    ('iBitrate', INT),
    # Number of lanes in DP connection. \ref define_lanecount_constants
    ('iNumberOfLanes', INT),
    # Color depth(in bits). \ref define_colordepth_constants
    ('iColorDepth', INT),
    # 3D capabilities. It could be used for some dongles. For instance:
    # alternate framepack. Value of this property is bit vector.
    ('iStereo3DCaps', INT),
    # /Output Bandwidth. Could be used for MST branch, DP or DP Active
    # dongle. \ref define_linkrate_constants
    ('iOutputBandwidth', INT),
]
# ////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing connection information
# /
# / this structure is used to retrieve the data from driver which includes
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLConnectionData._fields_ = [
    # /Connection type. based on the connection type either iNumberofPorts
    # or IDataSize,EDIDdata is valid, \ref define_connection_types
    ('iConnectionType', INT),
    # /Specifies the connection properties.
    ('aConnectionProperties', ADLConnectionProperties),
    # /Number of ports
    ('iNumberofPorts', INT),
    # /Number of Active Connections
    ('iActiveConnections', INT),
    # /actual size of EDID data block size.
    ('iDataSize', INT),
    # /EDID Data
    ('EdidData', CHAR * ADL_MAX_DISPLAY_EDID_DATA_SIZE),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about an controller mode
# including Number of Connectors
# /
# / This structure is used to store information of an controller mode
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLAdapterCapsX2._fields_ = [
    # / AdapterID for this adapter
    ('iAdapterID', INT),
    # / Number of controllers for this adapter
    ('iNumControllers', INT),
    # / Number of displays for this adapter
    ('iNumDisplays', INT),
    # / Number of overlays for this adapter
    ('iNumOverlays', INT),
    # / Number of GLSyncConnectors
    ('iNumOfGLSyncConnectors', INT),
    # / The bit mask identifies the adapter caps
    ('iCapsMask', INT),
    # / The bit identifies the adapter caps \ref define_adapter_caps
    ('iCapsValue', INT),
    # / Number of Connectors for this adapter
    ('iNumConnectors', INT),
]


class _ADL_ERROR_RECORD_SEVERITY(ENUM):
    ADL_GLOBALLY_UNCORRECTED = EnumItem(1).set_string('Globally Uncorrected')
    ADL_LOCALLY_UNCORRECTED = EnumItem(2).set_string('Locally Uncorrected')
    ADL_DEFFERRED = EnumItem(3).set_string('Deferred')
    ADL_CORRECTED = EnumItem(4).set_string('Corrected')


ADL_ERROR_RECORD_SEVERITY = _ADL_ERROR_RECORD_SEVERITY

ADL_GLOBALLY_UNCORRECTED = _ADL_ERROR_RECORD_SEVERITY.ADL_GLOBALLY_UNCORRECTED
ADL_LOCALLY_UNCORRECTED = _ADL_ERROR_RECORD_SEVERITY.ADL_LOCALLY_UNCORRECTED
ADL_DEFFERRED = _ADL_ERROR_RECORD_SEVERITY.ADL_DEFFERRED
ADL_CORRECTED = _ADL_ERROR_RECORD_SEVERITY.ADL_CORRECTED


class bits(ctypes.Structure):
    pass


bits._fields_ = [
    ('isEccAccessing', UINT, 1),
    ('reserved', UINT, 31),
]
_ADL_ECC_EDC_FLAG.bits = bits


_ADL_ECC_EDC_FLAG._fields_ = [
    ('bits', _ADL_ECC_EDC_FLAG.bits),
    ('u32All', UINT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about EDC Error Record
# /
# / This structure is used to store EDC Error Record
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLErrorRecord._fields_ = [
    # Severity of error
    ('Severity', ADL_ERROR_RECORD_SEVERITY),
    # Is the counter valid?
    ('countValid', INT),
    # Counter value, if valid
    ('count', UINT),
    # Is the location information valid?
    ('locationValid', INT),
    # CU number on which error occurred, if known
    ('CU', UINT),
    # e.g. LDS, TCC, etc.
    ('StructureName', CHAR * 32),
    # Time of error record creation
    # (e.g. time of query, or time of poison interrupt)
    ('tiestamp', CHAR * 32),
    ('padding', UINT * 3),
]


class _ADL_EDC_BLOCK_ID(ENUM):
    ADL_EDC_BLOCK_ID_SQCIS = 1
    ADL_EDC_BLOCK_ID_SQCDS = 2
    ADL_EDC_BLOCK_ID_SGPR = 3
    ADL_EDC_BLOCK_ID_VGPR = 4
    ADL_EDC_BLOCK_ID_LDS = 5
    ADL_EDC_BLOCK_ID_GDS = 6
    ADL_EDC_BLOCK_ID_TCL1 = 7
    ADL_EDC_BLOCK_ID_TCL2 = 8


ADL_EDC_BLOCK_ID = _ADL_EDC_BLOCK_ID

ADL_EDC_BLOCK_ID_SQCIS = _ADL_EDC_BLOCK_ID.ADL_EDC_BLOCK_ID_SQCIS
ADL_EDC_BLOCK_ID_SQCDS = _ADL_EDC_BLOCK_ID.ADL_EDC_BLOCK_ID_SQCDS
ADL_EDC_BLOCK_ID_SGPR = _ADL_EDC_BLOCK_ID.ADL_EDC_BLOCK_ID_SGPR
ADL_EDC_BLOCK_ID_VGPR = _ADL_EDC_BLOCK_ID.ADL_EDC_BLOCK_ID_VGPR
ADL_EDC_BLOCK_ID_LDS = _ADL_EDC_BLOCK_ID.ADL_EDC_BLOCK_ID_LDS
ADL_EDC_BLOCK_ID_GDS = _ADL_EDC_BLOCK_ID.ADL_EDC_BLOCK_ID_GDS
ADL_EDC_BLOCK_ID_TCL1 = _ADL_EDC_BLOCK_ID.ADL_EDC_BLOCK_ID_TCL1
ADL_EDC_BLOCK_ID_TCL2 = _ADL_EDC_BLOCK_ID.ADL_EDC_BLOCK_ID_TCL2


class _ADL_ERROR_INJECTION_MODE(ENUM):
    ADL_ERROR_INJECTION_MODE_SINGLE = 1
    ADL_ERROR_INJECTION_MODE_MULTIPLE = 2
    ADL_ERROR_INJECTION_MODE_ADDRESS = 3


ADL_ERROR_INJECTION_MODE = _ADL_ERROR_INJECTION_MODE

ADL_ERROR_INJECTION_MODE_SINGLE = _ADL_ERROR_INJECTION_MODE.ADL_ERROR_INJECTION_MODE_SINGLE
ADL_ERROR_INJECTION_MODE_MULTIPLE = _ADL_ERROR_INJECTION_MODE.ADL_ERROR_INJECTION_MODE_MULTIPLE
ADL_ERROR_INJECTION_MODE_ADDRESS = _ADL_ERROR_INJECTION_MODE.ADL_ERROR_INJECTION_MODE_ADDRESS


class bits(ctypes.Structure):
    pass


bits._fields_ = [
    ('EccInjVector', ULONG, 16),
    ('EccInjEn', ULONG, 9),
    ('EccBeatEn', ULONG, 4),
    ('EccChEn', ULONG, 4),
    ('reserved', ULONG, 31),
]
_ADL_ERROR_PATTERN.bits = bits


_ADL_ERROR_PATTERN._fields_ = [
    ('bits', _ADL_ERROR_PATTERN.bits),
    ('u64Value', ULONGLONG),
]

_ADL_ERROR_INJECTION_DATA._fields_ = [
    ('errorAddress', ULONGLONG),
    ('errorPattern', ADL_ERROR_PATTERN),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about EDC Error Injection
# /
# / This structure is used to store EDC Error Injection
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLErrorInjection._fields_ = [
    ('blockId', ADL_EDC_BLOCK_ID),
    ('errorInjectionMode', ADL_ERROR_INJECTION_MODE),
]

ADLErrorInjectionX2._fields_ = [
    ('blockId', ADL_EDC_BLOCK_ID),
    ('errorInjectionMode', ADL_ERROR_INJECTION_MODE),
    ('errorInjectionData', ADL_ERROR_INJECTION_DATA),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing per display FreeSync capability information.
# /
# / This structure is used to store the FreeSync capability of both the
# display and
# / the GPU the display is connected to.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLFreeSyncCap._fields_ = [
    # / FreeSync capability flags. \ref define_freesync_caps
    ('iCaps', INT),
    # / Reports minimum FreeSync refresh rate supported by the display in
    # micro hertz
    ('iMinRefreshRateInMicroHz', INT),
    # / Reports maximum FreeSync refresh rate supported by the display in
    # micro hertz
    ('iMaxRefreshRateInMicroHz', INT),
    # / Reserved
    ('iReserved', INT * 5),
]


# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing per display Display Connectivty Experience
# Settings
# /
# / This structure is used to store the Display Connectivity Experience
# settings of a
# / display
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
class Settings(ctypes.Union):
    pass


class HdmiLq(ctypes.Structure):
    pass


HdmiLq._fields_ = [
    ('qualityDetectionEnabled', BOOL),
]
Settings.HdmiLq = HdmiLq


class DpLink(ctypes.Structure):
    pass


DpLink._fields_ = [
    # Read-only
    ('linkRate', DpLinkRate),
    # Read-only
    ('numberOfActiveLanes', UINT),
    # Read-only
    ('numberofTotalLanes', UINT),
    # Allowable values are -2 to + 2
    ('relativePreEmphasis', INT),
    # Allowable values are -2 to + 2
    ('relativeVoltageSwing', INT),
    ('persistFlag', INT),
]
Settings.DpLink = DpLink


class Protection(ctypes.Structure):
    pass


Protection._fields_ = [
    # Read-only
    ('linkProtectionEnabled', BOOL),
]
Settings.Protection = Protection


Settings._fields_ = [
    ('HdmiLq', Settings.HdmiLq),
    ('DpLink', Settings.DpLink),
    ('Protection', Settings.Protection),
]
_ADLDceSettings.Settings = Settings


_ADLDceSettings._fields_ = [
    # Defines which structure is in the union below
    ('type', DceSettingsType),
    ('Settings', _ADLDceSettings.Settings),
    ('iReserved', INT * 15),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Graphic Core
# /
# / This structure is used to get Graphic Core Info
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLGraphicCoreInfo._fields_ = [
    # / indicate the graphic core generation
    ('iGCGen', INT),
    # / Total number of CUs. Valid for GCN (iGCGen == GCN)
    ('iNumCUs', INT),
    # / Number of processing elements per CU. Valid for GCN (iGCGen == GCN)
    ('iNumPEsPerCU', INT),
    # / Total number of SIMDs. Valid for Pre GCN (iGCGen == Pre-GCN)
    ('iNumSIMDs', INT),
    # / Total number of ROPs. Valid for both GCN and Pre GCN
    ('iNumROPs', INT),
    # / reserved for future use
    ('iReserved', INT * 11),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive N clock range
# /
# / This structure is used to store information about Overdrive N clock
# range
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLODNParameterRange._fields_ = [
    # / The starting value of the clock range
    ('iMode', INT),
    # / The starting value of the clock range
    ('iMin', INT),
    # / The ending value of the clock range
    ('iMax', INT),
    # / The minimum increment between clock values
    ('iStep', INT),
    # / The default clock values
    ('iDefault', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive N capabilities
# /
# / This structure is used to store information about Overdrive N
# capabilities
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLODNCapabilities._fields_ = [
    # / indicates the maximum clocks.
    ('iMaximumNumberOfPerformanceLevels', INT),
    # / clocks cannot be set outside this range.
    ('sEngineClockRange', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('sMemoryClockRange', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('svddcRange', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('power', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('powerTuneTemperature', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('fanTemperature', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('fanSpeed', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('minimumPerformanceClock', ADLODNParameterRange),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive N capabilities
# /
# / This structure is used to store information about Overdrive N
# capabilities
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLODNCapabilitiesX2._fields_ = [
    # / indicates the maximum clocks.
    ('iMaximumNumberOfPerformanceLevels', INT),
    # / \ref: ADLODNFEATURECONTROL
    ('iFlags', INT),
    # / clocks cannot be set outside this range.
    ('sEngineClockRange', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('sMemoryClockRange', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('svddcRange', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('power', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('powerTuneTemperature', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('fanTemperature', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('fanSpeed', ADLODNParameterRange),
    # / clocks cannot be set outside this range.
    ('minimumPerformanceClock', ADLODNParameterRange),
    # / Contains the hard limits of the throttleNotification
    ('throttleNotificaion', ADLODNParameterRange),
    # / Contains the hard limits of the Auto Systemclock
    ('autoSystemClock', ADLODNParameterRange),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive level.
# /
# / This structure is used to store information about Overdrive level.
# / This structure is used by ADLODPerformanceLevels.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODNPerformanceLevel._fields_ = [
    # / clock.
    ('iClock', INT),
    # / VDCC.
    ('iVddc', INT),
    # / enabled
    ('iEnabled', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive N performance
# levels.
# /
# / This structure is used to store information about Overdrive
# performance levels.
# / This structure is used by the ADL_OverdriveN_ODPerformanceLevels_Get()
# and ADL_OverdriveN_ODPerformanceLevels_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODNPerformanceLevels._fields_ = [
    ('iSize', INT),
    # Automatic/manual
    ('iMode', INT),
    # / Must be set to
    # (ctypes.sizeof( \ref ADLODPerformanceLevels ) + (ctypes.sizeof( \ref ADLODPerformanceLevel ) *
    # (ADLODParameters.iNumberOfPerformanceLevels - 1)
    ('iNumberOfPerformanceLevels', INT),
    # / Array of performance state descriptors. Must have
    # ADLODParameters.iNumberOfPerformanceLevels elements.
    ('aLevels', ADLODNPerformanceLevel * 1),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive N Fan Speed.
# /
# / This structure is used to store information about Overdrive Fan
# control .
# / This structure is used by the ADL_OverdriveN_ODPerformanceLevels_Get()
# and ADL_OverdriveN_ODPerformanceLevels_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODNFanControl._fields_ = [
    ('iMode', INT),
    ('iFanControlMode', INT),
    ('iCurrentFanSpeedMode', INT),
    ('iCurrentFanSpeed', INT),
    ('iTargetFanSpeed', INT),
    ('iTargetTemperature', INT),
    ('iMinPerformanceClock', INT),
    ('iMinFanLimit', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive N power limit.
# /
# / This structure is used to store information about Overdrive power
# limit.
# / This structure is used by the ADL_OverdriveN_ODPerformanceLevels_Get()
# and ADL_OverdriveN_ODPerformanceLevels_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODNPowerLimitSetting._fields_ = [
    ('iMode', INT),
    ('iTDPLimit', INT),
    ('iMaxOperatingTemperature', INT),
]
ADLODNPerformanceStatus._fields_ = [
    ('iCoreClock', INT),
    ('iMemoryClock', INT),
    ('iDCEFClock', INT),
    ('iGFXClock', INT),
    ('iUVDClock', INT),
    ('iVCEClock', INT),
    ('iGPUActivityPercent', INT),
    ('iCurrentCorePerformanceLevel', INT),
    ('iCurrentMemoryPerformanceLevel', INT),
    ('iCurrentDCEFPerformanceLevel', INT),
    ('iCurrentGFXPerformanceLevel', INT),
    ('iUVDPerformanceLevel', INT),
    ('iVCEPerformanceLevel', INT),
    ('iCurrentBusSpeed', INT),
    ('iCurrentBusLanes', INT),
    ('iMaximumBusLanes', INT),
    ('iVDDC', INT),
    ('iVDDCI', INT),
]
# /\brief Structure containing information about Overdrive level.
# /
# / This structure is used to store information about Overdrive level.
# / This structure is used by ADLODPerformanceLevels.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODNPerformanceLevelX2._fields_ = [
    # / clock.
    ('iClock', INT),
    # / VDCC.
    ('iVddc', INT),
    # / enabled
    ('iEnabled', INT),
    # / MASK
    ('iControl', INT),
]
# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive N performance
# levels.
# /
# / This structure is used to store information about Overdrive
# performance levels.
# / This structure is used by the ADL_OverdriveN_ODPerformanceLevels_Get()
# and ADL_OverdriveN_ODPerformanceLevels_Set() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLODNPerformanceLevelsX2._fields_ = [
    ('iSize', INT),
    # Automatic/manual
    ('iMode', INT),
    # / Must be set to
    # (ctypes.sizeof( \ref ADLODPerformanceLevels ) + (ctypes.sizeof( \ref ADLODPerformanceLevel ) *
    # (ADLODParameters.iNumberOfPerformanceLevels - 1)
    ('iNumberOfPerformanceLevels', INT),
    # / Array of performance state descriptors. Must have
    # ADLODParameters.iNumberOfPerformanceLevels elements.
    ('aLevels', ADLODNPerformanceLevelX2 * 1),
]


class _ADLODNCurrentPowerType(ENUM):
    ODN_GPU_TOTAL_POWER = 0
    ODN_GPU_PPT_POWER = 1
    ODN_GPU_SOCKET_POWER = 2
    ODN_GPU_CHIP_POWER = 3


ADLODNCurrentPowerType = _ADLODNCurrentPowerType

ODN_GPU_TOTAL_POWER = _ADLODNCurrentPowerType.ODN_GPU_TOTAL_POWER
ODN_GPU_PPT_POWER = _ADLODNCurrentPowerType.ODN_GPU_PPT_POWER
ODN_GPU_SOCKET_POWER = _ADLODNCurrentPowerType.ODN_GPU_SOCKET_POWER
ODN_GPU_CHIP_POWER = _ADLODNCurrentPowerType.ODN_GPU_CHIP_POWER

# in/out: CWDDEPM_CURRENTPOWERPARAMETERS
_ADLODNCurrentPowerParameters._fields_ = [
    ('size', INT),
    ('powerType', ADLODNCurrentPowerType),
    ('currentPower', INT),
]

# ODN Ext range data structure
_ADLODNExtSingleInitSetting._fields_ = [
    ('mode', int),
    ('minValue', int),
    ('maxValue', int),
    ('step', int),
    ('defaultValue', int),
]

# OD8 Ext range data structure
_ADLOD8SingleInitSetting._fields_ = [
    ('featureID', INT),
    ('minValue', INT),
    ('maxValue', INT),
    ('defaultValue', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive8 initial setting
# /
# / This structure is used to store information about Overdrive8 initial
# setting
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD8InitSetting._fields_ = [
    ('count', INT),
    ('overdrive8Capabilities', INT),
    ('od8SettingTable', ADLOD8SingleInitSetting * OD8_COUNT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive8 current setting
# /
# / This structure is used to store information about Overdrive8 current
# setting
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD8CurrentSetting._fields_ = [
    ('count', INT),
    ('Od8SettingTable', INT * OD8_COUNT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Overdrive8 set setting
# /
# / This structure is used to store information about Overdrive8 set
# setting
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLOD8SingleSetSetting._fields_ = [
    ('value', INT),
    # 0 - default , 1 - requested
    ('requested', INT),
    # 0 - do not reset , 1 - reset setting back to default
    ('reset', INT),
]

_ADLOD8SetSetting._fields_ = [
    ('count', INT),
    ('od8SettingTable', ADLOD8SingleSetSetting * OD8_COUNT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about Performance Metrics data
# /
# / This structure is used to store information about Performance Metrics
# data output
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLSingleSensorData._fields_ = [
    ('supported', INT),
    ('value', INT),
]

_ADLPMLogDataOutput._fields_ = [
    ('size', INT),
    ('sensors', ADLSingleSensorData * ADL_PMLOG_MAX_SENSORS),
]


class _ADLSensorType(ENUM):
    SENSOR_MAXTYPES = 0
    PMLOG_CLK_GFXCLK = 1
    PMLOG_CLK_MEMCLK = 2
    PMLOG_CLK_SOCCLK = 3
    PMLOG_CLK_UVDCLK1 = 4
    PMLOG_CLK_UVDCLK2 = 5
    PMLOG_CLK_VCECLK = 6
    PMLOG_CLK_VCNCLK = 7
    PMLOG_TEMPERATURE_EDGE = 8
    PMLOG_TEMPERATURE_MEM = 9
    PMLOG_TEMPERATURE_VRVDDC = 10
    PMLOG_TEMPERATURE_VRMVDD = 11
    PMLOG_TEMPERATURE_LIQUID = 12
    PMLOG_TEMPERATURE_PLX = 13
    PMLOG_FAN_RPM = 14
    PMLOG_FAN_PERCENTAGE = 15
    PMLOG_SOC_VOLTAGE = 16
    PMLOG_SOC_POWER = 17
    PMLOG_SOC_CURRENT = 18
    PMLOG_INFO_ACTIVITY_GFX = 19
    PMLOG_INFO_ACTIVITY_MEM = 20
    PMLOG_GFX_VOLTAGE = 21
    PMLOG_MEM_VOLTAGE = 22
    PMLOG_ASIC_POWER = 23
    PMLOG_TEMPERATURE_VRSOC = 24
    PMLOG_TEMPERATURE_VRMVDD0 = 25
    PMLOG_TEMPERATURE_VRMVDD1 = 26
    PMLOG_TEMPERATURE_HOTSPOT = 27


ADLSensorType = _ADLSensorType

SENSOR_MAXTYPES = _ADLSensorType.SENSOR_MAXTYPES
PMLOG_CLK_GFXCLK = _ADLSensorType.PMLOG_CLK_GFXCLK
PMLOG_CLK_MEMCLK = _ADLSensorType.PMLOG_CLK_MEMCLK
PMLOG_CLK_SOCCLK = _ADLSensorType.PMLOG_CLK_SOCCLK
PMLOG_CLK_UVDCLK1 = _ADLSensorType.PMLOG_CLK_UVDCLK1
PMLOG_CLK_UVDCLK2 = _ADLSensorType.PMLOG_CLK_UVDCLK2
PMLOG_CLK_VCECLK = _ADLSensorType.PMLOG_CLK_VCECLK
PMLOG_CLK_VCNCLK = _ADLSensorType.PMLOG_CLK_VCNCLK
PMLOG_TEMPERATURE_EDGE = _ADLSensorType.PMLOG_TEMPERATURE_EDGE
PMLOG_TEMPERATURE_MEM = _ADLSensorType.PMLOG_TEMPERATURE_MEM
PMLOG_TEMPERATURE_VRVDDC = _ADLSensorType.PMLOG_TEMPERATURE_VRVDDC
PMLOG_TEMPERATURE_VRMVDD = _ADLSensorType.PMLOG_TEMPERATURE_VRMVDD
PMLOG_TEMPERATURE_LIQUID = _ADLSensorType.PMLOG_TEMPERATURE_LIQUID
PMLOG_TEMPERATURE_PLX = _ADLSensorType.PMLOG_TEMPERATURE_PLX
PMLOG_FAN_RPM = _ADLSensorType.PMLOG_FAN_RPM
PMLOG_FAN_PERCENTAGE = _ADLSensorType.PMLOG_FAN_PERCENTAGE
PMLOG_SOC_VOLTAGE = _ADLSensorType.PMLOG_SOC_VOLTAGE
PMLOG_SOC_POWER = _ADLSensorType.PMLOG_SOC_POWER
PMLOG_SOC_CURRENT = _ADLSensorType.PMLOG_SOC_CURRENT
PMLOG_INFO_ACTIVITY_GFX = _ADLSensorType.PMLOG_INFO_ACTIVITY_GFX
PMLOG_INFO_ACTIVITY_MEM = _ADLSensorType.PMLOG_INFO_ACTIVITY_MEM
PMLOG_GFX_VOLTAGE = _ADLSensorType.PMLOG_GFX_VOLTAGE
PMLOG_MEM_VOLTAGE = _ADLSensorType.PMLOG_MEM_VOLTAGE
PMLOG_ASIC_POWER = _ADLSensorType.PMLOG_ASIC_POWER
PMLOG_TEMPERATURE_VRSOC = _ADLSensorType.PMLOG_TEMPERATURE_VRSOC
PMLOG_TEMPERATURE_VRMVDD0 = _ADLSensorType.PMLOG_TEMPERATURE_VRMVDD0
PMLOG_TEMPERATURE_VRMVDD1 = _ADLSensorType.PMLOG_TEMPERATURE_VRMVDD1
PMLOG_TEMPERATURE_HOTSPOT = _ADLSensorType.PMLOG_TEMPERATURE_HOTSPOT


# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about PPLog settings.
# /
# / This structure is used to store information about PPLog settings.
# / This structure is used by the ADL2_PPLogSettings_Set() and
# ADL2_PPLogSettings_Get() functions.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
ADLPPLogSettings._fields_ = [
    ('BreakOnAssert', INT),
    ('BreakOnWarn', INT),
    ('LogEnabled', INT),
    ('LogFieldMask', INT),
    ('LogDestinations', INT),
    ('LogSeverityEnabled', INT),
    ('LogSourceMask', INT),
    ('PowerProfilingEnabled', INT),
    ('PowerProfilingTimeInterval', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related Frames Per Second for
# AC and DC.
# /
# / This structure is used to store information related AC and DC Frames
# Per Second settings
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLFPSSettingsOutput._fields_ = [
    # / size
    ('ulSize', INT),
    # / FPS Monitor is enabled in the AC state if 1
    ('bACFPSEnabled', INT),
    # / FPS Monitor is enabled in the DC state if 1
    ('bDCFPSEnabled', INT),
    # / Current Value of FPS Monitor in AC state
    ('ulACFPSCurrent', INT),
    # / Current Value of FPS Monitor in DC state
    ('ulDCFPSCurrent', INT),
    # / Maximum FPS Threshold allowed in PPLib for AC
    ('ulACFPSMaximum', INT),
    # / Minimum FPS Threshold allowed in PPLib for AC
    ('ulACFPSMinimum', INT),
    # / Maximum FPS Threshold allowed in PPLib for DC
    ('ulDCFPSMaximum', INT),
    # / Minimum FPS Threshold allowed in PPLib for DC
    ('ulDCFPSMinimum', INT),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related Frames Per Second for
# AC and DC.
# /
# / This structure is used to store information related AC and DC Frames
# Per Second settings
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLFPSSettingsInput._fields_ = [
    # / size
    ('ulSize', INT),
    # / Settings are for Global FPS (used by CCC)
    ('bGlobalSettings', INT),
    # / Current Value of FPS Monitor in AC state
    ('ulACFPSCurrent', INT),
    # / Current Value of FPS Monitor in DC state
    ('ulDCFPSCurrent', INT),
    # / Reserved
    ('ulReserved', INT * 6),
]


# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related power management
# logging.
# /
# / This structure is used to store support information for power
# management logging.
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
class DUMMYENUM(ENUM):
    ADL_PMLOG_MAX_SUPPORTED_SENSORS = 256


ADL_PMLOG_MAX_SUPPORTED_SENSORS = DUMMYENUM.ADL_PMLOG_MAX_SUPPORTED_SENSORS


_ADLPMLogSupportInfo._fields_ = [
    # / list of sensors defined by ADL_PMLOG_SENSORS
    ('usSensors', USHORT * ADL_PMLOG_MAX_SUPPORTED_SENSORS),
    # / Reserved
    ('ulReserved', INT * 16),
]


class _ADL_PMLOG_SENSORS(ENUM):
    ADL_SENSOR_MAXTYPES = 0
    ADL_PMLOG_CLK_GFXCLK = 1
    ADL_PMLOG_CLK_MEMCLK = 2
    ADL_PMLOG_CLK_SOCCLK = 3
    ADL_PMLOG_CLK_UVDCLK1 = 4
    ADL_PMLOG_CLK_UVDCLK2 = 5
    ADL_PMLOG_CLK_VCECLK = 6
    ADL_PMLOG_CLK_VCNCLK = 7
    ADL_PMLOG_TEMPERATURE_EDGE = 8
    ADL_PMLOG_TEMPERATURE_MEM = 9
    ADL_PMLOG_TEMPERATURE_VRVDDC = 10
    ADL_PMLOG_TEMPERATURE_VRMVDD = 11
    ADL_PMLOG_TEMPERATURE_LIQUID = 12
    ADL_PMLOG_TEMPERATURE_PLX = 13
    ADL_PMLOG_FAN_RPM = 14
    ADL_PMLOG_FAN_PERCENTAGE = 15
    ADL_PMLOG_SOC_VOLTAGE = 16
    ADL_PMLOG_SOC_POWER = 17
    ADL_PMLOG_SOC_CURRENT = 18
    ADL_PMLOG_INFO_ACTIVITY_GFX = 19
    ADL_PMLOG_INFO_ACTIVITY_MEM = 20
    ADL_PMLOG_GFX_VOLTAGE = 21
    ADL_PMLOG_MEM_VOLTAGE = 22
    ADL_PMLOG_ASIC_POWER = 23
    ADL_PMLOG_TEMPERATURE_VRSOC = 24
    ADL_PMLOG_TEMPERATURE_VRMVDD0 = 25
    ADL_PMLOG_TEMPERATURE_VRMVDD1 = 26
    ADL_PMLOG_TEMPERATURE_HOTSPOT = 27


ADL_PMLOG_SENSORS = _ADL_PMLOG_SENSORS

ADL_SENSOR_MAXTYPES = _ADL_PMLOG_SENSORS.ADL_SENSOR_MAXTYPES
ADL_PMLOG_CLK_GFXCLK = _ADL_PMLOG_SENSORS.ADL_PMLOG_CLK_GFXCLK
ADL_PMLOG_CLK_MEMCLK = _ADL_PMLOG_SENSORS.ADL_PMLOG_CLK_MEMCLK
ADL_PMLOG_CLK_SOCCLK = _ADL_PMLOG_SENSORS.ADL_PMLOG_CLK_SOCCLK
ADL_PMLOG_CLK_UVDCLK1 = _ADL_PMLOG_SENSORS.ADL_PMLOG_CLK_UVDCLK1
ADL_PMLOG_CLK_UVDCLK2 = _ADL_PMLOG_SENSORS.ADL_PMLOG_CLK_UVDCLK2
ADL_PMLOG_CLK_VCECLK = _ADL_PMLOG_SENSORS.ADL_PMLOG_CLK_VCECLK
ADL_PMLOG_CLK_VCNCLK = _ADL_PMLOG_SENSORS.ADL_PMLOG_CLK_VCNCLK
ADL_PMLOG_TEMPERATURE_EDGE = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_EDGE
ADL_PMLOG_TEMPERATURE_MEM = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_MEM
ADL_PMLOG_TEMPERATURE_VRVDDC = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_VRVDDC
ADL_PMLOG_TEMPERATURE_VRMVDD = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_VRMVDD
ADL_PMLOG_TEMPERATURE_LIQUID = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_LIQUID
ADL_PMLOG_TEMPERATURE_PLX = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_PLX
ADL_PMLOG_FAN_RPM = _ADL_PMLOG_SENSORS.ADL_PMLOG_FAN_RPM
ADL_PMLOG_FAN_PERCENTAGE = _ADL_PMLOG_SENSORS.ADL_PMLOG_FAN_PERCENTAGE
ADL_PMLOG_SOC_VOLTAGE = _ADL_PMLOG_SENSORS.ADL_PMLOG_SOC_VOLTAGE
ADL_PMLOG_SOC_POWER = _ADL_PMLOG_SENSORS.ADL_PMLOG_SOC_POWER
ADL_PMLOG_SOC_CURRENT = _ADL_PMLOG_SENSORS.ADL_PMLOG_SOC_CURRENT
ADL_PMLOG_INFO_ACTIVITY_GFX = _ADL_PMLOG_SENSORS.ADL_PMLOG_INFO_ACTIVITY_GFX
ADL_PMLOG_INFO_ACTIVITY_MEM = _ADL_PMLOG_SENSORS.ADL_PMLOG_INFO_ACTIVITY_MEM
ADL_PMLOG_GFX_VOLTAGE = _ADL_PMLOG_SENSORS.ADL_PMLOG_GFX_VOLTAGE
ADL_PMLOG_MEM_VOLTAGE = _ADL_PMLOG_SENSORS.ADL_PMLOG_MEM_VOLTAGE
ADL_PMLOG_ASIC_POWER = _ADL_PMLOG_SENSORS.ADL_PMLOG_ASIC_POWER
ADL_PMLOG_TEMPERATURE_VRSOC = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_VRSOC
ADL_PMLOG_TEMPERATURE_VRMVDD0 = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_VRMVDD0
ADL_PMLOG_TEMPERATURE_VRMVDD1 = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_VRMVDD1
ADL_PMLOG_TEMPERATURE_HOTSPOT = _ADL_PMLOG_SENSORS.ADL_PMLOG_TEMPERATURE_HOTSPOT

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information to start power management
# logging.
# /
# / This structure is used as input to ADL2_Adapter_PMLog_Start
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLPMLogStartInput._fields_ = [
    # / list of sensors defined by ADL_PMLOG_SENSORS
    ('usSensors', USHORT * ADL_PMLOG_MAX_SUPPORTED_SENSORS),
    # / Sample rate in milliseconds
    ('ulSampleRate', ULONG),
    # / Reserved
    ('ulReserved', INT * 15),
]

_ADLPMLogData._fields_ = [
    # / Structure version
    ('ulVersion', UINT),
    # / Current driver sample rate
    ('ulActiveSampleRate', UINT),
    # / Timestamp of last update
    ('ulLastUpdated', ULONGLONG),
    # / 2D array of senesor and values
    ('ulValues', (UINT * ADL_PMLOG_MAX_SUPPORTED_SENSORS)(UINT * 2)),
    # / Reserved
    ('ulReserved', UINT * 256),
]


# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information to start power management
# logging.
# /
# / This structure is returned as output from ADL2_Adapter_PMLog_Start
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
class _Union_1(ctypes.Union):
    pass


_Union_1._fields_ = [
    ('pLoggingAddress', POINTER(VOID)),
    ('ptr_LoggingAddress', ULONGLONG),
]
_ADLPMLogStartOutput._Union_1 = _Union_1

_ADLPMLogStartOutput._anonymous_ = (
    '_Union_1',
)

# noinspection PyProtectedMember
_ADLPMLogStartOutput._fields_ = [
    # / Pointer to memory address containing logging data
    ('_Union_1', _ADLPMLogStartOutput._Union_1),
    # / Reserved
    ('ulReserved', INT * 14),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Get Error Counts
# Information
# /
# / This structure is used to store RAS Error Counts Get Input Information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASGetErrorCountsInput._fields_ = [
    ('Reserved', UINT * 16),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Get Error Counts
# Information
# /
# / This structure is used to store RAS Error Counts Get Output Information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASGetErrorCountsOutput._fields_ = [
    # includes both DRAM and SRAM ECC
    ('CorrectedErrors', UINT),
    # includes both DRAM and SRAM ECC
    ('UnCorrectedErrors', UINT),
    ('Reserved', UINT * 14),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Get Error Counts
# Information
# /
# / This structure is used to store RAS Error Counts Get Information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASGetErrorCounts._fields_ = [
    ('InputSize', UINT),
    ('Input', ADLRASGetErrorCountsInput),
    ('OutputSize', UINT),
    ('Output', ADLRASGetErrorCountsOutput),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Error Counts Reset
# Information
# /
# / This structure is used to store RAS Error Counts Reset Input
# Information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASResetErrorCountsInput._fields_ = [
    ('Reserved', UINT * 8),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Error Counts Reset
# Information
# /
# / This structure is used to store RAS Error Counts Reset Output
# Information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASResetErrorCountsOutput._fields_ = [
    ('Reserved', UINT * 8),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Error Counts Reset
# Information
# /
# / This structure is used to store RAS Error Counts Reset Information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASResetErrorCounts._fields_ = [
    ('InputSize', UINT),
    ('Input', ADLRASResetErrorCountsInput),
    ('OutputSize', UINT),
    ('Output', ADLRASResetErrorCountsOutput),
]


class _ADL_RAS_ERROR_INJECTION_MODE(ENUM):
    ADL_RAS_ERROR_INJECTION_MODE_SINGLE = 1
    ADL_RAS_ERROR_INJECTION_MODE_MULTIPLE = 2


ADL_RAS_ERROR_INJECTION_MODE = _ADL_RAS_ERROR_INJECTION_MODE

ADL_RAS_ERROR_INJECTION_MODE_SINGLE = _ADL_RAS_ERROR_INJECTION_MODE.ADL_RAS_ERROR_INJECTION_MODE_SINGLE
ADL_RAS_ERROR_INJECTION_MODE_MULTIPLE = _ADL_RAS_ERROR_INJECTION_MODE.ADL_RAS_ERROR_INJECTION_MODE_MULTIPLE


class _ADL_RAS_BLOCK_ID(ENUM):
    ADL_RAS_BLOCK_ID_UMC = 0
    ADL_RAS_BLOCK_ID_SDMA = 1
    ADL_RAS_BLOCK_ID_GFX_HUB = 2
    ADL_RAS_BLOCK_ID_MMHUB = 3
    ADL_RAS_BLOCK_ID_ATHUB = 4
    ADL_RAS_BLOCK_ID_PCIE_BIF = 5
    ADL_RAS_BLOCK_ID_HDP = 6
    ADL_RAS_BLOCK_ID_XGMI_WAFL = 7
    ADL_RAS_BLOCK_ID_DF = 8
    ADL_RAS_BLOCK_ID_SMN = 9
    ADL_RAS_BLOCK_ID_GFX = 10


ADL_RAS_BLOCK_ID = _ADL_RAS_BLOCK_ID

ADL_RAS_BLOCK_ID_UMC = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_UMC
ADL_RAS_BLOCK_ID_SDMA = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_SDMA
ADL_RAS_BLOCK_ID_GFX_HUB = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_GFX_HUB
ADL_RAS_BLOCK_ID_MMHUB = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_MMHUB
ADL_RAS_BLOCK_ID_ATHUB = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_ATHUB
ADL_RAS_BLOCK_ID_PCIE_BIF = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_PCIE_BIF
ADL_RAS_BLOCK_ID_HDP = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_HDP
ADL_RAS_BLOCK_ID_XGMI_WAFL = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_XGMI_WAFL
ADL_RAS_BLOCK_ID_DF = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_DF
ADL_RAS_BLOCK_ID_SMN = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_SMN
ADL_RAS_BLOCK_ID_GFX = _ADL_RAS_BLOCK_ID.ADL_RAS_BLOCK_ID_GFX

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Error Injection
# information
# /
# / This structure is used to store RAS Error Injection input information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASErrorInjectonInput._fields_ = [
    ('Address', ULONGLONG),
    ('Value', ULONGLONG),
    ('BlockId', UINT),
    ('InjectErrorType', UINT),
    ('SubBlockIndex', UINT),
    ('padding', UINT * 9),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Error Injection
# information
# /
# / This structure is used to store RAS Error Injection output information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASErrorInjectionOutput._fields_ = [
    ('ErrorInjectionStatus', UINT),
    ('padding', UINT * 15),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information related RAS Error Injection
# information
# /
# / This structure is used to store RAS Error Injection information
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLRASErrorInjection._fields_ = [
    ('InputSize', UINT),
    ('Input', ADLRASErrorInjectonInput),
    ('OutputSize', UINT),
    ('Output', ADLRASErrorInjectionOutput),
]

# /////////////////////////////////////////////////////////////////////////////////////
# /\brief Structure containing information about an application
# /
# / This structure is used to store basic information of a recently ran or
# currently running application
# / \nosubgrouping
# ////////////////////////////////////////////////////////////////////////////////////
_ADLSGApplicationInfo._fields_ = [
    # / Application file name
    ('strFileName', WCHAR * ADL_MAX_PATH),
    # / Application file path
    ('strFilePath', WCHAR * ADL_MAX_PATH),
    # / Application version
    ('strVersion', WCHAR * ADL_MAX_PATH),
    # / Timestamp at which application has run
    ('timeStamp', LONGLONG),
    # / Holds whether the applicaition profile exists or not
    ('iProfileExists', UINT),
    # / The GPU on which application runs
    ('iGPUAffinity', UINT),
    # / The BDF of the GPU on which application runs
    ('GPUBdf', ADLBdf),
]
