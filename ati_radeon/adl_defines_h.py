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
import ctypes
import sys


INT = ctypes.c_int
NULL = None
CHAR = ctypes.c_char
LONG = ctypes.c_long
FLOAT = ctypes.c_float
LONGLONG = ctypes.c_longlong
POINTER = ctypes.POINTER
SHORT = ctypes.c_short
WCHAR = ctypes.c_wchar
UINT = ctypes.c_uint
UCHAR = ctypes.c_ubyte
VOID = ctypes.c_void_p
ULONG = ctypes.c_ulong
ULONGLONG = ctypes.c_ulonglong
BOOL = ctypes.c_bool
USHORT = ctypes.c_ushort


try:
    long = long
except NameError:
    long = int


class EnumItem(long):

    def __init__(self, value):

        try:
            super(EnumItem, self).__init__(value)
        except TypeError:
            super(EnumItem, self).__init__()

        self._string = ''
        self._value = value

    def set_string(self, value):
        self._string = value
        return self

    def __eq__(self, other):
        if isinstance(other, (int, long)):
            if other == self._value:
                return True
            if str(other) in self._string:
                return True

            return False

        return other == self._string

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        if self._string:
            return self._string

        return super(EnumItem, self).__str__()


class Constant(int):

    def __init__(self, value):

        try:
            super(Constant, self).__init__(value)
        except TypeError:
            super(Constant, self).__init__()

        self._string = ''
        self._value = value

    def __repr__(self):
        if self._string:
            return repr(self._string)

        return int.__repr__(self)

    def set_string(self, value):
        self._string = value
        return self

    def __eq__(self, other):
        if isinstance(other, (int, long)):
            if other == self._value:
                return True
            if str(other) in self._string:
                return True

            return False

        return other == self._string

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        if self._string:
            return self._string

        return super(Constant, self).__str__()

    def __hash__(self):
        return int.__hash__(self)


class ENUM(INT):

    def __init__(self, value=None):

        if value is None:
            INT.__init__(self, 0)
        else:
            for k, v in self.__class__.__dict__.items():
                if k.startswith('_'):
                    continue

                if v == value:
                    value = v
                    break

            INT.__init__(self, value)

    @property
    def value(self):
        value = INT.value.__get__(self)
        for k, v in self.__class__.__dict__.items():
            if k.startswith('_'):
                continue

            if v == value:
                return v


def defined(macro):
    return macro


if sys.platform.startswith('win'):
    if ctypes.sizeof(ctypes.c_void_p) == 8:
        _WIN64 = True
        _WIN32 = False
    else:
        _WIN32 = True
        _WIN64 = False

    LINUX = False
else:
    LINUX = True
    _WIN32 = False
    _WIN64 = False


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
# / \file adl_defines.h
# / \brief Contains all definitions exposed by ADL for \ALL platforms.\n < b >
# Included in ADL SDK < /b >
# /
# / This file contains all definitions used by ADL.
# / The ADL definitions include the following:
# / \li ADL error codes
# / \li Enumerations for the ADLDisplayInfo structure
# / \li Maximum limits
# /

# / \defgroup DEFINES Constants and Definitions
# @{
# / \defgroup define_misc Miscellaneous Constant Definitions
# @{
# / \name General Definitions
# @{
# / Defines ADL_TRUE
ADL_TRUE = 1
# / Defines ADL_FALSE
ADL_FALSE = 0
# / Defines the maximum string length
ADL_MAX_CHAR = 4096
# / Defines the maximum string length
ADL_MAX_PATH = 256
# / Defines the maximum number of supported adapters
ADL_MAX_ADAPTERS = 250
# / Defines the maxumum number of supported displays
ADL_MAX_DISPLAYS = 150
# / Defines the maxumum string length for device name
ADL_MAX_DEVICENAME = 32
# / Defines for all adapters
ADL_ADAPTER_INDEX_ALL = -1
# / Defines APIs with iOption none
ADL_MAIN_API_OPTION_NONE = 0
# @}
# / \name Definitions for iOption parameter used by
# / ADL_Display_DDCBlockAccess_Get()
# @{
# / Switch to DDC line 2 before sending the command to the display.
ADL_DDC_OPTION_SWITCHDDC2 = 0x00000001
# / Save command in the registry under a unique key, corresponding to
# parameter \b iCommandIndex
ADL_DDC_OPTION_RESTORECOMMAND = 0x00000002
# / Combine write-read DDC block access command.
ADL_DDC_OPTION_COMBOWRITEREAD = 0x00000010
# / Direct DDC access to the immediate device connected to graphics card.
# / MST with this option set: DDC command is sent to first branch.
# / MST with this option not set: DDC command is sent to the end node sink
# device.
ADL_DDC_OPTION_SENDTOIMMEDIATEDEVICE = 0x00000020
# @}
# / \name Values for
# / ADLI2C.iAction used with ADL_Display_WriteAndReadI2C()
# @{
ADL_DL_I2C_ACTIONREAD = 0x00000001
ADL_DL_I2C_ACTIONWRITE = 0x00000002
ADL_DL_I2C_ACTIONREAD_REPEATEDSTART = 0x00000003
# @}
# @}  //Misc
# / \defgroup define_adl_results Result Codes
# / This group of definitions are the various results returned by all ADL
# functions \n
# @{
# / All OK, but need to wait
ADL_OK_WAIT = 4
# / All OK, but need restart
ADL_OK_RESTART = 3
# / All OK but need mode change
ADL_OK_MODE_CHANGE = 2
# / All OK, but with warning
ADL_OK_WARNING = 1
# / ADL function completed successfully
ADL_OK = 0
# / Generic Error. Most likely one or more of the Escape calls to the
# driver failednot
ADL_ERR = -1
# / ADL not initialized
ADL_ERR_NOT_INIT = -2
# / One of the parameter passed is invalid
ADL_ERR_INVALID_PARAM = -3
# / One of the parameter size is invalid
ADL_ERR_INVALID_PARAM_SIZE = -4
# / Invalid ADL index passed
ADL_ERR_INVALID_ADL_IDX = -5
# / Invalid controller index passed
ADL_ERR_INVALID_CONTROLLER_IDX = -6
# / Invalid display index passed
ADL_ERR_INVALID_DIPLAY_IDX = -7
# / Function not supported by the driver
ADL_ERR_NOT_SUPPORTED = -8
# / Null Pointer error
ADL_ERR_NULL_POINTER = -9
# / Call can't be made due to disabled adapter
ADL_ERR_DISABLED_ADAPTER = -10
# / Invalid Callback
ADL_ERR_INVALID_CALLBACK = -11
# / Display Resource conflict
ADL_ERR_RESOURCE_CONFLICT = -12
# Failed to update some of the values. Can be returned by set request that
# include multiple values if not all values were successfully committed.
ADL_ERR_SET_INCOMPLETE = -20
# / There's no Linux XDisplay in Linux Console environment
ADL_ERR_NO_XDISPLAY = -21
# @}
# / < /A >
# / \defgroup define_display_type Display Type
# / Define Monitor/CRT display type
# @{
# / Define Monitor display type
ADL_DT_MONITOR = Constant(0).set_string('Monitor')
# / Define TV display type
ADL_DT_TELEVISION = Constant(1).set_string('Television')
# / Define LCD display type
ADL_DT_LCD_PANEL = Constant(2).set_string('LCD Panel')
# / Define DFP display type
ADL_DT_DIGITAL_FLAT_PANEL = Constant(3).set_string('Digital Flat Panel')
# / Define Componment Video display type
ADL_DT_COMPONENT_VIDEO = Constant(4).set_string('Component Video')
# / Define Projector display type
ADL_DT_PROJECTOR = Constant(5).set_string('Projector')
# @}
# / \defgroup define_display_connection_type Display Connection Type
# @{
# / Define unknown display output type
ADL_DOT_UNKNOWN = Constant(0).set_string('Unknown')
# / Define composite display output type
ADL_DOT_COMPOSITE = Constant(1).set_string('Composite')
# / Define SVideo display output type
ADL_DOT_SVIDEO = Constant(2).set_string('SVideo')
# / Define analog display output type
ADL_DOT_ANALOG = Constant(3).set_string('Analog')
# / Define digital display output type
ADL_DOT_DIGITAL = Constant(4).set_string('Digital')
# @}
# / \defgroup define_color_type Display Color Type and Source
# / Define Display Color Type and Source
# @{
ADL_DISPLAY_COLOR_BRIGHTNESS = 1 << 0
ADL_DISPLAY_COLOR_CONTRAST = 1 << 1
ADL_DISPLAY_COLOR_SATURATION = 1 << 2
ADL_DISPLAY_COLOR_HUE = 1 << 3
ADL_DISPLAY_COLOR_TEMPERATURE = 1 << 4
# / Color Temperature Source is EDID
ADL_DISPLAY_COLOR_TEMPERATURE_SOURCE_EDID = 1 << 5
# / Color Temperature Source is User
ADL_DISPLAY_COLOR_TEMPERATURE_SOURCE_USER = 1 << 6
# @}
# / \defgroup define_adjustment_capabilities Display Adjustment
# Capabilities
# / Display adjustment capabilities values. Returned by
# ADL_Display_AdjustCaps_Get
# @{
ADL_DISPLAY_ADJUST_OVERSCAN = 1 << 0
ADL_DISPLAY_ADJUST_VERT_POS = 1 << 1
ADL_DISPLAY_ADJUST_HOR_POS = 1 << 2
ADL_DISPLAY_ADJUST_VERT_SIZE = 1 << 3
ADL_DISPLAY_ADJUST_HOR_SIZE = 1 << 4
ADL_DISPLAY_ADJUST_SIZEPOS = (
    ADL_DISPLAY_ADJUST_VERT_POS | 
    ADL_DISPLAY_ADJUST_HOR_POS | 
    ADL_DISPLAY_ADJUST_VERT_SIZE | 
    ADL_DISPLAY_ADJUST_HOR_SIZE
)
ADL_DISPLAY_CUSTOMMODES = 1 << 5
ADL_DISPLAY_ADJUST_UNDERSCAN = 1 << 6
# @}
# /Down-scale support
ADL_DISPLAY_CAPS_DOWNSCALE = 1 << 0
# / Sharpness support
ADL_DISPLAY_CAPS_SHARPNESS = 1 << 0
# / \defgroup define_desktop_config Desktop Configuration Flags
# / These flags are used by ADL_DesktopConfig_xxx
# / \deprecated This API has been deprecated because it was only used for
# RandR 1.1 (Red Hat 5.x) distributions which is now not supported.
# @{
# UNKNOWN desktop config
ADL_DESKTOPCONFIG_UNKNOWN = 0
# Single
ADL_DESKTOPCONFIG_SINGLE = 1 << 0
# Clone
ADL_DESKTOPCONFIG_CLONE = 1 << 2
# Big Desktop Horizontal
ADL_DESKTOPCONFIG_BIGDESK_H = 1 << 4
# Big Desktop Vertical
ADL_DESKTOPCONFIG_BIGDESK_V = 1 << 5
# Big Desktop Reverse Horz
ADL_DESKTOPCONFIG_BIGDESK_HR = 1 << 6
# Big Desktop Reverse Vert
ADL_DESKTOPCONFIG_BIGDESK_VR = 1 << 7
# RandR 1.2 Multi-display
ADL_DESKTOPCONFIG_RANDR12 = 1 << 8
# @}
# / needed for ADLDDCInfo structure
ADL_MAX_DISPLAY_NAME = 256
# / \defgroup define_edid_flags Values for ulDDCInfoFlag
# / defines for ulDDCInfoFlag EDID flag
# @{
ADL_DISPLAYDDCINFOEX_FLAG_PROJECTORDEVICE = 1 << 0
ADL_DISPLAYDDCINFOEX_FLAG_EDIDEXTENSION = 1 << 1
ADL_DISPLAYDDCINFOEX_FLAG_DIGITALDEVICE = 1 << 2
ADL_DISPLAYDDCINFOEX_FLAG_HDMIAUDIODEVICE = 1 << 3
ADL_DISPLAYDDCINFOEX_FLAG_SUPPORTS_AI = 1 << 4
ADL_DISPLAYDDCINFOEX_FLAG_SUPPORT_xvYCC601 = 1 << 5
ADL_DISPLAYDDCINFOEX_FLAG_SUPPORT_xvYCC709 = 1 << 6
# @}
# / \defgroup define_displayinfo_connector Display Connector Type
# / defines for ADLDisplayInfo.iDisplayConnector
# @{
ADL_DISPLAY_CONTYPE_UNKNOWN = Constant(0).set_string('Unknown')
ADL_DISPLAY_CONTYPE_VGA = Constant(1).set_string('VDA')
ADL_DISPLAY_CONTYPE_DVI_D = Constant(2).set_string('DVI-D')
ADL_DISPLAY_CONTYPE_DVI_I = Constant(3).set_string('DVI-I')
ADL_DISPLAY_CONTYPE_ATICVDONGLE_NTSC = Constant(4).set_string('NTSC I2C Dongle')
ADL_DISPLAY_CONTYPE_ATICVDONGLE_JPN = Constant(5).set_string('JPN I2C Dongle')
ADL_DISPLAY_CONTYPE_ATICVDONGLE_NONI2C_JPN = Constant(6).set_string('JPN Dongle')
ADL_DISPLAY_CONTYPE_ATICVDONGLE_NONI2C_NTSC = Constant(7).set_string('NTSC Dongle')
ADL_DISPLAY_CONTYPE_PROPRIETARY = Constant(8).set_string('Proprietary')
ADL_DISPLAY_CONTYPE_HDMI_TYPE_A = Constant(10).set_string('HDMI (type a)')
ADL_DISPLAY_CONTYPE_HDMI_TYPE_B = Constant(11).set_string('HDMI (type b)')
ADL_DISPLAY_CONTYPE_SVIDEO = Constant(12).set_string('SVideo')
ADL_DISPLAY_CONTYPE_COMPOSITE = Constant(13).set_string('Composite')
ADL_DISPLAY_CONTYPE_RCA_3COMPONENT = Constant(14).set_string('Component')
ADL_DISPLAY_CONTYPE_DISPLAYPORT = Constant(15).set_string('DisplayPort')
ADL_DISPLAY_CONTYPE_EDP = Constant(16).set_string('EDP')
ADL_DISPLAY_CONTYPE_WIRELESSDISPLAY = Constant(17).set_string('Wireless')
# @}
# / TV Capabilities and Standards
# / \defgroup define_tv_caps TV Capabilities and Standards
# / \deprecated Dropping support for TV displays
# @{
ADL_TV_STANDARDS = 1 << 0
ADL_TV_SCART = 1 << 1
# / TV Standards Definitions
ADL_STANDARD_NTSC_M = 1 << 0
ADL_STANDARD_NTSC_JPN = 1 << 1
ADL_STANDARD_NTSC_N = 1 << 2
ADL_STANDARD_PAL_B = 1 << 3
ADL_STANDARD_PAL_COMB_N = 1 << 4
ADL_STANDARD_PAL_D = 1 << 5
ADL_STANDARD_PAL_G = 1 << 6
ADL_STANDARD_PAL_H = 1 << 7
ADL_STANDARD_PAL_I = 1 << 8
ADL_STANDARD_PAL_K = 1 << 9
ADL_STANDARD_PAL_K1 = 1 << 10
ADL_STANDARD_PAL_L = 1 << 11
ADL_STANDARD_PAL_M = 1 << 12
ADL_STANDARD_PAL_N = 1 << 13
ADL_STANDARD_PAL_SECAM_D = 1 << 14
ADL_STANDARD_PAL_SECAM_K = 1 << 15
ADL_STANDARD_PAL_SECAM_K1 = 1 << 16
ADL_STANDARD_PAL_SECAM_L = 1 << 17
# @}
# / \defgroup define_video_custom_mode Video Custom Mode flags
# / Component Video Custom Mode flags. This is used by the iFlags
# parameter in ADLCustomMode
# @{
ADL_CUSTOMIZEDMODEFLAG_MODESUPPORTED = 1 << 0
ADL_CUSTOMIZEDMODEFLAG_NOTDELETETABLE = 1 << 1
ADL_CUSTOMIZEDMODEFLAG_INSERTBYDRIVER = 1 << 2
ADL_CUSTOMIZEDMODEFLAG_INTERLACED = 1 << 3
ADL_CUSTOMIZEDMODEFLAG_BASEMODE = 1 << 4
# @}
# / \defgroup define_cv_dongle Values used by ADL_CV_DongleSettings_xxx
# / The following is applicable to ADL_DISPLAY_CONTYPE_ATICVDONGLE_JP and
# ADL_DISPLAY_CONTYPE_ATICVDONGLE_NONI2C_D only
# / \deprecated Dropping support for Component Video displays
# @{
ADL_DISPLAY_CV_DONGLE_D1 = 1 << 0
ADL_DISPLAY_CV_DONGLE_D2 = 1 << 1
ADL_DISPLAY_CV_DONGLE_D3 = 1 << 2
ADL_DISPLAY_CV_DONGLE_D4 = 1 << 3
ADL_DISPLAY_CV_DONGLE_D5 = 1 << 4
# / The following is applicable to ADL_DISPLAY_CONTYPE_ATICVDONGLE_NA and
# ADL_DISPLAY_CONTYPE_ATICVDONGLE_NONI2C only
ADL_DISPLAY_CV_DONGLE_480I = 1 << 0
ADL_DISPLAY_CV_DONGLE_480P = 1 << 1
ADL_DISPLAY_CV_DONGLE_540P = 1 << 2
ADL_DISPLAY_CV_DONGLE_720P = 1 << 3
ADL_DISPLAY_CV_DONGLE_1080I = 1 << 4
ADL_DISPLAY_CV_DONGLE_1080P = 1 << 5
ADL_DISPLAY_CV_DONGLE_16_9 = 1 << 6
ADL_DISPLAY_CV_DONGLE_720P50 = 1 << 7
ADL_DISPLAY_CV_DONGLE_1080I25 = 1 << 8
ADL_DISPLAY_CV_DONGLE_576I25 = 1 << 9
ADL_DISPLAY_CV_DONGLE_576P50 = 1 << 10
ADL_DISPLAY_CV_DONGLE_1080P24 = 1 << 11
ADL_DISPLAY_CV_DONGLE_1080P25 = 1 << 12
ADL_DISPLAY_CV_DONGLE_1080P30 = 1 << 13
ADL_DISPLAY_CV_DONGLE_1080P50 = 1 << 14
# @}
# / \defgroup define_formats_ovr Formats Override Settings
# / Display force modes flags
# @{
# /

ADL_DISPLAY_FORMAT_FORCE_720P = Constant(0x00000001).set_string('720p')
ADL_DISPLAY_FORMAT_FORCE_1080I = Constant(0x00000002).set_string('1080i')
ADL_DISPLAY_FORMAT_FORCE_1080P = Constant(0x00000004).set_string('1080p')
ADL_DISPLAY_FORMAT_FORCE_720P50 = Constant(0x00000008).set_string('720p 50Hz')
ADL_DISPLAY_FORMAT_FORCE_1080I25 = Constant(0x00000010).set_string('1080i 25Hz')
ADL_DISPLAY_FORMAT_FORCE_576I25 = Constant(0x00000020).set_string('576i 25Hz')
ADL_DISPLAY_FORMAT_FORCE_576P50 = Constant(0x00000040).set_string('576p 50Hz')
ADL_DISPLAY_FORMAT_FORCE_1080P24 = Constant(0x00000080).set_string('1080p 24Hz')
ADL_DISPLAY_FORMAT_FORCE_1080P25 = Constant(0x00000100).set_string('1080p 25Hz')
ADL_DISPLAY_FORMAT_FORCE_1080P30 = Constant(0x00000200).set_string('1080p 30Hz')
ADL_DISPLAY_FORMAT_FORCE_1080P50 = Constant(0x00000400).set_string('1080p 50Hz')
# / < Below are \b EXTENDED display mode flags
ADL_DISPLAY_FORMAT_CVDONGLEOVERIDE = Constant(0x00000001).set_string('CV Dongle Override')
ADL_DISPLAY_FORMAT_CVMODEUNDERSCAN = Constant(0x00000002).set_string('CV Mode Underscan')
ADL_DISPLAY_FORMAT_FORCECONNECT_SUPPORTED = Constant(0x00000004).set_string('Force Connect Supported')
ADL_DISPLAY_FORMAT_RESTRICT_FORMAT_SELECTION = Constant(0x00000008).set_string('Restrict Format Selection')
ADL_DISPLAY_FORMAT_SETASPECRATIO = Constant(0x00000010).set_string('Set Aspect Ratio')
ADL_DISPLAY_FORMAT_FORCEMODES = Constant(0x00000020).set_string('Force Modes')
ADL_DISPLAY_FORMAT_LCDRTCCOEFF = Constant(0x00000040).set_string('LCD RTC Coefficient')
# @}
# / Defines used by OD5
ADL_PM_PARAM_DONT_CHANGE = 0
# / The following defines Bus types
# @{
# PCI bus
ADL_BUSTYPE_PCI = Constant(0).set_string('PCI')
# AGP bus
ADL_BUSTYPE_AGP = Constant(1).set_string('AGP')
# PCI Express bus
ADL_BUSTYPE_PCIE = Constant(2).set_string('PCIe')
# PCI Express 2nd generation bus
ADL_BUSTYPE_PCIE_GEN2 = Constant(3).set_string('PCIe Gen2')
# PCI Express 3rd generation bus
ADL_BUSTYPE_PCIE_GEN3 = Constant(4).set_string('PCIe Gen3')
# @}
# / \defgroup define_ws_caps Workstation Capabilities
# / Workstation values
# @{
# / This value indicates that the workstation card supports active stereo
# though stereo output connector
ADL_STEREO_SUPPORTED = Constant(1 << 2).set_string('Stereo Supported')
# though stereo output connector")
# / This value indicates that the workstation card supports active stereo
# via "blue-line"
ADL_STEREO_BLUE_LINE = Constant(1 << 3).set_string('Stereo Blue Line')
# / This value is used to turn off stereo mode.
ADL_STEREO_OFF = Constant(0).set_string('Stereo Off')
# / This value indicates that the workstation card supports active stereo.
# This is also used to set the stereo mode to active though the stereo
# output connector
ADL_STEREO_ACTIVE = Constant(1 << 1).set_string('Stereo Active')
# / This value indicates that the workstation card supports auto-stereo
# monitors with horizontal interleave. This is also used to set the stereo
# mode to use the auto-stereo monitor with horizontal interleave
ADL_STEREO_AUTO_HORIZONTAL = Constant(1 << 30).set_string('Stereo Auto Horizontal')
# / This value indicates that the workstation card supports auto-stereo
# monitors with vertical interleave. This is also used to set the stereo
# mode to use the auto-stereo monitor with vertical interleave
ADL_STEREO_AUTO_VERTICAL = Constant(1 << 31).set_string('Stereo Auto Vertical')
# / This value indicates that the workstation card supports passive
# stereo, ie. non stereo sync
ADL_STEREO_PASSIVE = Constant(1 << 6).set_string('Stereo Passive')
# / This value indicates that the workstation card supports auto-stereo
# monitors with vertical interleave. This is also used to set the stereo
# mode to use the auto-stereo monitor with vertical interleave
ADL_STEREO_PASSIVE_HORIZ = Constant(1 << 7).set_string('Stereo Passive Horizontal')
# / This value indicates that the workstation card supports auto-stereo
# monitors with vertical interleave. This is also used to set the stereo
# mode to use the auto-stereo monitor with vertical interleave
ADL_STEREO_PASSIVE_VERT = Constant(1 << 8).set_string('Stereo Passive Vertical')
# / This value indicates that the workstation card supports auto-stereo
# monitors with Samsung.
ADL_STEREO_AUTO_SAMSUNG = Constant(1 << 11).set_string('Stereo Auto Samsung')
# / This value indicates that the workstation card supports auto-stereo
# monitors with Tridility.
ADL_STEREO_AUTO_TSL = Constant(1 << 12).set_string('Auto Tridility')
# / This value indicates that the workstation card supports DeepBitDepth
# (10 bpp)
ADL_DEEPBITDEPTH_10BPP_SUPPORTED = 1 << 5
# / This value indicates that the workstation supports 8-Bit Grayscale
ADL_8BIT_GREYSCALE_SUPPORTED = 1 << 9
# / This value indicates that the workstation supports CUSTOM TIMING
ADL_CUSTOM_TIMING_SUPPORTED = 1 << 10
# / Load balancing is supported.
ADL_WORKSTATION_LOADBALANCING_SUPPORTED = 0x00000001
# / Load balancing is available.
ADL_WORKSTATION_LOADBALANCING_AVAILABLE = 0x00000002
# / Load balancing is disabled.
ADL_WORKSTATION_LOADBALANCING_DISABLED = 0x00000000
# / Load balancing is Enabled.
ADL_WORKSTATION_LOADBALANCING_ENABLED = 0x00000001
# @}
# / \defgroup define_adapterspeed speed setting from the adapter
# @{
# default asic running speed
ADL_CONTEXT_SPEED_UNFORCED = Constant(0).set_string('Unforced')
# asic running speed is forced to high
ADL_CONTEXT_SPEED_FORCEHIGH = Constant(1).set_string('Force High')
# asic running speed is forced to low
ADL_CONTEXT_SPEED_FORCELOW = Constant(2).set_string('Force Low')
# change asic running speed setting is supported
ADL_ADAPTER_SPEEDCAPS_SUPPORTED = Constant(1 << 0).set_string('Supported')
# @}
# / \defgroup define_glsync Genlock related values
# / GL-Sync port types (unique values)
# @{
# / Unknown port of GL-Sync module
ADL_GLSYNC_PORT_UNKNOWN = 0
# / BNC port of of GL-Sync module
ADL_GLSYNC_PORT_BNC = 1
# / RJ45(1) port of of GL-Sync module
ADL_GLSYNC_PORT_RJ45PORT1 = 2
# / RJ45(2) port of of GL-Sync module
ADL_GLSYNC_PORT_RJ45PORT2 = 3
# GL-Sync Genlock settings mask (bit-vector)
# / None of the ADLGLSyncGenlockConfig members are valid
ADL_GLSYNC_CONFIGMASK_NONE = 0
# / The ADLGLSyncGenlockConfig.lSignalSource member is valid
ADL_GLSYNC_CONFIGMASK_SIGNALSOURCE = 1 << 0
# / The ADLGLSyncGenlockConfig.iSyncField member is valid
ADL_GLSYNC_CONFIGMASK_SYNCFIELD = 1 << 1
# / The ADLGLSyncGenlockConfig.iSampleRate member is valid
ADL_GLSYNC_CONFIGMASK_SAMPLERATE = 1 << 2
# / The ADLGLSyncGenlockConfig.lSyncDelay member is valid
ADL_GLSYNC_CONFIGMASK_SYNCDELAY = 1 << 3
# / The ADLGLSyncGenlockConfig.iTriggerEdge member is valid
ADL_GLSYNC_CONFIGMASK_TRIGGEREDGE = 1 << 4
# / The ADLGLSyncGenlockConfig.iScanRateCoeff member is valid
ADL_GLSYNC_CONFIGMASK_SCANRATECOEFF = 1 << 5
# / The ADLGLSyncGenlockConfig.lFramelockCntlVector member is valid
ADL_GLSYNC_CONFIGMASK_FRAMELOCKCNTL = 1 << 6
# GL-Sync Framelock control mask (bit-vector)
# / Framelock is disabled
ADL_GLSYNC_FRAMELOCKCNTL_NONE = 0
# / Framelock is enabled
ADL_GLSYNC_FRAMELOCKCNTL_ENABLE = 1 << 0
ADL_GLSYNC_FRAMELOCKCNTL_DISABLE = 1 << 1
ADL_GLSYNC_FRAMELOCKCNTL_SWAP_COUNTER_RESET = 1 << 2
ADL_GLSYNC_FRAMELOCKCNTL_SWAP_COUNTER_ACK = 1 << 3
ADL_GLSYNC_FRAMELOCKCNTL_VERSION_KMD = 1 << 4
ADL_GLSYNC_FRAMELOCKCNTL_STATE_ENABLE = 1 << 0
ADL_GLSYNC_FRAMELOCKCNTL_STATE_KMD = 1 << 4
# GL-Sync Framelock counters mask (bit-vector)
ADL_GLSYNC_COUNTER_SWAP = 1 << 0
# GL-Sync Signal Sources (unique values)
# / GL-Sync signal source is undefined
ADL_GLSYNC_SIGNALSOURCE_UNDEFINED = 0x00000100
# / GL-Sync signal source is Free Run
ADL_GLSYNC_SIGNALSOURCE_FREERUN = 0x00000101
# / GL-Sync signal source is the BNC GL-Sync port
ADL_GLSYNC_SIGNALSOURCE_BNCPORT = 0x00000102
# / GL-Sync signal source is the RJ45(1) GL-Sync port
ADL_GLSYNC_SIGNALSOURCE_RJ45PORT1 = 0x00000103
# / GL-Sync signal source is the RJ45(2) GL-Sync port
ADL_GLSYNC_SIGNALSOURCE_RJ45PORT2 = 0x00000104
# GL-Sync Signal Types (unique values)
# / GL-Sync signal type is unknown
ADL_GLSYNC_SIGNALTYPE_UNDEFINED = 0
# / GL-Sync signal type is 480I
ADL_GLSYNC_SIGNALTYPE_480I = 1
# / GL-Sync signal type is 576I
ADL_GLSYNC_SIGNALTYPE_576I = 2
# / GL-Sync signal type is 480P
ADL_GLSYNC_SIGNALTYPE_480P = 3
# / GL-Sync signal type is 576P
ADL_GLSYNC_SIGNALTYPE_576P = 4
# / GL-Sync signal type is 720P
ADL_GLSYNC_SIGNALTYPE_720P = 5
# / GL-Sync signal type is 1080P
ADL_GLSYNC_SIGNALTYPE_1080P = 6
# / GL-Sync signal type is 1080I
ADL_GLSYNC_SIGNALTYPE_1080I = 7
# / GL-Sync signal type is SDI
ADL_GLSYNC_SIGNALTYPE_SDI = 8
# / GL-Sync signal type is TTL
ADL_GLSYNC_SIGNALTYPE_TTL = 9
# / GL_Sync signal type is Analog
ADL_GLSYNC_SIGNALTYPE_ANALOG = 10
# GL-Sync Sync Field options (unique values)
# /GL-Sync sync field option is undefined
ADL_GLSYNC_SYNCFIELD_UNDEFINED = 0
# /GL-Sync sync field option is Sync to Field 1
# (used for Interlaced signal types)
ADL_GLSYNC_SYNCFIELD_BOTH = 1
# /GL-Sync sync field option is Sync to Both fields
# (used for Interlaced signal types)
ADL_GLSYNC_SYNCFIELD_1 = 2
# GL-Sync trigger edge options (unique values)
# / GL-Sync trigger edge is undefined
ADL_GLSYNC_TRIGGEREDGE_UNDEFINED = 0
# / GL-Sync trigger edge is the rising edge
ADL_GLSYNC_TRIGGEREDGE_RISING = 1
# / GL-Sync trigger edge is the falling edge
ADL_GLSYNC_TRIGGEREDGE_FALLING = 2
# / GL-Sync trigger edge is both the rising and the falling edge
ADL_GLSYNC_TRIGGEREDGE_BOTH = 3
# GL-Sync scan rate coefficient/multiplier options (unique values)
# / GL-Sync scan rate coefficient/multiplier is undefined
ADL_GLSYNC_SCANRATECOEFF_UNDEFINED = 0
# / GL-Sync scan rate coefficient/multiplier is 5
ADL_GLSYNC_SCANRATECOEFF_x5 = 1
# / GL-Sync scan rate coefficient/multiplier is 4
ADL_GLSYNC_SCANRATECOEFF_x4 = 2
# / GL-Sync scan rate coefficient/multiplier is 3
ADL_GLSYNC_SCANRATECOEFF_x3 = 3
# / GL-Sync scan rate coefficient/multiplier is 5:2 (SMPTE)
ADL_GLSYNC_SCANRATECOEFF_x5_DIV_2 = 4
# / GL-Sync scan rate coefficient/multiplier is 2
ADL_GLSYNC_SCANRATECOEFF_x2 = 5
# / GL-Sync scan rate coefficient/multiplier is 3 : 2
ADL_GLSYNC_SCANRATECOEFF_x3_DIV_2 = 6
# / GL-Sync scan rate coefficient/multiplier is 5 : 4
ADL_GLSYNC_SCANRATECOEFF_x5_DIV_4 = 7
# / GL-Sync scan rate coefficient/multiplier is 1 (default)
ADL_GLSYNC_SCANRATECOEFF_x1 = 8
# / GL-Sync scan rate coefficient/multiplier is 4 : 5
ADL_GLSYNC_SCANRATECOEFF_x4_DIV_5 = 9
# / GL-Sync scan rate coefficient/multiplier is 2 : 3
ADL_GLSYNC_SCANRATECOEFF_x2_DIV_3 = 10
# / GL-Sync scan rate coefficient/multiplier is 1 : 2
ADL_GLSYNC_SCANRATECOEFF_x1_DIV_2 = 11
# / GL-Sync scan rate coefficient/multiplier is 2 : 5 (SMPTE)
ADL_GLSYNC_SCANRATECOEFF_x2_DIV_5 = 12
# / GL-Sync scan rate coefficient/multiplier is 1 : 3
ADL_GLSYNC_SCANRATECOEFF_x1_DIV_3 = 13
# / GL-Sync scan rate coefficient/multiplier is 1 : 4
ADL_GLSYNC_SCANRATECOEFF_x1_DIV_4 = 14
# / GL-Sync scan rate coefficient/multiplier is 1 : 5
ADL_GLSYNC_SCANRATECOEFF_x1_DIV_5 = 15
# GL-Sync port (signal presence) states (unique values)
# / GL-Sync port state is undefined
ADL_GLSYNC_PORTSTATE_UNDEFINED = 0
# / GL-Sync port is not connected
ADL_GLSYNC_PORTSTATE_NOCABLE = 1
# / GL-Sync port is Idle
ADL_GLSYNC_PORTSTATE_IDLE = 2
# / GL-Sync port has an Input signal
ADL_GLSYNC_PORTSTATE_INPUT = 3
# / GL-Sync port is Output
ADL_GLSYNC_PORTSTATE_OUTPUT = 4
# GL-Sync LED types
# (used index within ADL_Workstation_GLSyncPortState_Get returned ppGlSyncLEDs array) (unique values)
# 
# / Index into the ADL_Workstation_GLSyncPortState_Get returned
# ppGlSyncLEDs array for the one LED of the BNC port
ADL_GLSYNC_LEDTYPE_BNC = 0
# / Index into the ADL_Workstation_GLSyncPortState_Get returned
# ppGlSyncLEDs array for the Left LED of the RJ45(1) or RJ45(2) port
ADL_GLSYNC_LEDTYPE_RJ45_LEFT = 0
# / Index into the ADL_Workstation_GLSyncPortState_Get returned
# ppGlSyncLEDs array for the Right LED of the RJ45(1) or RJ45(2) port
ADL_GLSYNC_LEDTYPE_RJ45_RIGHT = 1
# GL-Sync LED colors (unique values)
# / GL-Sync LED undefined color
ADL_GLSYNC_LEDCOLOR_UNDEFINED = 0
# / GL-Sync LED is unlit
ADL_GLSYNC_LEDCOLOR_NOLIGHT = 1
# / GL-Sync LED is yellow
ADL_GLSYNC_LEDCOLOR_YELLOW = 2
# / GL-Sync LED is red
ADL_GLSYNC_LEDCOLOR_RED = 3
# / GL-Sync LED is green
ADL_GLSYNC_LEDCOLOR_GREEN = 4
# / GL-Sync LED is flashing green
ADL_GLSYNC_LEDCOLOR_FLASH_GREEN = 5
# GL-Sync Port Control (refers one GL-Sync Port) (unique values)
# / Used to configure the RJ54(1) or RJ42(2) port of GL-Sync is as Idle
ADL_GLSYNC_PORTCNTL_NONE = 0x00000000
# / Used to configure the RJ54(1) or RJ42(2) port of GL-Sync is as Output
ADL_GLSYNC_PORTCNTL_OUTPUT = 0x00000001
# GL-Sync Mode Control (refers one Display/Controller) (bitfields)
# / Used to configure the display to use internal timing (not genlocked)
ADL_GLSYNC_MODECNTL_NONE = 0x00000000
# / Bitfield used to configure the display as genlocked
# (either as Timing Client or as Timing Server)
ADL_GLSYNC_MODECNTL_GENLOCK = 0x00000001
# / Bitfield used to configure the display as Timing Server
ADL_GLSYNC_MODECNTL_TIMINGSERVER = 0x00000002
# GL-Sync Mode Status
# / Display is currently not genlocked
ADL_GLSYNC_MODECNTL_STATUS_NONE = 0x00000000
# / Display is currently genlocked
ADL_GLSYNC_MODECNTL_STATUS_GENLOCK = 0x00000001
# / Display requires a mode switch
ADL_GLSYNC_MODECNTL_STATUS_SETMODE_REQUIRED = 0x00000002
# / Display is capable of being genlocked
ADL_GLSYNC_MODECNTL_STATUS_GENLOCK_ALLOWED = 0x00000004
ADL_MAX_GLSYNC_PORTS = 8
ADL_MAX_GLSYNC_PORT_LEDS = 8
# @}
# / \defgroup define_crossfirestate CrossfireX state of a particular
# adapter CrossfireX combination
# @{
# Dongle / cable is missing
ADL_XFIREX_STATE_NOINTERCONNECT = Constant(1 << 0).set_string('No Interconnect')
# CrossfireX can be enabled if pipes are downgraded
ADL_XFIREX_STATE_DOWNGRADEPIPES = Constant(1 << 1).set_string('CrossfireX can be enabled if pipes are downgraded')
# CrossfireX cannot be enabled unless mem downgraded
ADL_XFIREX_STATE_DOWNGRADEMEM = Constant(1 << 2).set_string('CrossfireX cannot be enabled unless memory is downgraded')
# Card reversal recommended, CrossfireX cannot be enabled.
ADL_XFIREX_STATE_REVERSERECOMMENDED = Constant(1 << 3).set_string('CrossfireX cannot be enabled, card reversal recommended')
# 3D client is active - CrossfireX cannot be safely enabled
ADL_XFIREX_STATE_3DACTIVE = Constant(1 << 4).set_string('CrossfireX cannot be safely enabled, 3D client is active')
# Dongle is OK but master is on slave
ADL_XFIREX_STATE_MASTERONSLAVE = Constant(1 << 5).set_string('Dongle is OK but master is on slave')
# No (valid) display connected to master card.
ADL_XFIREX_STATE_NODISPLAYCONNECT = Constant(1 << 6).set_string('No (valid) display connected to master card')
# CrossfireX is enabled but master is not current primary device
ADL_XFIREX_STATE_NOPRIMARYVIEW = Constant(1 << 7).set_string(' CrossfireX is enabled but master is not current primary device')
# CrossfireX cannot be enabled unless visible mem downgraded
ADL_XFIREX_STATE_DOWNGRADEVISMEM = Constant(1 << 8).set_string('CrossfireX cannot be enabled unless visible memmemory is downgraded')
# CrossfireX can be enabled however performance not optimal due to < 8
# lanes
ADL_XFIREX_STATE_LESSTHAN8LANE_MASTER = Constant(1 << 9).set_string('CrossfireX can be enabled however performance not optimal due to master having < 8 lanes')
# CrossfireX can be enabled however performance not optimal due to < 8
# lanes
ADL_XFIREX_STATE_LESSTHAN8LANE_SLAVE = Constant(1 << 10).set_string('CrossfireX can be enabled however performance not optimal due to slave having < 8 lanes')
# CrossfireX cannot be enabled due to failed peer to peer test
ADL_XFIREX_STATE_PEERTOPEERFAILED = Constant(1 << 11).set_string('CrossfireX cannot be enabled due to failed peer to peer test')
# Notification that memory is currently downgraded
ADL_XFIREX_STATE_MEMISDOWNGRADED = Constant(1 << 16).set_string('Notification that memory is currently downgraded')
# Notification that pipes are currently downgraded
ADL_XFIREX_STATE_PIPESDOWNGRADED = Constant(1 << 17).set_string('Notification that pipes are currently downgraded')
# CrossfireX is enabled on current device
ADL_XFIREX_STATE_XFIREXACTIVE = Constant(1 << 18).set_string('CrossfireX is enabled')
# Notification that visible FB memory is currently downgraded
ADL_XFIREX_STATE_VISMEMISDOWNGRADED = Constant(1 << 19).set_string('Notification that visible FB memory is currently downgraded')
# Cannot support current inter-connection configuration
ADL_XFIREX_STATE_INVALIDINTERCONNECTION = Constant(1 << 20).set_string('Cannot support current inter-connection configuration')
# CrossfireX will only work with clients supporting non P2P mode
ADL_XFIREX_STATE_NONP2PMODE = Constant(1 << 21).set_string('CrossfireX will only work with clients supporting non P2P mode')
# CrossfireX cannot be enabled unless memory banks downgraded
ADL_XFIREX_STATE_DOWNGRADEMEMBANKS = Constant(1 << 22).set_string('CrossfireX cannot be enabled unless memory banks downgraded')
# Notification that memory banks are currently downgraded
ADL_XFIREX_STATE_MEMBANKSDOWNGRADED = Constant(1 << 23).set_string('Notification that memory banks are currently downgraded')
# Extended desktop or clone mode is allowed.
ADL_XFIREX_STATE_DUALDISPLAYSALLOWED = Constant(1 << 24).set_string(' Extended desktop or clone mode is allowed.')
# P2P mapping was through peer aperture
ADL_XFIREX_STATE_P2P_APERTURE_MAPPING = Constant(1 << 25).set_string('P2P mapping was through peer aperture')
# For back compatible
ADL_XFIREX_STATE_P2PFLUSH_REQUIRED = ADL_XFIREX_STATE_P2P_APERTURE_MAPPING
# There is CrossfireX side port connection between GPUs
ADL_XFIREX_STATE_XSP_CONNECTED = Constant(1 << 26).set_string('There is CrossfireX side port connection between GPUs')
# System needs a reboot bofore enable CrossfireX
ADL_XFIREX_STATE_ENABLE_CF_REBOOT_REQUIRED = Constant(1 << 27).set_string('System needs a reboot bofore enable CrossfireX')
# System needs a reboot after disable CrossfireX
ADL_XFIREX_STATE_DISABLE_CF_REBOOT_REQUIRED = Constant(1 << 28).set_string('System needs a reboot after disable CrossfireX')
# Indicate base driver handles the downgrade key updating
ADL_XFIREX_STATE_DRV_HANDLE_DOWNGRADE_KEY = Constant(1 << 29).set_string('Indicate base driver handles the downgrade key updating')
# CrossfireX need to be reconfigured by CCC because of a LDA chain broken
ADL_XFIREX_STATE_CF_RECONFIG_REQUIRED = Constant(1 << 30).set_string(' CrossfireX need to be reconfigured by CCC because of a LDA chain broken')
# Could not obtain current status
ADL_XFIREX_STATE_ERRORGETTINGSTATUS = Constant(1 << 31).set_string('Could not obtain current status')
# @}
# /////////////////////////////////////////////////////////////////////////
# ADL_DISPLAY_ADJUSTMENT_PIXELFORMAT adjustment values
# (bit-vector)
# /////////////////////////////////////////////////////////////////////////
# / \defgroup define_pixel_formats Pixel Formats values
# / This group defines the various Pixel Formats that a particular digital
# display can support. \n
# / Since a display can support multiple formats, these values can be
# bit-or'ed to indicate the various formats \n
# @{

ADL_DISPLAY_PIXELFORMAT_UNKNOWN = Constant(0).set_string('Unknown')
ADL_DISPLAY_PIXELFORMAT_RGB = Constant(1 << 0).set_string('RGB Full Range')
# Limited range
ADL_DISPLAY_PIXELFORMAT_YCRCB444 = Constant(1 << 0).set_string('YCRCB444')
# Limited range
ADL_DISPLAY_PIXELFORMAT_YCRCB422 = Constant(1 << 0).set_string('YCRCB422')
ADL_DISPLAY_PIXELFORMAT_RGB_LIMITED_RANGE = Constant(1 << 0).set_string('RGB Limited Range')
# Full range
ADL_DISPLAY_PIXELFORMAT_RGB_FULL_RANGE = ADL_DISPLAY_PIXELFORMAT_RGB
ADL_DISPLAY_PIXELFORMAT_YCRCB420 = Constant(1 << 0).set_string('YCRCB420')
# @}
# / \defgroup define_contype Connector Type Values
# / ADLDisplayConfig.ulConnectorType defines
# @{
ADL_DL_DISPLAYCONFIG_CONTYPE_UNKNOWN = 0
ADL_DL_DISPLAYCONFIG_CONTYPE_CV_NONI2C_JP = 1
ADL_DL_DISPLAYCONFIG_CONTYPE_CV_JPN = 2
ADL_DL_DISPLAYCONFIG_CONTYPE_CV_NA = 3
ADL_DL_DISPLAYCONFIG_CONTYPE_CV_NONI2C_NA = 4
ADL_DL_DISPLAYCONFIG_CONTYPE_VGA = 5
ADL_DL_DISPLAYCONFIG_CONTYPE_DVI_D = 6
ADL_DL_DISPLAYCONFIG_CONTYPE_DVI_I = 7
ADL_DL_DISPLAYCONFIG_CONTYPE_HDMI_TYPE_A = 8
ADL_DL_DISPLAYCONFIG_CONTYPE_HDMI_TYPE_B = 9
ADL_DL_DISPLAYCONFIG_CONTYPE_DISPLAYPORT = 10
# @}
# /////////////////////////////////////////////////////////////////////////
# ADL_DISPLAY_DISPLAYINFO_ Definitions
# for ADLDisplayInfo.iDisplayInfoMask and ADLDisplayInfo.iDisplayInfoValue
# (bit-vector)
# /////////////////////////////////////////////////////////////////////////
# / \defgroup define_displayinfomask Display Info Mask Values
# @{
ADL_DISPLAY_DISPLAYINFO_DISPLAYCONNECTED = Constant(0x00000001).set_string('DISPLAYCONNECTED')
ADL_DISPLAY_DISPLAYINFO_DISPLAYMAPPED = Constant(0x00000002).set_string('DISPLAYMAPPED')
ADL_DISPLAY_DISPLAYINFO_NONLOCAL = Constant(0x00000004).set_string('NONLOCAL')
ADL_DISPLAY_DISPLAYINFO_FORCIBLESUPPORTED = Constant(0x00000008).set_string('FORCIBLESUPPORTED')
ADL_DISPLAY_DISPLAYINFO_GENLOCKSUPPORTED = Constant(0x00000010).set_string('GENLOCKSUPPORTED')
ADL_DISPLAY_DISPLAYINFO_MULTIVPU_SUPPORTED = Constant(0x00000020).set_string('MULTIVPU_SUPPORTED')
ADL_DISPLAY_DISPLAYINFO_LDA_DISPLAY = Constant(0x00000040).set_string('LDA_DISPLAY')
ADL_DISPLAY_DISPLAYINFO_MODETIMING_OVERRIDESSUPPORTED = Constant(0x00000080).set_string('MODETIMING_OVERRIDESSUPPORTED')
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_SINGLE = Constant(0x00000100).set_string('MANNER_SUPPORTED_SINGLE')
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_CLONE = Constant(0x00000200).set_string('MANNER_SUPPORTED_CLONE')
# / Legacy support for XP
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_2VSTRETCH = Constant(0x00000400).set_string('MANNER_SUPPORTED_2VSTRETCH')
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_2HSTRETCH = Constant(0x00000800).set_string('MANNER_SUPPORTED_2HSTRETCH')
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_EXTENDED = Constant(0x00001000).set_string('MANNER_SUPPORTED_EXTENDED')
# / More support manners
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_NSTRETCH1GPU = Constant(0x00010000).set_string('MANNER_SUPPORTED_NSTRETCH1GPU')
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_NSTRETCHNGPU = Constant(0x00020000).set_string('MANNER_SUPPORTED_NSTRETCHNGPU')
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_RESERVED2 = Constant(0x00040000).set_string('MANNER_SUPPORTED_RESERVED2')
ADL_DISPLAY_DISPLAYINFO_MANNER_SUPPORTED_RESERVED3 = Constant(0x00080000).set_string('MANNER_SUPPORTED_RESERVED3')
# / Projector display type
ADL_DISPLAY_DISPLAYINFO_SHOWTYPE_PROJECTOR = Constant(0x00100000).set_string('SHOWTYPE_PROJECTOR')
# @}
# /////////////////////////////////////////////////////////////////////////
# ADL_ADAPTER_DISPLAY_MANNER_SUPPORTED_ Definitions
# for ADLAdapterDisplayCap of ADL_Adapter_Display_Cap()
# (bit-vector)
# /////////////////////////////////////////////////////////////////////////
# / \defgroup define_adaptermanner Adapter Manner Support Values
# @{
ADL_ADAPTER_DISPLAYCAP_MANNER_SUPPORTED_NOTACTIVE = 0x00000001
ADL_ADAPTER_DISPLAYCAP_MANNER_SUPPORTED_SINGLE = 0x00000002
ADL_ADAPTER_DISPLAYCAP_MANNER_SUPPORTED_CLONE = 0x00000004
ADL_ADAPTER_DISPLAYCAP_MANNER_SUPPORTED_NSTRETCH1GPU = 0x00000008
ADL_ADAPTER_DISPLAYCAP_MANNER_SUPPORTED_NSTRETCHNGPU = 0x00000010
# / Legacy support for XP
ADL_ADAPTER_DISPLAYCAP_MANNER_SUPPORTED_2VSTRETCH = 0x00000020
ADL_ADAPTER_DISPLAYCAP_MANNER_SUPPORTED_2HSTRETCH = 0x00000040
ADL_ADAPTER_DISPLAYCAP_MANNER_SUPPORTED_EXTENDED = 0x00000080
ADL_ADAPTER_DISPLAYCAP_PREFERDISPLAY_SUPPORTED = 0x00000100
ADL_ADAPTER_DISPLAYCAP_BEZEL_SUPPORTED = 0x00000200
# /////////////////////////////////////////////////////////////////////////
# ADL_DISPLAY_DISPLAYMAP_MANNER_ Definitions
# for ADLDisplayMap.iDisplayMapMask and ADLDisplayMap.iDisplayMapValue
# (bit-vector)
# /////////////////////////////////////////////////////////////////////////
ADL_DISPLAY_DISPLAYMAP_MANNER_RESERVED = 0x00000001
ADL_DISPLAY_DISPLAYMAP_MANNER_NOTACTIVE = 0x00000002
ADL_DISPLAY_DISPLAYMAP_MANNER_SINGLE = 0x00000004
ADL_DISPLAY_DISPLAYMAP_MANNER_CLONE = 0x00000008
# Removed NSTRETCH
ADL_DISPLAY_DISPLAYMAP_MANNER_RESERVED1 = 0x00000010
ADL_DISPLAY_DISPLAYMAP_MANNER_HSTRETCH = 0x00000020
ADL_DISPLAY_DISPLAYMAP_MANNER_VSTRETCH = 0x00000040
ADL_DISPLAY_DISPLAYMAP_MANNER_VLD = 0x00000080
# @}
# /////////////////////////////////////////////////////////////////////////
# ADL_DISPLAY_DISPLAYMAP_OPTION_ Definitions
# for iOption in function ADL_Display_DisplayMapConfig_Get
# (bit-vector)
# /////////////////////////////////////////////////////////////////////////
ADL_DISPLAY_DISPLAYMAP_OPTION_GPUINFO = 0x00000001
# /////////////////////////////////////////////////////////////////////////
# ADL_DISPLAY_DISPLAYTARGET_ Definitions
# for ADLDisplayTarget.iDisplayTargetMask and
# ADLDisplayTarget.iDisplayTargetValue
# (bit-vector)
# /////////////////////////////////////////////////////////////////////////
ADL_DISPLAY_DISPLAYTARGET_PREFERRED = 0x00000001
# /////////////////////////////////////////////////////////////////////////
# ADL_DISPLAY_POSSIBLEMAPRESULT_VALID Definitions
# for ADLPossibleMapResult.iPossibleMapResultMask and
# ADLPossibleMapResult.iPossibleMapResultValue
# (bit-vector)
# /////////////////////////////////////////////////////////////////////////
ADL_DISPLAY_POSSIBLEMAPRESULT_VALID = 0x00000001
ADL_DISPLAY_POSSIBLEMAPRESULT_BEZELSUPPORTED = 0x00000002
ADL_DISPLAY_POSSIBLEMAPRESULT_OVERLAPSUPPORTED = 0x00000004
# /////////////////////////////////////////////////////////////////////////
# ADL_DISPLAY_MODE_ Definitions
# for ADLMode.iModeMask, ADLMode.iModeValue, and ADLMode.iModeFlag
# (bit-vector)
# /////////////////////////////////////////////////////////////////////////
# / \defgroup define_displaymode Display Mode Values
# @{
ADL_DISPLAY_MODE_COLOURFORMAT_565 = 0x00000001
ADL_DISPLAY_MODE_COLOURFORMAT_8888 = 0x00000002
ADL_DISPLAY_MODE_ORIENTATION_SUPPORTED_000 = 0x00000004
ADL_DISPLAY_MODE_ORIENTATION_SUPPORTED_090 = 0x00000008
ADL_DISPLAY_MODE_ORIENTATION_SUPPORTED_180 = 0x00000010
ADL_DISPLAY_MODE_ORIENTATION_SUPPORTED_270 = 0x00000020
ADL_DISPLAY_MODE_REFRESHRATE_ROUNDED = 0x00000040
ADL_DISPLAY_MODE_REFRESHRATE_ONLY = 0x00000080
ADL_DISPLAY_MODE_PROGRESSIVE_FLAG = 0
ADL_DISPLAY_MODE_INTERLACED_FLAG = 2
# @}
# /////////////////////////////////////////////////////////////////////////
# ADL_OSMODEINFO Definitions
# /////////////////////////////////////////////////////////////////////////
# / \defgroup define_osmode OS Mode Values
# @{
ADL_OSMODEINFOXPOS_DEFAULT = -640
ADL_OSMODEINFOYPOS_DEFAULT = 0
ADL_OSMODEINFOXRES_DEFAULT = 640
ADL_OSMODEINFOYRES_DEFAULT = 480
ADL_OSMODEINFOXRES_DEFAULT800 = 800
ADL_OSMODEINFOYRES_DEFAULT600 = 600
ADL_OSMODEINFOREFRESHRATE_DEFAULT = 60
ADL_OSMODEINFOCOLOURDEPTH_DEFAULT = 8
ADL_OSMODEINFOCOLOURDEPTH_DEFAULT16 = 16
ADL_OSMODEINFOCOLOURDEPTH_DEFAULT24 = 24
ADL_OSMODEINFOCOLOURDEPTH_DEFAULT32 = 32
ADL_OSMODEINFOORIENTATION_DEFAULT = 0

if defined(_WIN32) or defined(_WIN64):

    class DUMMY_ENUM(ENUM):
        DISPLAYCONFIG_ROTATION_IDENTITY = EnumItem(0).set_string('Identity')
        DISPLAYCONFIG_ROTATION_ROTATE90 = EnumItem(1).set_string('90°')
        DISPLAYCONFIG_ROTATION_ROTATE180 = EnumItem(2).set_string('180°')
        DISPLAYCONFIG_ROTATION_ROTATE270 = EnumItem(3).set_string('730°')
        DISPLAYCONFIG_ROTATION_FORCE_UINT32 = EnumItem(4).set_string('Force UINT32')

    ADL_OSMODEINFOORIENTATION_DEFAULT_WIN7 = (
        DUMMY_ENUM.DISPLAYCONFIG_ROTATION_FORCE_UINT32
    )
ADL_OSMODEFLAG_DEFAULT = 0


# @}
# /////////////////////////////////////////////////////////////////////////
# ADLThreadingModel Enumeration
# /////////////////////////////////////////////////////////////////////////
# / \defgroup thread_model
# / Used with \ref ADL_Main_ControlX2_Create and \ref
# ADL2_Main_ControlX2_Create to specify how ADL handles API calls when
# executed by multiple threads concurrently.
# / \brief Declares ADL threading behavior.
# @{
class ADLThreadingModel(ENUM):

    # not < Default behavior. ADL will not enforce serialization of ADL
    # API executions by multiple threads. Multiple threads will be allowed
    # to enter to ADL at the same time. Note that ADL library is not
    # guaranteed to be thread-safe. Client that calls
    # ADL_Main_Control_Create have to provide its own mechanism for ADL
    # calls serialization.
    ADL_THREADING_UNLOCKED = EnumItem(0).set_string('Unlocked')

    # not < ADL will enforce serialization of ADL API when called by
    # multiple threads. Only single thread will be allowed to enter ADL
    # API at the time. This option makes ADL calls thread-safe. You
    # shouldn't use this option if ADL calls will be executed on Linux on
    # x-server rendering thread. It can cause the application to hung.
    ADL_THREADING_LOCKED = EnumItem(0).set_string('Locked')


ADL_THREADING_UNLOCKED = ADLThreadingModel.ADL_THREADING_UNLOCKED
ADL_THREADING_LOCKED = ADLThreadingModel.ADL_THREADING_LOCKED


# @}
# /////////////////////////////////////////////////////////////////////////
# ADLPurposeCode Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLPurposeCode(ENUM):
    ADL_PURPOSECODE_NORMAL = EnumItem(0).set_string('Normal')
    ADL_PURPOSECODE_HIDE_MODE_SWITCH = EnumItem(1).set_string('Hide Mode Switch.')
    ADL_PURPOSECODE_MODE_SWITCH = EnumItem(2).set_string('Mode switch.')
    ADL_PURPOSECODE_ATTATCH_DEVICE = EnumItem(3).set_string('Attach Device.')
    ADL_PURPOSECODE_DETACH_DEVICE = EnumItem(4).set_string('Detach device.')
    ADL_PURPOSECODE_SETPRIMARY_DEVICE = EnumItem(5).set_string('Set primary device.')
    ADL_PURPOSECODE_GDI_ROTATION = EnumItem(6).set_string('GDI Rotation.')
    ADL_PURPOSECODE_ATI_ROTATION = EnumItem(7).set_string('STI Rotation.')


ADL_PURPOSECODE_NORMAL = ADLPurposeCode.ADL_PURPOSECODE_NORMAL
ADL_PURPOSECODE_HIDE_MODE_SWITCH = ADLPurposeCode.ADL_PURPOSECODE_HIDE_MODE_SWITCH
ADL_PURPOSECODE_MODE_SWITCH = ADLPurposeCode.ADL_PURPOSECODE_MODE_SWITCH
ADL_PURPOSECODE_ATTATCH_DEVICE = ADLPurposeCode.ADL_PURPOSECODE_ATTATCH_DEVICE
ADL_PURPOSECODE_DETACH_DEVICE = ADLPurposeCode.ADL_PURPOSECODE_DETACH_DEVICE
ADL_PURPOSECODE_SETPRIMARY_DEVICE = ADLPurposeCode.ADL_PURPOSECODE_SETPRIMARY_DEVICE
ADL_PURPOSECODE_GDI_ROTATION = ADLPurposeCode.ADL_PURPOSECODE_GDI_ROTATION
ADL_PURPOSECODE_ATI_ROTATION = ADLPurposeCode.ADL_PURPOSECODE_ATI_ROTATION


# /////////////////////////////////////////////////////////////////////////
# ADLAngle Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLAngle(ENUM):
    ADL_ANGLE_LANDSCAPE = EnumItem(0).set_string('Landscape')
    ADL_ANGLE_ROTATERIGHT = EnumItem(90).set_string('Rotate right')
    ADL_ANGLE_ROTATE180 = EnumItem(150).set_string('Rotate 180')
    ADL_ANGLE_ROTATELEFT = EnumItem(270).set_string('Rotate left')


ADL_ANGLE_LANDSCAPE = ADLAngle.ADL_ANGLE_LANDSCAPE
ADL_ANGLE_ROTATERIGHT = ADLAngle.ADL_ANGLE_ROTATERIGHT
ADL_ANGLE_ROTATE180 = ADLAngle.ADL_ANGLE_ROTATE180
ADL_ANGLE_ROTATELEFT = ADLAngle.ADL_ANGLE_ROTATELEFT


# /////////////////////////////////////////////////////////////////////////
# ADLOrientationDataType Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLOrientationDataType(ENUM):
    ADL_ORIENTATIONTYPE_OSDATATYPE = EnumItem(1).set_string('OS Data Type')
    ADL_ORIENTATIONTYPE_NONOSDATATYPE = EnumItem(2).set_string('Non OS data type')


ADL_ORIENTATIONTYPE_OSDATATYPE = ADLOrientationDataType.ADL_ORIENTATIONTYPE_OSDATATYPE
ADL_ORIENTATIONTYPE_NONOSDATATYPE = ADLOrientationDataType.ADL_ORIENTATIONTYPE_NONOSDATATYPE


# /////////////////////////////////////////////////////////////////////////
# ADLPanningMode Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLPanningMode(ENUM):
    ADL_PANNINGMODE_NO_PANNING = EnumItem(0).set_string('No panning')
    ADL_PANNINGMODE_AT_LEAST_ONE_NO_PANNING = EnumItem(1).set_string('At Least one not painting')
    ADL_PANNINGMODE_ALLOW_PANNING = EnumItem(2).set_string('Allow panning')


ADL_PANNINGMODE_NO_PANNING = ADLPanningMode.ADL_PANNINGMODE_NO_PANNING
ADL_PANNINGMODE_AT_LEAST_ONE_NO_PANNING = ADLPanningMode.ADL_PANNINGMODE_AT_LEAST_ONE_NO_PANNING
ADL_PANNINGMODE_ALLOW_PANNING = ADLPanningMode.ADL_PANNINGMODE_ALLOW_PANNING


# /////////////////////////////////////////////////////////////////////////
# ADLLARGEDESKTOPTYPE Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLLARGEDESKTOPTYPE(ENUM):
    ADL_LARGEDESKTOPTYPE_NORMALDESKTOP = EnumItem(0).set_string('Normal Desktop')
    ADL_LARGEDESKTOPTYPE_PSEUDOLARGEDESKTOP = EnumItem(1).set_string('Pseudo Large Desktop')
    ADL_LARGEDESKTOPTYPE_VERYLARGEDESKTOP = EnumItem(2).set_string('Very large desktop')


ADL_LARGEDESKTOPTYPE_NORMALDESKTOP = ADLLARGEDESKTOPTYPE.ADL_LARGEDESKTOPTYPE_NORMALDESKTOP
ADL_LARGEDESKTOPTYPE_PSEUDOLARGEDESKTOP = ADLLARGEDESKTOPTYPE.ADL_LARGEDESKTOPTYPE_PSEUDOLARGEDESKTOP
ADL_LARGEDESKTOPTYPE_VERYLARGEDESKTOP = ADLLARGEDESKTOPTYPE.ADL_LARGEDESKTOPTYPE_VERYLARGEDESKTOP


# /////////////////////////////////////////////////////////////////////////
# ADLPlatform Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLPlatForm(ENUM):
    GRAPHICS_PLATFORM_DESKTOP = EnumItem(0).set_string('Desktop')
    GRAPHICS_PLATFORM_MOBILE = EnumItem(1).set_string('Mobile')


GRAPHICS_PLATFORM_DESKTOP = ADLPlatForm.GRAPHICS_PLATFORM_DESKTOP
GRAPHICS_PLATFORM_MOBILE = ADLPlatForm.GRAPHICS_PLATFORM_MOBILE


# /////////////////////////////////////////////////////////////////////////
# ADLGraphicCoreGeneration Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLGraphicCoreGeneration(ENUM):
    ADL_GRAPHIC_CORE_GENERATION_UNDEFINED = EnumItem(0).set_string('Undefined')
    ADL_GRAPHIC_CORE_GENERATION_PRE_GCN = EnumItem(1).set_string('Pre GCN')
    ADL_GRAPHIC_CORE_GENERATION_GCN = EnumItem(1).set_string('GCN')


ADL_GRAPHIC_CORE_GENERATION_UNDEFINED = ADLGraphicCoreGeneration.ADL_GRAPHIC_CORE_GENERATION_UNDEFINED
ADL_GRAPHIC_CORE_GENERATION_PRE_GCN = ADLGraphicCoreGeneration.ADL_GRAPHIC_CORE_GENERATION_PRE_GCN
ADL_GRAPHIC_CORE_GENERATION_GCN = ADLGraphicCoreGeneration.ADL_GRAPHIC_CORE_GENERATION_GCN

# Other Definitions for internal use
# Values for ADL_Display_WriteAndReadI2CRev_Get()
ADL_I2C_MAJOR_API_REV = 0x00000001
ADL_I2C_MINOR_DEFAULT_API_REV = 0x00000000
ADL_I2C_MINOR_OEM_API_REV = 0x00000001

# Values for ADL_Display_WriteAndReadI2C()
ADL_DL_I2C_LINE_OEM = 0x00000001
ADL_DL_I2C_LINE_OD_CONTROL = 0x00000002
ADL_DL_I2C_LINE_OEM2 = 0x00000003
ADL_DL_I2C_LINE_OEM3 = 0x00000004
ADL_DL_I2C_LINE_OEM4 = 0x00000005
ADL_DL_I2C_LINE_OEM5 = 0x00000006
ADL_DL_I2C_LINE_OEM6 = 0x00000007

# Max size of I2C data buffer
ADL_DL_I2C_MAXDATASIZE = 0x00000040
ADL_DL_I2C_MAXWRITEDATASIZE = 0x0000000C
ADL_DL_I2C_MAXADDRESSLENGTH = 0x00000006
ADL_DL_I2C_MAXOFFSETLENGTH = 0x00000004

# / Values for ADLDisplayProperty.iPropertyType
ADL_DL_DISPLAYPROPERTY_TYPE_UNKNOWN = 0
ADL_DL_DISPLAYPROPERTY_TYPE_EXPANSIONMODE = 1
ADL_DL_DISPLAYPROPERTY_TYPE_USEUNDERSCANSCALING = 2

# / Enables ITC processing for HDMI panels that are capable of the feature
ADL_DL_DISPLAYPROPERTY_TYPE_ITCFLAGENABLE = 9
ADL_DL_DISPLAYPROPERTY_TYPE_DOWNSCALE = 11

# / Values for ADLDisplayContent.iContentType
# / Certain HDMI panels that support ITC have support for a feature such
# that, the display on the panel
# / can be adjusted to optimize the view of the content being displayed,
# depending on the type of content.
ADL_DL_DISPLAYCONTENT_TYPE_GRAPHICS = Constant(1).set_string('Graphics')
ADL_DL_DISPLAYCONTENT_TYPE_PHOTO = Constant(2).set_string('Photo')
ADL_DL_DISPLAYCONTENT_TYPE_CINEMA = Constant(4).set_string('Cinema')
ADL_DL_DISPLAYCONTENT_TYPE_GAME = Constant(8).set_string('Game')

# values for ADLDisplayProperty.iExpansionMode
ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_CENTER = Constant(0).set_string('Center')
ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_FULLSCREEN = Constant(1).set_string('Full Screen')
ADL_DL_DISPLAYPROPERTY_EXPANSIONMODE_ASPECTRATIO = Constant(2).set_string('Aspect Ratio')

# /\defgroup define_dither_states Dithering options
# @{
# / Dithering disabled.

ADL_DL_DISPLAY_DITHER_DISABLED = Constant(0).set_string('Disabled')
# / Use default driver settings for dithering. Note that the default
# setting could be dithering disabled.
ADL_DL_DISPLAY_DITHER_DRIVER_DEFAULT = Constant(1).set_string('Default')
# / Temporal dithering to 6 bpc. Note that if the input is 12 bits, the
# two least significant bits will be truncated.
ADL_DL_DISPLAY_DITHER_FM6 = Constant(2).set_string('Temporal dithering to 6 bpc')
# / Temporal dithering to 8 bpc.
ADL_DL_DISPLAY_DITHER_FM8 = Constant(3).set_string('Temporal dithering to 8 bpc')
# / Temporal dithering to 10 bpc.
ADL_DL_DISPLAY_DITHER_FM10 = Constant(4).set_string('Temporal dithering to 10 bpc')
# / Spatial dithering to 6 bpc. Note that if the input is 12 bits, the two
# least significant bits will be truncated.
ADL_DL_DISPLAY_DITHER_DITH6 = Constant(5).set_string('Spatial dithering to 6 bpc')
# / Spatial dithering to 8 bpc.
ADL_DL_DISPLAY_DITHER_DITH8 = Constant(6).set_string('Spatial dithering to 8 bpc')
# / Spatial dithering to 10 bpc.
ADL_DL_DISPLAY_DITHER_DITH10 = Constant(7).set_string('Spatial dithering to 10 bpc')
# / Spatial dithering to 6 bpc. Random number generators are reset every
# frame, so the same input value of a certain pixel will always be
# dithered to the same output value. Note that if the input is 12 bits,
# the two least significant bits will be truncated.
ADL_DL_DISPLAY_DITHER_DITH6_NO_FRAME_RAND = Constant(8).set_string('Spatial dithering to 6 bpc random')
# / Spatial dithering to 8 bpc. Random number generators are reset every
# frame, so the same input value of a certain pixel will always be
# dithered to the same output value.
ADL_DL_DISPLAY_DITHER_DITH8_NO_FRAME_RAND = Constant(9).set_string('Spatial dithering to 8 bpc random')
# / Spatial dithering to 10 bpc. Random number generators are reset every
# frame, so the same input value of a certain pixel will always be
# dithered to the same output value.
ADL_DL_DISPLAY_DITHER_DITH10_NO_FRAME_RAND = Constant(10).set_string('Spatial dithering to 10 bpc random')
# / Truncation to 6 bpc.
ADL_DL_DISPLAY_DITHER_TRUN6 = Constant(11).set_string('Truncation to 6 bpc')
# / Truncation to 8 bpc.
ADL_DL_DISPLAY_DITHER_TRUN8 = Constant(12).set_string('Truncation to 8 bpc')
# / Truncation to 10 bpc.
ADL_DL_DISPLAY_DITHER_TRUN10 = Constant(13).set_string('Truncation to 10 bpc')
# / Truncation to 10 bpc followed by spatial dithering to 8 bpc.
ADL_DL_DISPLAY_DITHER_TRUN10_DITH8 = Constant(14).set_string(
    'Truncation to 10 bpc followed by spatial dithering to 8 bpc'
)
# / Truncation to 10 bpc followed by spatial dithering to 6 bpc.
ADL_DL_DISPLAY_DITHER_TRUN10_DITH6 = Constant(15).set_string(
    'Truncation to 10 bpc followed by spatial dithering to 6 bpc'
)
# / Truncation to 10 bpc followed by temporal dithering to 8 bpc.
ADL_DL_DISPLAY_DITHER_TRUN10_FM8 = Constant(16).set_string(
    'Truncation to 10 bpc followed by temporal dithering to 8 bpc'
)
# / Truncation to 10 bpc followed by temporal dithering to 6 bpc.
ADL_DL_DISPLAY_DITHER_TRUN10_FM6 = Constant(17).set_string(
    'Truncation to 10 bpc followed by temporal dithering to 6 bpc'
)
# / Truncation to 10 bpc followed by spatial dithering to 8 bpc and
# temporal dithering to 6 bpc.
ADL_DL_DISPLAY_DITHER_TRUN10_DITH8_FM6 = Constant(18).set_string(
    'Truncation to 10 bpc followed by spatial dithering to 8 bpc and temporal dithering to 6 bpc'
)
# / Spatial dithering to 10 bpc followed by temporal dithering to 8 bpc.
ADL_DL_DISPLAY_DITHER_DITH10_FM8 = Constant(19).set_string(
    'Spatial dithering to 10 bpc followed by temporal dithering to 8 bpc'
)
# / Spatial dithering to 10 bpc followed by temporal dithering to 6 bpc.
ADL_DL_DISPLAY_DITHER_DITH10_FM6 = Constant(20).set_string(
    'Spatial dithering to 10 bpc followed by temporal dithering to 6 bpc'
)
# / Truncation to 8 bpc followed by spatial dithering to 6 bpc.
ADL_DL_DISPLAY_DITHER_TRUN8_DITH6 = Constant(21).set_string(
    'Truncation to 8 bpc followed by spatial dithering to 6 bpc'
)
# / Truncation to 8 bpc followed by temporal dithering to 6 bpc.
ADL_DL_DISPLAY_DITHER_TRUN8_FM6 = Constant(22).set_string(
    'Truncation to 8 bpc followed by temporal dithering to 6 bpc'
)
# / Spatial dithering to 8 bpc followed by temporal dithering to 6 bpc.
ADL_DL_DISPLAY_DITHER_DITH8_FM6 = Constant(23).set_string(
    'Spatial dithering to 8 bpc followed by temporal dithering to 6 bpc'
)
ADL_DL_DISPLAY_DITHER_LAST = ADL_DL_DISPLAY_DITHER_DITH8_FM6
# @}
# / Display Get Cached EDID flag
# number of UCHAR
ADL_MAX_EDIDDATA_SIZE = 256

# number of UCHAR
ADL_MAX_OVERRIDEEDID_SIZE = 512
ADL_MAX_EDID_EXTENSION_BLOCKS = 3
ADL_DL_CONTROLLER_OVERLAY_ALPHA = 0
ADL_DL_CONTROLLER_OVERLAY_ALPHAPERPIX = 1
ADL_DL_DISPLAY_DATA_PACKET__INFO_PACKET_RESET = 0x00000000
ADL_DL_DISPLAY_DATA_PACKET__INFO_PACKET_SET = 0x00000001
ADL_DL_DISPLAY_DATA_PACKET__INFO_PACKET_SCAN = 0x00000002

# /\defgroup define_display_packet Display Data Packet Types
# @{
ADL_DL_DISPLAY_DATA_PACKET__TYPE__AVI = 0x00000001
ADL_DL_DISPLAY_DATA_PACKET__TYPE__GAMMUT = 0x00000002
ADL_DL_DISPLAY_DATA_PACKET__TYPE__VENDORINFO = 0x00000004
ADL_DL_DISPLAY_DATA_PACKET__TYPE__HDR = 0x00000008
ADL_DL_DISPLAY_DATA_PACKET__TYPE__SPD = 0x00000010
# @}
# matrix types
# SD matrix i.e. BT601
ADL_GAMUT_MATRIX_SD = 1

# HD matrix i.e. BT709
ADL_GAMUT_MATRIX_HD = 2

# /\defgroup define_clockinfo_flags Clock flags
# / Used by ADLAdapterODClockInfo.iFlag
# @{
ADL_DL_CLOCKINFO_FLAG_FULLSCREEN3DONLY = 0x00000001
ADL_DL_CLOCKINFO_FLAG_ALWAYSFULLSCREEN3D = 0x00000002
ADL_DL_CLOCKINFO_FLAG_VPURECOVERYREDUCED = 0x00000004
ADL_DL_CLOCKINFO_FLAG_THERMALPROTECTION = 0x00000008
# @}
# Supported GPUs
# ADL_Display_PowerXpressActiveGPU_Get()
ADL_DL_POWERXPRESS_GPU_INTEGRATED = 1
ADL_DL_POWERXPRESS_GPU_DISCRETE = 2

# Possible values for lpOperationResult
# ADL_Display_PowerXpressActiveGPU_Get()
# Switch procedure has been started - Windows platform only
ADL_DL_POWERXPRESS_SWITCH_RESULT_STARTED = 1

# Switch procedure cannot be started - All platforms
ADL_DL_POWERXPRESS_SWITCH_RESULT_DECLINED = 2

# System already has required status - All platforms
ADL_DL_POWERXPRESS_SWITCH_RESULT_ALREADY = 3

# Switch was deferred and requires an X restart - Linux platform only
ADL_DL_POWERXPRESS_SWITCH_RESULT_DEFERRED = 5

# PowerXpress support version
# ADL_Display_PowerXpressVersion_Get()
# Current PowerXpress support version 2.0
ADL_DL_POWERXPRESS_VERSION_MAJOR = 2
ADL_DL_POWERXPRESS_VERSION_MINOR = 0
ADL_DL_POWERXPRESS_VERSION = (
    (ADL_DL_POWERXPRESS_VERSION_MAJOR << 16) |
    ADL_DL_POWERXPRESS_VERSION_MINOR
)

# values for ADLThermalControllerInfo.iThermalControllerDomain
ADL_DL_THERMAL_DOMAIN_OTHER = 0
ADL_DL_THERMAL_DOMAIN_GPU = 1

# values for ADLThermalControllerInfo.iFlags
ADL_DL_THERMAL_FLAG_INTERRUPT = 1
ADL_DL_THERMAL_FLAG_FANCONTROL = 2

# /\defgroup define_fanctrl Fan speed cotrol
# / Values for ADLFanSpeedInfo.iFlags
# @{
ADL_DL_FANCTRL_SUPPORTS_PERCENT_READ = 1
ADL_DL_FANCTRL_SUPPORTS_PERCENT_WRITE = 2
ADL_DL_FANCTRL_SUPPORTS_RPM_READ = 4
ADL_DL_FANCTRL_SUPPORTS_RPM_WRITE = 8
# @}
# values for ADLFanSpeedValue.iSpeedType
ADL_DL_FANCTRL_SPEED_TYPE_PERCENT = 1
ADL_DL_FANCTRL_SPEED_TYPE_RPM = 2

# values for ADLFanSpeedValue.iFlags
ADL_DL_FANCTRL_FLAG_USER_DEFINED_SPEED = 1

# MVPU interfaces
ADL_DL_MAX_MVPU_ADAPTERS = 4
MVPU_ADAPTER_0 = 0x00000001
MVPU_ADAPTER_1 = 0x00000002
MVPU_ADAPTER_2 = 0x00000004
MVPU_ADAPTER_3 = 0x00000008
ADL_DL_MAX_REGISTRY_PATH = 256

# values for ADLMVPUStatus.iStatus
ADL_DL_MVPU_STATUS_OFF = 0
ADL_DL_MVPU_STATUS_ON = 1

# values for ASIC family
# /\defgroup define_Asic_type Detailed asic types
# / Defines for Adapter ASIC family type
# @{
ADL_ASIC_UNDEFINED = Constant(0).set_string('Undefined')
ADL_ASIC_DISCRETE = Constant(1 << 0).set_string('Discrete')
ADL_ASIC_INTEGRATED = Constant(1 << 1).set_string('Integrated')
ADL_ASIC_FIREGL = Constant(1 << 2).set_string('Fire GL')
ADL_ASIC_FIREMV = Constant(1 << 3).set_string('Fire MV')
ADL_ASIC_XGP = Constant(1 << 4).set_string('XGP')
ADL_ASIC_FUSION = Constant(1 << 5).set_string('Fusion')
ADL_ASIC_FIRESTREAM = Constant(1 << 6).set_string('Fire Stream')
ADL_ASIC_EMBEDDED = Constant(1 << 7).set_string('Embedded')
# @}
# /\defgroup define_detailed_timing_flags Detailed Timimg Flags
# / Defines for ADLDetailedTiming.sTimingFlags field
# @{
ADL_DL_TIMINGFLAG_DOUBLE_SCAN = 0x0001
# sTimingFlags is set when the mode is INTERLACED, if not PROGRESSIVE
ADL_DL_TIMINGFLAG_INTERLACED = 0x0002
# sTimingFlags is set when the Horizontal Sync is POSITIVE, if not NEGATIVE
ADL_DL_TIMINGFLAG_H_SYNC_POLARITY = 0x0004
# sTimingFlags is set when the Vertical Sync is POSITIVE, if not NEGATIVE
ADL_DL_TIMINGFLAG_V_SYNC_POLARITY = 0x0008
# @}
# /\defgroup define_modetiming_standard Timing Standards
# / Defines for ADLDisplayModeInfo.iTimingStandard field
# @{
# CVT Standard
ADL_DL_MODETIMING_STANDARD_CVT = 0x00000001
# GFT Standard
ADL_DL_MODETIMING_STANDARD_GTF = 0x00000002
# DMT Standard
ADL_DL_MODETIMING_STANDARD_DMT = 0x00000004
# User-defined standard
ADL_DL_MODETIMING_STANDARD_CUSTOM = 0x00000008
# Remove Mode from overriden list
ADL_DL_MODETIMING_STANDARD_DRIVER_DEFAULT = 0x00000010
# CVT-RB Standard
ADL_DL_MODETIMING_STANDARD_CVT_RB = 0x00000020
# @}
# \defgroup define_xserverinfo driver x-server info
# / These flags are used by ADL_XServerInfo_Get()
# @
# / Xinerama is active in the x-server, Xinerama extension may report it
# to be active but it
# / may not be active in x-server
ADL_XSERVERINFO_XINERAMAACTIVE = 1 << 0

# / RandR 1.2 is supported by driver, RandR extension may report version
# 1.2
# / but driver may not support it
ADL_XSERVERINFO_RANDR12SUPPORTED = 1 << 1

# @
# /\defgroup define_eyefinity_constants Eyefinity Definitions
# @{
# ADL_CONTROLLERINDEX_0 = 0, (1 < < ADL_CONTROLLERINDEX_0)
ADL_CONTROLLERVECTOR_0 = 1
# ADL_CONTROLLERINDEX_1 = 1, (1 < < ADL_CONTROLLERINDEX_1)
ADL_CONTROLLERVECTOR_1 = 2
ADL_DISPLAY_SLSGRID_ORIENTATION_000 = 0x00000001
ADL_DISPLAY_SLSGRID_ORIENTATION_090 = 0x00000002
ADL_DISPLAY_SLSGRID_ORIENTATION_180 = 0x00000004
ADL_DISPLAY_SLSGRID_ORIENTATION_270 = 0x00000008
ADL_DISPLAY_SLSGRID_CAP_OPTION_RELATIVETO_LANDSCAPE = 0x00000001
ADL_DISPLAY_SLSGRID_CAP_OPTION_RELATIVETO_CURRENTANGLE = 0x00000002
ADL_DISPLAY_SLSGRID_PORTAIT_MODE = 0x00000004
ADL_DISPLAY_SLSGRID_KEEPTARGETROTATION = 0x00000080
ADL_DISPLAY_SLSGRID_SAMEMODESLS_SUPPORT = 0x00000010
ADL_DISPLAY_SLSGRID_MIXMODESLS_SUPPORT = 0x00000020
ADL_DISPLAY_SLSGRID_DISPLAYROTATION_SUPPORT = 0x00000040
ADL_DISPLAY_SLSGRID_DESKTOPROTATION_SUPPORT = 0x00000080
ADL_DISPLAY_SLSMAP_SLSLAYOUTMODE_FIT = 0x0100
ADL_DISPLAY_SLSMAP_SLSLAYOUTMODE_FILL = 0x0200
ADL_DISPLAY_SLSMAP_SLSLAYOUTMODE_EXPAND = 0x0400
ADL_DISPLAY_SLSMAP_IS_SLS = 0x1000
ADL_DISPLAY_SLSMAP_IS_SLSBUILDER = 0x2000
ADL_DISPLAY_SLSMAP_IS_CLONEVT = 0x4000
ADL_DISPLAY_SLSMAPCONFIG_GET_OPTION_RELATIVETO_LANDSCAPE = 0x00000001
ADL_DISPLAY_SLSMAPCONFIG_GET_OPTION_RELATIVETO_CURRENTANGLE = 0x00000002
ADL_DISPLAY_SLSMAPCONFIG_CREATE_OPTION_RELATIVETO_LANDSCAPE = 0x00000001
ADL_DISPLAY_SLSMAPCONFIG_CREATE_OPTION_RELATIVETO_CURRENTANGLE = 0x00000002
ADL_DISPLAY_SLSMAPCONFIG_REARRANGE_OPTION_RELATIVETO_LANDSCAPE = 0x00000001
ADL_DISPLAY_SLSMAPCONFIG_REARRANGE_OPTION_RELATIVETO_CURRENTANGLE = (
    0x00000002
)
ADL_SLS_SAMEMODESLS_SUPPORT = 0x0001
ADL_SLS_MIXMODESLS_SUPPORT = 0x0002
ADL_SLS_DISPLAYROTATIONSLS_SUPPORT = 0x0004
ADL_SLS_DESKTOPROTATIONSLS_SUPPORT = 0x0008
ADL_SLS_TARGETS_INVALID = 0x0001
ADL_SLS_MODES_INVALID = 0x0002
ADL_SLS_ROTATIONS_INVALID = 0x0004
ADL_SLS_POSITIONS_INVALID = 0x0008
ADL_SLS_LAYOUTMODE_INVALID = 0x0010
ADL_DISPLAY_SLSDISPLAYOFFSET_VALID = 0x0002
ADL_DISPLAY_SLSGRID_RELATIVETO_LANDSCAPE = 0x00000010
ADL_DISPLAY_SLSGRID_RELATIVETO_CURRENTANGLE = 0x00000020
# / The bit mask identifies displays is currently in bezel mode.
ADL_DISPLAY_SLSMAP_BEZELMODE = 0x00000010
# / The bit mask identifies displays from this map is arranged.
ADL_DISPLAY_SLSMAP_DISPLAYARRANGED = 0x00000002
# / The bit mask identifies this map is currently in used for the current
# adapter.
ADL_DISPLAY_SLSMAP_CURRENTCONFIG = 0x00000004
# /For onlay active SLS map info
ADL_DISPLAY_SLSMAPINDEXLIST_OPTION_ACTIVE = 0x00000001
# /For Bezel
ADL_DISPLAY_BEZELOFFSET_STEPBYSTEPSET = 0x00000004
ADL_DISPLAY_BEZELOFFSET_COMMIT = 0x00000008


class _SLS_ImageCropType(ENUM):
    Fit = EnumItem(1).set_string('Fit')
    Fill = EnumItem(2).set_string('Fill')
    Expand = EnumItem(3).set_string('Expand')


SLS_ImageCropType = _SLS_ImageCropType
Fit = _SLS_ImageCropType.Fit
Fill = _SLS_ImageCropType.Fill
Expand = _SLS_ImageCropType.Expand


class _DceSettingsType(ENUM):
    DceSetting_HdmiLq = EnumItem(1).set_string('HDMI LQ')
    DceSetting_DpSettings = EnumItem(2).set_string('Dp Settings')
    DceSetting_Protection = EnumItem(3).set_string('Protection')


DceSettingsType = _DceSettingsType
DceSetting_HdmiLq = _DceSettingsType.DceSetting_HdmiLq
DceSetting_DpSettings = _DceSettingsType.DceSetting_DpSettings
DceSetting_Protection = _DceSettingsType.DceSetting_Protection


class _DpLinkRate(ENUM):
    DPLinkRate_Unknown = EnumItem(1).set_string('Unknown')
    DPLinkRate_RBR = EnumItem(2).set_string('RBR')
    DPLinkRate_HBR = EnumItem(3).set_string('HBR')
    DPLinkRate_HBR2 = EnumItem(4).set_string('HBR2')
    DPLinkRate_HBR3 = EnumItem(5).set_string('HBR3')


DpLinkRate = _DpLinkRate
DPLinkRate_Unknown = _DpLinkRate.DPLinkRate_Unknown
DPLinkRate_RBR = _DpLinkRate.DPLinkRate_RBR
DPLinkRate_HBR = _DpLinkRate.DPLinkRate_HBR
DPLinkRate_HBR2 = _DpLinkRate.DPLinkRate_HBR2
DPLinkRate_HBR3 = _DpLinkRate.DPLinkRate_HBR3

# @}
# /\defgroup define_powerxpress_constants PowerXpress Definitions
# / @{
# / The bit mask identifies PX caps for ADLPXConfigCaps.iPXConfigCapMask
# and ADLPXConfigCaps.iPXConfigCapValue
ADL_PX_CONFIGCAPS_SPLASHSCREEN_SUPPORT = 0x0001
ADL_PX_CONFIGCAPS_CF_SUPPORT = 0x0002
ADL_PX_CONFIGCAPS_MUXLESS = 0x0004
ADL_PX_CONFIGCAPS_PROFILE_COMPLIANT = 0x0008
ADL_PX_CONFIGCAPS_NON_AMD_DRIVEN_DISPLAYS = 0x0010
ADL_PX_CONFIGCAPS_FIXED_SUPPORT = 0x0020
ADL_PX_CONFIGCAPS_DYNAMIC_SUPPORT = 0x0040
ADL_PX_CONFIGCAPS_HIDE_AUTO_SWITCH = 0x0080

# / The bit mask identifies PX schemes for ADLPXSchemeRange
ADL_PX_SCHEMEMASK_FIXED = 0x0001
ADL_PX_SCHEMEMASK_DYNAMIC = 0x0002


# / PX Schemes
class _ADLPXScheme(ENUM):
    ADL_PX_SCHEME_INVALID = EnumItem(0).set_string('Invalid')
    ADL_PX_SCHEME_FIXED = EnumItem(ADL_PX_SCHEMEMASK_FIXED).set_string('Fixed')
    ADL_PX_SCHEME_DYNAMIC = EnumItem(ADL_PX_SCHEMEMASK_DYNAMIC).set_string('Dynamic')


ADLPXScheme = _ADLPXScheme
ADL_PX_SCHEME_INVALID = _ADLPXScheme.ADL_PX_SCHEME_INVALID
ADL_PX_SCHEME_FIXED = _ADLPXScheme.ADL_PX_SCHEME_FIXED
ADL_PX_SCHEME_DYNAMIC = _ADLPXScheme.ADL_PX_SCHEME_DYNAMIC


# / Just keep the old definitions for compatibility, need to be removed
# later
class PXScheme(ENUM):
    PX_SCHEME_INVALID = EnumItem(0).set_string('Invalid')
    PX_SCHEME_FIXED = EnumItem(1).set_string('Fixed')
    PX_SCHEME_DYNAMIC = EnumItem(2).set_string('Dynamic')


PX_SCHEME_INVALID = PXScheme.PX_SCHEME_INVALID
PX_SCHEME_FIXED = PXScheme.PX_SCHEME_FIXED
PX_SCHEME_DYNAMIC = PXScheme.PX_SCHEME_DYNAMIC
# / @}
# /\defgroup define_appprofiles For Application Profiles
# / @{
ADL_APP_PROFILE_FILENAME_LENGTH = 256
ADL_APP_PROFILE_TIMESTAMP_LENGTH = 32
ADL_APP_PROFILE_VERSION_LENGTH = 32
ADL_APP_PROFILE_PROPERTY_LENGTH = 64


class ApplicationListType(ENUM):
    ADL_PX40_MRU = EnumItem(1).set_string('PX40 MRU')
    ADL_PX40_MISSED = EnumItem(2).set_string('PX40 Missed')
    ADL_PX40_DISCRETE = EnumItem(3).set_string('PX40 Discrete')
    ADL_PX40_INTEGRATED = EnumItem(4).set_string('PX40 Intergrated')
    ADL_MMD_PROFILED = EnumItem(5).set_string('MMD Profiled')
    ADL_PX40_TOTAL = EnumItem(6).set_string('PX40 Total')


ADL_PX40_MRU = ApplicationListType.ADL_PX40_MRU
ADL_PX40_MISSED = ApplicationListType.ADL_PX40_MISSED
ADL_PX40_DISCRETE = ApplicationListType.ADL_PX40_DISCRETE
ADL_PX40_INTEGRATED = ApplicationListType.ADL_PX40_INTEGRATED
ADL_MMD_PROFILED = ApplicationListType.ADL_MMD_PROFILED
ADL_PX40_TOTAL = ApplicationListType.ADL_PX40_TOTAL


class _ADLProfilePropertyType(ENUM):
    ADL_PROFILEPROPERTY_TYPE_BINARY = EnumItem(0).set_string('BINARY')
    ADL_PROFILEPROPERTY_TYPE_BOOLEAN = EnumItem(1).set_string('BOOLEAN')
    ADL_PROFILEPROPERTY_TYPE_DWORD = EnumItem(2).set_string('DWORD')
    ADL_PROFILEPROPERTY_TYPE_QWORD = EnumItem(3).set_string('QWORD')
    ADL_PROFILEPROPERTY_TYPE_ENUMERATED = EnumItem(4).set_string('ENUM')
    ADL_PROFILEPROPERTY_TYPE_STRING = EnumItem(5).set_string('STRING')


ADLProfilePropertyType = _ADLProfilePropertyType
ADL_PROFILEPROPERTY_TYPE_BINARY = _ADLProfilePropertyType.ADL_PROFILEPROPERTY_TYPE_BINARY
ADL_PROFILEPROPERTY_TYPE_BOOLEAN = _ADLProfilePropertyType.ADL_PROFILEPROPERTY_TYPE_BOOLEAN
ADL_PROFILEPROPERTY_TYPE_DWORD = _ADLProfilePropertyType.ADL_PROFILEPROPERTY_TYPE_DWORD
ADL_PROFILEPROPERTY_TYPE_QWORD = _ADLProfilePropertyType.ADL_PROFILEPROPERTY_TYPE_QWORD
ADL_PROFILEPROPERTY_TYPE_ENUMERATED = _ADLProfilePropertyType.ADL_PROFILEPROPERTY_TYPE_ENUMERATED
ADL_PROFILEPROPERTY_TYPE_STRING = _ADLProfilePropertyType.ADL_PROFILEPROPERTY_TYPE_STRING

# / @}
# /\defgroup define_dp12 For Display Port 1.2
# / @{
# / Maximum Relative Address Link
ADL_MAX_RAD_LINK_COUNT = 15

# / @}
# /\defgroup defines_gamutspace Driver Supported Gamut Space
# / @{
# / The flags desribes that gamut is related to source or to destination
# and to overlay or to graphics
ADL_GAMUT_REFERENCE_SOURCE = 1 << 0
ADL_GAMUT_GAMUT_VIDEO_CONTENT = 1 << 1

# / The flags are used to describe the source of gamut and how read
# information from struct ADLGamutData
ADL_CUSTOM_WHITE_POINT = 1 << 0
ADL_CUSTOM_GAMUT = 1 << 1
ADL_GAMUT_REMAP_ONLY = 1 << 2

# / The define means the predefined gamut values .
# /Driver uses to find entry in the table and apply appropriate gamut
# space.
ADL_GAMUT_SPACE_CCIR_709 = 1 << 0
ADL_GAMUT_SPACE_CCIR_601 = 1 << 1
ADL_GAMUT_SPACE_ADOBE_RGB = 1 << 2
ADL_GAMUT_SPACE_CIE_RGB = 1 << 3
ADL_GAMUT_SPACE_CUSTOM = 1 << 4
ADL_GAMUT_SPACE_CCIR_2020 = 1 << 5
ADL_GAMUT_SPACE_APPCTRL = 1 << 6

# / Predefine white point values are structed similar to gamut .
ADL_WHITE_POINT_5000K = 1 << 0
ADL_WHITE_POINT_6500K = 1 << 1
ADL_WHITE_POINT_7500K = 1 << 2
ADL_WHITE_POINT_9300K = 1 << 3
ADL_WHITE_POINT_CUSTOM = 1 << 4

# /gamut and white point coordinates are from 0.0 -1.0 and divider is used
# to find the real value .
# / X FLOAT = X INT /divider
ADL_GAMUT_WHITEPOINT_DIVIDER = 10000

# /gamma a0 coefficient uses the following divider:
ADL_REGAMMA_COEFFICIENT_A0_DIVIDER = 10000000

# /gamma a1 ,a2,a3 coefficients use the following divider:
ADL_REGAMMA_COEFFICIENT_A1A2A3_DIVIDER = 1000

# /describes whether the coefficients are from EDID or custom user values.
ADL_EDID_REGAMMA_COEFFICIENTS = 1 << 0

# /Used for struct ADLRegamma. Feature if set use gamma ramp, if missing
# use regamma coefficents
ADL_USE_GAMMA_RAMP = 1 << 4

# /Used for struct ADLRegamma. If the gamma ramp flag is used then the
# driver could apply de gamma corretion to the supplied curve and this
# depends on this flag
ADL_APPLY_DEGAMMA = 1 << 5

# /specifies that standard SRGB gamma should be applied
ADL_EDID_REGAMMA_PREDEFINED_SRGB = 1 << 1

# /specifies that PQ gamma curve should be applied
ADL_EDID_REGAMMA_PREDEFINED_PQ = 1 << 2

# /specifies that PQ gamma curve should be applied, lower max nits
ADL_EDID_REGAMMA_PREDEFINED_PQ_2084_INTERIM = 1 << 3

# /specifies that 3.6 gamma should be applied
ADL_EDID_REGAMMA_PREDEFINED_36 = 1 << 6

# /specifies that BT709 gama should be applied
ADL_EDID_REGAMMA_PREDEFINED_BT709 = 1 << 7

# /specifies that regamma should be disabled, and application controls
# regamma content (of the whole screen)
ADL_EDID_REGAMMA_PREDEFINED_APPCTRL = 1 << 8

# / @}
# / \defgroup define_ddcinfo_pixelformats DDCInfo Pixel Formats
# / @{
# / defines for iPanelPixelFormat in struct ADLDDCInfo2
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_RGB656 = 0x00000001
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_RGB666 = 0x00000002
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_RGB888 = 0x00000004
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_RGB101010 = 0x00000008
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_RGB161616 = 0x00000010
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_RGB_RESERVED1 = 0x00000020
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_RGB_RESERVED2 = 0x00000040
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_RGB_RESERVED3 = 0x00000080
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_XRGB_BIAS101010 = 0x00000100
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR444_8BPCC = 0x00000200
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR444_10BPCC = 0x00000400
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR444_12BPCC = 0x00000800
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR422_8BPCC = 0x00001000
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR422_10BPCC = 0x00002000
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR422_12BPCC = 0x00004000
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR420_8BPCC = 0x00008000
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR420_10BPCC = 0x00010000
ADL_DISPLAY_DDCINFO_PIXEL_FORMAT_YCBCR420_12BPCC = 0x00020000

# / @}
# / \defgroup define_source_content_TF ADLSourceContentAttributes transfer
# functions (gamma)
# / @{
# / defines for iTransferFunction in ADLSourceContentAttributes
# / < sRGB
ADL_TF_sRGB = 0x0001

# / < BT.709
ADL_TF_BT709 = 0x0002

# / < PQ2084
ADL_TF_PQ2084 = 0x0004

# / < PQ2084-Interim
ADL_TF_PQ2084_INTERIM = 0x0008

# / < Linear 0 - 1
ADL_TF_LINEAR_0_1 = 0x0010

# / < Linear 0 - 125
ADL_TF_LINEAR_0_125 = 0x0020

# / < DolbyVision
ADL_TF_DOLBYVISION = 0x0040

# / < Plain 2.2 gamma curve
ADL_TF_GAMMA_22 = 0x0080

# / @}
# / \defgroup define_source_content_CS ADLSourceContentAttributes color
# spaces
# / @{
# / defines for iColorSpace in ADLSourceContentAttributes
# / < sRGB
ADL_CS_sRGB = 0x0001

# / < BT.601
ADL_CS_BT601 = 0x0002

# / < BT.709
ADL_CS_BT709 = 0x0004

# / < BT.2020
ADL_CS_BT2020 = 0x0008

# / < Adobe RGB
ADL_CS_ADOBE = 0x0010

# / < DCI-P3
ADL_CS_P3 = 0x0020

# / < scRGB (MS Reference)
ADL_CS_scRGB_MS_REF = 0x0040

# / < Display Native
ADL_CS_DISPLAY_NATIVE = 0x0080

# / < Application Controlled
ADL_CS_APP_CONTROL = 0x0100

# / < DolbyVision
ADL_CS_DOLBYVISION = 0x0200

# / @}
# / \defgroup define_HDR_support ADLDDCInfo2 HDR support options
# / @{
# / defines for iSupportedHDR in ADLDDCInfo2
# / < HDR10/CEA861.3 HDR supported
ADL_HDR_CEA861_3 = 0x0001

# / < DolbyVision HDR supported
ADL_HDR_DOLBYVISION = 0x0002

# / < FreeSync HDR supported
ADL_HDR_FREESYNC_HDR = 0x0004

# / @}
# / \defgroup define_FreesyncFlags ADLDDCInfo2 Freesync HDR flags
# / @{
# / defines for iFreesyncFlags in ADLDDCInfo2
# / < Global backlight control supported
ADL_HDR_FREESYNC_BACKLIGHT_SUPPORT = 0x0001

# / < Local dimming supported
ADL_HDR_FREESYNC_LOCAL_DIMMING = 0x0002

# / @}
# / \defgroup define_source_content_flags ADLSourceContentAttributes flags
# / @{
# / defines for iFlags in ADLSourceContentAttributes
# / < Disable local dimming
ADL_SCA_LOCAL_DIMMING_DISABLE = 0x0001

# / @}
# / \defgroup define_dbd_state Deep Bit Depth
# / @{
# / defines for ADL_Workstation_DeepBitDepth_Get and
# ADL_Workstation_DeepBitDepth_Set functions
# This value indicates that the deep bit depth state is forced off
ADL_DEEPBITDEPTH_FORCEOFF = 0

# / This value indicates that the deep bit depth state is set to auto, the
# driver will automatically enable the
# / appropriate deep bit depth state depending on what connected display
# supports.
ADL_DEEPBITDEPTH_10BPP_AUTO = 1

# / This value indicates that the deep bit depth state is forced on to 10
# bits per pixel, this is regardless if the display
# / supports 10 bpp.
ADL_DEEPBITDEPTH_10BPP_FORCEON = 2

# / defines for ADLAdapterConfigMemory of ADL_Adapter_ConfigMemory_Get
# / If this bit is set, it indicates that the Deep Bit Depth pixel is set
# on the display
ADL_ADAPTER_CONFIGMEMORY_DBD = 1 << 0

# / If this bit is set, it indicates that the display is rotated
# (90, 180 or 270)
ADL_ADAPTER_CONFIGMEMORY_ROTATE = 1 << 1

# / If this bit is set, it indicates that passive stereo is set on the
# display
ADL_ADAPTER_CONFIGMEMORY_STEREO_PASSIVE = 1 << 2

# / If this bit is set, it indicates that the active stereo is set on the
# display
ADL_ADAPTER_CONFIGMEMORY_STEREO_ACTIVE = 1 << 3

# / If this bit is set, it indicates that the tear free vsync is set on
# the display
ADL_ADAPTER_CONFIGMEMORY_ENHANCEDVSYNC = 1 << 4
ADL_ADAPTER_CONFIGMEMORY_TEARFREEVSYNC = 1 << 4

# / @}
# / \defgroup define_adl_validmemoryrequiredfields Memory Type
# / @{
# / This group defines memory types in ADLMemoryRequired struct \n
# / Indicates that this is the visible memory
ADL_MEMORYREQTYPE_VISIBLE = 1 << 0

# / Indicates that this is the invisible memory.
ADL_MEMORYREQTYPE_INVISIBLE = 1 << 1

# / Indicates that this is amount of visible memory per GPU that should be
# reserved for all other allocations.
ADL_MEMORYREQTYPE_GPURESERVEDVISIBLE = 1 << 2

# / @}
# / \defgroup define_adapter_tear_free_status
# / Used in ADL_Adapter_TEAR_FREE_Set and ADL_Adapter_TFD_Get functions to
# indicate the tear free
# / desktop status.
# / @{
# / Tear free desktop is enabled.
ADL_ADAPTER_TEAR_FREE_ON = 1

# / Tear free desktop can't be enabled due to a lack of graphic adapter
# memory.
ADL_ADAPTER_TEAR_FREE_NOTENOUGHMEM = -1

# / Tear free desktop can't be enabled due to quad buffer stereo being
# enabled.
ADL_ADAPTER_TEAR_FREE_OFF_ERR_QUADBUFFERSTEREO = -2

# / Tear free desktop can't be enabled due to MGPU-SLS being enabled.
ADL_ADAPTER_TEAR_FREE_OFF_ERR_MGPUSLD = -3

# / Tear free desktop is disabled.
ADL_ADAPTER_TEAR_FREE_OFF = 0

# / @}
# / \defgroup define_adapter_crossdisplay_platforminfo
# / Used in ADL_Adapter_CrossDisplayPlatformInfo_Get function to indicate
# the Crossdisplay platform info.
# / @{
# / CROSSDISPLAY platform.
ADL_CROSSDISPLAY_PLATFORM = 1 << 0

# / CROSSDISPLAY platform for Lasso station.
ADL_CROSSDISPLAY_PLATFORM_LASSO = 1 << 1

# / CROSSDISPLAY platform for docking station.
ADL_CROSSDISPLAY_PLATFORM_DOCKSTATION = 1 << 2

# / @}
# / \defgroup define_adapter_crossdisplay_option
# / Used in ADL_Adapter_CrossdisplayInfoX2_Set function to indicate cross
# display options.
# / @{
# / Checking if 3D application is runnning. If yes, not to do switch,
# return ADL_OK_WAIT; otherwise do switch.
ADL_CROSSDISPLAY_OPTION_NONE = 0

# / Force switching without checking for running 3D applications
ADL_CROSSDISPLAY_OPTION_FORCESWITCH = 1 << 0

# / @}
# / \defgroup define_adapter_states Adapter Capabilities
# / These defines the capabilities supported by an adapter. It is used by
# \ref ADL_Adapter_ConfigureState_Get
# / @{
# / Indicates that the adapter is headless
# (i.e. no displays can be connected to it)
ADL_ADAPTERCONFIGSTATE_HEADLESS = 1 << 2

# / Indicates that the adapter is configured to define the main rendering
# capabilities. For example, adapters
# / in Crossfire(TM) configuration, this bit would only be set on the
# adapter driving the display(s).
ADL_ADAPTERCONFIGSTATE_REQUISITE_RENDER = 1 << 0

# / Indicates that the adapter is configured to be used to unload some of
# the rendering work for a particular
# / requisite rendering adapter. For eample, for adapters in a Crossfire
# configuration, this bit would be set
# / on all adapters that are currently not driving the display(s)
ADL_ADAPTERCONFIGSTATE_ANCILLARY_RENDER = 1 << 1

# / Indicates that scatter gather feature enabled on the adapter
ADL_ADAPTERCONFIGSTATE_SCATTERGATHER = 1 << 4

# / @}
# / \defgroup define_controllermode_ulModifiers
# / These defines the detailed actions supported by set viewport. It is
# used by \ref ADL_Display_ViewPort_Set
# / @{
# / Indicate that the viewport set will change the view position
ADL_CONTROLLERMODE_CM_MODIFIER_VIEW_POSITION = 0x00000001

# / Indicate that the viewport set will change the view PanLock
ADL_CONTROLLERMODE_CM_MODIFIER_VIEW_PANLOCK = 0x00000002

# / Indicate that the viewport set will change the view size
ADL_CONTROLLERMODE_CM_MODIFIER_VIEW_SIZE = 0x00000008

# / @}
# / \defgroup defines for Mirabilis
# / These defines are used for the Mirabilis feature
# / @{
# /
# / Indicates the maximum number of audio sample rates
ADL_MAX_AUDIO_SAMPLE_RATE_COUNT = 16


# / @}
# /////////////////////////////////////////////////////////////////////////
# ADLMultiChannelSplitStateFlag Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLMultiChannelSplitStateFlag(ENUM):
    ADLMultiChannelSplit_Unitialized = EnumItem(0).set_string('Unitilized')
    ADLMultiChannelSplit_Disabled = EnumItem(1).set_string('Disabled')
    ADLMultiChannelSplit_Enabled = EnumItem(2).set_string('Enabled')
    ADLMultiChannelSplit_SaveProfile = EnumItem(3).set_string('Save profile')


ADLMultiChannelSplit_Unitialized = ADLMultiChannelSplitStateFlag.ADLMultiChannelSplit_Unitialized
ADLMultiChannelSplit_Disabled = ADLMultiChannelSplitStateFlag.ADLMultiChannelSplit_Disabled
ADLMultiChannelSplit_Enabled = ADLMultiChannelSplitStateFlag.ADLMultiChannelSplit_Enabled
ADLMultiChannelSplit_SaveProfile = ADLMultiChannelSplitStateFlag.ADLMultiChannelSplit_SaveProfile


# /////////////////////////////////////////////////////////////////////////
# ADLSampleRate Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLSampleRate(ENUM):
    ADLSampleRate_32KHz = EnumItem(0).set_string('32kHz')
    ADLSampleRate_44P1KHz = EnumItem(1).set_string('44.1kHz')
    ADLSampleRate_48KHz = EnumItem(2).set_string('48kHz')
    ADLSampleRate_88P2KHz = EnumItem(3).set_string('88.2kHz')
    ADLSampleRate_96KHz = EnumItem(4).set_string('96kHz')
    ADLSampleRate_176P4KHz = EnumItem(5).set_string('176.4kHz')
    ADLSampleRate_192KHz = EnumItem(6).set_string('192kHz')
    ADLSampleRate_384KHz = EnumItem(7).set_string('384kHz')
    ADLSampleRate_768KHz = EnumItem(8).set_string('768kHz')
    ADLSampleRate_Undefined = EnumItem(9).set_string('Undefined')


ADLSampleRate_32KHz = ADLSampleRate.ADLSampleRate_32KHz
ADLSampleRate_44P1KHz = ADLSampleRate.ADLSampleRate_44P1KHz
ADLSampleRate_48KHz = ADLSampleRate.ADLSampleRate_48KHz
ADLSampleRate_88P2KHz = ADLSampleRate.ADLSampleRate_88P2KHz
ADLSampleRate_96KHz = ADLSampleRate.ADLSampleRate_96KHz
ADLSampleRate_176P4KHz = ADLSampleRate.ADLSampleRate_176P4KHz
ADLSampleRate_192KHz = ADLSampleRate.ADLSampleRate_192KHz
ADLSampleRate_384KHz = ADLSampleRate.ADLSampleRate_384KHz
ADLSampleRate_768KHz = ADLSampleRate.ADLSampleRate_768KHz
ADLSampleRate_Undefined = ADLSampleRate.ADLSampleRate_Undefined

# / \defgroup define_overdrive6_capabilities
# / These defines the capabilities supported by Overdrive 6. It is used by
# \ref ADL_Overdrive6_Capabilities_Get
# @{
# / Indicate that core (engine) clock can be changed.
ADL_OD6_CAPABILITY_SCLK_CUSTOMIZATION = 0x00000001
# / Indicate that memory clock can be changed.
ADL_OD6_CAPABILITY_MCLK_CUSTOMIZATION = 0x00000002
# / Indicate that graphics activity reporting is supported.
ADL_OD6_CAPABILITY_GPU_ACTIVITY_MONITOR = 0x00000004
# / Indicate that power limit can be customized.
ADL_OD6_CAPABILITY_POWER_CONTROL = 0x00000008
# / Indicate that SVI2 Voltage Control is supported.
ADL_OD6_CAPABILITY_VOLTAGE_CONTROL = 0x00000010
# / Indicate that OD6+ percentage adjustment is supported.
ADL_OD6_CAPABILITY_PERCENT_ADJUSTMENT = 0x00000020
# / Indicate that Thermal Limit Unlock is supported.
ADL_OD6_CAPABILITY_THERMAL_LIMIT_UNLOCK = 0x00000040
# /Indicate that Fan speed needs to be displayed in RPM
ADL_OD6_CAPABILITY_FANSPEED_IN_RPM = 0x00000080
# @}
# / \defgroup define_overdrive6_supported_states
# / These defines the power states supported by Overdrive 6. It is used by
# \ref ADL_Overdrive6_Capabilities_Get
# @{
# / Indicate that overdrive is supported in the performance state. This is
# currently the only state supported.
ADL_OD6_SUPPORTEDSTATE_PERFORMANCE = 0x00000001
# / Do not use. Reserved for future use.
ADL_OD6_SUPPORTEDSTATE_POWER_SAVING = 0x00000002
# @}
# / \defgroup define_overdrive6_getstateinfo
# / These defines the power states to get information about. It is used by
# \ref ADL_Overdrive6_StateInfo_Get
# @{
# / Get default clocks for the performance state.
ADL_OD6_GETSTATEINFO_DEFAULT_PERFORMANCE = 0x00000001
# / Do not use. Reserved for future use.
ADL_OD6_GETSTATEINFO_DEFAULT_POWER_SAVING = 0x00000002
# / Get clocks for current state. Currently this is the same as \ref
# ADL_OD6_GETSTATEINFO_CUSTOM_PERFORMANCE
# / since only performance state is supported.
ADL_OD6_GETSTATEINFO_CURRENT = 0x00000003
# / Get the modified clocks (if any) for the performance state. If clocks
# were not modified
# / through Overdrive 6, then this will return the same clocks as \ref
# ADL_OD6_GETSTATEINFO_DEFAULT_PERFORMANCE.
ADL_OD6_GETSTATEINFO_CUSTOM_PERFORMANCE = 0x00000004
# / Do not use. Reserved for future use.
ADL_OD6_GETSTATEINFO_CUSTOM_POWER_SAVING = 0x00000005
# @}
# / \defgroup define_overdrive6_getstate and
# define_overdrive6_getmaxclockadjust
# / These defines the power states to get information about. It is used by
# \ref ADL_Overdrive6_StateEx_Get and \ref
# ADL_Overdrive6_MaxClockAdjust_Get
# @{
# / Get default clocks for the performance state. Only performance state
# is currently supported.
ADL_OD6_STATE_PERFORMANCE = 0x00000001
# @}
# / \defgroup define_overdrive6_setstate
# / These define which power state to set customized clocks on. It is used
# by \ref ADL_Overdrive6_State_Set
# @{
# / Set customized clocks for the performance state.
ADL_OD6_SETSTATE_PERFORMANCE = 0x00000001
# / Do not use. Reserved for future use.
ADL_OD6_SETSTATE_POWER_SAVING = 0x00000002
# @}
# / \defgroup define_overdrive6_thermalcontroller_caps
# / These defines the capabilities of the GPU thermal controller. It is
# used by \ref ADL_Overdrive6_ThermalController_Caps
# @{
# / GPU thermal controller is supported.
ADL_OD6_TCCAPS_THERMAL_CONTROLLER = 0x00000001
# / GPU fan speed control is supported.
ADL_OD6_TCCAPS_FANSPEED_CONTROL = 0x00000002
# / Fan speed percentage can be read.
ADL_OD6_TCCAPS_FANSPEED_PERCENT_READ = 0x00000100
# / Fan speed can be set by specifying a percentage value.
ADL_OD6_TCCAPS_FANSPEED_PERCENT_WRITE = 0x00000200
# / Fan speed RPM (revolutions-per-minute) can be read.
ADL_OD6_TCCAPS_FANSPEED_RPM_READ = 0x00000400
# / Fan speed can be set by specifying an RPM value.
ADL_OD6_TCCAPS_FANSPEED_RPM_WRITE = 0x00000800
# @}
# / \defgroup define_overdrive6_fanspeed_type
# / These defines the fan speed type being reported. It is used by \ref
# ADL_Overdrive6_FanSpeed_Get
# @{
# / Fan speed reported in percentage.
ADL_OD6_FANSPEED_TYPE_PERCENT = 0x00000001
# / Fan speed reported in RPM.
ADL_OD6_FANSPEED_TYPE_RPM = 0x00000002
# / Fan speed has been customized by the user, and fan is not running in
# automatic mode.
ADL_OD6_FANSPEED_USER_DEFINED = 0x00000100
# @}
# / \defgroup define_overdrive_EventCounter_type
# / These defines the EventCounter type being reported. It is used by \ref
# ADL2_OverdriveN_CountOfEvents_Get ,can be used on older OD version
# supported ASICs also.
# @{
ADL_ODN_EVENTCOUNTER_THERMAL = 0
ADL_ODN_EVENTCOUNTER_VPURECOVERY = 1
# @}


# /////////////////////////////////////////////////////////////////////////
# ADLODNControlType Enumeration
# /////////////////////////////////////////////////////////////////////////
class ADLODNControlType(ENUM):
    ODNControlType_Current = EnumItem(0).set_string('Current')
    ODNControlType_Default = EnumItem(1).set_string('Default')
    ODNControlType_Auto = EnumItem(2).set_string('Auto')
    ODNControlType_Manual = EnumItem(3).set_string('Manual')


ODNControlType_Current = ADLODNControlType.ODNControlType_Current
ODNControlType_Default = ADLODNControlType.ODNControlType_Default
ODNControlType_Auto = ADLODNControlType.ODNControlType_Auto
ODNControlType_Manual = ADLODNControlType.ODNControlType_Manual


class ADLODNDPMMaskType(ENUM):
    ADL_ODN_DPM_CLOCK = EnumItem(1 << 0).set_string('Clock')
    ADL_ODN_DPM_VDDC = EnumItem(1 << 1).set_string('VDDC')
    ADL_ODN_DPM_MASK = EnumItem(1 << 2).set_string('Mask')


ADL_ODN_DPM_CLOCK = ADLODNDPMMaskType.ADL_ODN_DPM_CLOCK
ADL_ODN_DPM_VDDC = ADLODNDPMMaskType.ADL_ODN_DPM_VDDC
ADL_ODN_DPM_MASK = ADLODNDPMMaskType.ADL_ODN_DPM_MASK


# ODN features Bits for ADLODNCapabilitiesX2
class ADLODNFeatureControl(ENUM):
    ADL_ODN_SCLK_DPM = EnumItem(1 << 0).set_string('SCLK DPM')
    ADL_ODN_MCLK_DPM = EnumItem(1 << 1).set_string('MCLK DPM')
    ADL_ODN_SCLK_VDD = EnumItem(1 << 2).set_string('SCLK VDD')
    ADL_ODN_MCLK_VDD = EnumItem(1 << 3).set_string('MCLK VDD')
    ADL_ODN_FAN_SPEED_MIN = EnumItem(1 << 4).set_string('Fan speed min')
    ADL_ODN_FAN_SPEED_TARGET = EnumItem(1 << 5).set_string('Fan speed target')
    ADL_ODN_ACOUSTIC_LIMIT_SCLK = EnumItem(1 << 6).set_string('Acoustic limit SCLK')
    ADL_ODN_TEMPERATURE_FAN_MAX = EnumItem(1 << 7).set_string('Temperature fan max')
    ADL_ODN_TEMPERATURE_SYSTEM = EnumItem(1 << 8).set_string('Temperature system')
    ADL_ODN_POWER_LIMIT = EnumItem(1 << 9).set_string('Power limit')
    ADL_ODN_SCLK_AUTO_LIMIT = EnumItem(1 << 10).set_string('SCLK auto limit')
    ADL_ODN_MCLK_AUTO_LIMIT = EnumItem(1 << 11).set_string('MCLK auto limit')
    ADL_ODN_SCLK_DPM_MASK_ENABLE = EnumItem(1 << 12).set_string('SCLK DPM mask enable')
    ADL_ODN_MCLK_DPM_MASK_ENABLE = EnumItem(1 << 13).set_string('MCLK DPM mask enable')
    ADL_ODN_MCLK_UNDERCLOCK_ENABLE = EnumItem(1 << 14).set_string('MCLK underclock enable')
    ADL_ODN_SCLK_DPM_THROTTLE_NOTIFY = EnumItem(1 << 15).set_string('SCLK DPM throttle notify')
    ADL_ODN_POWER_UTILIZATION = EnumItem(1 << 16).set_string('Power utilization')
    ADL_ODN_PERF_TUNING_SLIDER = EnumItem(1 << 17).set_string('Performance tuning slider')
    ADL_ODN_REMOVE_WATTMAN_PAGE = EnumItem(1 << 31).set_string('Remove wattman page')


ADL_ODN_SCLK_DPM = ADLODNFeatureControl.ADL_ODN_SCLK_DPM
ADL_ODN_MCLK_DPM = ADLODNFeatureControl.ADL_ODN_MCLK_DPM
ADL_ODN_SCLK_VDD = ADLODNFeatureControl.ADL_ODN_SCLK_VDD
ADL_ODN_MCLK_VDD = ADLODNFeatureControl.ADL_ODN_MCLK_VDD
ADL_ODN_FAN_SPEED_MIN = ADLODNFeatureControl.ADL_ODN_FAN_SPEED_MIN
ADL_ODN_FAN_SPEED_TARGET = ADLODNFeatureControl.ADL_ODN_FAN_SPEED_TARGET
ADL_ODN_ACOUSTIC_LIMIT_SCLK = ADLODNFeatureControl.ADL_ODN_ACOUSTIC_LIMIT_SCLK
ADL_ODN_TEMPERATURE_FAN_MAX = ADLODNFeatureControl.ADL_ODN_TEMPERATURE_FAN_MAX
ADL_ODN_TEMPERATURE_SYSTEM = ADLODNFeatureControl.ADL_ODN_TEMPERATURE_SYSTEM
ADL_ODN_POWER_LIMIT = ADLODNFeatureControl.ADL_ODN_POWER_LIMIT
ADL_ODN_SCLK_AUTO_LIMIT = ADLODNFeatureControl.ADL_ODN_SCLK_AUTO_LIMIT
ADL_ODN_MCLK_AUTO_LIMIT = ADLODNFeatureControl.ADL_ODN_MCLK_AUTO_LIMIT
ADL_ODN_SCLK_DPM_MASK_ENABLE = ADLODNFeatureControl.ADL_ODN_SCLK_DPM_MASK_ENABLE
ADL_ODN_MCLK_DPM_MASK_ENABLE = ADLODNFeatureControl.ADL_ODN_MCLK_DPM_MASK_ENABLE
ADL_ODN_MCLK_UNDERCLOCK_ENABLE = ADLODNFeatureControl.ADL_ODN_MCLK_UNDERCLOCK_ENABLE
ADL_ODN_SCLK_DPM_THROTTLE_NOTIFY = ADLODNFeatureControl.ADL_ODN_SCLK_DPM_THROTTLE_NOTIFY
ADL_ODN_POWER_UTILIZATION = ADLODNFeatureControl.ADL_ODN_POWER_UTILIZATION
ADL_ODN_PERF_TUNING_SLIDER = ADLODNFeatureControl.ADL_ODN_PERF_TUNING_SLIDER
ADL_ODN_REMOVE_WATTMAN_PAGE = ADLODNFeatureControl.ADL_ODN_REMOVE_WATTMAN_PAGE


# If any new feature is added, PPLIB only needs to add ext feature ID and
# Item ID(Seeting ID). These IDs should match the drive defined in
# CWDDEPM.h
class ADLODNExtFeatureControl(ENUM):
    ADL_ODN_EXT_FEATURE_MEMORY_TIMING_TUNE = EnumItem(1 << 0).set_string('Memory timing tune')
    ADL_ODN_EXT_FEATURE_FAN_ZERO_RPM_CONTROL = EnumItem(1 << 1).set_string('Fan zero rpm control')
    ADL_ODN_EXT_FEATURE_AUTO_UV_ENGINE = EnumItem(1 << 2).set_string('Auto UV engine')
    ADL_ODN_EXT_FEATURE_AUTO_OC_ENGINE = EnumItem(1 << 3).set_string('Auto OC engine')
    ADL_ODN_EXT_FEATURE_AUTO_OC_MEMORY = EnumItem(1 << 4).set_string('Auto OC memory')
    ADL_ODN_EXT_FEATURE_FAN_CURVE = EnumItem(1 << 5).set_string('Fan curve')


ADL_ODN_EXT_FEATURE_MEMORY_TIMING_TUNE = ADLODNExtFeatureControl.ADL_ODN_EXT_FEATURE_MEMORY_TIMING_TUNE
ADL_ODN_EXT_FEATURE_FAN_ZERO_RPM_CONTROL = ADLODNExtFeatureControl.ADL_ODN_EXT_FEATURE_FAN_ZERO_RPM_CONTROL
ADL_ODN_EXT_FEATURE_AUTO_UV_ENGINE = ADLODNExtFeatureControl.ADL_ODN_EXT_FEATURE_AUTO_UV_ENGINE
ADL_ODN_EXT_FEATURE_AUTO_OC_ENGINE = ADLODNExtFeatureControl.ADL_ODN_EXT_FEATURE_AUTO_OC_ENGINE
ADL_ODN_EXT_FEATURE_AUTO_OC_MEMORY = ADLODNExtFeatureControl.ADL_ODN_EXT_FEATURE_AUTO_OC_MEMORY
ADL_ODN_EXT_FEATURE_FAN_CURVE = ADLODNExtFeatureControl.ADL_ODN_EXT_FEATURE_FAN_CURVE


# If any new feature is added, PPLIB only needs to add ext feature ID and
# Item ID(Seeting ID).These IDs should match the drive defined in CWDDEPM.h
class ADLODNExtSettingId(ENUM):
    ADL_ODN_PARAMETER_AC_TIMING = EnumItem(0).set_string('AC timing')
    ADL_ODN_PARAMETER_FAN_ZERO_RPM_CONTROL = EnumItem(1).set_string('Fan zero RPM control')
    ADL_ODN_PARAMETER_AUTO_UV_ENGINE = EnumItem(2).set_string('Auto UV engine')
    ADL_ODN_PARAMETER_AUTO_OC_ENGINE = EnumItem(3).set_string('Auto OC engine')
    ADL_ODN_PARAMETER_AUTO_OC_MEMORY = EnumItem(4).set_string('Auto OC memory')
    ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_1 = EnumItem(5).set_string('Fan curve temperature 1')
    ADL_ODN_PARAMETER_FAN_CURVE_SPEED_1 = EnumItem(6).set_string('Fan curve speed 1')
    ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_2 = EnumItem(7).set_string('Fan curve temperature 2')
    ADL_ODN_PARAMETER_FAN_CURVE_SPEED_2 = EnumItem(8).set_string('Fan curve speed 2')
    ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_3 = EnumItem(9).set_string('Fan curve temperature 3')
    ADL_ODN_PARAMETER_FAN_CURVE_SPEED_3 = EnumItem(10).set_string('Fan curve speed 3')
    ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_4 = EnumItem(11).set_string('Fan curve temperature 4')
    ADL_ODN_PARAMETER_FAN_CURVE_SPEED_4 = EnumItem(12).set_string('Fan curve speed 4')
    ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_5 = EnumItem(13).set_string('Fan curve temperature 5')
    ADL_ODN_PARAMETER_FAN_CURVE_SPEED_5 = EnumItem(14).set_string('Fan curve speed 5')
    ODN_COUNT = EnumItem(15).set_string('ODN count')


ADL_ODN_PARAMETER_AC_TIMING = ADLODNExtSettingId.ADL_ODN_PARAMETER_AC_TIMING
ADL_ODN_PARAMETER_FAN_ZERO_RPM_CONTROL = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_ZERO_RPM_CONTROL
ADL_ODN_PARAMETER_AUTO_UV_ENGINE = ADLODNExtSettingId.ADL_ODN_PARAMETER_AUTO_UV_ENGINE
ADL_ODN_PARAMETER_AUTO_OC_ENGINE = ADLODNExtSettingId.ADL_ODN_PARAMETER_AUTO_OC_ENGINE
ADL_ODN_PARAMETER_AUTO_OC_MEMORY = ADLODNExtSettingId.ADL_ODN_PARAMETER_AUTO_OC_MEMORY
ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_1 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_1
ADL_ODN_PARAMETER_FAN_CURVE_SPEED_1 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_SPEED_1
ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_2 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_2
ADL_ODN_PARAMETER_FAN_CURVE_SPEED_2 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_SPEED_2
ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_3 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_3
ADL_ODN_PARAMETER_FAN_CURVE_SPEED_3 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_SPEED_3
ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_4 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_4
ADL_ODN_PARAMETER_FAN_CURVE_SPEED_4 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_SPEED_4
ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_5 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_TEMPERATURE_5
ADL_ODN_PARAMETER_FAN_CURVE_SPEED_5 = ADLODNExtSettingId.ADL_ODN_PARAMETER_FAN_CURVE_SPEED_5
ODN_COUNT = ADLODNExtSettingId.ODN_COUNT


# OD8 Capability features bits
class ADLOD8FeatureControl(ENUM):
    ADL_OD8_GFXCLK_LIMITS = EnumItem(1 << 0).set_string('GFX Clock Limits')
    ADL_OD8_GFXCLK_CURVE = EnumItem(1 << 1).set_string('GFX Clock Curve')
    ADL_OD8_UCLK_MAX = EnumItem(1 << 2).set_string('UCLK Max')
    ADL_OD8_POWER_LIMIT = EnumItem(1 << 3).set_string('Power Limit')
    ADL_OD8_ACOUSTIC_LIMIT_SCLK = EnumItem(1 << 4).set_string('Acoustioc Limit SCLK')
    ADL_OD8_FAN_SPEED_MIN = EnumItem(1 << 5).set_string('Fan Speed Min')
    ADL_OD8_TEMPERATURE_FAN = EnumItem(1 << 6).set_string('Temperature Fan')
    ADL_OD8_TEMPERATURE_SYSTEM = EnumItem(1 << 7).set_string('Temperature System')
    ADL_OD8_MEMORY_TIMING_TUNE = EnumItem(1 << 8).set_string('Memory Timing Tune')
    ADL_OD8_FAN_ZERO_RPM_CONTROL = EnumItem(1 << 9).set_string('Fan Zero RPM Control')
    ADL_OD8_AUTO_UV_ENGINE = EnumItem(1 << 10).set_string('Auto UV Engine')
    ADL_OD8_AUTO_OC_ENGINE = EnumItem(1 << 11).set_string('Auto OC Engine')
    ADL_OD8_AUTO_OC_MEMORY = EnumItem(1 << 12).set_string('Auto OC Memory')
    ADL_OD8_FAN_CURVE = EnumItem(1 << 13).set_string('Fan Curve')


ADL_OD8_GFXCLK_LIMITS = ADLOD8FeatureControl.ADL_OD8_GFXCLK_LIMITS
ADL_OD8_GFXCLK_CURVE = ADLOD8FeatureControl.ADL_OD8_GFXCLK_CURVE
ADL_OD8_UCLK_MAX = ADLOD8FeatureControl.ADL_OD8_UCLK_MAX
ADL_OD8_POWER_LIMIT = ADLOD8FeatureControl.ADL_OD8_POWER_LIMIT
ADL_OD8_ACOUSTIC_LIMIT_SCLK = ADLOD8FeatureControl.ADL_OD8_ACOUSTIC_LIMIT_SCLK
ADL_OD8_FAN_SPEED_MIN = ADLOD8FeatureControl.ADL_OD8_FAN_SPEED_MIN
ADL_OD8_TEMPERATURE_FAN = ADLOD8FeatureControl.ADL_OD8_TEMPERATURE_FAN
ADL_OD8_TEMPERATURE_SYSTEM = ADLOD8FeatureControl.ADL_OD8_TEMPERATURE_SYSTEM
ADL_OD8_MEMORY_TIMING_TUNE = ADLOD8FeatureControl.ADL_OD8_MEMORY_TIMING_TUNE
ADL_OD8_FAN_ZERO_RPM_CONTROL = ADLOD8FeatureControl.ADL_OD8_FAN_ZERO_RPM_CONTROL
ADL_OD8_AUTO_UV_ENGINE = ADLOD8FeatureControl.ADL_OD8_AUTO_UV_ENGINE
ADL_OD8_AUTO_OC_ENGINE = ADLOD8FeatureControl.ADL_OD8_AUTO_OC_ENGINE
ADL_OD8_AUTO_OC_MEMORY = ADLOD8FeatureControl.ADL_OD8_AUTO_OC_MEMORY
ADL_OD8_FAN_CURVE = ADLOD8FeatureControl.ADL_OD8_FAN_CURVE


class _ADLOD8SettingId(ENUM):
    OD8_GFXCLK_FMAX = EnumItem(0).set_string('GFX Clock FMax')
    OD8_GFXCLK_FMIN = EnumItem(1).set_string('GFX Clock FMin')
    OD8_GFXCLK_FREQ1 = EnumItem(2).set_string('GFX Clock Freq 1')
    OD8_GFXCLK_VOLTAGE1 = EnumItem(3).set_string('GFC Clock Voltage 1')
    OD8_GFXCLK_FREQ2 = EnumItem(4).set_string('GFX Clock Freq 2')
    OD8_GFXCLK_VOLTAGE2 = EnumItem(5).set_string('GFX Clock Voltage 2')
    OD8_GFXCLK_FREQ3 = EnumItem(6).set_string('GFX Clock Freq 3')
    OD8_GFXCLK_VOLTAGE3 = EnumItem(7).set_string('GFX Clock Voltage 3')
    OD8_UCLK_FMAX = EnumItem(8).set_string('U Clock FMax')
    OD8_POWER_PERCENTAGE = EnumItem(9).set_string('Power Percentage')
    OD8_FAN_MIN_SPEED = EnumItem(10).set_string('Fan Min Speed')
    OD8_FAN_ACOUSTIC_LIMIT = EnumItem(11).set_string('Fan Acoustic Limit')
    OD8_FAN_TARGET_TEMP = EnumItem(12).set_string('Fan Target Temperature')
    OD8_OPERATING_TEMP_MAX = EnumItem(13).set_string('Operating Temperature Max')
    OD8_AC_TIMING = EnumItem(14).set_string('AC Timing')
    OD8_FAN_ZERORPM_CONTROL = EnumItem(15).set_string('Fan Zero RPM Control')
    OD8_AUTO_UV_ENGINE_CONTROL = EnumItem(16).set_string('Auto UV Engine Control')
    OD8_AUTO_OC_ENGINE_CONTROL = EnumItem(17).set_string('Auto OC Engine Control')
    OD8_AUTO_OC_MEMORY_CONTROL = EnumItem(18).set_string('Auto OS Memory Control')
    OD8_FAN_CURVE_TEMPERATURE_1 = EnumItem(19).set_string('Fan Curve Temperature 1')
    OD8_FAN_CURVE_SPEED_1 = EnumItem(20).set_string('Fan Curve Speed 1')
    OD8_FAN_CURVE_TEMPERATURE_2 = EnumItem(21).set_string('Fan Curve Temperature 2')
    OD8_FAN_CURVE_SPEED_2 = EnumItem(22).set_string('Fan Curve Speed 2')
    OD8_FAN_CURVE_TEMPERATURE_3 = EnumItem(23).set_string('Fan Curve Temperature 3')
    OD8_FAN_CURVE_SPEED_3 = EnumItem(24).set_string('Fan Curve Speed 3')
    OD8_FAN_CURVE_TEMPERATURE_4 = EnumItem(25).set_string('Fan Curve Temperature 4')
    OD8_FAN_CURVE_SPEED_4 = EnumItem(26).set_string('Fan Curve Speed 4')
    OD8_FAN_CURVE_TEMPERATURE_5 = EnumItem(27).set_string('Fan Curve Temperature 5')
    OD8_FAN_CURVE_SPEED_5 = EnumItem(28).set_string('Fan Curve Speed 5')
    OD8_COUNT = EnumItem(29).set_string('ODN Count')


ADLOD8SettingId = _ADLOD8SettingId
OD8_GFXCLK_FMAX = _ADLOD8SettingId.OD8_GFXCLK_FMAX
OD8_GFXCLK_FMIN = _ADLOD8SettingId.OD8_GFXCLK_FMIN
OD8_GFXCLK_FREQ1 = _ADLOD8SettingId.OD8_GFXCLK_FREQ1
OD8_GFXCLK_VOLTAGE1 = _ADLOD8SettingId.OD8_GFXCLK_VOLTAGE1
OD8_GFXCLK_FREQ2 = _ADLOD8SettingId.OD8_GFXCLK_FREQ2
OD8_GFXCLK_VOLTAGE2 = _ADLOD8SettingId.OD8_GFXCLK_VOLTAGE2
OD8_GFXCLK_FREQ3 = _ADLOD8SettingId.OD8_GFXCLK_FREQ3
OD8_GFXCLK_VOLTAGE3 = _ADLOD8SettingId.OD8_GFXCLK_VOLTAGE3
OD8_UCLK_FMAX = _ADLOD8SettingId.OD8_UCLK_FMAX
OD8_POWER_PERCENTAGE = _ADLOD8SettingId.OD8_POWER_PERCENTAGE
OD8_FAN_MIN_SPEED = _ADLOD8SettingId.OD8_FAN_MIN_SPEED
OD8_FAN_ACOUSTIC_LIMIT = _ADLOD8SettingId.OD8_FAN_ACOUSTIC_LIMIT
OD8_FAN_TARGET_TEMP = _ADLOD8SettingId.OD8_FAN_TARGET_TEMP
OD8_OPERATING_TEMP_MAX = _ADLOD8SettingId.OD8_OPERATING_TEMP_MAX
OD8_AC_TIMING = _ADLOD8SettingId.OD8_AC_TIMING
OD8_FAN_ZERORPM_CONTROL = _ADLOD8SettingId.OD8_FAN_ZERORPM_CONTROL
OD8_AUTO_UV_ENGINE_CONTROL = _ADLOD8SettingId.OD8_AUTO_UV_ENGINE_CONTROL
OD8_AUTO_OC_ENGINE_CONTROL = _ADLOD8SettingId.OD8_AUTO_OC_ENGINE_CONTROL
OD8_AUTO_OC_MEMORY_CONTROL = _ADLOD8SettingId.OD8_AUTO_OC_MEMORY_CONTROL
OD8_FAN_CURVE_TEMPERATURE_1 = _ADLOD8SettingId.OD8_FAN_CURVE_TEMPERATURE_1
OD8_FAN_CURVE_SPEED_1 = _ADLOD8SettingId.OD8_FAN_CURVE_SPEED_1
OD8_FAN_CURVE_TEMPERATURE_2 = _ADLOD8SettingId.OD8_FAN_CURVE_TEMPERATURE_2
OD8_FAN_CURVE_SPEED_2 = _ADLOD8SettingId.OD8_FAN_CURVE_SPEED_2
OD8_FAN_CURVE_TEMPERATURE_3 = _ADLOD8SettingId.OD8_FAN_CURVE_TEMPERATURE_3
OD8_FAN_CURVE_SPEED_3 = _ADLOD8SettingId.OD8_FAN_CURVE_SPEED_3
OD8_FAN_CURVE_TEMPERATURE_4 = _ADLOD8SettingId.OD8_FAN_CURVE_TEMPERATURE_4
OD8_FAN_CURVE_SPEED_4 = _ADLOD8SettingId.OD8_FAN_CURVE_SPEED_4
OD8_FAN_CURVE_TEMPERATURE_5 = _ADLOD8SettingId.OD8_FAN_CURVE_TEMPERATURE_5
OD8_FAN_CURVE_SPEED_5 = _ADLOD8SettingId.OD8_FAN_CURVE_SPEED_5
OD8_COUNT = _ADLOD8SettingId.OD8_COUNT

# Define Performance Metrics Log max sensors number
ADL_PMLOG_MAX_SENSORS = 256

# / \defgroup define_ecc_mode_states
# / These defines the ECC(Error Correction Code) state. It is used by \ref
# ADL_Workstation_ECC_Get,ADL_Workstation_ECC_Set
# @{
# / Error Correction is OFF.
ECC_MODE_OFF = 0
# / Error Correction is ECCV2.
ECC_MODE_ON = 2
# / Error Correction is HBM.
ECC_MODE_HBM = 3
# @}
# / \defgroup define_board_layout_flags
# / These defines are the board layout flags state which indicates what
# are the valid properties of \ref ADLBoardLayoutInfo . It is used by \ref
# ADL_Adapter_BoardLayout_Get
# @{
# / Indicates the number of slots is valid.
ADL_BLAYOUT_VALID_NUMBER_OF_SLOTS = 0x1
# / Indicates the slot sizes are valid. Size of the slot consists of the
# length and width.
ADL_BLAYOUT_VALID_SLOT_SIZES = 0x2
# / Indicates the connector offsets are valid.
ADL_BLAYOUT_VALID_CONNECTOR_OFFSETS = 0x4
# / Indicates the connector lengths is valid.
ADL_BLAYOUT_VALID_CONNECTOR_LENGTHS = 0x8
# @}
# / \defgroup define_max_constants
# / These defines are the maximum value constants.
# @{
# / Indicates the Maximum supported slots on board.
ADL_ADAPTER_MAX_SLOTS = 4
# / Indicates the Maximum supported connectors on slot.
ADL_ADAPTER_MAX_CONNECTORS = 10
# / Indicates the Maximum supported properties of connection
ADL_MAX_CONNECTION_TYPES = 32
# / Indicates the Maximum relative address link count.
ADL_MAX_RELATIVE_ADDRESS_LINK_COUNT = 15
# / Indicates the Maximum size of EDID data block size
ADL_MAX_DISPLAY_EDID_DATA_SIZE = 1024
# / Indicates the Maximum count of Error Records.
ADL_MAX_ERROR_RECORDS_COUNT = 256
# / Indicates the maximum number of power states supported
ADL_MAX_POWER_POLICY = 6
# @}
# / \defgroup define_connection_types
# / These defines are the connection types constants which indicates what
# are the valid connection type of given connector. It is used by \ref
# ADL_Adapter_SupportedConnections_Get
# @{
# / Indicates the VGA connection type is valid.
ADL_CONNECTION_TYPE_VGA = Constant(0).set_string('VGA')
# / Indicates the DVI_I connection type is valid.
ADL_CONNECTION_TYPE_DVI = Constant(1).set_string('DVI-D')
# / Indicates the DVI_SL connection type is valid.
ADL_CONNECTION_TYPE_DVI_SL = Constant(2).set_string('DVI-I')
# / Indicates the HDMI connection type is valid.
ADL_CONNECTION_TYPE_HDMI = Constant(3).set_string('HDMI')
# / Indicates the DISPLAY PORT connection type is valid.
ADL_CONNECTION_TYPE_DISPLAY_PORT = Constant(4).set_string('DisplayPort')
# / Indicates the Active dongle DP.DVI(single link) connection type is
# valid.
ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_SL = Constant(5).set_string('DisplayPort --> DVI-I (active)')
# / Indicates the Active dongle DP.DVI(DOUBLE link) connection type is
# valid.
ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_DVI_DL = Constant(6).set_string('DisplayPort --> DVI-D (active)')
# / Indicates the Active dongle DP.HDMI connection type is valid.
ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_HDMI = Constant(7).set_string('DisplayPort --> HDMI (active)')
# / Indicates the Active dongle DP.VGA connection type is valid.
ADL_CONNECTION_TYPE_ACTIVE_DONGLE_DP_VGA = Constant(8).set_string('DisplayPort --> VGA (active)')
# / Indicates the Passive dongle DP.HDMI connection type is valid.
ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_HDMI = Constant(9).set_string('DisplayPort --> HDMI (passive)')
# / Indicates the Active dongle DP.VGA connection type is valid.
ADL_CONNECTION_TYPE_PASSIVE_DONGLE_DP_DVI = Constant(10).set_string('DisplayPort --> DVI-D (passive)')
# / Indicates the MST type is valid.
ADL_CONNECTION_TYPE_MST = Constant(11).set_string('Display Branch')
# / Indicates the active dongle, all types.
ADL_CONNECTION_TYPE_ACTIVE_DONGLE = Constant(12).set_string('Active Dongle')
# / Indicates the Virtual Connection Type.
ADL_CONNECTION_TYPE_VIRTUAL = Constant(13).set_string('Virtual')


# / Macros for generating bitmask from index.
def ADL_CONNECTION_BITMAST_FROM_INDEX(index):
    return 1 << index
# @}


# / \defgroup define_connection_properties
# / These defines are the connection properties which indicates what are
# the valid properties of given connection type. It is used by \ref
# ADL_Adapter_SupportedConnections_Get
# @{
# / Indicates the property Bitrate is valid.
ADL_CONNECTION_PROPERTY_BITRATE = 0x1
# / Indicates the property number of lanes is valid.
ADL_CONNECTION_PROPERTY_NUMBER_OF_LANES = 0x2
# / Indicates the property 3D caps is valid.
ADL_CONNECTION_PROPERTY_3DCAPS = 0x4
# / Indicates the property output bandwidth is valid.
ADL_CONNECTION_PROPERTY_OUTPUT_BANDWIDTH = 0x8
# / Indicates the property colordepth is valid.
ADL_CONNECTION_PROPERTY_COLORDEPTH = 0x10
# @}
# / \defgroup define_lanecount_constants
# / These defines are the Lane count constants which will be used in DP &
# etc.
# @{
# / Indicates if lane count is unknown
ADL_LANECOUNT_UNKNOWN = 0
# / Indicates if lane count is 1
ADL_LANECOUNT_ONE = 1
# / Indicates if lane count is 2
ADL_LANECOUNT_TWO = 2
# / Indicates if lane count is 4
ADL_LANECOUNT_FOUR = 4
# / Indicates if lane count is 8
ADL_LANECOUNT_EIGHT = 8
# / Indicates default value of lane count
ADL_LANECOUNT_DEF = ADL_LANECOUNT_FOUR
# @}
# / \defgroup define_linkrate_constants
# / These defines are the link rate constants which will be used in DP &
# etc.
# @{
# / Indicates if link rate is unknown
ADL_LINK_BITRATE_UNKNOWN = Constant(0).set_string('Unknown')
# / Indicates if link rate is 1.62Ghz
ADL_LINK_BITRATE_1_62_GHZ = Constant(0x06).set_string('1.62GHz')
# / Indicates if link rate is 2.7Ghz
ADL_LINK_BITRATE_2_7_GHZ = Constant(0x0A).set_string('2.7GHz')
# / Indicates if link rate is 3.24Ghz
ADL_LINK_BTIRATE_3_24_GHZ = Constant(0x0C).set_string('3.24GHz')
# / Indicates if link rate is 5.4Ghz
ADL_LINK_BITRATE_5_4_GHZ = Constant(0x14).set_string('5.4GHz')
# / Indicates default value of link rate
ADL_LINK_BITRATE_DEF = ADL_LINK_BITRATE_2_7_GHZ
# @}
# / \defgroup define_colordepth_constants
# / These defines are the color depth constants which will be used in DP &
# etc.
# @{
ADL_CONNPROP_S3D_ALTERNATE_TO_FRAME_PACK = Constant(0x00000001).set_string('Alternate Frame Pack')
# @}
# / \defgroup define_colordepth_constants
# / These defines are the color depth constants which will be used in DP &
# etc.
# @{
# / Indicates if color depth is unknown
ADL_COLORDEPTH_UNKNOWN = Constant(0).set_string('Unknown')
# / Indicates if color depth is 666
ADL_COLORDEPTH_666 = Constant(1).set_string('6bit')
# / Indicates if color depth is 888
ADL_COLORDEPTH_888 = Constant(2).set_string('8bit')
# / Indicates if color depth is 101010
ADL_COLORDEPTH_101010 = Constant(3).set_string('10bit')
# / Indicates if color depth is 121212
ADL_COLORDEPTH_121212 = Constant(4).set_string('12bit')
# / Indicates if color depth is 141414
ADL_COLORDEPTH_141414 = Constant(5).set_string('14bit')
# / Indicates if color depth is 161616
ADL_COLORDEPTH_161616 = Constant(6).set_string('16bit')
# / Indicates default value of color depth
ADL_COLOR_DEPTH_DEF = ADL_COLORDEPTH_888
# @}
# / \defgroup define_emulation_status
# / These defines are the status of emulation
# @{
# / Indicates if real device is connected.
ADL_EMUL_STATUS_REAL_DEVICE_CONNECTED = Constant(0x1).set_string('Real Device Connected')
# / Indicates if emulated device is presented.
ADL_EMUL_STATUS_EMULATED_DEVICE_PRESENT = Constant(0x2).set_string('Emulated Device Present')
# / Indicates if emulated device is used.
ADL_EMUL_STATUS_EMULATED_DEVICE_USED = Constant(0x4).set_string('Emulated Device Used')
# / In case when last active real/emulated device used
# (when persistence is enabled but no emulation enforced then persistence will use last connected/emulated device).
# 
ADL_EMUL_STATUS_LAST_ACTIVE_DEVICE_USED = Constant(0x8).set_string('Last Active Device Used')
# @}
# / \defgroup define_emulation_mode
# / These defines are the modes of emulation
# @{
# / Indicates if no emulation is used
ADL_EMUL_MODE_OFF = Constant(0).set_string('Off')
# / Indicates if emulation is used when display connected
ADL_EMUL_MODE_ON_CONNECTED = Constant(1).set_string('Display Connected')
# / Indicates if emulation is used when display dis connected
ADL_EMUL_MODE_ON_DISCONNECTED = Constant(2).set_string('Display Disconnected')
# / Indicates if emulation is used always
ADL_EMUL_MODE_ALWAYS = Constant(3).set_string('Always')
# @}
# / \defgroup define_emulation_query
# / These defines are the modes of emulation
# @{
# / Indicates Data from real device
ADL_QUERY_REAL_DATA = 0
# / Indicates Emulated data
ADL_QUERY_EMULATED_DATA = 1
# / Indicates Data currently in use
ADL_QUERY_CURRENT_DATA = 2
# @}
# / \defgroup define_persistence_state
# / These defines are the states of persistence
# @{
# / Indicates persistence is disabled
ADL_EDID_PERSISTANCE_DISABLED = 0
# / Indicates persistence is enabled
ADL_EDID_PERSISTANCE_ENABLED = 1
# @}
# / \defgroup define_connector_types Connector Type
# / defines for ADLConnectorInfo.iType
# @{
# / Indicates unknown Connector type
ADL_CONNECTOR_TYPE_UNKNOWN = Constant(0).set_string('Unknown')
# / Indicates VGA Connector type
ADL_CONNECTOR_TYPE_VGA = Constant(1).set_string('VGA')
# / Indicates DVI-D Connector type
ADL_CONNECTOR_TYPE_DVI_D = Constant(2).set_string('DVI-D')
# / Indicates DVI-I Connector type
ADL_CONNECTOR_TYPE_DVI_I = Constant(3).set_string('DVI-I')
# / Indicates Active Dongle-NA Connector type
ADL_CONNECTOR_TYPE_ATICVDONGLE_NA = Constant(4).set_string('Active Dongle-NA')
# / Indicates Active Dongle-JP Connector type
ADL_CONNECTOR_TYPE_ATICVDONGLE_JP = Constant(5).set_string('Active Dongle-JP')
# / Indicates Active Dongle-NONI2C Connector type
ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C = Constant(6).set_string('Active Dongle-NONI2C')
# / Indicates Active Dongle-NONI2C-D Connector type
ADL_CONNECTOR_TYPE_ATICVDONGLE_NONI2C_D = Constant(7).set_string('Active Dongle-NONI2C-D')
# / Indicates HDMI-Type A Connector type
ADL_CONNECTOR_TYPE_HDMI_TYPE_A = Constant(8).set_string('HDMI-Type A')
# / Indicates HDMI-Type B Connector type
ADL_CONNECTOR_TYPE_HDMI_TYPE_B = Constant(9).set_string(' HDMI-Type B')
# / Indicates Display port Connector type
ADL_CONNECTOR_TYPE_DISPLAYPORT = Constant(10).set_string('DisplayPort')
# / Indicates EDP Connector type
ADL_CONNECTOR_TYPE_EDP = Constant(11).set_string('EDP')
# / Indicates MiniDP Connector type
ADL_CONNECTOR_TYPE_MINI_DISPLAYPORT = Constant(12).set_string('DisplayPort (Mini)')
# / Indicates Virtual Connector type
ADL_CONNECTOR_TYPE_VIRTUAL = Constant(13).set_string('Virtual')
# @}
# / \defgroup define_freesync_usecase
# / These defines are to specify use cases in which FreeSync should be
# enabled
# / They are a bit mask. To specify FreeSync for more than one use case,
# the input value
# / should be set to include multiple bits set
# @{
# / Indicates FreeSync is enabled for Static Screen case
ADL_FREESYNC_USECASE_STATIC = Constant(0x1).set_string('Static')
# / Indicates FreeSync is enabled for Video use case
ADL_FREESYNC_USECASE_VIDEO = Constant(0x2).set_string('Video')
# / Indicates FreeSync is enabled for Gaming use case
ADL_FREESYNC_USECASE_GAMING = Constant(0x4).set_string('Gaming')
# @}
# / \defgroup define_freesync_caps
# / These defines are used to retrieve FreeSync display capabilities.
# / GPU support flag also indicates whether the display is
# / connected to a GPU that actually supports FreeSync
# @{
ADL_FREESYNC_CAP_SUPPORTED = 1 << 0
ADL_FREESYNC_CAP_GPUSUPPORTED = 1 << 1
ADL_FREESYNC_CAP_DISPLAYSUPPORTED = 1 << 2
ADL_FREESYNC_CAP_CURRENTMODESUPPORTED = 1 << 3
ADL_FREESYNC_CAP_NOCFXORCFXSUPPORTED = 1 << 4
ADL_FREESYNC_CAP_NOGENLOCKORGENLOCKSUPPORTED = 1 << 5
ADL_FREESYNC_CAP_BORDERLESSWINDOWSUPPORTED = 1 << 6
# @}
# / \defgroup define_MST_CommandLine_execute
# @{
# / Indicates the MST command line for branch message if the bit is set.
# Otherwise, it is display message
ADL_MST_COMMANDLINE_PATH_MSG = 0x1
# / Indicates the MST command line to send message in broadcast way it the
# bit is set
ADL_MST_COMMANDLINE_BROADCAST = 0x2
# @}
# / \defgroup define_Adapter_CloneTypes_Get
# @{
# / Indicates there is crossGPU clone with non-AMD dispalys
ADL_CROSSGPUDISPLAYCLONE_AMD_WITH_NONAMD = 0x1
# / Indicates there is crossGPU clone
ADL_CROSSGPUDISPLAYCLONE = 0x2
# @}
# / \defgroup define_D3DKMT_HANDLE
# @{
# / Handle can be used to create Device Handle when using CreateDevice()
ADL_D3DKMT_HANDLE = UINT
# @}
# End Bracket for Constants and Definitions. Add new groups ABOVE this
# linenot
# @}# END IF  ADL_DEFINES_H_
