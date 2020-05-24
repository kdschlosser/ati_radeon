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

    def __idiv__(self, other):
        return self.__ifloordiv__(other)

    def __itruediv__(self, other):
        return self.__idiv__(other)

    def __ifloordiv__(self, other):
        if self._obj.set_value is None:
            return self

        value = self.real // other
        value = self._obj.set_value(value)

        if value is None:
            return self

        cls = self.__class__(value)
        cls._obj = self._obj

        self = cls

        return self

    def __imul__(self, other):
        if self._obj.set_value is None:
            return self

        value = self.real * other
        value = self._obj.set_value(value)

        if value is None:
            return self

        cls = self.__class__(value)
        cls._obj = self._obj
        self = cls

        return self

    def __iadd__(self, other):
        if self._obj.set_value is None:
            return self

        value = self.real + other

        value = self._obj.set_value(value)

        if value is None:
            return self

        cls = self.__class__(value)
        cls._obj = self._obj

        self = cls

        return self

    def __isub__(self, other):
        if self._obj.set_value is None:
            return self

        value = self.real - other
        value = self._obj.set_value(value)

        if value is None:
            return self

        cls = self.__class__(value)
        cls._obj = self._obj

        self = cls

        return self

    @property
    def max(self):
        if self._obj.max_value is None:
            raise NotImplementedError

        return self._obj.max_value

    @property
    def min(self):
        if self._obj.min_value is None:
            raise NotImplementedError

        return self._obj.min_value

    @property
    def step(self):
        if self._obj.step_value is None:
            raise NotImplementedError

        return self._obj.step_value

    @property
    def default(self):
        if self._obj.default_value is None:
            raise NotImplementedError

        return self._obj.default_value


class Display(object):

    def __init__(
        self,
        adapter_index,
        display_id,
        display_name,
        display_manufacturer,
        display_type,
        display_output_type
    ):

        self._adapter_index = adapter_index
        self._display_id = display_id
        self._display_name = display_name
        self._display_manufacturer = display_manufacturer
        self._display_type = display_type
        self._display_output_type = display_output_type
        self._display_index = display_id.iDisplayLogicalIndex
        self.__position = None
        self.__size = None
        self.__overscan = None
        self.__underscan = None
        self.__brightness = None
        self.__contrast = None
        self.__saturation = None
        self.__hue = None
        self.__color_temperature = None
        self.__deflicker = None
        self.__filter_svideo = None


    @property
    def name(self):
        return self._display_name

    @property
    def manufacturer(self):
        return self._display_manufacturer

    @property
    def type(self):
        return self._display_type

    @property
    def output_type(self):
        return self._display_output_type

    @property
    def _color_caps(self):
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)
        lpCaps = INT()
        lpValids = INT()

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ColorCaps_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpCaps),
                ctypes.byref(lpValids)
            )

            return lpValids.value

    @property
    def is_brightness_supported(self):
        lpValids = self._color_caps
        return utils.get_bit(lpValids, ADL_DISPLAY_COLOR_BRIGHTNESS)



    @property
    def brightness(self):
        if self.__brightness is None:
            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)
            iColorType = INT(ADL_DISPLAY_COLOR_BRIGHTNESS)
            lpCurrent = INT(0)
            lpDefault = INT(0)
            lpMin = INT(0)
            lpMax = INT(0)
            lpStep = INT(0)

            def _set_value(value):
                value -= value % lpStep.value

                if value < lpMin.value or value > lpMax.value:
                    return

                lpCurrent = INT(value)

                with ADL2_Main_Control_Create as ctext:
                    _ADL2_Display_Color_Set(
                        ctext,
                        iAdapterIndex,
                        iDisplayIndex,
                        iColorType,
                        lpCurrent
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Color_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iColorType,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                brightness = IntValueWrapper(lpCurrent.value)
                brightness._obj = Value

                self.__brightness = brightness

        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        brightness = self.brightness
        brightness += value - brightness.real

    @property
    def is_contrast_supported(self):
        lpValids = self._color_caps
        return utils.get_bit(lpValids, ADL_DISPLAY_COLOR_CONTRAST)

    @property
    def contrast(self):
        if self.__contrast is None:
            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)
            iColorType = INT(ADL_DISPLAY_COLOR_CONTRAST)
            lpCurrent = INT(0)
            lpDefault = INT(0)
            lpMin = INT(0)
            lpMax = INT(0)
            lpStep = INT(0)

            def _set_value(value):
                value -= value % lpStep.value

                if value < lpMin.value or value > lpMax.value:
                    return

                lpCurrent = INT(value)

                with ADL2_Main_Control_Create as ctext:
                    _ADL2_Display_Color_Set(
                        ctext,
                        iAdapterIndex,
                        iDisplayIndex,
                        iColorType,
                        lpCurrent
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Color_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iColorType,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                contrast = IntValueWrapper(lpCurrent.value)
                contrast._obj = Value

                self.__contrast = contrast

        return self.__contrast

    @contrast.setter
    def contrast(self, value):
        contrast = self.contrast
        contrast += value - contrast.real

    @property
    def is_saturation_supported(self):
        lpValids = self._color_caps
        return utils.get_bit(lpValids, ADL_DISPLAY_COLOR_SATURATION)

    @property
    def saturation(self):
        if self.__saturation is None:
            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)
            iColorType = INT(ADL_DISPLAY_COLOR_SATURATION)
            lpCurrent = INT(0)
            lpDefault = INT(0)
            lpMin = INT(0)
            lpMax = INT(0)
            lpStep = INT(0)

            def _set_value(value):
                value -= value % lpStep.value

                if value < lpMin.value or value > lpMax.value:
                    return

                lpCurrent = INT(value)

                with ADL2_Main_Control_Create as ctext:
                    _ADL2_Display_Color_Set(
                        ctext,
                        iAdapterIndex,
                        iDisplayIndex,
                        iColorType,
                        lpCurrent
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Color_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iColorType,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                saturation = IntValueWrapper(lpCurrent.value)
                saturation._obj = Value

                self.__saturation = saturation

        return self.__saturation

    @saturation.setter
    def saturation(self, value):
        saturation = self.saturation
        saturation += value - saturation.real

    @property
    def is_hue_supported(self):
        lpValids = self._color_caps
        return utils.get_bit(lpValids, ADL_DISPLAY_COLOR_HUE)

    @property
    def hue(self):
        if self.__hue is None:
            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)
            iColorType = INT(ADL_DISPLAY_COLOR_HUE)
            lpCurrent = INT(0)
            lpDefault = INT(0)
            lpMin = INT(0)
            lpMax = INT(0)
            lpStep = INT(0)

            def _set_value(value):
                value -= value % lpStep.value

                if value < lpMin.value or value > lpMax.value:
                    return

                lpCurrent = INT(value)

                with ADL2_Main_Control_Create as ctext:
                    _ADL2_Display_Color_Set(
                        ctext,
                        iAdapterIndex,
                        iDisplayIndex,
                        iColorType,
                        lpCurrent
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Color_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iColorType,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                hue = IntValueWrapper(lpCurrent.value)
                hue._obj = Value

                self.__hue = hue

        return self.__hue

    @hue.setter
    def hue(self, value):
        hue = self.contrast
        hue += value - hue.real

    @property
    def is_color_temperature_supported(self):
        lpValids = self._color_caps
        return utils.get_bit(lpValids, ADL_DISPLAY_COLOR_TEMPERATURE)

    @property
    def color_temperature(self):
        if self.__color_temperature is None:
            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)
            iColorType = INT(ADL_DISPLAY_COLOR_TEMPERATURE)
            lpCurrent = INT(0)
            lpDefault = INT(0)
            lpMin = INT(0)
            lpMax = INT(0)
            lpStep = INT(0)

            def _set_value(value):
                value -= value % lpStep.value

                if value < lpMin.value or value > lpMax.value:
                    return

                lpCurrent = INT(value)

                with ADL2_Main_Control_Create as ctext:
                    _ADL2_Display_Color_Set(
                        ctext,
                        iAdapterIndex,
                        iDisplayIndex,
                        iColorType,
                        lpCurrent
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Color_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    iColorType,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                color_temperature = IntValueWrapper(lpCurrent.value)
                color_temperature._obj = Value

                self.__color_temperature = color_temperature

        return self.__color_temperature

    @color_temperature.setter
    def color_temperature(self, value):
        color_temperature = self.color_temperature
        color_temperature += value - color_temperature.real

    @property
    def color_temperature_source(self):
        mapping = [
            ADL_DISPLAY_COLOR_TEMPERATURE_SOURCE_EDID,
            ADL_DISPLAY_COLOR_TEMPERATURE_SOURCE_USER
        ]
        lpTempSource = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ColorTemperatureSource_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpTempSource)
            )

            if lpTempSource.value in mapping:
                return mapping[mapping.index(lpTempSource.value)]

        return 'Unknown'

    @color_temperature_source.setter
    def color_temperature_source(self, value):
        mapping = [
            ADL_DISPLAY_COLOR_TEMPERATURE_SOURCE_EDID,
            ADL_DISPLAY_COLOR_TEMPERATURE_SOURCE_USER
        ]

        for item in mapping:
            if value in (item, str(item)):
                break

        else:
            return

        iTempSource = INT(item)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ColorTemperatureSource_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iTempSource
            )

    @property
    def color_temperature_source_default(self):
        mapping = [
            ADL_DISPLAY_COLOR_TEMPERATURE_SOURCE_EDID,
            ADL_DISPLAY_COLOR_TEMPERATURE_SOURCE_USER
        ]
        lpTempSourceDefault = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ColorTemperatureSourceDefault_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpTempSourceDefault)
            )

            if lpTempSourceDefault.value in mapping:
                return mapping[mapping.index(lpTempSourceDefault.value)]

        return 'Unknown'

    @property
    def _gpu_scaling(self):
        lpSupport = INT()
        lpCurrent = INT()
        lpDefault = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_DFP_GPUScalingEnable_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSupport),
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault)
            )

            return bool(lpSupport.value), bool(lpDefault.value), bool(lpCurrent.value)

    @property
    def is_gpu_scaling_supported(self):
        return self._gpu_scaling[0]

    @property
    def gpu_scaling_default(self):
        return self._gpu_scaling[1]

    @property
    def gpu_scaling(self):
        return self._gpu_scaling[2]

    @gpu_scaling.setter
    def gpu_scaling(self, value):
        iCurrent = INT(int(value))
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_DFP_GPUScalingEnable_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iCurrent,
            )

    @property
    def __preserve_aspect_ratio(self):
        lpSupport = INT()
        lpCurrent = INT()
        lpDefault = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_PreservedAspectRatio_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSupport),
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault)
            )
            return lpSupport.value == 1, lpCurrent.value == 1, lpDefault.value == 1

    @property
    def is_preserve_aspect_ratio_supported(self):
        return self.__preserve_aspect_ratio[0]

    @property
    def preserve_aspect_ratio_default(self):
        return self.__preserve_aspect_ratio[2]

    @property
    def preserve_aspect_ratio(self):
        return self.__preserve_aspect_ratio[1]

    @preserve_aspect_ratio.setter
    def preserve_aspect_ratio(self, value):
        lpCurrent = INT(int(value))
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
            _ADL2_Display_ImageExpansion_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSupport),
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault),
            )
            return lpSupport.value == 1, lpCurrent.value == 1, lpDefault.value == 1

    @property
    def is_image_expansion_supported(self):
        return self.__image_expansion[0]

    @property
    def image_expansion_default(self):
        return self.__image_expansion[2]

    @property
    def image_expansion(self):
        return self.__image_expansion[1]

    @image_expansion.setter
    def image_expansion(self, value):
        lpCurrent = INT(int(value))
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
        mapping = [
            ADL_DL_DISPLAY_DITHER_DISABLED,
            ADL_DL_DISPLAY_DITHER_DRIVER_DEFAULT,
            ADL_DL_DISPLAY_DITHER_FM6,
            ADL_DL_DISPLAY_DITHER_FM8,
            ADL_DL_DISPLAY_DITHER_FM10,
            ADL_DL_DISPLAY_DITHER_DITH6,
            ADL_DL_DISPLAY_DITHER_DITH8,
            ADL_DL_DISPLAY_DITHER_DITH10,
            ADL_DL_DISPLAY_DITHER_DITH6_NO_FRAME_RAND,
            ADL_DL_DISPLAY_DITHER_DITH8_NO_FRAME_RAND,
            ADL_DL_DISPLAY_DITHER_DITH10_NO_FRAME_RAND,
            ADL_DL_DISPLAY_DITHER_TRUN6,
            ADL_DL_DISPLAY_DITHER_TRUN8,
            ADL_DL_DISPLAY_DITHER_TRUN10,
            ADL_DL_DISPLAY_DITHER_TRUN10_DITH8,
            ADL_DL_DISPLAY_DITHER_TRUN10_DITH6,
            ADL_DL_DISPLAY_DITHER_TRUN10_FM8,
            ADL_DL_DISPLAY_DITHER_TRUN10_FM6,
            ADL_DL_DISPLAY_DITHER_TRUN10_DITH8_FM6,
            ADL_DL_DISPLAY_DITHER_DITH10_FM8,
            ADL_DL_DISPLAY_DITHER_DITH10_FM6,
            ADL_DL_DISPLAY_DITHER_TRUN8_DITH6,
            ADL_DL_DISPLAY_DITHER_TRUN8_FM6,
            ADL_DL_DISPLAY_DITHER_DITH8_FM6
        ]
        iDitherState = INT(0)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_DitherState_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(iDitherState)
            )

            return mapping[mapping.index(iDitherState.value)]

    @dither.setter
    def dither(self, value):
        mapping = [
            ADL_DL_DISPLAY_DITHER_DISABLED,
            ADL_DL_DISPLAY_DITHER_DRIVER_DEFAULT,
            ADL_DL_DISPLAY_DITHER_FM6,
            ADL_DL_DISPLAY_DITHER_FM8,
            ADL_DL_DISPLAY_DITHER_FM10,
            ADL_DL_DISPLAY_DITHER_DITH6,
            ADL_DL_DISPLAY_DITHER_DITH8,
            ADL_DL_DISPLAY_DITHER_DITH10,
            ADL_DL_DISPLAY_DITHER_DITH6_NO_FRAME_RAND,
            ADL_DL_DISPLAY_DITHER_DITH8_NO_FRAME_RAND,
            ADL_DL_DISPLAY_DITHER_DITH10_NO_FRAME_RAND,
            ADL_DL_DISPLAY_DITHER_TRUN6,
            ADL_DL_DISPLAY_DITHER_TRUN8,
            ADL_DL_DISPLAY_DITHER_TRUN10,
            ADL_DL_DISPLAY_DITHER_TRUN10_DITH8,
            ADL_DL_DISPLAY_DITHER_TRUN10_DITH6,
            ADL_DL_DISPLAY_DITHER_TRUN10_FM8,
            ADL_DL_DISPLAY_DITHER_TRUN10_FM6,
            ADL_DL_DISPLAY_DITHER_TRUN10_DITH8_FM6,
            ADL_DL_DISPLAY_DITHER_DITH10_FM8,
            ADL_DL_DISPLAY_DITHER_DITH10_FM6,
            ADL_DL_DISPLAY_DITHER_TRUN8_DITH6,
            ADL_DL_DISPLAY_DITHER_TRUN8_FM6,
            ADL_DL_DISPLAY_DITHER_DITH8_FM6
        ]

        for item in mapping:
            if value in (item, str(item)):
                break
        else:
            return

        iDitherState = INT(item)
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
    def supported_pixel_formats(self):
        mapping = [
            ADL_DISPLAY_PIXELFORMAT_RGB,
            ADL_DISPLAY_PIXELFORMAT_YCRCB444,
            ADL_DISPLAY_PIXELFORMAT_YCRCB422,
            ADL_DISPLAY_PIXELFORMAT_RGB_LIMITED_RANGE,
            ADL_DISPLAY_PIXELFORMAT_RGB_FULL_RANGE,
            ADL_DISPLAY_PIXELFORMAT_YCRCB420
        ]

        lpPixelFormat = INT(0)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_SupportedPixelFormat_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpPixelFormat)
            )
            res = []
            for item in mapping:
                if utils.get_bit(lpPixelFormat.value, item):
                    res += [item]

            return res

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
        mapping = [
            ADL_DISPLAY_PIXELFORMAT_UNKNOWN,
            ADL_DISPLAY_PIXELFORMAT_RGB,
            ADL_DISPLAY_PIXELFORMAT_YCRCB444,
            ADL_DISPLAY_PIXELFORMAT_YCRCB422,
            ADL_DISPLAY_PIXELFORMAT_RGB_LIMITED_RANGE,
            ADL_DISPLAY_PIXELFORMAT_RGB_FULL_RANGE,
            ADL_DISPLAY_PIXELFORMAT_YCRCB420
        ]

        iPixelFormat = INT(0)
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_PixelFormat_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(iPixelFormat)
            )

            return mapping[mapping.index(iPixelFormat.value)]

    @pixel_format.setter
    def pixel_format(self, value):
        mapping = [
            ADL_DISPLAY_PIXELFORMAT_RGB,
            ADL_DISPLAY_PIXELFORMAT_YCRCB444,
            ADL_DISPLAY_PIXELFORMAT_YCRCB422,
            ADL_DISPLAY_PIXELFORMAT_RGB_LIMITED_RANGE,
            ADL_DISPLAY_PIXELFORMAT_RGB_FULL_RANGE,
            ADL_DISPLAY_PIXELFORMAT_YCRCB420
        ]
        for item in mapping:
            if value in (item, str(item)):
                break
        else:
            return

        iPixelFormat = INT(item)
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
        lpAdjustmentCoherentCurrent = INT(0)
        lpAdjustmentCoherentDefault = INT(0)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_AdjustmentCoherent_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpAdjustmentCoherentCurrent),
                ctypes.byref(lpAdjustmentCoherentDefault)
            )
            return bool(lpAdjustmentCoherentDefault.value)

    @property
    def adjustment_coherent(self):
        lpAdjustmentCoherentCurrent = INT(0)
        lpAdjustmentCoherentDefault = INT(0)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_AdjustmentCoherent_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpAdjustmentCoherentCurrent),
                ctypes.byref(lpAdjustmentCoherentDefault)
            )
            return bool(lpAdjustmentCoherentCurrent.value)

    @adjustment_coherent.setter
    def adjustment_coherent(self, value):
        iAdjustmentCoherent = INT(int(value))
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
        lpReducedBlankingCurrent = INT(0)
        lpReducedBlankingDefault = INT(0)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ReducedBlanking_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpReducedBlankingCurrent),
                ctypes.byref(lpReducedBlankingDefault)
            )
            return lpReducedBlankingDefault.value

    @property
    def reduced_blanking(self):
        lpReducedBlankingCurrent = INT(0)
        lpReducedBlankingDefault = INT(0)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ReducedBlanking_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpReducedBlankingCurrent),
                ctypes.byref(lpReducedBlankingDefault)
            )
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
        mapping = [
            ADL_DISPLAY_FORMAT_FORCE_720P,
            ADL_DISPLAY_FORMAT_FORCE_1080I,
            ADL_DISPLAY_FORMAT_FORCE_1080P,
            ADL_DISPLAY_FORMAT_FORCE_720P50,
            ADL_DISPLAY_FORMAT_FORCE_1080I25,
            ADL_DISPLAY_FORMAT_FORCE_576I25,
            ADL_DISPLAY_FORMAT_FORCE_576P50,
            ADL_DISPLAY_FORMAT_FORCE_1080P24,
            ADL_DISPLAY_FORMAT_FORCE_1080P25,
            ADL_DISPLAY_FORMAT_FORCE_1080P30,
            ADL_DISPLAY_FORMAT_FORCE_1080P50
        ]

        mapping_ex = [
            ADL_DISPLAY_FORMAT_CVDONGLEOVERIDE,
            ADL_DISPLAY_FORMAT_CVMODEUNDERSCAN,
            ADL_DISPLAY_FORMAT_FORCECONNECT_SUPPORTED,
            ADL_DISPLAY_FORMAT_RESTRICT_FORMAT_SELECTION,
            ADL_DISPLAY_FORMAT_SETASPECRATIO,
            ADL_DISPLAY_FORMAT_FORCEMODES,
            ADL_DISPLAY_FORMAT_LCDRTCCOEFF
        ]
        lpSettingsSupported = INT()
        lpSettingsSupportedEx = INT()
        lpCurSettings = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_FormatsOverride_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSettingsSupported),
                ctypes.byref(lpSettingsSupportedEx),
                ctypes.byref(lpCurSettings)
            )
            res = []

            for item in mapping:

                if utils.get_bit(lpSettingsSupported.value, item):
                    res += [item]

            res_ex = []

            for item in mapping_ex:
                if utils.get_bit(lpSettingsSupportedEx.value, item):
                    res_ex += [item]

            res_cur = []

            for item in mapping:
                if utils.get_bit(lpCurSettings.value, item):
                    res_cur += [item]

            for item in mapping_ex:
                if (
                    utils.get_bit(lpCurSettings.value, item) and
                    item not in res_cur
                ):
                    res_cur += [item]

            return res, res_ex, res_cur

    @property
    def formats_override_supported(self):
        return self.__formats_override[0]

    @property
    def formats_override_supported_ex(self):
        return self.__formats_override[1]

    @property
    def formats_override(self):
        return self.__formats_override[2]

    @formats_override.setter
    def formats_override(self, value):
        mapping = [
            ADL_DISPLAY_FORMAT_FORCE_720P,
            ADL_DISPLAY_FORMAT_FORCE_1080I,
            ADL_DISPLAY_FORMAT_FORCE_1080P,
            ADL_DISPLAY_FORMAT_FORCE_720P50,
            ADL_DISPLAY_FORMAT_FORCE_1080I25,
            ADL_DISPLAY_FORMAT_FORCE_576I25,
            ADL_DISPLAY_FORMAT_FORCE_576P50,
            ADL_DISPLAY_FORMAT_FORCE_1080P24,
            ADL_DISPLAY_FORMAT_FORCE_1080P25,
            ADL_DISPLAY_FORMAT_FORCE_1080P30,
            ADL_DISPLAY_FORMAT_FORCE_1080P50
        ]

        mapping_ex = [
            ADL_DISPLAY_FORMAT_CVDONGLEOVERIDE,
            ADL_DISPLAY_FORMAT_CVMODEUNDERSCAN,
            ADL_DISPLAY_FORMAT_FORCECONNECT_SUPPORTED,
            ADL_DISPLAY_FORMAT_RESTRICT_FORMAT_SELECTION,
            ADL_DISPLAY_FORMAT_SETASPECRATIO,
            ADL_DISPLAY_FORMAT_FORCEMODES,
            ADL_DISPLAY_FORMAT_LCDRTCCOEFF
        ]

        if not isinstance(value, (list, tuple)):
            return

        val = 0
        value = list(value)

        for v in value[:]:
            for item in mapping:
                if v in (item, str(item)):
                    break
            else:
                for item in mapping_ex:
                    if v in (item, str(item)):
                        break
                else:
                    return

            val |= item

        iOverrideSettings = INT(val)
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
    def deflicker(self):
        if self.__deflicker is None:
            lpCurrent = INT()
            lpDefault = INT()
            lpMin = INT()
            lpMax = INT()
            lpStep = INT()

            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)

            def _set_value(value):
                value -= value % lpStep.value

                if value < lpMin.value or value > lpMax.value:
                    return

                iCurrent = INT(value)
                with ADL2_Main_Control_Create as ctext:
                    _ADL2_Display_Deflicker_Set(
                        ctext,
                        iAdapterIndex,
                        iDisplayIndex,
                        iCurrent,
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Deflicker_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                deflicker = IntValueWrapper(lpCurrent.value)
                deflicker._obj = Value

                self.__deflicker = deflicker

        return self.__deflicker

    @deflicker.setter
    def deflicker(self, value):
        deflicker = self.deflicker
        deflicker += value - deflicker.real

    @property
    def filter_svideo(self):
        if self.__filter_svideo is None:
            lpCurrent = INT()
            lpDefault = INT()
            lpMin = INT()
            lpMax = INT()
            lpStep = INT()

            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)

            def _set_value(value):
                value -= value % lpStep.value

                if value < lpMin.value or value > lpMax.value:
                    return

                iCurrent = INT(value)
                with ADL2_Main_Control_Create as ctext:
                    _ADL2_Display_FilterSVideo_Set(
                        ctext,
                        iAdapterIndex,
                        iDisplayIndex,
                        iCurrent,
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_FilterSVideo_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                filter_svideo = IntValueWrapper(lpCurrent.value)
                filter_svideo._obj = Value

                self.__filter_svideo = filter_svideo

        return self.__filter_svideo

    @filter_svideo.setter
    def filter_svideo(self, value):
        filter_svideo = self.filter_svideo
        filter_svideo += value - filter_svideo.real

    @property
    def freesync(self):
        return FreeSync(self._adapter_index, self._display_index)

    @property
    def is_freesync_supported(self):
        lpFreeSyncCaps = ADLFreeSyncCap()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_FreeSync_Cap(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpFreeSyncCaps),
            )

            return lpFreeSyncCaps.iCaps | ADL_FREESYNC_CAP_GPUSUPPORTED == lpFreeSyncCaps.iCaps

    @property
    def supported_contents(self):
        mapping = [
            ADL_DL_DISPLAYCONTENT_TYPE_GRAPHICS,
            ADL_DL_DISPLAYCONTENT_TYPE_PHOTO,
            ADL_DL_DISPLAYCONTENT_TYPE_CINEMA,
            ADL_DL_DISPLAYCONTENT_TYPE_GAME
        ]
        pCapContent = INT(0)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        res = []
        with ADL2_Main_Control_Create as context:
            _ADL2_Display_DisplayContent_Cap(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(pCapContent)
            )

            for item in mapping:
                if pCapContent.value | item ==  pCapContent.value:
                    res += [item]

        return res

    @property
    def is_virtual_super_resolution_supported(self):
        lpDisplayProperty = ADLDisplayProperty()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)
        lpDisplayProperty.iSize = ctypes.sizeof(ADLDisplayProperty)
        lpDisplayProperty.iPropertyType = ADL_DL_DISPLAYPROPERTY_TYPE_DOWNSCALE

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Property_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpDisplayProperty)
            )

            return lpDisplayProperty.iSupport == 1

    @property
    def virtual_super_resolution(self):
        lpDisplayProperty = ADLDisplayProperty()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)
        lpDisplayProperty.iSize = ctypes.sizeof(ADLDisplayProperty)
        lpDisplayProperty.iPropertyType = ADL_DL_DISPLAYPROPERTY_TYPE_DOWNSCALE

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Property_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpDisplayProperty)
            )

            return lpDisplayProperty.iCurrent == 1

    @virtual_super_resolution.setter
    def virtual_super_resolution(self, value):
        lpDisplayProperty = ADLDisplayProperty()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)
        lpDisplayProperty.iSize = ctypes.sizeof(ADLDisplayProperty)
        lpDisplayProperty.iPropertyType = ADL_DL_DISPLAYPROPERTY_TYPE_DOWNSCALE
        lpDisplayProperty.iCurrent = int(value)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Property_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpDisplayProperty)
            )

    @property
    def is_expansion_mode_supported(self):
        lpDisplayProperty = ADLDisplayProperty()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)
        lpDisplayProperty.iSize = ctypes.sizeof(ADLDisplayProperty)
        lpDisplayProperty.iPropertyType = ADL_DL_DISPLAYPROPERTY_TYPE_EXPANSIONMODE

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Property_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpDisplayProperty)
            )

            return lpDisplayProperty.iSupport == 1

    @property
    def expansion_mode(self):
        mapping = [
            ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_CENTER,
            ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_FULLSCREEN,
            ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_ASPECTRATIO
        ]

        lpDisplayProperty = ADLDisplayProperty()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)
        lpDisplayProperty.iSize = ctypes.sizeof(ADLDisplayProperty)
        lpDisplayProperty.iPropertyType = ADL_DL_DISPLAYPROPERTY_TYPE_EXPANSIONMODE

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Property_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpDisplayProperty)
            )

            if lpDisplayProperty.iExpansionMode in mapping:
                return mapping[mapping.index(lpDisplayProperty.iExpansionMode)]

    @expansion_mode.setter
    def expansion_mode(self, value):
        mapping = [
            ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_CENTER,
            ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_FULLSCREEN,
            ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_ASPECTRATIO
        ]

        for item in mapping:
            if value in (item, str(item)):
                break
        else:
            return

        lpDisplayProperty = ADLDisplayProperty()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)
        lpDisplayProperty.iSize = ctypes.sizeof(ADLDisplayProperty)
        lpDisplayProperty.iPropertyType = ADL_DL_DISPLAYPROPERTY_TYPE_EXPANSIONMODE
        lpDisplayProperty.iExpansionMode = item

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_Property_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpDisplayProperty)
            )

    @property
    def content(self):
        mapping = [
            ADL_DL_DISPLAYCONTENT_TYPE_GRAPHICS,
            ADL_DL_DISPLAYCONTENT_TYPE_PHOTO,
            ADL_DL_DISPLAYCONTENT_TYPE_CINEMA,
            ADL_DL_DISPLAYCONTENT_TYPE_GAME
        ]
        piContent = INT(0)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_DisplayContent_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(piContent)
            )

            if piContent.value in mapping:
                return mapping[mapping.index(piContent.value)]
        return 'Unknown'

    @content.setter
    def content(self, value):
        mapping = [
            ADL_DL_DISPLAYCONTENT_TYPE_GRAPHICS,
            ADL_DL_DISPLAYCONTENT_TYPE_PHOTO,
            ADL_DL_DISPLAYCONTENT_TYPE_CINEMA,
            ADL_DL_DISPLAYCONTENT_TYPE_GAME
        ]

        for item in mapping:
            if value in (item, str(item)):
                break

        else:
            return

        piContent = INT(item)

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_DisplayContent_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                piContent
            )

    @property
    def is_overscan_supported(self):
        lpInfo = self.__caps

        if lpInfo is not None:
            return lpInfo | ADL_DISPLAY_ADJUST_OVERSCAN == lpInfo

    @property
    def overscan(self):
        if self.__overscan is None:
            lpCurrent = INT()
            lpDefault = INT()
            lpMin = INT()
            lpMax = INT()
            lpStep = INT()

            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)

            def _set_value(value):
                value -= value % lpStep.value

                if value < lpMin.value or value > lpMax.value:
                    return

                iCurrent = INT(value)
                with ADL2_Main_Control_Create as ctext:
                    _ADL2_Display_Overscan_Set(
                        ctext,
                        iAdapterIndex,
                        iDisplayIndex,
                        iCurrent,
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Overscan_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                overscan = IntValueWrapper(lpCurrent.value)
                overscan._obj = Value

                self.__overscan = overscan

        return self.__overscan

    @overscan.setter
    def overscan(self, value):
        overscan = self.overscan
        overscan += value - overscan.real

    @property
    def is_underscan_supported(self):
        lpSupport = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            res = _ADL2_Display_UnderscanSupport_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpSupport),
            )
            return lpSupport.value == 1

    @property
    def underscan(self):
        if self.__underscan is None:
            lpCurrent = INT()
            lpDefault = INT()
            lpMin = INT()
            lpMax = INT()
            lpStep = INT()

            iAdapterIndex = INT(self._adapter_index)
            iDisplayIndex = INT(self._display_index)

            def _set_value(value):
                value -= value % lpStep.value

                if value > lpMax.value:
                    return

                if value < lpMin.value:
                    value = 0

                with ADL2_Main_Control_Create as ctext:
                    if value:
                        iUnderscanEnabled = INT(1)
                        iCurrent = INT(value)

                        _ADL2_Display_Underscan_Set(
                            ctext,
                            iAdapterIndex,
                            iDisplayIndex,
                            iCurrent,
                        )
                    else:
                        iUnderscanEnabled = INT(0)

                    _ADL2_Display_UnderscanState_Set(
                        ctext,
                        iAdapterIndex,
                        iUnderscanEnabled
                    )

                    return value

            with ADL2_Main_Control_Create as context:
                _ADL2_Display_Underscan_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    ctypes.byref(lpCurrent),
                    ctypes.byref(lpDefault),
                    ctypes.byref(lpMin),
                    ctypes.byref(lpMax),
                    ctypes.byref(lpStep)
                )

                class Value(object):
                    default_value = lpDefault.value
                    min_value = lpMin.value
                    max_value = lpMax.value
                    step_value = lpStep.value
                    set_value = _set_value

                underscan = IntValueWrapper(lpCurrent.value)
                underscan._obj = Value

                self.__underscan = underscan

        return self.__underscan

    @underscan.setter
    def underscan(self, value):
        underscan = self.underscan
        if value == 0:
            value = underscan.real

        underscan += value - underscan.real

    @property
    def supported_color_depths(self):
        mapping = [
            ADL_COLORDEPTH_666,
            ADL_COLORDEPTH_888,
            ADL_COLORDEPTH_101010,
            ADL_COLORDEPTH_121212,
            ADL_COLORDEPTH_141414,
            ADL_COLORDEPTH_161616
        ]

        iColorDepth = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_SupportedColorDepth_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iColorDepth
            )

            res = []

            for item in mapping:
                if utils.get_bit(iColorDepth.value, item):
                    res += [item]

            return res

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
        mapping = [
            ADL_COLORDEPTH_UNKNOWN,
            ADL_COLORDEPTH_666,
            ADL_COLORDEPTH_888,
            ADL_COLORDEPTH_101010,
            ADL_COLORDEPTH_121212,
            ADL_COLORDEPTH_141414,
            ADL_COLORDEPTH_161616
        ]

        iColorDepth = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_ColorDepth_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(iColorDepth)
            )

            return mapping[mapping.index(iColorDepth.value)]

    @color_depth.setter
    def color_depth(self, value):
        mapping = [
            ADL_COLORDEPTH_666,
            ADL_COLORDEPTH_888,
            ADL_COLORDEPTH_101010,
            ADL_COLORDEPTH_121212,
            ADL_COLORDEPTH_141414,
            ADL_COLORDEPTH_161616
        ]

        for item in mapping:
            if value in (item, str(item)):
                break
        else:
            return

        iColorDepth = INT(item)
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
        if self.__position is None:
            self.__position = Position(self._adapter_index, self._display_index)

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, (list, tuple)):
            return

        x = value[0]
        y = value[1]

        position = self.position
        position.x = x
        position.y = y

    @property
    def size(self):
        if self.__size is None:
            self.__size = Size(self._adapter_index, self._display_index)

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (list, tuple)):
            return

        width = value[0]
        height = value[1]

        size = self.size
        size.width = width
        size.height = height

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
    def can_set_custom_modes(self):
        lpInfo = self.__caps

        if lpInfo is not None:
            return lpInfo & ADL_DISPLAY_CUSTOMMODES != 0


class Position(object):
    def __init__(self, adapter_index, display_index):
        self._adapter_index = adapter_index
        self._display_index = display_index
        self.__x = None
        self.__y = None

    @property
    def __caps(self):
        lpInfo = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_AdjustCaps_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    ctypes.byref(lpInfo),
            )
            return lpInfo.value

    @property
    def is_vertical_position_supported(self):
        lpInfo = self.__caps

        return (
            lpInfo | ADL_DISPLAY_ADJUST_VERT_POS == lpInfo or
            lpInfo | ADL_DISPLAY_ADJUST_SIZEPOS == lpInfo
        )

    @property
    def is_horizontal_position_supported(self):
        lpInfo = self.__caps

        return (
            lpInfo | ADL_DISPLAY_ADJUST_HOR_POS == lpInfo or
            lpInfo | ADL_DISPLAY_ADJUST_SIZEPOS == lpInfo
        )

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
            res = _ADL2_Display_Position_Get(
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
            )
            return (
                lpX.value,
                lpY.value,
                lpXDefault.value,
                lpYDefault.value,
                lpMinX.value,
                lpMinY.value,
                lpMaxX.value,
                lpMaxY.value,
                lpStepX.value,
                lpStepY.value,
            )

    @property
    def x(self):
        if self.__x is None:
            position = self.__position

            lpX = position[0]
            lpXDefault = position[2]
            lpMinX = position[4]
            lpMaxX = position[6]
            lpStepX = position[8]

            def _set_value(value):
                value -= value % lpStepX

                if value < lpMinX or value > lpMaxX:
                    return

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

                    return value

            class Value(object):
                default_value = lpXDefault
                min_value = lpMinX
                max_value = lpMaxX
                step_value = lpStepX
                set_value = _set_value

            x = IntValueWrapper(lpX)
            x._obj = Value
            self.__x = x

        return self.__x

    @x.setter
    def x(self, value):
        x = self.x
        x += value - x.real

    @property
    def y(self):
        if self.__y is None:
            position = self.__position

            lpY = position[1]
            lpYDefault = position[3]
            lpMinY = position[5]
            lpMaxY = position[7]
            lpStepY = position[9]

            def _set_value(value):
                value -= value % lpStepY

                if value < lpMinY or value > lpMaxY:
                    return

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

                    return value

            class Value(object):
                default_value = lpYDefault
                min_value = lpMinY
                max_value = lpMaxY
                step_value = lpStepY
                set_value = _set_value

            y = IntValueWrapper(lpY)
            y._obj = Value
            self.__y = y

        return self.__y

    @y.setter
    def y(self, value):
        y = self.y
        y += y - y.real

    def __iter__(self):
        yield self.x
        yield self.y


class Size(object):
    def __init__(self, adapter_index, display_index):
        self._adapter_index = adapter_index
        self._display_index = display_index
        self.__width = None
        self.__height = None

    @property
    def __caps(self):
        lpInfo = INT()
        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_AdjustCaps_Get(
                    context,
                    iAdapterIndex,
                    iDisplayIndex,
                    ctypes.byref(lpInfo),
            )
            return lpInfo.value

    @property
    def is_vertical_size_supported(self):
        lpInfo = self.__caps

        return (
            lpInfo | ADL_DISPLAY_ADJUST_VERT_SIZE == lpInfo or
            lpInfo | ADL_DISPLAY_ADJUST_SIZEPOS == lpInfo
        )

    @property
    def is_horizontal_size_supported(self):
        lpInfo = self.__caps

        return (
            lpInfo | ADL_DISPLAY_ADJUST_HOR_SIZE == lpInfo or
            lpInfo | ADL_DISPLAY_ADJUST_SIZEPOS == lpInfo
        )

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
            res = _ADL2_Display_Size_Get(
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
            )
            return (
                lpWidth.value,
                lpHeight.value,
                lpDefaultWidth.value,
                lpDefaultHeight.value,
                lpMinWidth.value,
                lpMinHeight.value,
                lpMaxWidth.value,
                lpMaxHeight.value,
                lpStepWidth.value,
                lpStepHeight.value,
            )

    @property
    def width(self):
        if self.__width is None:
            size = self.__size

            lpWidth = size[0]
            lpDefaultWidth = size[2]
            lpMinWidth = size[4]
            lpMaxWidth = size[6]
            lpStepWidth = size[8]

            def _set_value(value):
                value -= value % lpStepWidth

                if value < lpMinWidth or value > lpMaxWidth:
                    return

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

                    return value

            class Value(object):
                default_value = lpDefaultWidth
                min_value = lpMinWidth
                max_value = lpMaxWidth
                step_value = lpStepWidth
                set_value = _set_value

            width = IntValueWrapper(lpWidth)
            width._obj = Value
            self.__width = width

        return self.__width

    @width.setter
    def width(self, value):
        width = self.width
        width += value - width.real

    @property
    def height(self):
        if self.__height is None:
            size = self.__size

            lpHeight = size[1]
            lpDefaultHeight = size[3]
            lpMinHeight = size[5]
            lpMaxHeight = size[7]
            lpStepHeight = size[9]

            def _set_value(value):
                value -= value % lpStepHeight

                if value < lpMinHeight or value > lpMaxHeight:
                    return

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

                    return value

            class Value(object):
                default_value = lpDefaultHeight
                min_value = lpMinHeight
                max_value = lpMaxHeight
                step_value = lpStepHeight
                set_value = _set_value

            height = IntValueWrapper(lpHeight)
            height._obj = Value
            self.__height = height

        return self.__height

    @height.setter
    def height(self, value):
        height = self.height
        height += value - height.real

    def __iter__(self):
        yield self.width
        yield self.height


class FreeSync(object):

    def __init__(self, adapter_index, display_index):
        self._adapter_index = adapter_index
        self._display_index = display_index


    @property
    def _freesync(self):
        lpCurrent = INT()
        lpDefault = INT()
        lpMinRefreshRateInMicroHz = INT()
        lpMaxRefreshRateInMicroHz = INT()

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_FreeSyncState_Get(
                context,
                iAdapterIndex,
                iDisplayIndex,
                ctypes.byref(lpCurrent),
                ctypes.byref(lpDefault),
                ctypes.byref(lpMinRefreshRateInMicroHz),
                ctypes.byref(lpMaxRefreshRateInMicroHz),
            )

            return (
                lpCurrent.value,
                lpDefault.value,
                lpMinRefreshRateInMicroHz.value,
                lpMaxRefreshRateInMicroHz.value
            )

    @property
    def min_refresh(self):
        return self._freesync[2]

    @property
    def max_refresh(self):
        return self._freesync[3]

    @property
    def default_mode(self):
        mapping = [
            ADL_FREESYNC_USECASE_STATIC,
            ADL_FREESYNC_USECASE_VIDEO,
            ADL_FREESYNC_USECASE_GAMING
        ]

        lpDefault = self._freesync[1]

        for item in mapping:
            if utils.get_bit(lpDefault, item):
                return item

    @property
    def mode(self):
        mapping = [
            ADL_FREESYNC_USECASE_STATIC,
            ADL_FREESYNC_USECASE_VIDEO,
            ADL_FREESYNC_USECASE_GAMING
        ]

        lpCurrent = self._freesync[0]

        for item in mapping:
            if utils.get_bit(lpCurrent, item):
                return item

    def set_mode(self, mode, refresh_rate):
        lpMinRefreshRateInMicroHz, lpMaxRefreshRateInMicroHz = self._freesync[-2:]

        if (
            refresh_rate < lpMinRefreshRateInMicroHz or
            refresh_rate > lpMaxRefreshRateInMicroHz
        ):
            return

        mapping = [
            ADL_FREESYNC_USECASE_STATIC,
            ADL_FREESYNC_USECASE_VIDEO,
            ADL_FREESYNC_USECASE_GAMING
        ]

        for item in mapping:
            if mode in (item, str(item)):
                break
        else:
            return

        iAdapterIndex = INT(self._adapter_index)
        iDisplayIndex = INT(self._display_index)
        iSetting = INT(item)
        iRefreshRateInMicroHz = INT(refresh_rate)

        with ADL2_Main_Control_Create as context:
            _ADL2_Display_FreeSyncState_Set(
                context,
                iAdapterIndex,
                iDisplayIndex,
                iSetting,
                iRefreshRateInMicroHz
            )