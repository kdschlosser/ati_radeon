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


ADL2_DISPLAY_DISPLAYINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayInfo)),
    INT
)
ADL_DISPLAY_DISPLAYINFO_GET = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayInfo)),
    INT
)
ADL2_DISPLAY_DPMSTINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayDPMSTInfo)),
    INT
)
ADL_DISPLAY_DPMSTINFO_GET = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayDPMSTInfo)),
    INT
)
ADL2_DISPLAY_NUMBEROFDISPLAYS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_NUMBEROFDISPLAYS_GET = _int(
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_PRESERVEDASPECTRATIO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_PRESERVEDASPECTRATIO_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_PRESERVEDASPECTRATIO_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_PRESERVEDASPECTRATIO_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_IMAGEEXPANSION_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_IMAGEEXPANSION_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_IMAGEEXPANSION_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_IMAGEEXPANSION_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_POSITION_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_POSITION_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_POSITION_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT
)
ADL_DISPLAY_POSITION_SET = _int(
    INT,
    INT,
    INT,
    INT
)
ADL2_DISPLAY_SIZE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_SIZE_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_SIZE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT
)
ADL_DISPLAY_SIZE_SET = _int(
    INT,
    INT,
    INT,
    INT
)
ADL2_DISPLAY_ADJUSTCAPS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_ADJUSTCAPS_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_CAPABILITIES_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_CAPABILITIES_GET = _int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_CONNECTEDDISPLAYS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_CONNECTEDDISPLAYS_GET = _int(
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_DEVICECONFIG_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayConfig)
)
ADL_DISPLAY_DEVICECONFIG_GET = _int(
    INT,
    INT,
    POINTER(ADLDisplayConfig)
)
ADL2_DISPLAY_PROPERTY_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayProperty)
)
ADL_DISPLAY_PROPERTY_GET = _int(
    INT,
    INT,
    POINTER(ADLDisplayProperty)
)
ADL2_DISPLAY_PROPERTY_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayProperty)
)
ADL_DISPLAY_PROPERTY_SET = _int(
    INT,
    INT,
    POINTER(ADLDisplayProperty)
)
ADL2_DISPLAY_SWITCHINGCAPABILITY_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_SWITCHINGCAPABILITY_GET = _int(
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_DITHERSTATE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_DITHERSTATE_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_DITHERSTATE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_DITHERSTATE_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_SUPPORTEDPIXELFORMAT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_SUPPORTEDPIXELFORMAT_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_PIXELFORMAT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_PIXELFORMAT_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_PIXELFORMATDEFAULT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_PIXELFORMAT_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_PIXELFORMAT_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_SUPPORTEDCOLORDEPTH_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_SUPPORTEDCOLORDEPTH_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_COLORDEPTH_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_COLORDEPTH_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_COLORDEPTH_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_COLORDEPTH_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_ODCLOCKINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLAdapterODClockInfo)
)
ADL_DISPLAY_ODCLOCKINFO_GET = _int(
    INT,
    POINTER(ADLAdapterODClockInfo)
)
ADL2_DISPLAY_ODCLOCKCONFIG_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLAdapterODClockConfig)
)
ADL_DISPLAY_ODCLOCKCONFIG_SET = _int(
    INT,
    POINTER(ADLAdapterODClockConfig)
)
ADL2_DISPLAY_ADJUSTMENTCOHERENT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_ADJUSTMENTCOHERENT_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_ADJUSTMENTCOHERENT_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_ADJUSTMENTCOHERENT_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_REDUCEDBLANKING_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_REDUCEDBLANKING_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_REDUCEDBLANKING_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_REDUCEDBLANKING_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_FORMATSOVERRIDE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_FORMATSOVERRIDE_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_FORMATSOVERRIDE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_FORMATSOVERRIDE_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_MVPUCAPS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLMVPUCaps)
)
ADL_DISPLAY_MVPUCAPS_GET = _int(
    INT,
    POINTER(ADLMVPUCaps)
)
ADL2_DISPLAY_MVPUSTATUS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLMVPUStatus)
)
ADL_DISPLAY_MVPUSTATUS_GET = _int(
    INT,
    POINTER(ADLMVPUStatus)
)
ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTCAPS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLControllerOverlayInput),
    POINTER(ADLControllerOverlayInfo)
)
ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTCAPS_GET = _int(
    INT,
    POINTER(ADLControllerOverlayInput),
    POINTER(ADLControllerOverlayInfo)
)
ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLControllerOverlayInput)
)
ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_GET = _int(
    INT,
    POINTER(ADLControllerOverlayInput)
)
ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLControllerOverlayInput)
)
ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_SET = _int(
    INT,
    POINTER(ADLControllerOverlayInput)
)
ADL2_DISPLAY_VIEWPORT_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLControllerMode)
)
ADL_DISPLAY_VIEWPORT_SET = _int(
    INT,
    INT,
    POINTER(ADLControllerMode)
)
ADL2_DISPLAY_VIEWPORT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLControllerMode)
)
ADL_DISPLAY_VIEWPORT_GET = _int(
    INT,
    INT,
    POINTER(ADLControllerMode)
)
ADL2_DISPLAY_VIEWPORT_CAP = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_VIEWPORT_CAP = _int(
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_WRITEANDREADI2CREV_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_WRITEANDREADI2CREV_GET = _int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_WRITEANDREADI2C = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLI2C)
)
ADL_DISPLAY_WRITEANDREADI2C = _int(
    INT,
    POINTER(ADLI2C)
)
ADL2_DISPLAY_DDCBLOCKACCESS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT,
    INT,
    POINTER(CHAR),
    POINTER(INT),
    POINTER(CHAR)
)
ADL_DISPLAY_DDCBLOCKACCESS_GET = _int(
    INT,
    INT,
    INT,
    INT,
    INT,
    POINTER(CHAR),
    POINTER(INT),
    POINTER(CHAR)
)
ADL2_DISPLAY_DDCINFO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDDCInfo)
)
ADL_DISPLAY_DDCINFO_GET = _int(
    INT,
    INT,
    POINTER(ADLDDCInfo)
)
ADL2_DISPLAY_DDCINFO2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDDCInfo2)
)
ADL_DISPLAY_DDCINFO2_GET = _int(
    INT,
    INT,
    POINTER(ADLDDCInfo2)
)
ADL2_DISPLAY_EDIDDATA_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayEDIDData)
)
ADL_DISPLAY_EDIDDATA_GET = _int(
    INT,
    INT,
    POINTER(ADLDisplayEDIDData)
)
ADL2_DISPLAY_COLORCAPS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_COLORCAPS_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_COLOR_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT
)
ADL_DISPLAY_COLOR_SET = _int(
    INT,
    INT,
    INT,
    INT
)
ADL2_DISPLAY_COLOR_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_COLOR_GET = _int(
    INT,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_COLORTEMPERATURESOURCE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_COLORTEMPERATURESOURCE_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_COLORTEMPERATURESOURCEDEFAULT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_COLORTEMPERATURESOURCE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_COLORTEMPERATURESOURCE_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_MODETIMINGOVERRIDE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayMode),
    POINTER(ADLDisplayModeInfo)
)
ADL_DISPLAY_MODETIMINGOVERRIDE_GET = _int(
    INT,
    INT,
    POINTER(ADLDisplayMode),
    POINTER(ADLDisplayModeInfo)
)
ADL2_DISPLAY_MODETIMINGOVERRIDE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayModeInfo),
    INT
)
ADL_DISPLAY_MODETIMINGOVERRIDE_SET = _int(
    INT,
    INT,
    POINTER(ADLDisplayModeInfo),
    INT
)
ADL2_DISPLAY_MODETIMINGOVERRIDELIST_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLDisplayModeInfo),
    POINTER(INT)
)
ADL_DISPLAY_MODETIMINGOVERRIDELIST_GET = _int(
    INT,
    INT,
    INT,
    POINTER(ADLDisplayModeInfo),
    POINTER(INT)
)
ADL2_DISPLAY_CUSTOMIZEDMODELISTNUM_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_CUSTOMIZEDMODELISTNUM_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_CUSTOMIZEDMODELIST_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLCustomMode),
    INT
)
ADL_DISPLAY_CUSTOMIZEDMODELIST_GET = _int(
    INT,
    INT,
    POINTER(ADLCustomMode),
    INT
)
ADL2_DISPLAY_CUSTOMIZEDMODE_ADD = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    ADLCustomMode
)
ADL_DISPLAY_CUSTOMIZEDMODE_ADD = _int(
    INT,
    INT,
    ADLCustomMode
)
ADL2_DISPLAY_CUSTOMIZEDMODE_DELETE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_CUSTOMIZEDMODE_DELETE = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_CUSTOMIZEDMODE_VALIDATE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    ADLCustomMode,
    POINTER(INT)
)
ADL_DISPLAY_CUSTOMIZEDMODE_VALIDATE = _int(
    INT,
    INT,
    ADLCustomMode,
    POINTER(INT)
)
ADL2_DISPLAY_UNDERSCANSUPPORT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_UNDERSCANSTATE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_UNDERSCANSTATE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL2_DISPLAY_UNDERSCAN_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_UNDERSCAN_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_UNDERSCAN_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_UNDERSCAN_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_OVERSCAN_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_OVERSCAN_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_OVERSCAN_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_OVERSCAN_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DFP_BASEAUDIOSUPPORT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DFP_BASEAUDIOSUPPORT_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DFP_HDMISUPPORT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DFP_HDMISUPPORT_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DFP_MVPUANALOGSUPPORT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DFP_MVPUANALOGSUPPORT_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DFP_PIXELFORMAT_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_DFP_PIXELFORMAT_CAPS = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DFP_PIXELFORMAT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_DFP_PIXELFORMAT_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_DFP_PIXELFORMAT_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DFP_PIXELFORMAT_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DFP_GPUSCALINGENABLE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DFP_GPUSCALINGENABLE_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DFP_GPUSCALINGENABLE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DFP_GPUSCALINGENABLE_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DFP_ALLOWONLYCETIMINGS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DFP_ALLOWONLYCETIMINGS_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DFP_ALLOWONLYCETIMINGS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DFP_ALLOWONLYCETIMINGS_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_TVCAPS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_TVCAPS_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_TV_STANDARD_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_TV_STANDARD_SET = _int(
    INT,
    INT,
    INT
)
ADL2_TV_STANDARD_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_TV_STANDARD_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_CV_DONGLESETTINGS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_CV_DONGLESETTINGS_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_CV_DONGLESETTINGS_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_CV_DONGLESETTINGS_SET = _int(
    INT,
    INT,
    INT
)
ADL2_CV_DONGLESETTINGS_RESET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_CV_DONGLESETTINGS_RESET = _int(
    INT,
    INT
)
ADL2_DISPLAY_UNDERSCAN_AUTO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_UNDERSCAN_AUTO_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_UNDERSCAN_AUTO_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_UNDERSCAN_AUTO_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_DEFLICKER_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_DEFLICKER_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_DEFLICKER_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_DEFLICKER_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_FILTERSVIDEO_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_FILTERSVIDEO_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_FILTERSVIDEO_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_FILTERSVIDEO_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_DISPLAYCONTENT_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_DISPLAYCONTENT_SET = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_DISPLAYCONTENT_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_DISPLAYCONTENT_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_DISPLAYCONTENT_CAP = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_DISPLAYCONTENT_CAP = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_MODETIMINGOVERRIDE_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_MODETIMINGOVERRIDE_CAPS = _int(
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_TARGETTIMING_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDisplayID,
    POINTER(ADLDisplayModeInfo)
)
ADL_DISPLAY_TARGETTIMING_GET = _int(
    INT,
    ADLDisplayID,
    POINTER(ADLDisplayModeInfo)
)
ADL2_DISPLAY_MODETIMINGOVERRIDEX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDisplayID,
    POINTER(ADLDisplayModeX2),
    POINTER(ADLDisplayModeInfo)
)
ADL_DISPLAY_MODETIMINGOVERRIDEX2_GET = _int(
    INT,
    ADLDisplayID,
    POINTER(ADLDisplayModeX2),
    POINTER(ADLDisplayModeInfo)
)
ADL2_DISPLAY_MODETIMINGOVERRIDELISTX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDisplayID,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayModeInfo))
)
ADL_DISPLAY_MODETIMINGOVERRIDELISTX2_GET = _int(
    INT,
    ADLDisplayID,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayModeInfo))
)
ADL2_DISPLAY_MODETIMINGOVERRIDE_DELETE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDisplayID,
    POINTER(ADLDisplayModeX2),
    INT
)
ADL_DISPLAY_MODETIMINGOVERRIDE_DELETE = _int(
    INT,
    ADLDisplayID,
    POINTER(ADLDisplayModeX2),
    INT
)
ADL_DISPLAY_DOWNSCALING_CAPS = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_DOWNSCALING_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_FREESYNCSTATE_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_DISPLAY_FREESYNCSTATE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_DISPLAY_FREESYNCSTATE_SET = _int(
    INT,
    INT,
    INT,
    INT
)
ADL2_DISPLAY_FREESYNCSTATE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT
)
ADL2_DISPLAY_DCE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDceSettings)
)
ADL_DISPLAY_DCE_SET = _int(
    INT,
    INT,
    POINTER(ADLDceSettings)
)
ADL2_DISPLAY_DCE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDceSettings)
)
ADL_DISPLAY_DCE_GET = _int(
    INT,
    INT,
    POINTER(ADLDceSettings)
)
ADL2_DISPLAY_FREESYNC_CAP = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLFreeSyncCap)
)
ADL_DISPLAY_FREESYNC_CAP = _int(
    INT,
    INT,
    POINTER(ADLFreeSyncCap)
)
ADL_CDS_UNSAFEMODE_SET = _int(
    INT,
    INT
)
ADL2_CDS_UNSAFEMODE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)


# Function to retrieve the adapter display information.
_ADL2_Display_DisplayInfo_Get = ADL2_DISPLAY_DISPLAYINFO_GET

# Function to retrieve the adapter display information.
_ADL_Display_DisplayInfo_Get = ADL_DISPLAY_DISPLAYINFO_GET

# Function to retrieve the Display Port MST information.
_ADL2_Display_DpMstInfo_Get = ADL2_DISPLAY_DPMSTINFO_GET

# Function to retrieve the Display Port MST information.
_ADL_Display_DpMstInfo_Get = ADL_DISPLAY_DPMSTINFO_GET

# Function to retrieve the number of displays supported by an adapter.
_ADL2_Display_NumberOfDisplays_Get = ADL2_DISPLAY_NUMBEROFDISPLAYS_GET

# Function to retrieve the number of displays supported by an adapter.
_ADL_Display_NumberOfDisplays_Get = ADL_DISPLAY_NUMBEROFDISPLAYS_GET

# Function to retrieve the display perserved aspect ratio of an adapter.
_ADL2_Display_PreservedAspectRatio_Get = ADL2_DISPLAY_PRESERVEDASPECTRATIO_GET

# Function to retrieve the display perserved aspect ratio of an adapter.
_ADL_Display_PreservedAspectRatio_Get = ADL_DISPLAY_PRESERVEDASPECTRATIO_GET

# Function to set the display preserved aspect ratio.
_ADL2_Display_PreservedAspectRatio_Set = ADL2_DISPLAY_PRESERVEDASPECTRATIO_SET

# Function to set the display preserved aspect ratio.
_ADL_Display_PreservedAspectRatio_Set = ADL_DISPLAY_PRESERVEDASPECTRATIO_SET

# Function to retrieve the display image expansion setting.
_ADL2_Display_ImageExpansion_Get = ADL2_DISPLAY_IMAGEEXPANSION_GET

# Function to retrieve the display image expansion setting.
_ADL_Display_ImageExpansion_Get = ADL_DISPLAY_IMAGEEXPANSION_GET

# Function to set the display image expansion setting.
_ADL2_Display_ImageExpansion_Set = ADL2_DISPLAY_IMAGEEXPANSION_SET

# Function to set the display image expansion setting.
_ADL_Display_ImageExpansion_Set = ADL_DISPLAY_IMAGEEXPANSION_SET

# Function to get Device Display Position.
_ADL2_Display_Position_Get = ADL2_DISPLAY_POSITION_GET

# Function to get Device Display Position.
_ADL_Display_Position_Get = ADL_DISPLAY_POSITION_GET

# Function to set the Device Display Position.
_ADL2_Display_Position_Set = ADL2_DISPLAY_POSITION_SET

# Function to set the Device Display Position.
_ADL_Display_Position_Set = ADL_DISPLAY_POSITION_SET

# Function to get the Device Display Size.
_ADL2_Display_Size_Get = ADL2_DISPLAY_SIZE_GET

# Function to get the Device Display Size.
_ADL_Display_Size_Get = ADL_DISPLAY_SIZE_GET

# Function to set the Device Display Size.
_ADL2_Display_Size_Set = ADL2_DISPLAY_SIZE_SET

# Function to set the Device Display Size.
_ADL_Display_Size_Set = ADL_DISPLAY_SIZE_SET

# Function to retrieve the adjustment display information.
_ADL2_Display_AdjustCaps_Get = ADL2_DISPLAY_ADJUSTCAPS_GET

# Function to retrieve the adjustment display information.
_ADL_Display_AdjustCaps_Get = ADL_DISPLAY_ADJUSTCAPS_GET

# Function to get the number of displays and controllers supported by an adapter.
_ADL2_Display_Capabilities_Get = ADL2_DISPLAY_CAPABILITIES_GET

# Function to get the number of displays and controllers supported by an adapter.
_ADL_Display_Capabilities_Get = ADL_DISPLAY_CAPABILITIES_GET

# Function to indicate whether displays are physically connected to an adapter.
_ADL2_Display_ConnectedDisplays_Get = ADL2_DISPLAY_CONNECTEDDISPLAYS_GET

# Function to indicate whether displays are physically connected to an adapter.
_ADL_Display_ConnectedDisplays_Get = ADL_DISPLAY_CONNECTEDDISPLAYS_GET

# Function to get HDTV capability settings.
_ADL2_Display_DeviceConfig_Get = ADL2_DISPLAY_DEVICECONFIG_GET

# Function to get HDTV capability settings.
_ADL_Display_DeviceConfig_Get = ADL_DISPLAY_DEVICECONFIG_GET

# Function to get the current display property value.
_ADL2_Display_Property_Get = ADL2_DISPLAY_PROPERTY_GET

# Function to get the current display property value.
_ADL_Display_Property_Get = ADL_DISPLAY_PROPERTY_GET

# Function to set current display property value.
_ADL2_Display_Property_Set = ADL2_DISPLAY_PROPERTY_SET

# Function to set current display property value.
_ADL_Display_Property_Set = ADL_DISPLAY_PROPERTY_SET

# Function to retrieve the Display Switching Flag from the registry.
_ADL2_Display_SwitchingCapability_Get = ADL2_DISPLAY_SWITCHINGCAPABILITY_GET

_ADL_Display_SwitchingCapability_Get = ADL_DISPLAY_SWITCHINGCAPABILITY_GET

# Function to retrieve the dither state.
_ADL2_Display_DitherState_Get = ADL2_DISPLAY_DITHERSTATE_GET

# Function to retrieve the dither state.
_ADL_Display_DitherState_Get = ADL_DISPLAY_DITHERSTATE_GET

# Function to set the dither state.
_ADL2_Display_DitherState_Set = ADL2_DISPLAY_DITHERSTATE_SET

# Function to set the dither state.
_ADL_Display_DitherState_Set = ADL_DISPLAY_DITHERSTATE_SET

# Function to retrieve the supported pixel format. HDMI only.
_ADL2_Display_SupportedPixelFormat_Get = ADL2_DISPLAY_SUPPORTEDPIXELFORMAT_GET

# Function to retrieve the supported pixel format. HDMI only.
_ADL_Display_SupportedPixelFormat_Get = ADL_DISPLAY_SUPPORTEDPIXELFORMAT_GET

# Function to retrieve the current display pixel format. HDMI only.
_ADL2_Display_PixelFormat_Get = ADL2_DISPLAY_PIXELFORMAT_GET

# Function to retrieve the current display pixel format. HDMI only.
_ADL_Display_PixelFormat_Get = ADL_DISPLAY_PIXELFORMAT_GET

# Function to retrieve the current display pixel format. HDMI only.
_ADL2_Display_PixelFormatDefault_Get = ADL2_DISPLAY_PIXELFORMATDEFAULT_GET

# Function to set the current display pixel format. HDMI only.
_ADL2_Display_PixelFormat_Set = ADL2_DISPLAY_PIXELFORMAT_SET

# Function to set the current display pixel format. HDMI only.
_ADL_Display_PixelFormat_Set = ADL_DISPLAY_PIXELFORMAT_SET

# Function to retrieve the supported color depth. HDMI and DPonly.
_ADL2_Display_SupportedColorDepth_Get = ADL2_DISPLAY_SUPPORTEDCOLORDEPTH_GET

# Function to retrieve the supported color depth. HDMI and DPonly.
_ADL_Display_SupportedColorDepth_Get = ADL_DISPLAY_SUPPORTEDCOLORDEPTH_GET

# Function to get color depth. HDMI and DPonly.
_ADL2_Display_ColorDepth_Get = ADL2_DISPLAY_COLORDEPTH_GET

# Function to get color depth. HDMI and DPonly.
_ADL_Display_ColorDepth_Get = ADL_DISPLAY_COLORDEPTH_GET

# Function to set color depth. HDMI and DPonly.
_ADL2_Display_ColorDepth_Set = ADL2_DISPLAY_COLORDEPTH_SET

# Function to set color depth. HDMI and DPonly.
_ADL_Display_ColorDepth_Set = ADL_DISPLAY_COLORDEPTH_SET

# Function to retrieve the OD clock information.
_ADL2_Display_ODClockInfo_Get = ADL2_DISPLAY_ODCLOCKINFO_GET

# Function to retrieve the OD clock information.
_ADL_Display_ODClockInfo_Get = ADL_DISPLAY_ODCLOCKINFO_GET

# Function to set the OD clock configuration.
_ADL2_Display_ODClockConfig_Set = ADL2_DISPLAY_ODCLOCKCONFIG_SET

# Function to set the OD clock configuration.
_ADL_Display_ODClockConfig_Set = ADL_DISPLAY_ODCLOCKCONFIG_SET

# Function to retrieve the adjustment coherent setting.
_ADL2_Display_AdjustmentCoherent_Get = ADL2_DISPLAY_ADJUSTMENTCOHERENT_GET

# Function to retrieve the adjustment coherent setting.
_ADL_Display_AdjustmentCoherent_Get = ADL_DISPLAY_ADJUSTMENTCOHERENT_GET

# Function to set the adjustment coherent setting.
_ADL2_Display_AdjustmentCoherent_Set = ADL2_DISPLAY_ADJUSTMENTCOHERENT_SET

# Function to set the adjustment coherent setting.
_ADL_Display_AdjustmentCoherent_Set = ADL_DISPLAY_ADJUSTMENTCOHERENT_SET

# Function to retrieve the reduced blanking setting.
_ADL2_Display_ReducedBlanking_Get = ADL2_DISPLAY_REDUCEDBLANKING_GET

# Function to retrieve the reduced blanking setting.
_ADL_Display_ReducedBlanking_Get = ADL_DISPLAY_REDUCEDBLANKING_GET

# Function to set the reduced blanking setting.
_ADL2_Display_ReducedBlanking_Set = ADL2_DISPLAY_REDUCEDBLANKING_SET

# Function to set the reduced blanking setting.
_ADL_Display_ReducedBlanking_Set = ADL_DISPLAY_REDUCEDBLANKING_SET

# Function to retrieve the available display formats.
_ADL2_Display_FormatsOverride_Get = ADL2_DISPLAY_FORMATSOVERRIDE_GET

# Function to retrieve the available display formats.
_ADL_Display_FormatsOverride_Get = ADL_DISPLAY_FORMATSOVERRIDE_GET

# Function to overide the display formats.
_ADL2_Display_FormatsOverride_Set = ADL2_DISPLAY_FORMATSOVERRIDE_SET

# Function to overide the display formats.
_ADL_Display_FormatsOverride_Set = ADL_DISPLAY_FORMATSOVERRIDE_SET

# Function to retrieve the information about MultiVPU capabilities.
_ADL2_Display_MVPUCaps_Get = ADL2_DISPLAY_MVPUCAPS_GET

# Function to retrieve the information about MultiVPU capabilities.
_ADL_Display_MVPUCaps_Get = ADL_DISPLAY_MVPUCAPS_GET

# Function to retrieve information about MultiVPU status.
_ADL2_Display_MVPUStatus_Get = ADL2_DISPLAY_MVPUSTATUS_GET

# Function to retrieve information about MultiVPU status.
_ADL_Display_MVPUStatus_Get = ADL_DISPLAY_MVPUSTATUS_GET

# Function to get the minimum, maximum, and default values of an overlay adjustment.
_ADL2_Display_ControllerOverlayAdjustmentCaps_Get = ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTCAPS_GET

# Function to get the minimum, maximum, and default values of an overlay adjustment.
_ADL_Display_ControllerOverlayAdjustmentCaps_Get = ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTCAPS_GET

# Function to retrieve the current setting of an overlay adjustment.
_ADL2_Display_ControllerOverlayAdjustmentData_Get = ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_GET

# Function to retrieve the current setting of an overlay adjustment.
_ADL_Display_ControllerOverlayAdjustmentData_Get = ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_GET

# Function to set the current setting of an overlay adjustment.
_ADL2_Display_ControllerOverlayAdjustmentData_Set = ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_SET

# Function to set the current setting of an overlay adjustment.
_ADL_Display_ControllerOverlayAdjustmentData_Set = ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_SET

# Function to change the view position, view size or view pan lock of a selected display.
_ADL2_Display_ViewPort_Set = ADL2_DISPLAY_VIEWPORT_SET

# Function to change the view position, view size or view pan lock of a selected display.
_ADL_Display_ViewPort_Set = ADL_DISPLAY_VIEWPORT_SET

# Function to get the view position, view size or view pan lock of a selected display.
_ADL2_Display_ViewPort_Get = ADL2_DISPLAY_VIEWPORT_GET

# Function to get the view position, view size or view pan lock of a selected display.
_ADL_Display_ViewPort_Get = ADL_DISPLAY_VIEWPORT_GET

# Function to check if the selected adapter supports the view port control.
_ADL2_Display_ViewPort_Cap = ADL2_DISPLAY_VIEWPORT_CAP

# Function to check if the selected adapter supports the view port control.
_ADL_Display_ViewPort_Cap = ADL_DISPLAY_VIEWPORT_CAP

# Function to retrieve the I2C API revision.
_ADL2_Display_WriteAndReadI2CRev_Get = ADL2_DISPLAY_WRITEANDREADI2CREV_GET

# Function to retrieve the I2C API revision.
_ADL_Display_WriteAndReadI2CRev_Get = ADL_DISPLAY_WRITEANDREADI2CREV_GET

# Function to write and read I2C.
_ADL2_Display_WriteAndReadI2C = ADL2_DISPLAY_WRITEANDREADI2C

# Function to write and read I2C.
_ADL_Display_WriteAndReadI2C = ADL_DISPLAY_WRITEANDREADI2C

# Function to get Display DDC block access.
_ADL2_Display_DDCBlockAccess_Get = ADL2_DISPLAY_DDCBLOCKACCESS_GET

# Function to get Display DDC block access.
_ADL_Display_DDCBlockAccess_Get = ADL_DISPLAY_DDCBLOCKACCESS_GET

# Function to get the DDC info.
_ADL2_Display_DDCInfo_Get = ADL2_DISPLAY_DDCINFO_GET

# Function to get the DDC info.
_ADL_Display_DDCInfo_Get = ADL_DISPLAY_DDCINFO_GET

# Function to get the DDC info.
_ADL2_Display_DDCInfo2_Get = ADL2_DISPLAY_DDCINFO2_GET

# Function to get the DDC info.
_ADL_Display_DDCInfo2_Get = ADL_DISPLAY_DDCINFO2_GET

# Function to get the EDID data.
_ADL2_Display_EdidData_Get = ADL2_DISPLAY_EDIDDATA_GET

# Function to get the EDID data.
_ADL_Display_EdidData_Get = ADL_DISPLAY_EDIDDATA_GET

# Function to get the Color Caps display information.
_ADL2_Display_ColorCaps_Get = ADL2_DISPLAY_COLORCAPS_GET

# Function to get the Color Caps display information.
_ADL_Display_ColorCaps_Get = ADL_DISPLAY_COLORCAPS_GET

# Function to set the current value of a specific color and type.
_ADL2_Display_Color_Set = ADL2_DISPLAY_COLOR_SET

# Function to set the current value of a specific color and type.
_ADL_Display_Color_Set = ADL_DISPLAY_COLOR_SET

# Function to retrieve the detailed information a specified display color item.
_ADL2_Display_Color_Get = ADL2_DISPLAY_COLOR_GET

# Function to retrieve the detailed information a specified display color item.
_ADL_Display_Color_Get = ADL_DISPLAY_COLOR_GET

# Function to get color temperature source.
_ADL2_Display_ColorTemperatureSource_Get = ADL2_DISPLAY_COLORTEMPERATURESOURCE_GET

# Function to get color temperature source.
_ADL_Display_ColorTemperatureSource_Get = ADL_DISPLAY_COLORTEMPERATURESOURCE_GET

# Function to get default color temperature source.
_ADL2_Display_ColorTemperatureSourceDefault_Get = ADL2_DISPLAY_COLORTEMPERATURESOURCEDEFAULT_GET

# Function to set the color temperature source.
_ADL2_Display_ColorTemperatureSource_Set = ADL2_DISPLAY_COLORTEMPERATURESOURCE_SET

# Function to set the color temperature source.
_ADL_Display_ColorTemperatureSource_Set = ADL_DISPLAY_COLORTEMPERATURESOURCE_SET

# Function to retrieve display mode timing override information.
_ADL2_Display_ModeTimingOverride_Get = ADL2_DISPLAY_MODETIMINGOVERRIDE_GET

# Function to retrieve display mode timing override information.
_ADL_Display_ModeTimingOverride_Get = ADL_DISPLAY_MODETIMINGOVERRIDE_GET

# Function to set display mode timing override information.
_ADL2_Display_ModeTimingOverride_Set = ADL2_DISPLAY_MODETIMINGOVERRIDE_SET

# Function to set display mode timing override information.
_ADL_Display_ModeTimingOverride_Set = ADL_DISPLAY_MODETIMINGOVERRIDE_SET

# Function to get the display mode timing override list.
_ADL2_Display_ModeTimingOverrideList_Get = ADL2_DISPLAY_MODETIMINGOVERRIDELIST_GET

# Function to get the display mode timing override list.
_ADL_Display_ModeTimingOverrideList_Get = ADL_DISPLAY_MODETIMINGOVERRIDELIST_GET

# Function to retrieve the number of customized modes.
_ADL2_Display_CustomizedModeListNum_Get = ADL2_DISPLAY_CUSTOMIZEDMODELISTNUM_GET

# Function to retrieve the number of customized modes.
_ADL_Display_CustomizedModeListNum_Get = ADL_DISPLAY_CUSTOMIZEDMODELISTNUM_GET

# Function to retrieve the customized mode list.
_ADL2_Display_CustomizedModeList_Get = ADL2_DISPLAY_CUSTOMIZEDMODELIST_GET

# Function to retrieve the customized mode list.
_ADL_Display_CustomizedModeList_Get = ADL_DISPLAY_CUSTOMIZEDMODELIST_GET

# Function to add a customized mode.
_ADL2_Display_CustomizedMode_Add = ADL2_DISPLAY_CUSTOMIZEDMODE_ADD

# Function to add a customized mode.
_ADL_Display_CustomizedMode_Add = ADL_DISPLAY_CUSTOMIZEDMODE_ADD

# Function to delete a customized mode.
_ADL2_Display_CustomizedMode_Delete = ADL2_DISPLAY_CUSTOMIZEDMODE_DELETE

# Function to delete a customized mode.
_ADL_Display_CustomizedMode_Delete = ADL_DISPLAY_CUSTOMIZEDMODE_DELETE

# Function to validate a customized mode.
_ADL2_Display_CustomizedMode_Validate = ADL2_DISPLAY_CUSTOMIZEDMODE_VALIDATE

# Function to validate a customized mode.
_ADL_Display_CustomizedMode_Validate = ADL_DISPLAY_CUSTOMIZEDMODE_VALIDATE

# Function to get the value of under scan support.
_ADL2_Display_UnderscanSupport_Get = ADL2_DISPLAY_UNDERSCANSUPPORT_GET

# Function to get the value of under scan enabled.
_ADL2_Display_UnderscanState_Get = ADL2_DISPLAY_UNDERSCANSTATE_GET

# Function to set the value of under scan enabled.
_ADL2_Display_UnderscanState_Set = ADL2_DISPLAY_UNDERSCANSTATE_SET

# Function to set the current value of underscan.
_ADL2_Display_Underscan_Set = ADL2_DISPLAY_UNDERSCAN_SET

# Function to set the current value of underscan.
_ADL_Display_Underscan_Set = ADL_DISPLAY_UNDERSCAN_SET

# Function to retrieve the detailed information for underscan.
_ADL2_Display_Underscan_Get = ADL2_DISPLAY_UNDERSCAN_GET

# Function to retrieve the detailed information for underscan.
_ADL_Display_Underscan_Get = ADL_DISPLAY_UNDERSCAN_GET

# Function to set the current value of gamma for each controller.
_ADL2_Display_Overscan_Set = ADL2_DISPLAY_OVERSCAN_SET

# Function to set the current value of gamma for each controller.
_ADL_Display_Overscan_Set = ADL_DISPLAY_OVERSCAN_SET

# Function to retrieve the current value of gamma for each controller.
_ADL2_Display_Overscan_Get = ADL2_DISPLAY_OVERSCAN_GET

# Function to retrieve the current value of gamma for each controller.
_ADL_Display_Overscan_Get = ADL_DISPLAY_OVERSCAN_GET

# Function to get the display base audio support.
_ADL2_DFP_BaseAudioSupport_Get = ADL2_DFP_BASEAUDIOSUPPORT_GET

# Function to get the display base audio support.
_ADL_DFP_BaseAudioSupport_Get = ADL_DFP_BASEAUDIOSUPPORT_GET

# Function to get the display HDMI support.
_ADL2_DFP_HDMISupport_Get = ADL2_DFP_HDMISUPPORT_GET

# Function to get the display HDMI support.
_ADL_DFP_HDMISupport_Get = ADL_DFP_HDMISUPPORT_GET

# Function to get the display MVPU analog support.
_ADL2_DFP_MVPUAnalogSupport_Get = ADL2_DFP_MVPUANALOGSUPPORT_GET

# Function to get the display MVPU analog support.
_ADL_DFP_MVPUAnalogSupport_Get = ADL_DFP_MVPUANALOGSUPPORT_GET

# Function to retrieve PixelFormat caps.
_ADL2_DFP_PixelFormat_Caps = ADL2_DFP_PIXELFORMAT_CAPS

# Function to retrieve PixelFormat caps.
_ADL_DFP_PixelFormat_Caps = ADL_DFP_PIXELFORMAT_CAPS

# Function to retrieve current pixel format setting.
_ADL2_DFP_PixelFormat_Get = ADL2_DFP_PIXELFORMAT_GET

# Function to retrieve current pixel format setting.
_ADL_DFP_PixelFormat_Get = ADL_DFP_PIXELFORMAT_GET

# Function to set the current pixel format setting.
_ADL2_DFP_PixelFormat_Set = ADL2_DFP_PIXELFORMAT_SET

# Function to set the current pixel format setting.
_ADL_DFP_PixelFormat_Set = ADL_DFP_PIXELFORMAT_SET

# Function to get the GPUScalingEnable setting.
_ADL2_DFP_GPUScalingEnable_Get = ADL2_DFP_GPUSCALINGENABLE_GET

# Function to get the GPUScalingEnable setting.
_ADL_DFP_GPUScalingEnable_Get = ADL_DFP_GPUSCALINGENABLE_GET

# Function to set the GPUScalingEnable setting.
_ADL2_DFP_GPUScalingEnable_Set = ADL2_DFP_GPUSCALINGENABLE_SET

# Function to set the GPUScalingEnable setting.
_ADL_DFP_GPUScalingEnable_Set = ADL_DFP_GPUSCALINGENABLE_SET

# Function to get the Allow Only CE Timings setting.
_ADL2_DFP_AllowOnlyCETimings_Get = ADL2_DFP_ALLOWONLYCETIMINGS_GET

# Function to get the Allow Only CE Timings setting.
_ADL_DFP_AllowOnlyCETimings_Get = ADL_DFP_ALLOWONLYCETIMINGS_GET

# Function to set the Allow Only CE Timings setting.
_ADL2_DFP_AllowOnlyCETimings_Set = ADL2_DFP_ALLOWONLYCETIMINGS_SET

# Function to set the Allow Only CE Timings setting.
_ADL_DFP_AllowOnlyCETimings_Set = ADL_DFP_ALLOWONLYCETIMINGS_SET

# Function to retrieve the TV Caps display information.
_ADL2_Display_TVCaps_Get = ADL2_DISPLAY_TVCAPS_GET

# Function to retrieve the TV Caps display information.
_ADL_Display_TVCaps_Get = ADL_DISPLAY_TVCAPS_GET

# Function to set the TV standard.
_ADL2_TV_Standard_Set = ADL2_TV_STANDARD_SET

# Function to set the TV standard.
_ADL_TV_Standard_Set = ADL_TV_STANDARD_SET

# Function to retrieve the TV standard.
_ADL2_TV_Standard_Get = ADL2_TV_STANDARD_GET

# Function to retrieve the TV standard.
_ADL_TV_Standard_Get = ADL_TV_STANDARD_GET

# Function to retrieve the settings of the CV dongle.
_ADL2_CV_DongleSettings_Get = ADL2_CV_DONGLESETTINGS_GET

# Function to retrieve the settings of the CV dongle.
_ADL_CV_DongleSettings_Get = ADL_CV_DONGLESETTINGS_GET

# Function to set the current CV dongle settings.
_ADL2_CV_DongleSettings_Set = ADL2_CV_DONGLESETTINGS_SET

# Function to set the current CV dongle settings.
_ADL_CV_DongleSettings_Set = ADL_CV_DONGLESETTINGS_SET

# Function to reset the CV settings to its default settings.
_ADL2_CV_DongleSettings_Reset = ADL2_CV_DONGLESETTINGS_RESET

# Function to reset the CV settings to its default settings.
_ADL_CV_DongleSettings_Reset = ADL_CV_DONGLESETTINGS_RESET

# Function to get the current UnderScan Auto setting from the display. This function 
# retrieves the UnderScan Auto information for a specified display.
_ADL2_Display_UnderScan_Auto_Get = ADL2_DISPLAY_UNDERSCAN_AUTO_GET

# Function to get the current UnderScan Auto setting from the display. This function 
# retrieves the UnderScan Auto information for a specified display.
_ADL_Display_UnderScan_Auto_Get = ADL_DISPLAY_UNDERSCAN_AUTO_GET

# Function to set the current UnderScan Auto setting for the display. This function set 
# the UnderScan Auto setting for a specified display.
_ADL2_Display_UnderScan_Auto_Set = ADL2_DISPLAY_UNDERSCAN_AUTO_SET

# Function to set the current UnderScan Auto setting for the display. This function set 
# the UnderScan Auto setting for a specified display.
_ADL_Display_UnderScan_Auto_Set = ADL_DISPLAY_UNDERSCAN_AUTO_SET

# Function to get the current Deflicker setting from the display. This function retrieves 
# the Deflicker information for a specified display.
_ADL2_Display_Deflicker_Get = ADL2_DISPLAY_DEFLICKER_GET

# Function to get the current Deflicker setting from the display. This function retrieves 
# the Deflicker information for a specified display.
_ADL_Display_Deflicker_Get = ADL_DISPLAY_DEFLICKER_GET

# Function to set the current Deflicker setting for the display. This function set the 
# Deflicker setting for a specified display.
_ADL2_Display_Deflicker_Set = ADL2_DISPLAY_DEFLICKER_SET

# Function to set the current Deflicker setting for the display. This function set the 
# Deflicker setting for a specified display.
_ADL_Display_Deflicker_Set = ADL_DISPLAY_DEFLICKER_SET

# Function to get the current FilterSVideo setting from the display. This function retrieves 
# the S-Video Sharpness Control information for a specified display.
_ADL2_Display_FilterSVideo_Get = ADL2_DISPLAY_FILTERSVIDEO_GET

# Function to get the current FilterSVideo setting from the display. This function retrieves 
# the S-Video Sharpness Control information for a specified display.
_ADL_Display_FilterSVideo_Get = ADL_DISPLAY_FILTERSVIDEO_GET

# Function to set the current FilterSVideo setting for the display. This function set the 
# S-Video Sharpness Control setting for a specified display.
_ADL2_Display_FilterSVideo_Set = ADL2_DISPLAY_FILTERSVIDEO_SET

# Function to set the current FilterSVideo setting for the display. This function set the 
# S-Video Sharpness Control setting for a specified display.
_ADL_Display_FilterSVideo_Set = ADL_DISPLAY_FILTERSVIDEO_SET

# This function sets the picture setting (Graphics, Photo, Cinema or Gaming) on any 
# HDMI that supports these modes. The application associated with this function is 
# designed such that, the ITC display option must be toggled 'ON' (checked) before
# display content options become available for setting. If the display content is set,
# but the ITC is toggled 'OFF', the display content options will disable (gray-out), 
# but still show which display content was last 'set'.
_ADL2_Display_DisplayContent_Set = ADL2_DISPLAY_DISPLAYCONTENT_SET

# This function sets the picture setting (Graphics, Photo, Cinema or Gaming) on any 
# HDMI that supports these modes. The application associated with this function is 
# designed such that, the ITC display option must be toggled 'ON' (checked) before 
# display content options become available for setting. If the display content is set,
# but the ITC is toggled 'OFF', the display content options will disable (gray-out), 
# but still show which display content was last 'set'.
_ADL_Display_DisplayContent_Set = ADL_DISPLAY_DISPLAYCONTENT_SET

# This function gets the picture setting (Graphics, Photo, Cinema or Gaming) on any 
# HDMI that supports these modes. The application associated with this function is designed 
# such that, even if the ITC display option is toggled 'OFF' (unchecked), this function will 
# still return the last display content mode that was set (or initial value of Graphics).
_ADL2_Display_DisplayContent_Get = ADL2_DISPLAY_DISPLAYCONTENT_GET

# This function gets the picture setting (Graphics, Photo, Cinema or Gaming) on any 
# HDMI that supports these modes. The application associated with this function is designed 
# such that, even if the ITC display option is toggled 'OFF' (unchecked), this function will 
# still return the last display content mode that was set (or initial value of Graphics).
_ADL_Display_DisplayContent_Get = ADL_DISPLAY_DISPLAYCONTENT_GET

# This function gets the application availability for display content value and ITC flag.
_ADL2_Display_DisplayContent_Cap = ADL2_DISPLAY_DISPLAYCONTENT_CAP

# This function gets the application availability for display content value and ITC flag.
_ADL_Display_DisplayContent_Cap = ADL_DISPLAY_DISPLAYCONTENT_CAP

# Function to retrieve Timing Override support.
_ADL2_Adapter_ModeTimingOverride_Caps = ADL2_ADAPTER_MODETIMINGOVERRIDE_CAPS

# Function to retrieve Timing Override support.
_ADL_Adapter_ModeTimingOverride_Caps = ADL_ADAPTER_MODETIMINGOVERRIDE_CAPS

# Function to retrieve current display mode timing override information.
_ADL2_Display_TargetTiming_Get = ADL2_DISPLAY_TARGETTIMING_GET

# Function to retrieve current display mode timing override information.
_ADL_Display_TargetTiming_Get = ADL_DISPLAY_TARGETTIMING_GET

# Function to retrieve display mode timing override information.
_ADL2_Display_ModeTimingOverrideX2_Get = ADL2_DISPLAY_MODETIMINGOVERRIDEX2_GET

# Function to retrieve display mode timing override information.
_ADL_Display_ModeTimingOverrideX2_Get = ADL_DISPLAY_MODETIMINGOVERRIDEX2_GET

# Function to get the display mode timing override list.
_ADL2_Display_ModeTimingOverrideListX2_Get = ADL2_DISPLAY_MODETIMINGOVERRIDELISTX2_GET

# Function to get the display mode timing override list.
_ADL_Display_ModeTimingOverrideListX2_Get = ADL_DISPLAY_MODETIMINGOVERRIDELISTX2_GET

# Function to delete display mode timing override information.
_ADL2_Display_ModeTimingOverride_Delete = ADL2_DISPLAY_MODETIMINGOVERRIDE_DELETE

# Function to delete display mode timing override information.
_ADL_Display_ModeTimingOverride_Delete = ADL_DISPLAY_MODETIMINGOVERRIDE_DELETE

# Function to get the Down-scaling Caps display information.
_ADL_Display_Downscaling_Caps = ADL_DISPLAY_DOWNSCALING_CAPS

# Function to get the Down-scaling Caps display information.
_ADL2_Display_Downscaling_Caps = ADL2_DISPLAY_DOWNSCALING_CAPS

# Function to get the current state and capability of the FreeSync feature.
_ADL_Display_FreeSyncState_Get = ADL_DISPLAY_FREESYNCSTATE_GET

# Function to get the current state and capability of the FreeSync feature.
_ADL2_Display_FreeSyncState_Get = ADL2_DISPLAY_FREESYNCSTATE_GET

# Function to set the current state of the FreeSync feature.
_ADL_Display_FreeSyncState_Set = ADL_DISPLAY_FREESYNCSTATE_SET

# Function to set the current state of the FreeSync feature.
_ADL2_Display_FreeSyncState_Set = ADL2_DISPLAY_FREESYNCSTATE_SET

# Function to retrieve per display Display Connectivity Experience information.
_ADL2_Display_DCE_Set = ADL2_DISPLAY_DCE_SET

# Function to retrieve per display Display Connectivity Experience information.
_ADL_Display_DCE_Set = ADL_DISPLAY_DCE_SET

# Function to retrieve per display Display Connectivity Experience information.
_ADL2_Display_DCE_Get = ADL2_DISPLAY_DCE_GET

# Function to retrieve per display Display Connectivity Experience information.
_ADL_Display_DCE_Get = ADL_DISPLAY_DCE_GET

# Function to retrieve per display FreeSync capability information.
_ADL2_Display_FreeSync_Cap = ADL2_DISPLAY_FREESYNC_CAP

# Function to retrieve per display FreeSync capability information.
_ADL_Display_FreeSync_Cap = ADL_DISPLAY_FREESYNC_CAP

# Function to set the current EDS mode enumeration mode.
_ADL_CDS_UnsafeMode_Set = ADL_CDS_UNSAFEMODE_SET

# Function to set the current EDS mode enumeration mode.
_ADL2_CDS_UnsafeMode_Set = ADL2_CDS_UNSAFEMODE_SET


def Init(hDLL):
    global _ADL2_Display_DisplayInfo_Get
    global _ADL_Display_DisplayInfo_Get
    global _ADL2_Display_DpMstInfo_Get
    global _ADL_Display_DpMstInfo_Get
    global _ADL2_Display_NumberOfDisplays_Get
    global _ADL_Display_NumberOfDisplays_Get
    global _ADL2_Display_PreservedAspectRatio_Get
    global _ADL_Display_PreservedAspectRatio_Get
    global _ADL2_Display_PreservedAspectRatio_Set
    global _ADL_Display_PreservedAspectRatio_Set
    global _ADL2_Display_ImageExpansion_Get
    global _ADL_Display_ImageExpansion_Get
    global _ADL2_Display_ImageExpansion_Set
    global _ADL_Display_ImageExpansion_Set
    global _ADL2_Display_Position_Get
    global _ADL_Display_Position_Get
    global _ADL2_Display_Position_Set
    global _ADL_Display_Position_Set
    global _ADL2_Display_Size_Get
    global _ADL_Display_Size_Get
    global _ADL2_Display_Size_Set
    global _ADL_Display_Size_Set
    global _ADL2_Display_AdjustCaps_Get
    global _ADL_Display_AdjustCaps_Get
    global _ADL2_Display_Capabilities_Get
    global _ADL_Display_Capabilities_Get
    global _ADL2_Display_ConnectedDisplays_Get
    global _ADL_Display_ConnectedDisplays_Get
    global _ADL2_Display_DeviceConfig_Get
    global _ADL_Display_DeviceConfig_Get
    global _ADL2_Display_Property_Get
    global _ADL_Display_Property_Get
    global _ADL2_Display_Property_Set
    global _ADL_Display_Property_Set
    global _ADL2_Display_SwitchingCapability_Get
    global _ADL_Display_SwitchingCapability_Get
    global _ADL2_Display_DitherState_Get
    global _ADL_Display_DitherState_Get
    global _ADL2_Display_DitherState_Set
    global _ADL_Display_DitherState_Set
    global _ADL2_Display_SupportedPixelFormat_Get
    global _ADL_Display_SupportedPixelFormat_Get
    global _ADL2_Display_PixelFormat_Get
    global _ADL_Display_PixelFormat_Get
    global _ADL2_Display_PixelFormatDefault_Get
    global _ADL2_Display_PixelFormat_Set
    global _ADL_Display_PixelFormat_Set
    global _ADL2_Display_SupportedColorDepth_Get
    global _ADL_Display_SupportedColorDepth_Get
    global _ADL2_Display_ColorDepth_Get
    global _ADL_Display_ColorDepth_Get
    global _ADL2_Display_ColorDepth_Set
    global _ADL_Display_ColorDepth_Set
    global _ADL2_Display_ODClockInfo_Get
    global _ADL_Display_ODClockInfo_Get
    global _ADL2_Display_ODClockConfig_Set
    global _ADL_Display_ODClockConfig_Set
    global _ADL2_Display_AdjustmentCoherent_Get
    global _ADL_Display_AdjustmentCoherent_Get
    global _ADL2_Display_AdjustmentCoherent_Set
    global _ADL_Display_AdjustmentCoherent_Set
    global _ADL2_Display_ReducedBlanking_Get
    global _ADL_Display_ReducedBlanking_Get
    global _ADL2_Display_ReducedBlanking_Set
    global _ADL_Display_ReducedBlanking_Set
    global _ADL2_Display_FormatsOverride_Get
    global _ADL_Display_FormatsOverride_Get
    global _ADL2_Display_FormatsOverride_Set
    global _ADL_Display_FormatsOverride_Set
    global _ADL2_Display_MVPUCaps_Get
    global _ADL_Display_MVPUCaps_Get
    global _ADL2_Display_MVPUStatus_Get
    global _ADL_Display_MVPUStatus_Get
    global _ADL2_Display_ControllerOverlayAdjustmentCaps_Get
    global _ADL_Display_ControllerOverlayAdjustmentCaps_Get
    global _ADL2_Display_ControllerOverlayAdjustmentData_Get
    global _ADL_Display_ControllerOverlayAdjustmentData_Get
    global _ADL2_Display_ControllerOverlayAdjustmentData_Set
    global _ADL_Display_ControllerOverlayAdjustmentData_Set
    global _ADL2_Display_ViewPort_Set
    global _ADL_Display_ViewPort_Set
    global _ADL2_Display_ViewPort_Get
    global _ADL_Display_ViewPort_Get
    global _ADL2_Display_ViewPort_Cap
    global _ADL_Display_ViewPort_Cap
    global _ADL2_Display_WriteAndReadI2CRev_Get
    global _ADL_Display_WriteAndReadI2CRev_Get
    global _ADL2_Display_WriteAndReadI2C
    global _ADL_Display_WriteAndReadI2C
    global _ADL2_Display_DDCBlockAccess_Get
    global _ADL_Display_DDCBlockAccess_Get
    global _ADL2_Display_DDCInfo_Get
    global _ADL_Display_DDCInfo_Get
    global _ADL2_Display_DDCInfo2_Get
    global _ADL_Display_DDCInfo2_Get
    global _ADL2_Display_EdidData_Get
    global _ADL_Display_EdidData_Get
    global _ADL2_Display_ColorCaps_Get
    global _ADL_Display_ColorCaps_Get
    global _ADL2_Display_Color_Set
    global _ADL_Display_Color_Set
    global _ADL2_Display_Color_Get
    global _ADL_Display_Color_Get
    global _ADL2_Display_ColorTemperatureSource_Get
    global _ADL_Display_ColorTemperatureSource_Get
    global _ADL2_Display_ColorTemperatureSourceDefault_Get
    global _ADL2_Display_ColorTemperatureSource_Set
    global _ADL_Display_ColorTemperatureSource_Set
    global _ADL2_Display_ModeTimingOverride_Get
    global _ADL_Display_ModeTimingOverride_Get
    global _ADL2_Display_ModeTimingOverride_Set
    global _ADL_Display_ModeTimingOverride_Set
    global _ADL2_Display_ModeTimingOverrideList_Get
    global _ADL_Display_ModeTimingOverrideList_Get
    global _ADL2_Display_CustomizedModeListNum_Get
    global _ADL_Display_CustomizedModeListNum_Get
    global _ADL2_Display_CustomizedModeList_Get
    global _ADL_Display_CustomizedModeList_Get
    global _ADL2_Display_CustomizedMode_Add
    global _ADL_Display_CustomizedMode_Add
    global _ADL2_Display_CustomizedMode_Delete
    global _ADL_Display_CustomizedMode_Delete
    global _ADL2_Display_CustomizedMode_Validate
    global _ADL_Display_CustomizedMode_Validate
    global _ADL2_Display_UnderscanSupport_Get
    global _ADL2_Display_UnderscanState_Get
    global _ADL2_Display_UnderscanState_Set
    global _ADL2_Display_Underscan_Set
    global _ADL_Display_Underscan_Set
    global _ADL2_Display_Underscan_Get
    global _ADL_Display_Underscan_Get
    global _ADL2_Display_Overscan_Set
    global _ADL_Display_Overscan_Set
    global _ADL2_Display_Overscan_Get
    global _ADL_Display_Overscan_Get
    global _ADL2_DFP_BaseAudioSupport_Get
    global _ADL_DFP_BaseAudioSupport_Get
    global _ADL2_DFP_HDMISupport_Get
    global _ADL_DFP_HDMISupport_Get
    global _ADL2_DFP_MVPUAnalogSupport_Get
    global _ADL_DFP_MVPUAnalogSupport_Get
    global _ADL2_DFP_PixelFormat_Caps
    global _ADL_DFP_PixelFormat_Caps
    global _ADL2_DFP_PixelFormat_Get
    global _ADL_DFP_PixelFormat_Get
    global _ADL2_DFP_PixelFormat_Set
    global _ADL_DFP_PixelFormat_Set
    global _ADL2_DFP_GPUScalingEnable_Get
    global _ADL_DFP_GPUScalingEnable_Get
    global _ADL2_DFP_GPUScalingEnable_Set
    global _ADL_DFP_GPUScalingEnable_Set
    global _ADL2_DFP_AllowOnlyCETimings_Get
    global _ADL_DFP_AllowOnlyCETimings_Get
    global _ADL2_DFP_AllowOnlyCETimings_Set
    global _ADL_DFP_AllowOnlyCETimings_Set
    global _ADL2_Display_TVCaps_Get
    global _ADL_Display_TVCaps_Get
    global _ADL2_TV_Standard_Set
    global _ADL_TV_Standard_Set
    global _ADL2_TV_Standard_Get
    global _ADL_TV_Standard_Get
    global _ADL2_CV_DongleSettings_Get
    global _ADL_CV_DongleSettings_Get
    global _ADL2_CV_DongleSettings_Set
    global _ADL_CV_DongleSettings_Set
    global _ADL2_CV_DongleSettings_Reset
    global _ADL_CV_DongleSettings_Reset
    global _ADL2_Display_UnderScan_Auto_Get
    global _ADL_Display_UnderScan_Auto_Get
    global _ADL2_Display_UnderScan_Auto_Set
    global _ADL_Display_UnderScan_Auto_Set
    global _ADL2_Display_Deflicker_Get
    global _ADL_Display_Deflicker_Get
    global _ADL2_Display_Deflicker_Set
    global _ADL_Display_Deflicker_Set
    global _ADL2_Display_FilterSVideo_Get
    global _ADL_Display_FilterSVideo_Get
    global _ADL2_Display_FilterSVideo_Set
    global _ADL_Display_FilterSVideo_Set
    global _ADL2_Display_DisplayContent_Set
    global _ADL_Display_DisplayContent_Set
    global _ADL2_Display_DisplayContent_Get
    global _ADL_Display_DisplayContent_Get
    global _ADL2_Display_DisplayContent_Cap
    global _ADL_Display_DisplayContent_Cap
    global _ADL2_Adapter_ModeTimingOverride_Caps
    global _ADL_Adapter_ModeTimingOverride_Caps
    global _ADL2_Display_TargetTiming_Get
    global _ADL_Display_TargetTiming_Get
    global _ADL2_Display_ModeTimingOverrideX2_Get
    global _ADL_Display_ModeTimingOverrideX2_Get
    global _ADL2_Display_ModeTimingOverrideListX2_Get
    global _ADL_Display_ModeTimingOverrideListX2_Get
    global _ADL2_Display_ModeTimingOverride_Delete
    global _ADL_Display_ModeTimingOverride_Delete
    global _ADL_Display_Downscaling_Caps
    global _ADL2_Display_Downscaling_Caps
    global _ADL_Display_FreeSyncState_Get
    global _ADL2_Display_FreeSyncState_Get
    global _ADL_Display_FreeSyncState_Set
    global _ADL2_Display_FreeSyncState_Set
    global _ADL2_Display_DCE_Set
    global _ADL_Display_DCE_Set
    global _ADL2_Display_DCE_Get
    global _ADL_Display_DCE_Get
    global _ADL2_Display_FreeSync_Cap
    global _ADL_Display_FreeSync_Cap
    global _ADL_CDS_UnsafeMode_Set
    global _ADL2_CDS_UnsafeMode_Set

    _ADL2_Display_DisplayInfo_Get = ADL2_DISPLAY_DISPLAYINFO_GET(
          GetProcAddress(hDLL, "ADL2_Display_DisplayInfo_Get")
    )
    _ADL_Display_DisplayInfo_Get = ADL_DISPLAY_DISPLAYINFO_GET(
          GetProcAddress(hDLL, "ADL_Display_DisplayInfo_Get")
    )
    _ADL2_Display_DpMstInfo_Get = ADL2_DISPLAY_DPMSTINFO_GET(
          GetProcAddress(hDLL, "ADL2_Display_DpMstInfo_Get")
    )
    _ADL_Display_DpMstInfo_Get = ADL_DISPLAY_DPMSTINFO_GET(
          GetProcAddress(hDLL, "ADL_Display_DpMstInfo_Get")
    )
    _ADL2_Display_NumberOfDisplays_Get = ADL2_DISPLAY_NUMBEROFDISPLAYS_GET(
          GetProcAddress(hDLL, "ADL2_Display_NumberOfDisplays_Get")
    )
    _ADL_Display_NumberOfDisplays_Get = ADL_DISPLAY_NUMBEROFDISPLAYS_GET(
          GetProcAddress(hDLL, "ADL_Display_NumberOfDisplays_Get")
    )
    _ADL2_Display_PreservedAspectRatio_Get = ADL2_DISPLAY_PRESERVEDASPECTRATIO_GET(
          GetProcAddress(hDLL, "ADL2_Display_PreservedAspectRatio_Get")
    )
    _ADL_Display_PreservedAspectRatio_Get = ADL_DISPLAY_PRESERVEDASPECTRATIO_GET(
          GetProcAddress(hDLL, "ADL_Display_PreservedAspectRatio_Get")
    )
    _ADL2_Display_PreservedAspectRatio_Set = ADL2_DISPLAY_PRESERVEDASPECTRATIO_SET(
          GetProcAddress(hDLL, "ADL2_Display_PreservedAspectRatio_Set")
    )
    _ADL_Display_PreservedAspectRatio_Set = ADL_DISPLAY_PRESERVEDASPECTRATIO_SET(
          GetProcAddress(hDLL, "ADL_Display_PreservedAspectRatio_Set")
    )
    _ADL2_Display_ImageExpansion_Get = ADL2_DISPLAY_IMAGEEXPANSION_GET(
          GetProcAddress(hDLL, "ADL2_Display_ImageExpansion_Get")
    )
    _ADL_Display_ImageExpansion_Get = ADL_DISPLAY_IMAGEEXPANSION_GET(
          GetProcAddress(hDLL, "ADL_Display_ImageExpansion_Get")
    )
    _ADL2_Display_ImageExpansion_Set = ADL2_DISPLAY_IMAGEEXPANSION_SET(
          GetProcAddress(hDLL, "ADL2_Display_ImageExpansion_Set")
    )
    _ADL_Display_ImageExpansion_Set = ADL_DISPLAY_IMAGEEXPANSION_SET(
          GetProcAddress(hDLL, "ADL_Display_ImageExpansion_Set")
    )
    _ADL2_Display_Position_Get = ADL2_DISPLAY_POSITION_GET(
          GetProcAddress(hDLL, "ADL2_Display_Position_Get")
    )
    _ADL_Display_Position_Get = ADL_DISPLAY_POSITION_GET(
          GetProcAddress(hDLL, "ADL_Display_Position_Get")
    )
    _ADL2_Display_Position_Set = ADL2_DISPLAY_POSITION_SET(
          GetProcAddress(hDLL, "ADL2_Display_Position_Set")
    )
    _ADL_Display_Position_Set = ADL_DISPLAY_POSITION_SET(
          GetProcAddress(hDLL, "ADL_Display_Position_Set")
    )
    _ADL2_Display_Size_Get = ADL2_DISPLAY_SIZE_GET(
          GetProcAddress(hDLL, "ADL2_Display_Size_Get")
    )
    _ADL_Display_Size_Get = ADL_DISPLAY_SIZE_GET(
          GetProcAddress(hDLL, "ADL_Display_Size_Get")
    )
    _ADL2_Display_Size_Set = ADL2_DISPLAY_SIZE_SET(
          GetProcAddress(hDLL, "ADL2_Display_Size_Set")
    )
    _ADL_Display_Size_Set = ADL_DISPLAY_SIZE_SET(
          GetProcAddress(hDLL, "ADL_Display_Size_Set")
    )
    _ADL2_Display_AdjustCaps_Get = ADL2_DISPLAY_ADJUSTCAPS_GET(
          GetProcAddress(hDLL, "ADL2_Display_AdjustCaps_Get")
    )
    _ADL_Display_AdjustCaps_Get = ADL_DISPLAY_ADJUSTCAPS_GET(
          GetProcAddress(hDLL, "ADL_Display_AdjustCaps_Get")
    )
    _ADL2_Display_Capabilities_Get = ADL2_DISPLAY_CAPABILITIES_GET(
          GetProcAddress(hDLL, "ADL2_Display_Capabilities_Get")
    )
    _ADL_Display_Capabilities_Get = ADL_DISPLAY_CAPABILITIES_GET(
          GetProcAddress(hDLL, "ADL_Display_Capabilities_Get")
    )
    _ADL2_Display_ConnectedDisplays_Get = ADL2_DISPLAY_CONNECTEDDISPLAYS_GET(
          GetProcAddress(hDLL, "ADL2_Display_ConnectedDisplays_Get")
    )
    _ADL_Display_ConnectedDisplays_Get = ADL_DISPLAY_CONNECTEDDISPLAYS_GET(
          GetProcAddress(hDLL, "ADL_Display_ConnectedDisplays_Get")
    )
    _ADL2_Display_DeviceConfig_Get = ADL2_DISPLAY_DEVICECONFIG_GET(
          GetProcAddress(hDLL, "ADL2_Display_DeviceConfig_Get")
    )
    _ADL_Display_DeviceConfig_Get = ADL_DISPLAY_DEVICECONFIG_GET(
          GetProcAddress(hDLL, "ADL_Display_DeviceConfig_Get")
    )
    _ADL2_Display_Property_Get = ADL2_DISPLAY_PROPERTY_GET(
          GetProcAddress(hDLL, "ADL2_Display_Property_Get")
    )
    _ADL_Display_Property_Get = ADL_DISPLAY_PROPERTY_GET(
          GetProcAddress(hDLL, "ADL_Display_Property_Get")
    )
    _ADL2_Display_Property_Set = ADL2_DISPLAY_PROPERTY_SET(
          GetProcAddress(hDLL, "ADL2_Display_Property_Set")
    )
    _ADL_Display_Property_Set = ADL_DISPLAY_PROPERTY_SET(
          GetProcAddress(hDLL, "ADL_Display_Property_Set")
    )
    _ADL2_Display_SwitchingCapability_Get = ADL2_DISPLAY_SWITCHINGCAPABILITY_GET(
          GetProcAddress(hDLL, "ADL2_Display_SwitchingCapability_Get")
    )
    _ADL_Display_SwitchingCapability_Get = ADL_DISPLAY_SWITCHINGCAPABILITY_GET(
          GetProcAddress(hDLL, "ADL_Display_SwitchingCapability_Get")
    )
    _ADL2_Display_DitherState_Get = ADL2_DISPLAY_DITHERSTATE_GET(
          GetProcAddress(hDLL, "ADL2_Display_DitherState_Get")
    )
    _ADL_Display_DitherState_Get = ADL_DISPLAY_DITHERSTATE_GET(
          GetProcAddress(hDLL, "ADL_Display_DitherState_Get")
    )
    _ADL2_Display_DitherState_Set = ADL2_DISPLAY_DITHERSTATE_SET(
          GetProcAddress(hDLL, "ADL2_Display_DitherState_Set")
    )
    _ADL_Display_DitherState_Set = ADL_DISPLAY_DITHERSTATE_SET(
          GetProcAddress(hDLL, "ADL_Display_DitherState_Set")
    )
    _ADL2_Display_SupportedPixelFormat_Get = ADL2_DISPLAY_SUPPORTEDPIXELFORMAT_GET(
          GetProcAddress(hDLL, "ADL2_Display_SupportedPixelFormat_Get")
    )
    _ADL_Display_SupportedPixelFormat_Get = ADL_DISPLAY_SUPPORTEDPIXELFORMAT_GET(
          GetProcAddress(hDLL, "ADL_Display_SupportedPixelFormat_Get")
    )
    _ADL2_Display_PixelFormat_Get = ADL2_DISPLAY_PIXELFORMAT_GET(
          GetProcAddress(hDLL, "ADL2_Display_PixelFormat_Get")
    )
    _ADL_Display_PixelFormat_Get = ADL_DISPLAY_PIXELFORMAT_GET(
          GetProcAddress(hDLL, "ADL_Display_PixelFormat_Get")
    )
    _ADL2_Display_PixelFormatDefault_Get = ADL2_DISPLAY_PIXELFORMATDEFAULT_GET(
          GetProcAddress(hDLL, "ADL2_Display_PixelFormatDefault_Get")
    )
    _ADL2_Display_PixelFormat_Set = ADL2_DISPLAY_PIXELFORMAT_SET(
          GetProcAddress(hDLL, "ADL2_Display_PixelFormat_Set")
    )
    _ADL_Display_PixelFormat_Set = ADL_DISPLAY_PIXELFORMAT_SET(
          GetProcAddress(hDLL, "ADL_Display_PixelFormat_Set")
    )
    _ADL2_Display_SupportedColorDepth_Get = ADL2_DISPLAY_SUPPORTEDCOLORDEPTH_GET(
          GetProcAddress(hDLL, "ADL2_Display_SupportedColorDepth_Get")
    )
    _ADL_Display_SupportedColorDepth_Get = ADL_DISPLAY_SUPPORTEDCOLORDEPTH_GET(
          GetProcAddress(hDLL, "ADL_Display_SupportedColorDepth_Get")
    )
    _ADL2_Display_ColorDepth_Get = ADL2_DISPLAY_COLORDEPTH_GET(
          GetProcAddress(hDLL, "ADL2_Display_ColorDepth_Get")
    )
    _ADL_Display_ColorDepth_Get = ADL_DISPLAY_COLORDEPTH_GET(
          GetProcAddress(hDLL, "ADL_Display_ColorDepth_Get")
    )
    _ADL2_Display_ColorDepth_Set = ADL2_DISPLAY_COLORDEPTH_SET(
          GetProcAddress(hDLL, "ADL2_Display_ColorDepth_Set")
    )
    _ADL_Display_ColorDepth_Set = ADL_DISPLAY_COLORDEPTH_SET(
          GetProcAddress(hDLL, "ADL_Display_ColorDepth_Set")
    )
    _ADL2_Display_ODClockInfo_Get = ADL2_DISPLAY_ODCLOCKINFO_GET(
          GetProcAddress(hDLL, "ADL2_Display_ODClockInfo_Get")
    )
    _ADL_Display_ODClockInfo_Get = ADL_DISPLAY_ODCLOCKINFO_GET(
          GetProcAddress(hDLL, "ADL_Display_ODClockInfo_Get")
    )
    _ADL2_Display_ODClockConfig_Set = ADL2_DISPLAY_ODCLOCKCONFIG_SET(
          GetProcAddress(hDLL, "ADL2_Display_ODClockConfig_Set")
    )
    _ADL_Display_ODClockConfig_Set = ADL_DISPLAY_ODCLOCKCONFIG_SET(
          GetProcAddress(hDLL, "ADL_Display_ODClockConfig_Set")
    )
    _ADL2_Display_AdjustmentCoherent_Get = ADL2_DISPLAY_ADJUSTMENTCOHERENT_GET(
          GetProcAddress(hDLL, "ADL2_Display_AdjustmentCoherent_Get")
    )
    _ADL_Display_AdjustmentCoherent_Get = ADL_DISPLAY_ADJUSTMENTCOHERENT_GET(
          GetProcAddress(hDLL, "ADL_Display_AdjustmentCoherent_Get")
    )
    _ADL2_Display_AdjustmentCoherent_Set = ADL2_DISPLAY_ADJUSTMENTCOHERENT_SET(
          GetProcAddress(hDLL, "ADL2_Display_AdjustmentCoherent_Set")
    )
    _ADL_Display_AdjustmentCoherent_Set = ADL_DISPLAY_ADJUSTMENTCOHERENT_SET(
          GetProcAddress(hDLL, "ADL_Display_AdjustmentCoherent_Set")
    )
    _ADL2_Display_ReducedBlanking_Get = ADL2_DISPLAY_REDUCEDBLANKING_GET(
          GetProcAddress(hDLL, "ADL2_Display_ReducedBlanking_Get")
    )
    _ADL_Display_ReducedBlanking_Get = ADL_DISPLAY_REDUCEDBLANKING_GET(
          GetProcAddress(hDLL, "ADL_Display_ReducedBlanking_Get")
    )
    _ADL2_Display_ReducedBlanking_Set = ADL2_DISPLAY_REDUCEDBLANKING_SET(
          GetProcAddress(hDLL, "ADL2_Display_ReducedBlanking_Set")
    )
    _ADL_Display_ReducedBlanking_Set = ADL_DISPLAY_REDUCEDBLANKING_SET(
          GetProcAddress(hDLL, "ADL_Display_ReducedBlanking_Set")
    )
    _ADL2_Display_FormatsOverride_Get = ADL2_DISPLAY_FORMATSOVERRIDE_GET(
          GetProcAddress(hDLL, "ADL2_Display_FormatsOverride_Get")
    )
    _ADL_Display_FormatsOverride_Get = ADL_DISPLAY_FORMATSOVERRIDE_GET(
          GetProcAddress(hDLL, "ADL_Display_FormatsOverride_Get")
    )
    _ADL2_Display_FormatsOverride_Set = ADL2_DISPLAY_FORMATSOVERRIDE_SET(
          GetProcAddress(hDLL, "ADL2_Display_FormatsOverride_Set")
    )
    _ADL_Display_FormatsOverride_Set = ADL_DISPLAY_FORMATSOVERRIDE_SET(
          GetProcAddress(hDLL, "ADL_Display_FormatsOverride_Set")
    )
    _ADL2_Display_MVPUCaps_Get = ADL2_DISPLAY_MVPUCAPS_GET(
          GetProcAddress(hDLL, "ADL2_Display_MVPUCaps_Get")
    )
    _ADL_Display_MVPUCaps_Get = ADL_DISPLAY_MVPUCAPS_GET(
          GetProcAddress(hDLL, "ADL_Display_MVPUCaps_Get")
    )
    _ADL2_Display_MVPUStatus_Get = ADL2_DISPLAY_MVPUSTATUS_GET(
          GetProcAddress(hDLL, "ADL2_Display_MVPUStatus_Get")
    )
    _ADL_Display_MVPUStatus_Get = ADL_DISPLAY_MVPUSTATUS_GET(
          GetProcAddress(hDLL, "ADL_Display_MVPUStatus_Get")
    )
    _ADL2_Display_ControllerOverlayAdjustmentCaps_Get = ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTCAPS_GET(
          GetProcAddress(hDLL, "ADL2_Display_ControllerOverlayAdjustmentCaps_Get")
    )
    _ADL_Display_ControllerOverlayAdjustmentCaps_Get = ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTCAPS_GET(
          GetProcAddress(hDLL, "ADL_Display_ControllerOverlayAdjustmentCaps_Get")
    )
    _ADL2_Display_ControllerOverlayAdjustmentData_Get = ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_GET(
          GetProcAddress(hDLL, "ADL2_Display_ControllerOverlayAdjustmentData_Get")
    )
    _ADL_Display_ControllerOverlayAdjustmentData_Get = ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_GET(
          GetProcAddress(hDLL, "ADL_Display_ControllerOverlayAdjustmentData_Get")
    )
    _ADL2_Display_ControllerOverlayAdjustmentData_Set = ADL2_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_SET(
          GetProcAddress(hDLL, "ADL2_Display_ControllerOverlayAdjustmentData_Set")
    )
    _ADL_Display_ControllerOverlayAdjustmentData_Set = ADL_DISPLAY_CONTROLLEROVERLAYADJUSTMENTDATA_SET(
          GetProcAddress(hDLL, "ADL_Display_ControllerOverlayAdjustmentData_Set")
    )
    _ADL2_Display_ViewPort_Set = ADL2_DISPLAY_VIEWPORT_SET(
          GetProcAddress(hDLL, "ADL2_Display_ViewPort_Set")
    )
    _ADL_Display_ViewPort_Set = ADL_DISPLAY_VIEWPORT_SET(
          GetProcAddress(hDLL, "ADL_Display_ViewPort_Set")
    )
    _ADL2_Display_ViewPort_Get = ADL2_DISPLAY_VIEWPORT_GET(
          GetProcAddress(hDLL, "ADL2_Display_ViewPort_Get")
    )
    _ADL_Display_ViewPort_Get = ADL_DISPLAY_VIEWPORT_GET(
          GetProcAddress(hDLL, "ADL_Display_ViewPort_Get")
    )
    _ADL2_Display_ViewPort_Cap = ADL2_DISPLAY_VIEWPORT_CAP(
          GetProcAddress(hDLL, "ADL2_Display_ViewPort_Cap")
    )
    _ADL_Display_ViewPort_Cap = ADL_DISPLAY_VIEWPORT_CAP(
          GetProcAddress(hDLL, "ADL_Display_ViewPort_Cap")
    )
    _ADL2_Display_WriteAndReadI2CRev_Get = ADL2_DISPLAY_WRITEANDREADI2CREV_GET(
          GetProcAddress(hDLL, "ADL2_Display_WriteAndReadI2CRev_Get")
    )
    _ADL_Display_WriteAndReadI2CRev_Get = ADL_DISPLAY_WRITEANDREADI2CREV_GET(
          GetProcAddress(hDLL, "ADL_Display_WriteAndReadI2CRev_Get")
    )
    _ADL2_Display_WriteAndReadI2C = ADL2_DISPLAY_WRITEANDREADI2C(
          GetProcAddress(hDLL, "ADL2_Display_WriteAndReadI2C")
    )
    _ADL_Display_WriteAndReadI2C = ADL_DISPLAY_WRITEANDREADI2C(
          GetProcAddress(hDLL, "ADL_Display_WriteAndReadI2C")
    )
    _ADL2_Display_DDCBlockAccess_Get = ADL2_DISPLAY_DDCBLOCKACCESS_GET(
          GetProcAddress(hDLL, "ADL2_Display_DDCBlockAccess_Get")
    )
    _ADL_Display_DDCBlockAccess_Get = ADL_DISPLAY_DDCBLOCKACCESS_GET(
          GetProcAddress(hDLL, "ADL_Display_DDCBlockAccess_Get")
    )
    _ADL2_Display_DDCInfo_Get = ADL2_DISPLAY_DDCINFO_GET(
          GetProcAddress(hDLL, "ADL2_Display_DDCInfo_Get")
    )
    _ADL_Display_DDCInfo_Get = ADL_DISPLAY_DDCINFO_GET(
          GetProcAddress(hDLL, "ADL_Display_DDCInfo_Get")
    )
    _ADL2_Display_DDCInfo2_Get = ADL2_DISPLAY_DDCINFO2_GET(
          GetProcAddress(hDLL, "ADL2_Display_DDCInfo2_Get")
    )
    _ADL_Display_DDCInfo2_Get = ADL_DISPLAY_DDCINFO2_GET(
          GetProcAddress(hDLL, "ADL_Display_DDCInfo2_Get")
    )
    _ADL2_Display_EdidData_Get = ADL2_DISPLAY_EDIDDATA_GET(
          GetProcAddress(hDLL, "ADL2_Display_EdidData_Get")
    )
    _ADL_Display_EdidData_Get = ADL_DISPLAY_EDIDDATA_GET(
          GetProcAddress(hDLL, "ADL_Display_EdidData_Get")
    )
    _ADL2_Display_ColorCaps_Get = ADL2_DISPLAY_COLORCAPS_GET(
          GetProcAddress(hDLL, "ADL2_Display_ColorCaps_Get")
    )
    _ADL_Display_ColorCaps_Get = ADL_DISPLAY_COLORCAPS_GET(
          GetProcAddress(hDLL, "ADL_Display_ColorCaps_Get")
    )
    _ADL2_Display_Color_Set = ADL2_DISPLAY_COLOR_SET(
          GetProcAddress(hDLL, "ADL2_Display_Color_Set")
    )
    _ADL_Display_Color_Set = ADL_DISPLAY_COLOR_SET(
          GetProcAddress(hDLL, "ADL_Display_Color_Set")
    )
    _ADL2_Display_Color_Get = ADL2_DISPLAY_COLOR_GET(
          GetProcAddress(hDLL, "ADL2_Display_Color_Get")
    )
    _ADL_Display_Color_Get = ADL_DISPLAY_COLOR_GET(
          GetProcAddress(hDLL, "ADL_Display_Color_Get")
    )
    _ADL2_Display_ColorTemperatureSource_Get = ADL2_DISPLAY_COLORTEMPERATURESOURCE_GET(
          GetProcAddress(hDLL, "ADL2_Display_ColorTemperatureSource_Get")
    )
    _ADL_Display_ColorTemperatureSource_Get = ADL_DISPLAY_COLORTEMPERATURESOURCE_GET(
          GetProcAddress(hDLL, "ADL_Display_ColorTemperatureSource_Get")
    )
    _ADL2_Display_ColorTemperatureSourceDefault_Get = ADL2_DISPLAY_COLORTEMPERATURESOURCEDEFAULT_GET(
          GetProcAddress(hDLL, "ADL2_Display_ColorTemperatureSourceDefault_Get")
    )
    _ADL2_Display_ColorTemperatureSource_Set = ADL2_DISPLAY_COLORTEMPERATURESOURCE_SET(
          GetProcAddress(hDLL, "ADL2_Display_ColorTemperatureSource_Set")
    )
    _ADL_Display_ColorTemperatureSource_Set = ADL_DISPLAY_COLORTEMPERATURESOURCE_SET(
          GetProcAddress(hDLL, "ADL_Display_ColorTemperatureSource_Set")
    )
    _ADL2_Display_ModeTimingOverride_Get = ADL2_DISPLAY_MODETIMINGOVERRIDE_GET(
          GetProcAddress(hDLL, "ADL2_Display_ModeTimingOverride_Get")
    )
    _ADL_Display_ModeTimingOverride_Get = ADL_DISPLAY_MODETIMINGOVERRIDE_GET(
          GetProcAddress(hDLL, "ADL_Display_ModeTimingOverride_Get")
    )
    _ADL2_Display_ModeTimingOverride_Set = ADL2_DISPLAY_MODETIMINGOVERRIDE_SET(
          GetProcAddress(hDLL, "ADL2_Display_ModeTimingOverride_Set")
    )
    _ADL_Display_ModeTimingOverride_Set = ADL_DISPLAY_MODETIMINGOVERRIDE_SET(
          GetProcAddress(hDLL, "ADL_Display_ModeTimingOverride_Set")
    )
    _ADL2_Display_ModeTimingOverrideList_Get = ADL2_DISPLAY_MODETIMINGOVERRIDELIST_GET(
          GetProcAddress(hDLL, "ADL2_Display_ModeTimingOverrideList_Get")
    )
    _ADL_Display_ModeTimingOverrideList_Get = ADL_DISPLAY_MODETIMINGOVERRIDELIST_GET(
          GetProcAddress(hDLL, "ADL_Display_ModeTimingOverrideList_Get")
    )
    _ADL2_Display_CustomizedModeListNum_Get = ADL2_DISPLAY_CUSTOMIZEDMODELISTNUM_GET(
          GetProcAddress(hDLL, "ADL2_Display_CustomizedModeListNum_Get")
    )
    _ADL_Display_CustomizedModeListNum_Get = ADL_DISPLAY_CUSTOMIZEDMODELISTNUM_GET(
          GetProcAddress(hDLL, "ADL_Display_CustomizedModeListNum_Get")
    )
    _ADL2_Display_CustomizedModeList_Get = ADL2_DISPLAY_CUSTOMIZEDMODELIST_GET(
          GetProcAddress(hDLL, "ADL2_Display_CustomizedModeList_Get")
    )
    _ADL_Display_CustomizedModeList_Get = ADL_DISPLAY_CUSTOMIZEDMODELIST_GET(
          GetProcAddress(hDLL, "ADL_Display_CustomizedModeList_Get")
    )
    _ADL2_Display_CustomizedMode_Add = ADL2_DISPLAY_CUSTOMIZEDMODE_ADD(
          GetProcAddress(hDLL, "ADL2_Display_CustomizedMode_Add")
    )
    _ADL_Display_CustomizedMode_Add = ADL_DISPLAY_CUSTOMIZEDMODE_ADD(
          GetProcAddress(hDLL, "ADL_Display_CustomizedMode_Add")
    )
    _ADL2_Display_CustomizedMode_Delete = ADL2_DISPLAY_CUSTOMIZEDMODE_DELETE(
          GetProcAddress(hDLL, "ADL2_Display_CustomizedMode_Delete")
    )
    _ADL_Display_CustomizedMode_Delete = ADL_DISPLAY_CUSTOMIZEDMODE_DELETE(
          GetProcAddress(hDLL, "ADL_Display_CustomizedMode_Delete")
    )
    _ADL2_Display_CustomizedMode_Validate = ADL2_DISPLAY_CUSTOMIZEDMODE_VALIDATE(
          GetProcAddress(hDLL, "ADL2_Display_CustomizedMode_Validate")
    )
    _ADL_Display_CustomizedMode_Validate = ADL_DISPLAY_CUSTOMIZEDMODE_VALIDATE(
          GetProcAddress(hDLL, "ADL_Display_CustomizedMode_Validate")
    )
    _ADL2_Display_UnderscanSupport_Get = ADL2_DISPLAY_UNDERSCANSUPPORT_GET(
          GetProcAddress(hDLL, "ADL2_Display_UnderscanSupport_Get")
    )
    _ADL2_Display_UnderscanState_Get = ADL2_DISPLAY_UNDERSCANSTATE_GET(
          GetProcAddress(hDLL, "ADL2_Display_UnderscanState_Get")
    )
    _ADL2_Display_UnderscanState_Set = ADL2_DISPLAY_UNDERSCANSTATE_SET(
          GetProcAddress(hDLL, "ADL2_Display_UnderscanState_Set")
    )
    _ADL2_Display_Underscan_Set = ADL2_DISPLAY_UNDERSCAN_SET(
          GetProcAddress(hDLL, "ADL2_Display_Underscan_Set")
    )
    _ADL_Display_Underscan_Set = ADL_DISPLAY_UNDERSCAN_SET(
          GetProcAddress(hDLL, "ADL_Display_Underscan_Set")
    )
    _ADL2_Display_Underscan_Get = ADL2_DISPLAY_UNDERSCAN_GET(
          GetProcAddress(hDLL, "ADL2_Display_Underscan_Get")
    )
    _ADL_Display_Underscan_Get = ADL_DISPLAY_UNDERSCAN_GET(
          GetProcAddress(hDLL, "ADL_Display_Underscan_Get")
    )
    _ADL2_Display_Overscan_Set = ADL2_DISPLAY_OVERSCAN_SET(
          GetProcAddress(hDLL, "ADL2_Display_Overscan_Set")
    )
    _ADL_Display_Overscan_Set = ADL_DISPLAY_OVERSCAN_SET(
          GetProcAddress(hDLL, "ADL_Display_Overscan_Set")
    )
    _ADL2_Display_Overscan_Get = ADL2_DISPLAY_OVERSCAN_GET(
          GetProcAddress(hDLL, "ADL2_Display_Overscan_Get")
    )
    _ADL_Display_Overscan_Get = ADL_DISPLAY_OVERSCAN_GET(
          GetProcAddress(hDLL, "ADL_Display_Overscan_Get")
    )
    _ADL2_DFP_BaseAudioSupport_Get = ADL2_DFP_BASEAUDIOSUPPORT_GET(
          GetProcAddress(hDLL, "ADL2_DFP_BaseAudioSupport_Get")
    )
    _ADL_DFP_BaseAudioSupport_Get = ADL_DFP_BASEAUDIOSUPPORT_GET(
          GetProcAddress(hDLL, "ADL_DFP_BaseAudioSupport_Get")
    )
    _ADL2_DFP_HDMISupport_Get = ADL2_DFP_HDMISUPPORT_GET(
          GetProcAddress(hDLL, "ADL2_DFP_HDMISupport_Get")
    )
    _ADL_DFP_HDMISupport_Get = ADL_DFP_HDMISUPPORT_GET(
          GetProcAddress(hDLL, "ADL_DFP_HDMISupport_Get")
    )
    _ADL2_DFP_MVPUAnalogSupport_Get = ADL2_DFP_MVPUANALOGSUPPORT_GET(
          GetProcAddress(hDLL, "ADL2_DFP_MVPUAnalogSupport_Get")
    )
    _ADL_DFP_MVPUAnalogSupport_Get = ADL_DFP_MVPUANALOGSUPPORT_GET(
          GetProcAddress(hDLL, "ADL_DFP_MVPUAnalogSupport_Get")
    )
    _ADL2_DFP_PixelFormat_Caps = ADL2_DFP_PIXELFORMAT_CAPS(
          GetProcAddress(hDLL, "ADL2_DFP_PixelFormat_Caps")
    )
    _ADL_DFP_PixelFormat_Caps = ADL_DFP_PIXELFORMAT_CAPS(
          GetProcAddress(hDLL, "ADL_DFP_PixelFormat_Caps")
    )
    _ADL2_DFP_PixelFormat_Get = ADL2_DFP_PIXELFORMAT_GET(
          GetProcAddress(hDLL, "ADL2_DFP_PixelFormat_Get")
    )
    _ADL_DFP_PixelFormat_Get = ADL_DFP_PIXELFORMAT_GET(
          GetProcAddress(hDLL, "ADL_DFP_PixelFormat_Get")
    )
    _ADL2_DFP_PixelFormat_Set = ADL2_DFP_PIXELFORMAT_SET(
          GetProcAddress(hDLL, "ADL2_DFP_PixelFormat_Set")
    )
    _ADL_DFP_PixelFormat_Set = ADL_DFP_PIXELFORMAT_SET(
          GetProcAddress(hDLL, "ADL_DFP_PixelFormat_Set")
    )
    _ADL2_DFP_GPUScalingEnable_Get = ADL2_DFP_GPUSCALINGENABLE_GET(
          GetProcAddress(hDLL, "ADL2_DFP_GPUScalingEnable_Get")
    )
    _ADL_DFP_GPUScalingEnable_Get = ADL_DFP_GPUSCALINGENABLE_GET(
          GetProcAddress(hDLL, "ADL_DFP_GPUScalingEnable_Get")
    )
    _ADL2_DFP_GPUScalingEnable_Set = ADL2_DFP_GPUSCALINGENABLE_SET(
          GetProcAddress(hDLL, "ADL2_DFP_GPUScalingEnable_Set")
    )
    _ADL_DFP_GPUScalingEnable_Set = ADL_DFP_GPUSCALINGENABLE_SET(
          GetProcAddress(hDLL, "ADL_DFP_GPUScalingEnable_Set")
    )
    _ADL2_DFP_AllowOnlyCETimings_Get = ADL2_DFP_ALLOWONLYCETIMINGS_GET(
          GetProcAddress(hDLL, "ADL2_DFP_AllowOnlyCETimings_Get")
    )
    _ADL_DFP_AllowOnlyCETimings_Get = ADL_DFP_ALLOWONLYCETIMINGS_GET(
          GetProcAddress(hDLL, "ADL_DFP_AllowOnlyCETimings_Get")
    )
    _ADL2_DFP_AllowOnlyCETimings_Set = ADL2_DFP_ALLOWONLYCETIMINGS_SET(
          GetProcAddress(hDLL, "ADL2_DFP_AllowOnlyCETimings_Set")
    )
    _ADL_DFP_AllowOnlyCETimings_Set = ADL_DFP_ALLOWONLYCETIMINGS_SET(
          GetProcAddress(hDLL, "ADL_DFP_AllowOnlyCETimings_Set")
    )
    _ADL2_Display_TVCaps_Get = ADL2_DISPLAY_TVCAPS_GET(
          GetProcAddress(hDLL, "ADL2_Display_TVCaps_Get")
    )
    _ADL_Display_TVCaps_Get = ADL_DISPLAY_TVCAPS_GET(
          GetProcAddress(hDLL, "ADL_Display_TVCaps_Get")
    )
    _ADL2_TV_Standard_Set = ADL2_TV_STANDARD_SET(
          GetProcAddress(hDLL, "ADL2_TV_Standard_Set")
    )
    _ADL_TV_Standard_Set = ADL_TV_STANDARD_SET(
          GetProcAddress(hDLL, "ADL_TV_Standard_Set")
    )
    _ADL2_TV_Standard_Get = ADL2_TV_STANDARD_GET(
          GetProcAddress(hDLL, "ADL2_TV_Standard_Get")
    )
    _ADL_TV_Standard_Get = ADL_TV_STANDARD_GET(
          GetProcAddress(hDLL, "ADL_TV_Standard_Get")
    )
    _ADL2_CV_DongleSettings_Get = ADL2_CV_DONGLESETTINGS_GET(
          GetProcAddress(hDLL, "ADL2_CV_DongleSettings_Get")
    )
    _ADL_CV_DongleSettings_Get = ADL_CV_DONGLESETTINGS_GET(
          GetProcAddress(hDLL, "ADL_CV_DongleSettings_Get")
    )
    _ADL2_CV_DongleSettings_Set = ADL2_CV_DONGLESETTINGS_SET(
          GetProcAddress(hDLL, "ADL2_CV_DongleSettings_Set")
    )
    _ADL_CV_DongleSettings_Set = ADL_CV_DONGLESETTINGS_SET(
          GetProcAddress(hDLL, "ADL_CV_DongleSettings_Set")
    )
    _ADL2_CV_DongleSettings_Reset = ADL2_CV_DONGLESETTINGS_RESET(
          GetProcAddress(hDLL, "ADL2_CV_DongleSettings_Reset")
    )
    _ADL_CV_DongleSettings_Reset = ADL_CV_DONGLESETTINGS_RESET(
          GetProcAddress(hDLL, "ADL_CV_DongleSettings_Reset")
    )
    _ADL2_Display_UnderScan_Auto_Get = ADL2_DISPLAY_UNDERSCAN_AUTO_GET(
          GetProcAddress(hDLL, "ADL2_Display_UnderScan_Auto_Get")
    )
    _ADL_Display_UnderScan_Auto_Get = ADL_DISPLAY_UNDERSCAN_AUTO_GET(
          GetProcAddress(hDLL, "ADL_Display_UnderScan_Auto_Get")
    )
    _ADL2_Display_UnderScan_Auto_Set = ADL2_DISPLAY_UNDERSCAN_AUTO_SET(
          GetProcAddress(hDLL, "ADL2_Display_UnderScan_Auto_Set")
    )
    _ADL_Display_UnderScan_Auto_Set = ADL_DISPLAY_UNDERSCAN_AUTO_SET(
          GetProcAddress(hDLL, "ADL_Display_UnderScan_Auto_Set")
    )
    _ADL2_Display_Deflicker_Get = ADL2_DISPLAY_DEFLICKER_GET(
          GetProcAddress(hDLL, "ADL2_Display_Deflicker_Get")
    )
    _ADL_Display_Deflicker_Get = ADL_DISPLAY_DEFLICKER_GET(
          GetProcAddress(hDLL, "ADL_Display_Deflicker_Get")
    )
    _ADL2_Display_Deflicker_Set = ADL2_DISPLAY_DEFLICKER_SET(
          GetProcAddress(hDLL, "ADL2_Display_Deflicker_Set")
    )
    _ADL_Display_Deflicker_Set = ADL_DISPLAY_DEFLICKER_SET(
          GetProcAddress(hDLL, "ADL_Display_Deflicker_Set")
    )
    _ADL2_Display_FilterSVideo_Get = ADL2_DISPLAY_FILTERSVIDEO_GET(
          GetProcAddress(hDLL, "ADL2_Display_FilterSVideo_Get")
    )
    _ADL_Display_FilterSVideo_Get = ADL_DISPLAY_FILTERSVIDEO_GET(
          GetProcAddress(hDLL, "ADL_Display_FilterSVideo_Get")
    )
    _ADL2_Display_FilterSVideo_Set = ADL2_DISPLAY_FILTERSVIDEO_SET(
          GetProcAddress(hDLL, "ADL2_Display_FilterSVideo_Set")
    )
    _ADL_Display_FilterSVideo_Set = ADL_DISPLAY_FILTERSVIDEO_SET(
          GetProcAddress(hDLL, "ADL_Display_FilterSVideo_Set")
    )
    _ADL2_Display_DisplayContent_Set = ADL2_DISPLAY_DISPLAYCONTENT_SET(
          GetProcAddress(hDLL, "ADL2_Display_DisplayContent_Set")
    )
    _ADL_Display_DisplayContent_Set = ADL_DISPLAY_DISPLAYCONTENT_SET(
          GetProcAddress(hDLL, "ADL_Display_DisplayContent_Set")
    )
    _ADL2_Display_DisplayContent_Get = ADL2_DISPLAY_DISPLAYCONTENT_GET(
          GetProcAddress(hDLL, "ADL2_Display_DisplayContent_Get")
    )
    _ADL_Display_DisplayContent_Get = ADL_DISPLAY_DISPLAYCONTENT_GET(
          GetProcAddress(hDLL, "ADL_Display_DisplayContent_Get")
    )
    _ADL2_Display_DisplayContent_Cap = ADL2_DISPLAY_DISPLAYCONTENT_CAP(
          GetProcAddress(hDLL, "ADL2_Display_DisplayContent_Cap")
    )
    _ADL_Display_DisplayContent_Cap = ADL_DISPLAY_DISPLAYCONTENT_CAP(
          GetProcAddress(hDLL, "ADL_Display_DisplayContent_Cap")
    )
    _ADL2_Adapter_ModeTimingOverride_Caps = ADL2_ADAPTER_MODETIMINGOVERRIDE_CAPS(
          GetProcAddress(hDLL, "ADL2_Adapter_ModeTimingOverride_Caps")
    )
    _ADL_Adapter_ModeTimingOverride_Caps = ADL_ADAPTER_MODETIMINGOVERRIDE_CAPS(
          GetProcAddress(hDLL, "ADL_Adapter_ModeTimingOverride_Caps")
    )
    _ADL2_Display_TargetTiming_Get = ADL2_DISPLAY_TARGETTIMING_GET(
          GetProcAddress(hDLL, "ADL2_Display_TargetTiming_Get")
    )
    _ADL_Display_TargetTiming_Get = ADL_DISPLAY_TARGETTIMING_GET(
          GetProcAddress(hDLL, "ADL_Display_TargetTiming_Get")
    )
    _ADL2_Display_ModeTimingOverrideX2_Get = ADL2_DISPLAY_MODETIMINGOVERRIDEX2_GET(
          GetProcAddress(hDLL, "ADL2_Display_ModeTimingOverrideX2_Get")
    )
    _ADL_Display_ModeTimingOverrideX2_Get = ADL_DISPLAY_MODETIMINGOVERRIDEX2_GET(
          GetProcAddress(hDLL, "ADL_Display_ModeTimingOverrideX2_Get")
    )
    _ADL2_Display_ModeTimingOverrideListX2_Get = ADL2_DISPLAY_MODETIMINGOVERRIDELISTX2_GET(
          GetProcAddress(hDLL, "ADL2_Display_ModeTimingOverrideListX2_Get")
    )
    _ADL_Display_ModeTimingOverrideListX2_Get = ADL_DISPLAY_MODETIMINGOVERRIDELISTX2_GET(
          GetProcAddress(hDLL, "ADL_Display_ModeTimingOverrideListX2_Get")
    )
    _ADL2_Display_ModeTimingOverride_Delete = ADL2_DISPLAY_MODETIMINGOVERRIDE_DELETE(
          GetProcAddress(hDLL, "ADL2_Display_ModeTimingOverride_Delete")
    )
    _ADL_Display_ModeTimingOverride_Delete = ADL_DISPLAY_MODETIMINGOVERRIDE_DELETE(
          GetProcAddress(hDLL, "ADL_Display_ModeTimingOverride_Delete")
    )
    _ADL_Display_Downscaling_Caps = ADL_DISPLAY_DOWNSCALING_CAPS(
          GetProcAddress(hDLL, "ADL_Display_Downscaling_Caps")
    )
    _ADL2_Display_Downscaling_Caps = ADL2_DISPLAY_DOWNSCALING_CAPS(
          GetProcAddress(hDLL, "ADL2_Display_Downscaling_Caps")
    )
    _ADL_Display_FreeSyncState_Get = ADL_DISPLAY_FREESYNCSTATE_GET(
          GetProcAddress(hDLL, "ADL_Display_FreeSyncState_Get")
    )
    _ADL2_Display_FreeSyncState_Get = ADL2_DISPLAY_FREESYNCSTATE_GET(
          GetProcAddress(hDLL, "ADL2_Display_FreeSyncState_Get")
    )
    _ADL_Display_FreeSyncState_Set = ADL_DISPLAY_FREESYNCSTATE_SET(
          GetProcAddress(hDLL, "ADL_Display_FreeSyncState_Set")
    )
    _ADL2_Display_FreeSyncState_Set = ADL2_DISPLAY_FREESYNCSTATE_SET(
          GetProcAddress(hDLL, "ADL2_Display_FreeSyncState_Set")
    )
    _ADL2_Display_DCE_Set = ADL2_DISPLAY_DCE_SET(
          GetProcAddress(hDLL, "ADL2_Display_DCE_Set")
    )
    _ADL_Display_DCE_Set = ADL_DISPLAY_DCE_SET(
          GetProcAddress(hDLL, "ADL_Display_DCE_Set")
    )
    _ADL2_Display_DCE_Get = ADL2_DISPLAY_DCE_GET(
          GetProcAddress(hDLL, "ADL2_Display_DCE_Get")
    )
    _ADL_Display_DCE_Get = ADL_DISPLAY_DCE_GET(
          GetProcAddress(hDLL, "ADL_Display_DCE_Get")
    )
    _ADL2_Display_FreeSync_Cap = ADL2_DISPLAY_FREESYNC_CAP(
          GetProcAddress(hDLL, "ADL2_Display_FreeSync_Cap")
    )
    _ADL_Display_FreeSync_Cap = ADL_DISPLAY_FREESYNC_CAP(
          GetProcAddress(hDLL, "ADL_Display_FreeSync_Cap")
    )
    _ADL_CDS_UnsafeMode_Set = ADL_CDS_UNSAFEMODE_SET(
          GetProcAddress(hDLL, "ADL_CDS_UnsafeMode_Set")
    )
    _ADL2_CDS_UnsafeMode_Set = ADL2_CDS_UNSAFEMODE_SET(
          GetProcAddress(hDLL, "ADL2_CDS_UnsafeMode_Set")
    )


__all__ = (
    '_ADL2_Display_DisplayInfo_Get',
    '_ADL_Display_DisplayInfo_Get',
    '_ADL2_Display_DpMstInfo_Get',
    '_ADL_Display_DpMstInfo_Get',
    '_ADL2_Display_NumberOfDisplays_Get',
    '_ADL_Display_NumberOfDisplays_Get',
    '_ADL2_Display_PreservedAspectRatio_Get',
    '_ADL_Display_PreservedAspectRatio_Get',
    '_ADL2_Display_PreservedAspectRatio_Set',
    '_ADL_Display_PreservedAspectRatio_Set',
    '_ADL2_Display_ImageExpansion_Get',
    '_ADL_Display_ImageExpansion_Get',
    '_ADL2_Display_ImageExpansion_Set',
    '_ADL_Display_ImageExpansion_Set',
    '_ADL2_Display_Position_Get',
    '_ADL_Display_Position_Get',
    '_ADL2_Display_Position_Set',
    '_ADL_Display_Position_Set',
    '_ADL2_Display_Size_Get',
    '_ADL_Display_Size_Get',
    '_ADL2_Display_Size_Set',
    '_ADL_Display_Size_Set',
    '_ADL2_Display_AdjustCaps_Get',
    '_ADL_Display_AdjustCaps_Get',
    '_ADL2_Display_Capabilities_Get',
    '_ADL_Display_Capabilities_Get',
    '_ADL2_Display_ConnectedDisplays_Get',
    '_ADL_Display_ConnectedDisplays_Get',
    '_ADL2_Display_DeviceConfig_Get',
    '_ADL_Display_DeviceConfig_Get',
    '_ADL2_Display_Property_Get',
    '_ADL_Display_Property_Get',
    '_ADL2_Display_Property_Set',
    '_ADL_Display_Property_Set',
    '_ADL2_Display_SwitchingCapability_Get',
    '_ADL_Display_SwitchingCapability_Get',
    '_ADL2_Display_DitherState_Get',
    '_ADL_Display_DitherState_Get',
    '_ADL2_Display_DitherState_Set',
    '_ADL_Display_DitherState_Set',
    '_ADL2_Display_SupportedPixelFormat_Get',
    '_ADL_Display_SupportedPixelFormat_Get',
    '_ADL2_Display_PixelFormat_Get',
    '_ADL_Display_PixelFormat_Get',
    '_ADL2_Display_PixelFormatDefault_Get',
    '_ADL2_Display_PixelFormat_Set',
    '_ADL_Display_PixelFormat_Set',
    '_ADL2_Display_SupportedColorDepth_Get',
    '_ADL_Display_SupportedColorDepth_Get',
    '_ADL2_Display_ColorDepth_Get',
    '_ADL_Display_ColorDepth_Get',
    '_ADL2_Display_ColorDepth_Set',
    '_ADL_Display_ColorDepth_Set',
    '_ADL2_Display_ODClockInfo_Get',
    '_ADL_Display_ODClockInfo_Get',
    '_ADL2_Display_ODClockConfig_Set',
    '_ADL_Display_ODClockConfig_Set',
    '_ADL2_Display_AdjustmentCoherent_Get',
    '_ADL_Display_AdjustmentCoherent_Get',
    '_ADL2_Display_AdjustmentCoherent_Set',
    '_ADL_Display_AdjustmentCoherent_Set',
    '_ADL2_Display_ReducedBlanking_Get',
    '_ADL_Display_ReducedBlanking_Get',
    '_ADL2_Display_ReducedBlanking_Set',
    '_ADL_Display_ReducedBlanking_Set',
    '_ADL2_Display_FormatsOverride_Get',
    '_ADL_Display_FormatsOverride_Get',
    '_ADL2_Display_FormatsOverride_Set',
    '_ADL_Display_FormatsOverride_Set',
    '_ADL2_Display_MVPUCaps_Get',
    '_ADL_Display_MVPUCaps_Get',
    '_ADL2_Display_MVPUStatus_Get',
    '_ADL_Display_MVPUStatus_Get',
    '_ADL2_Display_ControllerOverlayAdjustmentCaps_Get',
    '_ADL_Display_ControllerOverlayAdjustmentCaps_Get',
    '_ADL2_Display_ControllerOverlayAdjustmentData_Get',
    '_ADL_Display_ControllerOverlayAdjustmentData_Get',
    '_ADL2_Display_ControllerOverlayAdjustmentData_Set',
    '_ADL_Display_ControllerOverlayAdjustmentData_Set',
    '_ADL2_Display_ViewPort_Set',
    '_ADL_Display_ViewPort_Set',
    '_ADL2_Display_ViewPort_Get',
    '_ADL_Display_ViewPort_Get',
    '_ADL2_Display_ViewPort_Cap',
    '_ADL_Display_ViewPort_Cap',
    '_ADL2_Display_WriteAndReadI2CRev_Get',
    '_ADL_Display_WriteAndReadI2CRev_Get',
    '_ADL2_Display_WriteAndReadI2C',
    '_ADL_Display_WriteAndReadI2C',
    '_ADL2_Display_DDCBlockAccess_Get',
    '_ADL_Display_DDCBlockAccess_Get',
    '_ADL2_Display_DDCInfo_Get',
    '_ADL_Display_DDCInfo_Get',
    '_ADL2_Display_DDCInfo2_Get',
    '_ADL_Display_DDCInfo2_Get',
    '_ADL2_Display_EdidData_Get',
    '_ADL_Display_EdidData_Get',
    '_ADL2_Display_ColorCaps_Get',
    '_ADL_Display_ColorCaps_Get',
    '_ADL2_Display_Color_Set',
    '_ADL_Display_Color_Set',
    '_ADL2_Display_Color_Get',
    '_ADL_Display_Color_Get',
    '_ADL2_Display_ColorTemperatureSource_Get',
    '_ADL_Display_ColorTemperatureSource_Get',
    '_ADL2_Display_ColorTemperatureSourceDefault_Get',
    '_ADL2_Display_ColorTemperatureSource_Set',
    '_ADL_Display_ColorTemperatureSource_Set',
    '_ADL2_Display_ModeTimingOverride_Get',
    '_ADL_Display_ModeTimingOverride_Get',
    '_ADL2_Display_ModeTimingOverride_Set',
    '_ADL_Display_ModeTimingOverride_Set',
    '_ADL2_Display_ModeTimingOverrideList_Get',
    '_ADL_Display_ModeTimingOverrideList_Get',
    '_ADL2_Display_CustomizedModeListNum_Get',
    '_ADL_Display_CustomizedModeListNum_Get',
    '_ADL2_Display_CustomizedModeList_Get',
    '_ADL_Display_CustomizedModeList_Get',
    '_ADL2_Display_CustomizedMode_Add',
    '_ADL_Display_CustomizedMode_Add',
    '_ADL2_Display_CustomizedMode_Delete',
    '_ADL_Display_CustomizedMode_Delete',
    '_ADL2_Display_CustomizedMode_Validate',
    '_ADL_Display_CustomizedMode_Validate',
    '_ADL2_Display_UnderscanSupport_Get',
    '_ADL2_Display_UnderscanState_Get',
    '_ADL2_Display_UnderscanState_Set',
    '_ADL2_Display_Underscan_Set',
    '_ADL_Display_Underscan_Set',
    '_ADL2_Display_Underscan_Get',
    '_ADL_Display_Underscan_Get',
    '_ADL2_Display_Overscan_Set',
    '_ADL_Display_Overscan_Set',
    '_ADL2_Display_Overscan_Get',
    '_ADL_Display_Overscan_Get',
    '_ADL2_DFP_BaseAudioSupport_Get',
    '_ADL_DFP_BaseAudioSupport_Get',
    '_ADL2_DFP_HDMISupport_Get',
    '_ADL_DFP_HDMISupport_Get',
    '_ADL2_DFP_MVPUAnalogSupport_Get',
    '_ADL_DFP_MVPUAnalogSupport_Get',
    '_ADL2_DFP_PixelFormat_Caps',
    '_ADL_DFP_PixelFormat_Caps',
    '_ADL2_DFP_PixelFormat_Get',
    '_ADL_DFP_PixelFormat_Get',
    '_ADL2_DFP_PixelFormat_Set',
    '_ADL_DFP_PixelFormat_Set',
    '_ADL2_DFP_GPUScalingEnable_Get',
    '_ADL_DFP_GPUScalingEnable_Get',
    '_ADL2_DFP_GPUScalingEnable_Set',
    '_ADL_DFP_GPUScalingEnable_Set',
    '_ADL2_DFP_AllowOnlyCETimings_Get',
    '_ADL_DFP_AllowOnlyCETimings_Get',
    '_ADL2_DFP_AllowOnlyCETimings_Set',
    '_ADL_DFP_AllowOnlyCETimings_Set',
    '_ADL2_Display_TVCaps_Get',
    '_ADL_Display_TVCaps_Get',
    '_ADL2_TV_Standard_Set',
    '_ADL_TV_Standard_Set',
    '_ADL2_TV_Standard_Get',
    '_ADL_TV_Standard_Get',
    '_ADL2_CV_DongleSettings_Get',
    '_ADL_CV_DongleSettings_Get',
    '_ADL2_CV_DongleSettings_Set',
    '_ADL_CV_DongleSettings_Set',
    '_ADL2_CV_DongleSettings_Reset',
    '_ADL_CV_DongleSettings_Reset',
    '_ADL2_Display_UnderScan_Auto_Get',
    '_ADL_Display_UnderScan_Auto_Get',
    '_ADL2_Display_UnderScan_Auto_Set',
    '_ADL_Display_UnderScan_Auto_Set',
    '_ADL2_Display_Deflicker_Get',
    '_ADL_Display_Deflicker_Get',
    '_ADL2_Display_Deflicker_Set',
    '_ADL_Display_Deflicker_Set',
    '_ADL2_Display_FilterSVideo_Get',
    '_ADL_Display_FilterSVideo_Get',
    '_ADL2_Display_FilterSVideo_Set',
    '_ADL_Display_FilterSVideo_Set',
    '_ADL2_Display_DisplayContent_Set',
    '_ADL_Display_DisplayContent_Set',
    '_ADL2_Display_DisplayContent_Get',
    '_ADL_Display_DisplayContent_Get',
    '_ADL2_Display_DisplayContent_Cap',
    '_ADL_Display_DisplayContent_Cap',
    '_ADL2_Adapter_ModeTimingOverride_Caps',
    '_ADL_Adapter_ModeTimingOverride_Caps',
    '_ADL2_Display_TargetTiming_Get',
    '_ADL_Display_TargetTiming_Get',
    '_ADL2_Display_ModeTimingOverrideX2_Get',
    '_ADL_Display_ModeTimingOverrideX2_Get',
    '_ADL2_Display_ModeTimingOverrideListX2_Get',
    '_ADL_Display_ModeTimingOverrideListX2_Get',
    '_ADL2_Display_ModeTimingOverride_Delete',
    '_ADL_Display_ModeTimingOverride_Delete',
    '_ADL_Display_Downscaling_Caps',
    '_ADL2_Display_Downscaling_Caps',
    '_ADL_Display_FreeSyncState_Get',
    '_ADL2_Display_FreeSyncState_Get',
    '_ADL_Display_FreeSyncState_Set',
    '_ADL2_Display_FreeSyncState_Set',
    '_ADL2_Display_DCE_Set',
    '_ADL_Display_DCE_Set',
    '_ADL2_Display_DCE_Get',
    '_ADL_Display_DCE_Get',
    '_ADL2_Display_FreeSync_Cap',
    '_ADL_Display_FreeSync_Cap',
    '_ADL_CDS_UnsafeMode_Set',
    '_ADL2_CDS_UnsafeMode_Set',
    'Display'
)


from .adl_sdk_h import ADL2_Main_Control_Create  # NOQA
from .underscan_h import *  # NOQA


class Display(object):

    def __init__(self, adapter_index, display_index):
        self._adapter_index = adapter_index
        self._display_index = display_index

    @property
    def __preserve_aspect_ratio(self):
        lpSupport = INT()
        lpCurrent = INT()
        lpDefault = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_PreservedAspectRatio_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSupport),
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault),
            ) == ADL_OK:

                return lpSupport, lpCurrent, lpDefault

    @property
    def is_preserve_aspect_ratio_supported(self):
        lpSupport = self.__preserve_aspect_ratio

        if lpSupport is not None:
            return lpSupport[0].value == 1

    @property
    def preserve_aspect_ratio_default(self):
        lpDefault = self.__preserve_aspect_ratio

        if lpDefault is not None:
            return lpDefault[2].value

    @property
    def preserve_aspect_ratio(self):
        lpCurrent = self.__preserve_aspect_ratio

        if lpCurrent is not None:
            return lpCurrent[1].value

    @preserve_aspect_ratio.setter
    def preserve_aspect_ratio(self, value):
        lpCurrent = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_PreservedAspectRatio_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                lpCurrent,
            )

    @property
    def __image_expansion(self):
        lpSupport = INT()
        lpCurrent = INT()
        lpDefault = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_ImageExpansion_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSupport),
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault),
            ) == ADL_OK:
                return lpSupport, lpCurrent, lpDefault

    @property
    def is_image_expansion_supported(self):
        lpSupport = self.__image_expansion

        if lpSupport is not None:
            return lpSupport[0].value == 1

    @property
    def image_expansion_default(self):
        lpDefault = self.__image_expansion

        if lpDefault is not None:
            return lpDefault[2].value

    @property
    def image_expansion(self):
        lpCurrent = self.__image_expansion

        if lpCurrent is not None:
            return lpCurrent[1].value

    @image_expansion.setter
    def image_expansion(self, value):
        lpCurrent = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ImageExpansion_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                lpCurrent,
            )

    @property
    def dither(self):
        iDitherState = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_DitherState_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(iDitherState)
            ) == ADL_OK:
                return iDitherState.value

    @dither.setter
    def dither(self, value):
        iDitherState = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_DitherState_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iDitherState,
            )

    @property
    def suppoorted_pixel_format(self):
        iDitherState = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_SupportedPixelFormat_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(iDitherState)
            ) == ADL_OK:
                return iDitherState.value

    @property
    def pixel_format(self):
        """
        ADL_DISPLAY_PIXELFORMAT_UNKNOWN
        ADL_DISPLAY_PIXELFORMAT_YCRCB444
        ADL_DISPLAY_PIXELFORMAT_YCRCB422
        ADL_DISPLAY_PIXELFORMAT_RGB_LIMITED_RANGE
        ADL_DISPLAY_PIXELFORMAT_RGB_FULL_RANGE
        ADL_DISPLAY_PIXELFORMAT_YCRCB420
        :return:
        """
        iPixelFormat = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_PixelFormat_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(iPixelFormat)
            ) == ADL_OK:

                mapping = [
                    ADL_DISPLAY_PIXELFORMAT_UNKNOWN,
                    ADL_DISPLAY_PIXELFORMAT_YCRCB444,
                    ADL_DISPLAY_PIXELFORMAT_YCRCB422,
                    ADL_DISPLAY_PIXELFORMAT_RGB_LIMITED_RANGE,
                    ADL_DISPLAY_PIXELFORMAT_RGB_FULL_RANGE,
                    ADL_DISPLAY_PIXELFORMAT_YCRCB420
                ]
                return mapping[mapping.index(iPixelFormat.value)]

        return ADL_DISPLAY_PIXELFORMAT_UNKNOWN

    @pixel_format.setter
    def pixel_format(self, value):
        for item in (
            ADL_DISPLAY_PIXELFORMAT_UNKNOWN,
            ADL_DISPLAY_PIXELFORMAT_YCRCB444,
            ADL_DISPLAY_PIXELFORMAT_YCRCB422,
            ADL_DISPLAY_PIXELFORMAT_RGB_LIMITED_RANGE,
            ADL_DISPLAY_PIXELFORMAT_RGB_FULL_RANGE,
            ADL_DISPLAY_PIXELFORMAT_YCRCB420,
        ):
            if value == str(item):
                value = item
            if value == item:
                break
        else:
            return

        iPixelFormat = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_PixelFormat_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iPixelFormat,
            )

    @property
    def adjustment_coherent_default(self):
        lpAdjustmentCoherentCurrent = INT()
        lpAdjustmentCoherentDefault = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_AdjustmentCoherent_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpAdjustmentCoherentCurrent),
                ctypes.byref(lpAdjustmentCoherentDefault)
            ) == ADL_OK:
                return lpAdjustmentCoherentDefault.value

    @property
    def adjustment_coherent(self):
        lpAdjustmentCoherentCurrent = INT()
        lpAdjustmentCoherentDefault = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_AdjustmentCoherent_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpAdjustmentCoherentCurrent),
                ctypes.byref(lpAdjustmentCoherentDefault)
            ) == ADL_OK:
                return lpAdjustmentCoherentCurrent.value

    @adjustment_coherent.setter
    def adjustment_coherent(self, value):
        iAdjustmentCoherent = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_AdjustmentCoherent_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iAdjustmentCoherent,
            )

    @property
    def reduced_blanking_default(self):
        lpReducedBlankingCurrent = INT()
        lpReducedBlankingDefault = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_ReducedBlanking_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpReducedBlankingCurrent),
                ctypes.byref(lpReducedBlankingDefault)
            ) == ADL_OK:
                return lpReducedBlankingDefault.value

    @property
    def reduced_blanking(self):
        lpReducedBlankingCurrent = INT()
        lpReducedBlankingDefault = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_ReducedBlanking_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpReducedBlankingCurrent),
                ctypes.byref(lpReducedBlankingDefault)
            ) == ADL_OK:
                return lpReducedBlankingCurrent.value

    @reduced_blanking.setter
    def reduced_blanking(self, value):
        iReducedBlanking = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ReducedBlanking_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iReducedBlanking,
            )

    @property
    def __formats_override(self):
        lpSettingsSupported = INT()
        lpSettingsSupportedEx = INT()
        lpCurSettings = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_ReducedBlanking_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSettingsSupported),
                ctypes.byref(lpSettingsSupportedEx),
                ctypes.byref(lpCurSettings)
            ) == ADL_OK:
                return (
                    lpSettingsSupported,
                    lpSettingsSupportedEx,
                    lpCurSettings
                )

    @property
    def formats_override_supported(self):
        formats_override = self.__formats_override

        if formats_override is not None:
            return formats_override[0].value

    @property
    def formats_override_supported_ex(self):
        formats_override = self.__formats_override

        if formats_override is not None:
            return formats_override[1].value

    @property
    def formats_override(self):
        formats_override = self.__formats_override

        if formats_override is not None:
            return formats_override[2].value

    @formats_override.setter
    def formats_override(self, value):
        iOverrideSettings = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_FormatsOverride_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iOverrideSettings,
            )

    @property
    def can_underscan(self):
        lpSupport = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_UnderscanSupport_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSupport),
            ) == ADL_OK:
                return lpSupport.value == 1

    @property
    def overscan(self):
        lpCurrent = INT()
        lpDefault = INT()
        lpMin = INT()
        lpMax = INT()
        lpStep = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_Overscan_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault),
                ctypes.byref(lpMin),
                ctypes.byref(lpMax),
                ctypes.byref(lpStep)
            ) == ADL_OK:
                class Value(object):
                    default = lpDefault.value
                    min = lpMin.value
                    max = lpMax.value
                    step = lpStep.value

                overscan = ValueWrapper(lpCurrent.value)
                overscan._set_object(Value)

                return overscan

    @overscan.setter
    def overscan(self, value):
        overscan = self.overscan
        if not overscan.max >= value >= overscan.min:
            return

        if value % overscan.step:
            return

        iCurrent = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Overscan_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iCurrent,
            )

    @property
    def underscan(self):
        lpCurrent = INT()
        lpDefault = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_UnderscanState_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault)
            ) == ADL_OK:
                if not lpCurrent.value:
                    return

        lpCurrent = INT()
        lpDefault = INT()
        lpMin = INT()
        lpMax = INT()
        lpStep = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_Underscan_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault),
                ctypes.byref(lpMin),
                ctypes.byref(lpMax),
                ctypes.byref(lpStep)
            ) == ADL_OK:
                class Value(object):
                    default = lpDefault.value
                    min = lpMin.value
                    max = lpMax.value
                    step = lpStep.value

                underscan = ValueWrapper(lpCurrent.value)
                underscan._set_object(Value)

                return underscan

    @underscan.setter
    def underscan(self, value):
        underscan = self.underscan

        if underscan is None and value is None:
            return

        if underscan is None and value is not None:
            iCurrent = INT(1)
            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Underscan_Set(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iCurrent,
                )

            underscan = self.underscan

        elif underscan is not None and value is None:
            iCurrent = INT(0)
            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Underscan_Set(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iCurrent,
                )

            return

        if not underscan.max >= value >= underscan.min:
            return

        if value % underscan.step:
            return

        iCurrent = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Underscan_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iCurrent,
            )

    @property
    def suppoorted_color_depth(self):
        iColorDepth = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_SupportedColorDepth_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(iColorDepth)
            ) == ADL_OK:
                return iColorDepth.value

    @property
    def color_depth(self):
        """
        ADL_COLORDEPTH_UNKNOWN
        ADL_COLORDEPTH_666: Indicates if color depth is 6bit
        ADL_COLORDEPTH_888: Indicates if color depth is 8bit
        ADL_COLORDEPTH_101010: Indicates if color depth is 10bit
        ADL_COLORDEPTH_121212: Indicates if color depth is 12bit
        ADL_COLORDEPTH_141414: Indicates if color depth is 14bit
        ADL_COLORDEPTH_161616: Indicates if color depth is 16bit
        :return:
        """
        iColorDepth = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_ColorDepth_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(iColorDepth)
            ) == ADL_OK:
                mapping = [
                    ADL_COLORDEPTH_UNKNOWN,
                    ADL_COLORDEPTH_666,
                    ADL_COLORDEPTH_888,
                    ADL_COLORDEPTH_101010,
                    ADL_COLORDEPTH_121212,
                    ADL_COLORDEPTH_141414,
                    ADL_COLORDEPTH_161616
                ]

                return mapping[mapping.index(iColorDepth.value)]

        return ADL_COLORDEPTH_UNKNOWN

    @color_depth.setter
    def color_depth(self, value):

        for item in (
            ADL_COLORDEPTH_666,
            ADL_COLORDEPTH_888,
            ADL_COLORDEPTH_101010,
            ADL_COLORDEPTH_121212,
            ADL_COLORDEPTH_141414,
            ADL_COLORDEPTH_161616
        ):
            if value == str(item):
                value = item
            if value == item:
                break
        else:
            return

        iColorDepth = INT(value)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ColorDepth_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iColorDepth,
            )

    @property
    def position(self):
        return Position(self._adapter_index, self._display_index)

    @position.setter
    def position(self, value):
        if isinstance(value, (list, tuple)):
            iX = INT(value[0])
            iY = INT(value[1])

            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Position_Set(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iX,
                    iY
                )

    @property
    def size(self):
        return Size(self._adapter_index, self._display_index)

    @size.setter
    def size(self, value):
        if isinstance(value, (list, tuple)):
            iWidth = INT(value[0])
            iHeight = INT(value[1])

            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Size_Set(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iWidth,
                    iHeight
                )

    @property
    def __caps(self):
        lpInfo = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_AdjustCaps_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    ctypes.byref(lpInfo),
            ) == ADL_OK:
                return lpInfo.value

    @property
    def can_overscan(self):
        lpInfo = self.__caps

        if lpInfo is not None:
            return lpInfo & ADL_DISPLAY_ADJUST_OVERSCAN != 0

    @property
    def can_adjust_vertical_position(self):
        lpInfo = self.__caps

        if lpInfo is not None:
            return lpInfo & ADL_DISPLAY_ADJUST_VERT_POS != 0

    @property
    def can_adjust_horizontal_position(self):
        lpInfo = self.__caps

        if lpInfo is not None:
            return lpInfo & ADL_DISPLAY_ADJUST_HOR_POS != 0

    @property
    def can_adjust_vertical_size(self):
        lpInfo = self.__caps

        if lpInfo is not None:
            return lpInfo & ADL_DISPLAY_ADJUST_VERT_SIZE != 0

    @property
    def can_adjust_horizontal_size(self):
        lpInfo = self.__caps

        if lpInfo is not None:
            return lpInfo & ADL_DISPLAY_ADJUST_HOR_SIZE != 0

    @property
    def can_set_custom_modes(self):
        lpInfo = self.__caps

        if lpInfo is not None:
            return lpInfo & ADL_DISPLAY_CUSTOMMODES != 0


class Position(object):
    def __init__(self, adapter_index, display_index):
        self._adapter_index = adapter_index
        self._display_index = display_index

    @property
    def __position(self):
        lpX = INT()
        lpY = INT()
        lpXDefault = INT()
        lpYDefault = INT()
        lpMinX = INT()
        lpMinY = INT()
        lpMaxX = INT()
        lpMaxY = INT()
        lpStepX = INT()
        lpStepY = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_Position_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpX),
                ctypes.byref(lpY),
                ctypes.byref(lpXDefault),
                ctypes.byref(lpYDefault),
                ctypes.byref(lpMinX),
                ctypes.byref(lpMinY),
                ctypes.byref(lpMaxX),
                ctypes.byref(lpMaxY),
                ctypes.byref(lpStepX),
                ctypes.byref(lpStepY),
            ) == ADL_OK:
                return (
                    lpX,
                    lpY,
                    lpXDefault,
                    lpYDefault,
                    lpMinX,
                    lpMinY,
                    lpMaxX,
                    lpMaxY,
                    lpStepX,
                    lpStepY,
                )

    @property
    def x(self):
        position = self.__position

        if position is not None:
            return position[0].value

    @x.setter
    def x(self, value):
        iX = INT(value)
        iY = INT(self.y)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Position_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iX,
                iY
            )

    @property
    def y(self):
        position = self.__position

        if position is not None:
            return position[1].value

    @y.setter
    def y(self, value):
        iX = INT(self.x)
        iY = INT(value)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Position_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iX,
                iY
            )

    @property
    def default_x(self):
        position = self.__position

        if position is not None:
            return position[2].value

    @property
    def default_y(self):
        position = self.__position

        if position is not None:
            return position[3].value

    @property
    def min_x(self):
        position = self.__position

        if position is not None:
            return position[4].value

    @property
    def min_y(self):
        position = self.__position

        if position is not None:
            return position[5].value

    @property
    def max_x(self):
        position = self.__position

        if position is not None:
            return position[6].value

    @property
    def max_y(self):
        position = self.__position

        if position is not None:
            return position[7].value

    @property
    def step_x(self):
        position = self.__position

        if position is not None:
            return position[8].value

    @property
    def step_y(self):
        position = self.__position

        if position is not None:
            return position[9].value

    def __iter__(self):
        yield self.x
        yield self.y


class Size(object):
    def __init__(self, adapter_index, display_index):
        self._adapter_index = adapter_index
        self._display_index = display_index

    @property
    def __size(self):
        lpWidth = INT()
        lpHeight = INT()
        lpDefaultWidth = INT()
        lpDefaultHeight = INT()
        lpMinWidth = INT()
        lpMinHeight = INT()
        lpMaxWidth = INT()
        lpMaxHeight = INT()
        lpStepWidth = INT()
        lpStepHeight = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Display_Size_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpWidth),
                ctypes.byref(lpHeight),
                ctypes.byref(lpDefaultWidth),
                ctypes.byref(lpDefaultHeight),
                ctypes.byref(lpMinWidth),
                ctypes.byref(lpMinHeight),
                ctypes.byref(lpMaxWidth),
                ctypes.byref(lpMaxHeight),
                ctypes.byref(lpStepWidth),
                ctypes.byref(lpStepHeight),
            ) == ADL_OK:
                return (
                    lpWidth,
                    lpHeight,
                    lpDefaultWidth,
                    lpDefaultHeight,
                    lpMinWidth,
                    lpMinHeight,
                    lpMaxWidth,
                    lpMaxHeight,
                    lpStepWidth,
                    lpStepHeight,
                )

    @property
    def width(self):
        size = self.__size

        if size is not None:
            return size[0].value

    @width.setter
    def width(self, value):
        iWidth = INT(value)
        iHeight = INT(self.height)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Size_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iWidth,
                iHeight
            )

    @property
    def height(self):
        size = self.__size

        if size is not None:
            return size[1].value

    @height.setter
    def height(self, value):
        iWidth = INT(self.width)
        iHeight = INT(value)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Size_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iWidth,
                iHeight
            )

    @property
    def default_width(self):
        size = self.__size

        if size is not None:
            return size[2].value

    @property
    def default_height(self):
        size = self.__size

        if size is not None:
            return size[3].value

    @property
    def min_width(self):
        size = self.__size

        if size is not None:
            return size[4].value

    @property
    def min_height(self):
        size = self.__size

        if size is not None:
            return size[5].value

    @property
    def max_width(self):
        size = self.__size

        if size is not None:
            return size[6].value

    @property
    def max_height(self):
        size = self.__size

        if size is not None:
            return size[7].value

    @property
    def step_width(self):
        size = self.__size

        if size is not None:
            return size[8].value

    @property
    def step_height(self):
        size = self.__size

        if size is not None:
            return size[9].value

    def __iter__(self):
        yield self.width
        yield self.height

    def __list__(self):
        return [self.width, self.height]

    def __tuple__(self):
        return self.width, self.height
