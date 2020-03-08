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


ADL2_ADAPTER_ACTIVE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_ACTIVE_SET = int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_ACTIVE_SETPREFER = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT)
)
ADL_ADAPTER_ACTIVE_SETPREFER = int(
    INT,
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT)
)
ADL2_ADAPTER_PRIMARY_GET = int(
    ADL_CONTEXT_HANDLE,
    POINTER(INT)
)
ADL_ADAPTER_PRIMARY_GET = int(
    POINTER(INT)
)
ADL2_ADAPTER_PRIMARY_SET = int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_ADAPTER_PRIMARY_SET = int(
    INT
)
ADL2_ADAPTER_MODESWITCH = int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_ADAPTER_MODESWITCH = int(
    INT
)
ADL2_DISPLAY_MODES_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL_DISPLAY_MODES_GET = int(
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL2_DISPLAY_MODES_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLMode)
)
ADL_DISPLAY_MODES_SET = int(
    INT,
    INT,
    INT,
    POINTER(ADLMode)
)
ADL2_DISPLAY_POSSIBLEMODE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL_DISPLAY_POSSIBLEMODE_GET = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL2_DISPLAY_FORCIBLEDISPLAY_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_FORCIBLEDISPLAY_GET = int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_FORCIBLEDISPLAY_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_FORCIBLEDISPLAY_SET = int(
    INT,
    INT,
    INT
)
ADL2_ADAPTER_NUMBEROFACTIVATABLESOURCES_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLActivatableSource))
)
ADL_ADAPTER_NUMBEROFACTIVATABLESOURCES_GET = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLActivatableSource))
)
ADL2_ADAPTER_DISPLAY_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLAdapterDisplayCap))
)
ADL_ADAPTER_DISPLAY_CAPS = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLAdapterDisplayCap))
)
ADL2_DISPLAY_DISPLAYMAPCONFIG_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayMap)),
    POINTER(INT),
    POINTER(POINTER(ADLDisplayTarget)),
    INT
)
ADL_DISPLAY_DISPLAYMAPCONFIG_GET = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayMap)),
    POINTER(INT),
    POINTER(POINTER(ADLDisplayTarget)),
    INT
)
ADL2_DISPLAY_DISPLAYMAPCONFIG_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayMap),
    INT,
    POINTER(ADLDisplayTarget)
)
ADL_DISPLAY_DISPLAYMAPCONFIG_SET = int(
    INT,
    INT,
    POINTER(ADLDisplayMap),
    INT,
    POINTER(ADLDisplayTarget)
)
ADL2_DISPLAY_POSSIBLEMAPPING_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLPossibleMapping),
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLPossibleMapping))
)
ADL_DISPLAY_POSSIBLEMAPPING_GET = int(
    INT,
    INT,
    POINTER(ADLPossibleMapping),
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLPossibleMapping))
)
ADL2_DISPLAY_DISPLAYMAPCONFIG_VALIDATE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLPossibleMap),
    POINTER(INT),
    POINTER(POINTER(ADLPossibleMapResult))
)
ADL_DISPLAY_DISPLAYMAPCONFIG_VALIDATE = int(
    INT,
    INT,
    POINTER(ADLPossibleMap),
    POINTER(INT),
    POINTER(POINTER(ADLPossibleMapResult))
)
ADL2_DISPLAY_DISPLAYMAPCONFIG_POSSIBLEADDANDREMOVE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayMap),
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT),
    POINTER(POINTER(ADLDisplayTarget)),
    POINTER(INT),
    POINTER(POINTER(ADLDisplayTarget))
)
ADL_DISPLAY_DISPLAYMAPCONFIG_POSSIBLEADDANDREMOVE = int(
    INT,
    INT,
    POINTER(ADLDisplayMap),
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT),
    POINTER(POINTER(ADLDisplayTarget)),
    POINTER(INT),
    POINTER(POINTER(ADLDisplayTarget))
)
ADL2_DISPLAY_SLSGRID_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLSLSGrid)),
    INT
)
ADL_DISPLAY_SLSGRID_CAPS = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLSLSGrid)),
    INT
)
ADL2_DISPLAY_SLSMAPINDEXLIST_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(INT)),
    INT
)
ADL_DISPLAY_SLSMAPINDEXLIST_GET = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(INT)),
    INT
)
ADL2_DISPLAY_SLSMAPINDEX_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT)
)
ADL_DISPLAY_SLSMAPINDEX_GET = int(
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT)
)
ADL2_DISPLAY_SLSMAPCONFIGX2_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLSLSMap),
    POINTER(INT),
    POINTER(POINTER(ADLSLSTarget)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSOffset)),
    POINTER(INT),
    POINTER(POINTER(ADLBezelTransientMode)),
    POINTER(INT),
    POINTER(POINTER(ADLBezelTransientMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSOffset)),
    INT
)
ADL_DISPLAY_SLSMAPCONFIGX2_GET = int(
    INT,
    INT,
    POINTER(ADLSLSMap),
    POINTER(INT),
    POINTER(POINTER(ADLSLSTarget)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSOffset)),
    POINTER(INT),
    POINTER(POINTER(ADLBezelTransientMode)),
    POINTER(INT),
    POINTER(POINTER(ADLBezelTransientMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSOffset)),
    INT
)
ADL2_DISPLAY_SLSMAPCONFIG_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLSLSMap),
    POINTER(INT),
    POINTER(POINTER(ADLSLSTarget)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    POINTER(INT),
    POINTER(POINTER(ADLBezelTransientMode)),
    POINTER(INT),
    POINTER(POINTER(ADLBezelTransientMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSOffset)),
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_GET = int(
    INT,
    INT,
    POINTER(ADLSLSMap),
    POINTER(INT),
    POINTER(POINTER(ADLSLSTarget)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    POINTER(INT),
    POINTER(POINTER(ADLBezelTransientMode)),
    POINTER(INT),
    POINTER(POINTER(ADLBezelTransientMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSOffset)),
    INT
)
ADL2_DISPLAY_SLSMAPCONFIG_CREATE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLSLSMap,
    INT,
    POINTER(ADLSLSTarget),
    INT,
    POINTER(INT),
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_CREATE = int(
    INT,
    ADLSLSMap,
    INT,
    POINTER(ADLSLSTarget),
    INT,
    POINTER(INT),
    INT
)
ADL2_DISPLAY_SLSMAPCONFIG_DELETE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_DELETE = int(
    INT,
    INT
)
ADL2_DISPLAY_SLSMAPCONFIGX2_DELETE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_SLSMAPCONFIG_SETSTATE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_SETSTATE = int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_SLSMAPCONFIG_REARRANGE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLSLSTarget),
    ADLSLSMap,
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_REARRANGE = int(
    INT,
    INT,
    INT,
    POINTER(ADLSLSTarget),
    ADLSLSMap,
    INT
)
ADL2_DISPLAY_POSSIBLEMODE_WINXP_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL_DISPLAY_POSSIBLEMODE_WINXP_GET = int(
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL2_DISPLAY_BEZELOFFSETSTEPPINGSIZE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLBezelOffsetSteppingSize))
)
ADL_DISPLAY_BEZELOFFSETSTEPPINGSIZE_GET = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLBezelOffsetSteppingSize))
)
ADL2_DISPLAY_BEZELOFFSET_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    LPADLSLSOffset,
    ADLSLSMap,
    INT
)
ADL_DISPLAY_BEZELOFFSET_SET = int(
    INT,
    INT,
    INT,
    LPADLSLSOffset,
    ADLSLSMap,
    INT
)
ADL2_DISPLAY_BEZELSUPPORTED_VALIDATE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    LPADLPossibleSLSMap,
    POINTER(INT),
    POINTER(LPADLPossibleMapResult)
)
ADL_DISPLAY_BEZELSUPPORTED_VALIDATE = int(
    INT,
    INT,
    LPADLPossibleSLSMap,
    POINTER(INT),
    POINTER(LPADLPossibleMapResult)
)
ADL2_DISPLAY_OVERLAP_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    LPADLSLSTargetOverlap,
    INT,
    LPADLSLSOffset,
    ADLSLSMap
)
ADL_DISPLAY_OVERLAP_SET = int(
    INT,
    INT,
    INT,
    LPADLSLSTargetOverlap,
    INT,
    LPADLSLSOffset,
    ADLSLSMap
)
ADL2_DISPLAY_SLSMIDDLEMODE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    INT
)
ADL_DISPLAY_SLSMIDDLEMODE_GET = int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    POINTER(INT),
    POINTER(POINTER(ADLSLSMode)),
    INT
)
ADL2_DISPLAY_SLSMIDDLEMODE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLSLSMode),
    INT
)
ADL_DISPLAY_SLSMIDDLEMODE_SET = int(
    INT,
    INT,
    INT,
    POINTER(ADLSLSMode),
    INT
)
ADL2_WORKSTATION_ENABLEUNSUPPORTEDDISPLAYMODES = int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_WORKSTATION_ENABLEUNSUPPORTEDDISPLAYMODES = int(
    INT
)
ADL2_DISPLAY_SLSRECORDS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDisplayID,
    POINTER(INT),
    POINTER(POINTER(INT))
)
ADL_DISPLAY_SLSRECORDS_GET = int(
    INT,
    ADLDisplayID,
    POINTER(INT),
    POINTER(POINTER(INT))
)
ADL2_ADAPTER_AMDANDNONAMDDISPLAYCLONE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_CLONETYPES_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_CROSSGPUCLONE_DISABLE = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)


# Function to set the current extended desktop mode status for a display.
_ADL2_Adapter_Active_Set = ADL2_ADAPTER_ACTIVE_SET

# Function to set the current extended desktop mode status for a display.
_ADL_Adapter_Active_Set = ADL_ADAPTER_ACTIVE_SET

# Function to set the current extended desktop mode status for the display.
_ADL2_Adapter_Active_SetPrefer = ADL2_ADAPTER_ACTIVE_SETPREFER

# Function to set the current extended desktop mode status for the display.
_ADL_Adapter_Active_SetPrefer = ADL_ADAPTER_ACTIVE_SETPREFER

# Function to retrieve the primary display adapter index.
_ADL2_Adapter_Primary_Get = ADL2_ADAPTER_PRIMARY_GET

# Function to retrieve the primary display adapter index.
_ADL_Adapter_Primary_Get = ADL_ADAPTER_PRIMARY_GET

# Function to set the primary display adapter index.
_ADL2_Adapter_Primary_Set = ADL2_ADAPTER_PRIMARY_SET

# Function to set the primary display adapter index.
_ADL_Adapter_Primary_Set = ADL_ADAPTER_PRIMARY_SET

# Function to perform a mode switch for an adapter.
_ADL2_Adapter_ModeSwitch = ADL2_ADAPTER_MODESWITCH

# Function to perform a mode switch for an adapter.
_ADL_Adapter_ModeSwitch = ADL_ADAPTER_MODESWITCH

# Function to retrieve the display mode information.
_ADL2_Display_Modes_Get = ADL2_DISPLAY_MODES_GET

# Function to retrieve the display mode information.
_ADL_Display_Modes_Get = ADL_DISPLAY_MODES_GET

# Function to set display mode information.
_ADL2_Display_Modes_Set = ADL2_DISPLAY_MODES_SET

# Function to set display mode information.
_ADL_Display_Modes_Set = ADL_DISPLAY_MODES_SET

# Function to retrieve the OS possible modes list for an adapter (all OS platforms).
_ADL2_Display_PossibleMode_Get = ADL2_DISPLAY_POSSIBLEMODE_GET

# Function to retrieve the OS possible modes list for an adapter (all OS platforms).
_ADL_Display_PossibleMode_Get = ADL_DISPLAY_POSSIBLEMODE_GET

# Function to retrieve the forcible connected status of a display.
_ADL2_Display_ForcibleDisplay_Get = ADL2_DISPLAY_FORCIBLEDISPLAY_GET

# Function to retrieve the forcible connected status of a display.
_ADL_Display_ForcibleDisplay_Get = ADL_DISPLAY_FORCIBLEDISPLAY_GET

# Function to set the forcible connected status of a display.
_ADL2_Display_ForcibleDisplay_Set = ADL2_DISPLAY_FORCIBLEDISPLAY_SET

# Function to set the forcible connected status of a display.
_ADL_Display_ForcibleDisplay_Set = ADL_DISPLAY_FORCIBLEDISPLAY_SET

# Function to retrieve the number of Activatable sources based on ADL Index.
_ADL2_Adapter_NumberOfActivatableSources_Get = ADL2_ADAPTER_NUMBEROFACTIVATABLESOURCES_GET

# Function to retrieve the number of Activatable sources based on ADL Index.
_ADL_Adapter_NumberOfActivatableSources_Get = ADL_ADAPTER_NUMBEROFACTIVATABLESOURCES_GET

# Function to retrieve the adapter display manner capabilities based on ADL index.
_ADL2_Adapter_Display_Caps = ADL2_ADAPTER_DISPLAY_CAPS

# Function to retrieve the adapter display manner capabilities based on ADL index.
_ADL_Adapter_Display_Caps = ADL_ADAPTER_DISPLAY_CAPS

# Function to retrieve current display map configurations.
_ADL2_Display_DisplayMapConfig_Get = ADL2_DISPLAY_DISPLAYMAPCONFIG_GET

# Function to retrieve current display map configurations.
_ADL_Display_DisplayMapConfig_Get = ADL_DISPLAY_DISPLAYMAPCONFIG_GET

# Function to set the current display configuration.
_ADL2_Display_DisplayMapConfig_Set = ADL2_DISPLAY_DISPLAYMAPCONFIG_SET

# Function to set the current display configuration.
_ADL_Display_DisplayMapConfig_Set = ADL_DISPLAY_DISPLAYMAPCONFIG_SET

# Function to retrieve the possible display mappings.
_ADL2_Display_PossibleMapping_Get = ADL2_DISPLAY_POSSIBLEMAPPING_GET

# Function to retrieve the possible display mappings.
_ADL_Display_PossibleMapping_Get = ADL_DISPLAY_POSSIBLEMAPPING_GET

# Function to validate the list of the display configurations based on ADL Index.
_ADL2_Display_DisplayMapConfig_Validate = ADL2_DISPLAY_DISPLAYMAPCONFIG_VALIDATE

# Function to validate the list of the display configurations based on ADL Index.
_ADL_Display_DisplayMapConfig_Validate = ADL_DISPLAY_DISPLAYMAPCONFIG_VALIDATE

# Function to validate a list of display configurations.
_ADL2_Display_DisplayMapConfig_PossibleAddAndRemove = ADL2_DISPLAY_DISPLAYMAPCONFIG_POSSIBLEADDANDREMOVE

# Function to validate a list of display configurations.
_ADL_Display_DisplayMapConfig_PossibleAddAndRemove = ADL_DISPLAY_DISPLAYMAPCONFIG_POSSIBLEADDANDREMOVE

# Function to get the current supported SLS grid patterns (MxN) for a GPU.
_ADL2_Display_SLSGrid_Caps = ADL2_DISPLAY_SLSGRID_CAPS

# Function to get the current supported SLS grid patterns (MxN) for a GPU.
_ADL_Display_SLSGrid_Caps = ADL_DISPLAY_SLSGRID_CAPS

# Function to get the active SLS map index list for a given GPU.
_ADL2_Display_SLSMapIndexList_Get = ADL2_DISPLAY_SLSMAPINDEXLIST_GET

# Function to get the active SLS map index list for a given GPU.
_ADL_Display_SLSMapIndexList_Get = ADL_DISPLAY_SLSMAPINDEXLIST_GET

# Function to get the SLS map index for a given adapter and a given display device.
_ADL2_Display_SLSMapIndex_Get = ADL2_DISPLAY_SLSMAPINDEX_GET

# Function to get the SLS map index for a given adapter and a given display device.
_ADL_Display_SLSMapIndex_Get = ADL_DISPLAY_SLSMAPINDEX_GET

# Function to retrieve an SLS configuration.
_ADL2_Display_SLSMapConfigX2_Get = ADL2_DISPLAY_SLSMAPCONFIGX2_GET

# Function to retrieve an SLS configuration.
_ADL_Display_SLSMapConfigX2_Get = ADL_DISPLAY_SLSMAPCONFIGX2_GET

# Function to retrieve an SLS configuration.
_ADL2_Display_SLSMapConfig_Get = ADL2_DISPLAY_SLSMAPCONFIG_GET

# Function to retrieve an SLS configuration.
_ADL_Display_SLSMapConfig_Get = ADL_DISPLAY_SLSMAPCONFIG_GET

# Function to create an SLS configuration.
_ADL2_Display_SLSMapConfig_Create = ADL2_DISPLAY_SLSMAPCONFIG_CREATE

# Function to create an SLS configuration.
_ADL_Display_SLSMapConfig_Create = ADL_DISPLAY_SLSMAPCONFIG_CREATE

# Function to delete an SLS map from the driver database.
_ADL2_Display_SLSMapConfig_Delete = ADL2_DISPLAY_SLSMAPCONFIG_DELETE

# Function to delete an SLS map from the driver database.
_ADL_Display_SLSMapConfig_Delete = ADL_DISPLAY_SLSMAPCONFIG_DELETE

# Function to delete an list of SLS map indexes from the driver database.
_ADL2_Display_SLSMapConfigX2_Delete = ADL2_DISPLAY_SLSMAPCONFIGX2_DELETE

# Function to enable/disable SLS bind.
_ADL2_Display_SLSMapConfig_SetState = ADL2_DISPLAY_SLSMAPCONFIG_SETSTATE

# Function to enable/disable SLS bind.
_ADL_Display_SLSMapConfig_SetState = ADL_DISPLAY_SLSMAPCONFIG_SETSTATE

# Function to rearrange display orders in an SLS map.
_ADL2_Display_SLSMapConfig_Rearrange = ADL2_DISPLAY_SLSMAPCONFIG_REARRANGE

# Function to rearrange display orders in an SLS map.
_ADL_Display_SLSMapConfig_Rearrange = ADL_DISPLAY_SLSMAPCONFIG_REARRANGE

# Function to retrieve the ATI possible modes list for an adapter and preset mapping (Windows XP).
_ADL2_Display_PossibleMode_WinXP_Get = ADL2_DISPLAY_POSSIBLEMODE_WINXP_GET

# Function to retrieve the ATI possible modes list for an adapter and preset mapping (Windows XP).
_ADL_Display_PossibleMode_WinXP_Get = ADL_DISPLAY_POSSIBLEMODE_WINXP_GET

# Get bezel offset stepping size for the input adapter.
_ADL2_Display_BezelOffsetSteppingSize_Get = ADL2_DISPLAY_BEZELOFFSETSTEPPINGSIZE_GET

# Get bezel offset stepping size for the input adapter.
_ADL_Display_BezelOffsetSteppingSize_Get = ADL_DISPLAY_BEZELOFFSETSTEPPINGSIZE_GET

# Set SLS bezel offsets for each display index.
_ADL2_Display_BezelOffset_Set = ADL2_DISPLAY_BEZELOFFSET_SET

# Set SLS bezel offsets for each display index.
_ADL_Display_BezelOffset_Set = ADL_DISPLAY_BEZELOFFSET_SET

# Validate the list of the SLS display configurations to determine if bezel is supported or not.
_ADL2_Display_BezelSupported_Validate = ADL2_DISPLAY_BEZELSUPPORTED_VALIDATE

# Validate the list of the SLS display configurations to determine if bezel is supported or not.
_ADL_Display_BezelSupported_Validate = ADL_DISPLAY_BEZELSUPPORTED_VALIDATE

# Set SLS overlap offsets for each display index.
_ADL2_Display_Overlap_Set = ADL2_DISPLAY_OVERLAP_SET

# Set SLS overlap offsets for each display index.
_ADL_Display_Overlap_Set = ADL_DISPLAY_OVERLAP_SET

# Get SLS middle mode for specific adapter.
_ADL2_Display_SLSMiddleMode_Get = ADL2_DISPLAY_SLSMIDDLEMODE_GET

# Get SLS middle mode for specific adapter.
_ADL_Display_SLSMiddleMode_Get = ADL_DISPLAY_SLSMIDDLEMODE_GET

# Set SLS middle mode for specific adapter.
_ADL2_Display_SLSMiddleMode_Set = ADL2_DISPLAY_SLSMIDDLEMODE_SET

# Set SLS middle mode for specific adapter.
_ADL_Display_SLSMiddleMode_Set = ADL_DISPLAY_SLSMIDDLEMODE_SET

# Function to set the Registry key "UnsupportedMonitorModesAllowed" when 10bit 
# Pixel format is enabled from workstation aspect.
_ADL2_Workstation_EnableUnsupportedDisplayModes = ADL2_WORKSTATION_ENABLEUNSUPPORTEDDISPLAYMODES

# Function to set the Registry key "UnsupportedMonitorModesAllowed" when 10bit Pixel 
# format is enabled from workstation aspect.
_ADL_Workstation_EnableUnsupportedDisplayModes = ADL_WORKSTATION_ENABLEUNSUPPORTEDDISPLAYMODES

# Function to Get an SLS records from the driver database.
_ADL2_Display_SLSRecords_Get = ADL2_DISPLAY_SLSRECORDS_GET

# Function to Get an SLS records from the driver database.
_ADL_Display_SLSRecords_Get = ADL_DISPLAY_SLSRECORDS_GET

# ADL local interface. Retrieves GPU information of any AMD and non-AMD 
# displays cloned for given GPU or all OS-known GPUs.
_ADL2_Adapter_AMDAndNonAMDDIsplayClone_Get = ADL2_ADAPTER_AMDANDNONAMDDISPLAYCLONE_GET

# ADL local interface. Retrieves GPU information of special clone types for given GPU or all OS-known GPUs.
_ADL2_Adapter_CloneTypes_Get = ADL2_ADAPTER_CLONETYPES_GET

# ADL local interface. Disable all cross-GPU clone for given GPU or all OS-known GPUs.
_ADL2_Adapter_CrossGPUClone_Disable = ADL2_ADAPTER_CROSSGPUCLONE_DISABLE


def Init(hDLL):
    global _ADL2_Adapter_Active_Set
    global _ADL_Adapter_Active_Set
    global _ADL2_Adapter_Active_SetPrefer
    global _ADL_Adapter_Active_SetPrefer
    global _ADL2_Adapter_Primary_Get
    global _ADL_Adapter_Primary_Get
    global _ADL2_Adapter_Primary_Set
    global _ADL_Adapter_Primary_Set
    global _ADL2_Adapter_ModeSwitch
    global _ADL_Adapter_ModeSwitch
    global _ADL2_Display_Modes_Get
    global _ADL_Display_Modes_Get
    global _ADL2_Display_Modes_Set
    global _ADL_Display_Modes_Set
    global _ADL2_Display_PossibleMode_Get
    global _ADL_Display_PossibleMode_Get
    global _ADL2_Display_ForcibleDisplay_Get
    global _ADL_Display_ForcibleDisplay_Get
    global _ADL2_Display_ForcibleDisplay_Set
    global _ADL_Display_ForcibleDisplay_Set
    global _ADL2_Adapter_NumberOfActivatableSources_Get
    global _ADL_Adapter_NumberOfActivatableSources_Get
    global _ADL2_Adapter_Display_Caps
    global _ADL_Adapter_Display_Caps
    global _ADL2_Display_DisplayMapConfig_Get
    global _ADL_Display_DisplayMapConfig_Get
    global _ADL2_Display_DisplayMapConfig_Set
    global _ADL_Display_DisplayMapConfig_Set
    global _ADL2_Display_PossibleMapping_Get
    global _ADL_Display_PossibleMapping_Get
    global _ADL2_Display_DisplayMapConfig_Validate
    global _ADL_Display_DisplayMapConfig_Validate
    global _ADL2_Display_DisplayMapConfig_PossibleAddAndRemove
    global _ADL_Display_DisplayMapConfig_PossibleAddAndRemove
    global _ADL2_Display_SLSGrid_Caps
    global _ADL_Display_SLSGrid_Caps
    global _ADL2_Display_SLSMapIndexList_Get
    global _ADL_Display_SLSMapIndexList_Get
    global _ADL2_Display_SLSMapIndex_Get
    global _ADL_Display_SLSMapIndex_Get
    global _ADL2_Display_SLSMapConfigX2_Get
    global _ADL_Display_SLSMapConfigX2_Get
    global _ADL2_Display_SLSMapConfig_Get
    global _ADL_Display_SLSMapConfig_Get
    global _ADL2_Display_SLSMapConfig_Create
    global _ADL_Display_SLSMapConfig_Create
    global _ADL2_Display_SLSMapConfig_Delete
    global _ADL_Display_SLSMapConfig_Delete
    global _ADL2_Display_SLSMapConfigX2_Delete
    global _ADL2_Display_SLSMapConfig_SetState
    global _ADL_Display_SLSMapConfig_SetState
    global _ADL2_Display_SLSMapConfig_Rearrange
    global _ADL_Display_SLSMapConfig_Rearrange
    global _ADL2_Display_PossibleMode_WinXP_Get
    global _ADL_Display_PossibleMode_WinXP_Get
    global _ADL2_Display_BezelOffsetSteppingSize_Get
    global _ADL_Display_BezelOffsetSteppingSize_Get
    global _ADL2_Display_BezelOffset_Set
    global _ADL_Display_BezelOffset_Set
    global _ADL2_Display_BezelSupported_Validate
    global _ADL_Display_BezelSupported_Validate
    global _ADL2_Display_Overlap_Set
    global _ADL_Display_Overlap_Set
    global _ADL2_Display_SLSMiddleMode_Get
    global _ADL_Display_SLSMiddleMode_Get
    global _ADL2_Display_SLSMiddleMode_Set
    global _ADL_Display_SLSMiddleMode_Set
    global _ADL2_Workstation_EnableUnsupportedDisplayModes
    global _ADL_Workstation_EnableUnsupportedDisplayModes
    global _ADL2_Display_SLSRecords_Get
    global _ADL_Display_SLSRecords_Get
    global _ADL2_Adapter_AMDAndNonAMDDIsplayClone_Get
    global _ADL2_Adapter_CloneTypes_Get
    global _ADL2_Adapter_CrossGPUClone_Disable

    _ADL2_Adapter_Active_Set = ADL2_ADAPTER_ACTIVE_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_Active_Set")
    )
    _ADL_Adapter_Active_Set = ADL_ADAPTER_ACTIVE_SET(
          GetProcAddress(hDLL, "ADL_Adapter_Active_Set")
    )
    _ADL2_Adapter_Active_SetPrefer = ADL2_ADAPTER_ACTIVE_SETPREFER(
          GetProcAddress(hDLL, "ADL2_Adapter_Active_SetPrefer")
    )
    _ADL_Adapter_Active_SetPrefer = ADL_ADAPTER_ACTIVE_SETPREFER(
          GetProcAddress(hDLL, "ADL_Adapter_Active_SetPrefer")
    )
    _ADL2_Adapter_Primary_Get = ADL2_ADAPTER_PRIMARY_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_Primary_Get")
    )
    _ADL_Adapter_Primary_Get = ADL_ADAPTER_PRIMARY_GET(
          GetProcAddress(hDLL, "ADL_Adapter_Primary_Get")
    )
    _ADL2_Adapter_Primary_Set = ADL2_ADAPTER_PRIMARY_SET(
          GetProcAddress(hDLL, "ADL2_Adapter_Primary_Set")
    )
    _ADL_Adapter_Primary_Set = ADL_ADAPTER_PRIMARY_SET(
          GetProcAddress(hDLL, "ADL_Adapter_Primary_Set")
    )
    _ADL2_Adapter_ModeSwitch = ADL2_ADAPTER_MODESWITCH(
          GetProcAddress(hDLL, "ADL2_Adapter_ModeSwitch")
    )
    _ADL_Adapter_ModeSwitch = ADL_ADAPTER_MODESWITCH(
          GetProcAddress(hDLL, "ADL_Adapter_ModeSwitch")
    )
    _ADL2_Display_Modes_Get = ADL2_DISPLAY_MODES_GET(
          GetProcAddress(hDLL, "ADL2_Display_Modes_Get")
    )
    _ADL_Display_Modes_Get = ADL_DISPLAY_MODES_GET(
          GetProcAddress(hDLL, "ADL_Display_Modes_Get")
    )
    _ADL2_Display_Modes_Set = ADL2_DISPLAY_MODES_SET(
          GetProcAddress(hDLL, "ADL2_Display_Modes_Set")
    )
    _ADL_Display_Modes_Set = ADL_DISPLAY_MODES_SET(
          GetProcAddress(hDLL, "ADL_Display_Modes_Set")
    )
    _ADL2_Display_PossibleMode_Get = ADL2_DISPLAY_POSSIBLEMODE_GET(
          GetProcAddress(hDLL, "ADL2_Display_PossibleMode_Get")
    )
    _ADL_Display_PossibleMode_Get = ADL_DISPLAY_POSSIBLEMODE_GET(
          GetProcAddress(hDLL, "ADL_Display_PossibleMode_Get")
    )
    _ADL2_Display_ForcibleDisplay_Get = ADL2_DISPLAY_FORCIBLEDISPLAY_GET(
          GetProcAddress(hDLL, "ADL2_Display_ForcibleDisplay_Get")
    )
    _ADL_Display_ForcibleDisplay_Get = ADL_DISPLAY_FORCIBLEDISPLAY_GET(
          GetProcAddress(hDLL, "ADL_Display_ForcibleDisplay_Get")
    )
    _ADL2_Display_ForcibleDisplay_Set = ADL2_DISPLAY_FORCIBLEDISPLAY_SET(
          GetProcAddress(hDLL, "ADL2_Display_ForcibleDisplay_Set")
    )
    _ADL_Display_ForcibleDisplay_Set = ADL_DISPLAY_FORCIBLEDISPLAY_SET(
          GetProcAddress(hDLL, "ADL_Display_ForcibleDisplay_Set")
    )
    _ADL2_Adapter_NumberOfActivatableSources_Get = ADL2_ADAPTER_NUMBEROFACTIVATABLESOURCES_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_NumberOfActivatableSources_Get")
    )
    _ADL_Adapter_NumberOfActivatableSources_Get = ADL_ADAPTER_NUMBEROFACTIVATABLESOURCES_GET(
          GetProcAddress(hDLL, "ADL_Adapter_NumberOfActivatableSources_Get")
    )
    _ADL2_Adapter_Display_Caps = ADL2_ADAPTER_DISPLAY_CAPS(
          GetProcAddress(hDLL, "ADL2_Adapter_Display_Caps")
    )
    _ADL_Adapter_Display_Caps = ADL_ADAPTER_DISPLAY_CAPS(
          GetProcAddress(hDLL, "ADL_Adapter_Display_Caps")
    )
    _ADL2_Display_DisplayMapConfig_Get = ADL2_DISPLAY_DISPLAYMAPCONFIG_GET(
          GetProcAddress(hDLL, "ADL2_Display_DisplayMapConfig_Get")
    )
    _ADL_Display_DisplayMapConfig_Get = ADL_DISPLAY_DISPLAYMAPCONFIG_GET(
          GetProcAddress(hDLL, "ADL_Display_DisplayMapConfig_Get")
    )
    _ADL2_Display_DisplayMapConfig_Set = ADL2_DISPLAY_DISPLAYMAPCONFIG_SET(
          GetProcAddress(hDLL, "ADL2_Display_DisplayMapConfig_Set")
    )
    _ADL_Display_DisplayMapConfig_Set = ADL_DISPLAY_DISPLAYMAPCONFIG_SET(
          GetProcAddress(hDLL, "ADL_Display_DisplayMapConfig_Set")
    )
    _ADL2_Display_PossibleMapping_Get = ADL2_DISPLAY_POSSIBLEMAPPING_GET(
          GetProcAddress(hDLL, "ADL2_Display_PossibleMapping_Get")
    )
    _ADL_Display_PossibleMapping_Get = ADL_DISPLAY_POSSIBLEMAPPING_GET(
          GetProcAddress(hDLL, "ADL_Display_PossibleMapping_Get")
    )
    _ADL2_Display_DisplayMapConfig_Validate = ADL2_DISPLAY_DISPLAYMAPCONFIG_VALIDATE(
          GetProcAddress(hDLL, "ADL2_Display_DisplayMapConfig_Validate")
    )
    _ADL_Display_DisplayMapConfig_Validate = ADL_DISPLAY_DISPLAYMAPCONFIG_VALIDATE(
          GetProcAddress(hDLL, "ADL_Display_DisplayMapConfig_Validate")
    )
    _ADL2_Display_DisplayMapConfig_PossibleAddAndRemove = ADL2_DISPLAY_DISPLAYMAPCONFIG_POSSIBLEADDANDREMOVE(
          GetProcAddress(hDLL, "ADL2_Display_DisplayMapConfig_PossibleAddAndRemove")
    )
    _ADL_Display_DisplayMapConfig_PossibleAddAndRemove = ADL_DISPLAY_DISPLAYMAPCONFIG_POSSIBLEADDANDREMOVE(
          GetProcAddress(hDLL, "ADL_Display_DisplayMapConfig_PossibleAddAndRemove")
    )
    _ADL2_Display_SLSGrid_Caps = ADL2_DISPLAY_SLSGRID_CAPS(
          GetProcAddress(hDLL, "ADL2_Display_SLSGrid_Caps")
    )
    _ADL_Display_SLSGrid_Caps = ADL_DISPLAY_SLSGRID_CAPS(
          GetProcAddress(hDLL, "ADL_Display_SLSGrid_Caps")
    )
    _ADL2_Display_SLSMapIndexList_Get = ADL2_DISPLAY_SLSMAPINDEXLIST_GET(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapIndexList_Get")
    )
    _ADL_Display_SLSMapIndexList_Get = ADL_DISPLAY_SLSMAPINDEXLIST_GET(
          GetProcAddress(hDLL, "ADL_Display_SLSMapIndexList_Get")
    )
    _ADL2_Display_SLSMapIndex_Get = ADL2_DISPLAY_SLSMAPINDEX_GET(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapIndex_Get")
    )
    _ADL_Display_SLSMapIndex_Get = ADL_DISPLAY_SLSMAPINDEX_GET(
          GetProcAddress(hDLL, "ADL_Display_SLSMapIndex_Get")
    )
    _ADL2_Display_SLSMapConfigX2_Get = ADL2_DISPLAY_SLSMAPCONFIGX2_GET(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapConfigX2_Get")
    )
    _ADL_Display_SLSMapConfigX2_Get = ADL_DISPLAY_SLSMAPCONFIGX2_GET(
          GetProcAddress(hDLL, "ADL_Display_SLSMapConfigX2_Get")
    )
    _ADL2_Display_SLSMapConfig_Get = ADL2_DISPLAY_SLSMAPCONFIG_GET(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapConfig_Get")
    )
    _ADL_Display_SLSMapConfig_Get = ADL_DISPLAY_SLSMAPCONFIG_GET(
          GetProcAddress(hDLL, "ADL_Display_SLSMapConfig_Get")
    )
    _ADL2_Display_SLSMapConfig_Create = ADL2_DISPLAY_SLSMAPCONFIG_CREATE(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapConfig_Create")
    )
    _ADL_Display_SLSMapConfig_Create = ADL_DISPLAY_SLSMAPCONFIG_CREATE(
          GetProcAddress(hDLL, "ADL_Display_SLSMapConfig_Create")
    )
    _ADL2_Display_SLSMapConfig_Delete = ADL2_DISPLAY_SLSMAPCONFIG_DELETE(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapConfig_Delete")
    )
    _ADL_Display_SLSMapConfig_Delete = ADL_DISPLAY_SLSMAPCONFIG_DELETE(
          GetProcAddress(hDLL, "ADL_Display_SLSMapConfig_Delete")
    )
    _ADL2_Display_SLSMapConfigX2_Delete = ADL2_DISPLAY_SLSMAPCONFIGX2_DELETE(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapConfigX2_Delete")
    )
    _ADL2_Display_SLSMapConfig_SetState = ADL2_DISPLAY_SLSMAPCONFIG_SETSTATE(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapConfig_SetState")
    )
    _ADL_Display_SLSMapConfig_SetState = ADL_DISPLAY_SLSMAPCONFIG_SETSTATE(
          GetProcAddress(hDLL, "ADL_Display_SLSMapConfig_SetState")
    )
    _ADL2_Display_SLSMapConfig_Rearrange = ADL2_DISPLAY_SLSMAPCONFIG_REARRANGE(
          GetProcAddress(hDLL, "ADL2_Display_SLSMapConfig_Rearrange")
    )
    _ADL_Display_SLSMapConfig_Rearrange = ADL_DISPLAY_SLSMAPCONFIG_REARRANGE(
          GetProcAddress(hDLL, "ADL_Display_SLSMapConfig_Rearrange")
    )
    _ADL2_Display_PossibleMode_WinXP_Get = ADL2_DISPLAY_POSSIBLEMODE_WINXP_GET(
          GetProcAddress(hDLL, "ADL2_Display_PossibleMode_WinXP_Get")
    )
    _ADL_Display_PossibleMode_WinXP_Get = ADL_DISPLAY_POSSIBLEMODE_WINXP_GET(
          GetProcAddress(hDLL, "ADL_Display_PossibleMode_WinXP_Get")
    )
    _ADL2_Display_BezelOffsetSteppingSize_Get = ADL2_DISPLAY_BEZELOFFSETSTEPPINGSIZE_GET(
          GetProcAddress(hDLL, "ADL2_Display_BezelOffsetSteppingSize_Get")
    )
    _ADL_Display_BezelOffsetSteppingSize_Get = ADL_DISPLAY_BEZELOFFSETSTEPPINGSIZE_GET(
          GetProcAddress(hDLL, "ADL_Display_BezelOffsetSteppingSize_Get")
    )
    _ADL2_Display_BezelOffset_Set = ADL2_DISPLAY_BEZELOFFSET_SET(
          GetProcAddress(hDLL, "ADL2_Display_BezelOffset_Set")
    )
    _ADL_Display_BezelOffset_Set = ADL_DISPLAY_BEZELOFFSET_SET(
          GetProcAddress(hDLL, "ADL_Display_BezelOffset_Set")
    )
    _ADL2_Display_BezelSupported_Validate = ADL2_DISPLAY_BEZELSUPPORTED_VALIDATE(
          GetProcAddress(hDLL, "ADL2_Display_BezelSupported_Validate")
    )
    _ADL_Display_BezelSupported_Validate = ADL_DISPLAY_BEZELSUPPORTED_VALIDATE(
          GetProcAddress(hDLL, "ADL_Display_BezelSupported_Validate")
    )
    _ADL2_Display_Overlap_Set = ADL2_DISPLAY_OVERLAP_SET(
          GetProcAddress(hDLL, "ADL2_Display_Overlap_Set")
    )
    _ADL_Display_Overlap_Set = ADL_DISPLAY_OVERLAP_SET(
          GetProcAddress(hDLL, "ADL_Display_Overlap_Set")
    )
    _ADL2_Display_SLSMiddleMode_Get = ADL2_DISPLAY_SLSMIDDLEMODE_GET(
          GetProcAddress(hDLL, "ADL2_Display_SLSMiddleMode_Get")
    )
    _ADL_Display_SLSMiddleMode_Get = ADL_DISPLAY_SLSMIDDLEMODE_GET(
          GetProcAddress(hDLL, "ADL_Display_SLSMiddleMode_Get")
    )
    _ADL2_Display_SLSMiddleMode_Set = ADL2_DISPLAY_SLSMIDDLEMODE_SET(
          GetProcAddress(hDLL, "ADL2_Display_SLSMiddleMode_Set")
    )
    _ADL_Display_SLSMiddleMode_Set = ADL_DISPLAY_SLSMIDDLEMODE_SET(
          GetProcAddress(hDLL, "ADL_Display_SLSMiddleMode_Set")
    )
    _ADL2_Workstation_EnableUnsupportedDisplayModes = ADL2_WORKSTATION_ENABLEUNSUPPORTEDDISPLAYMODES(
          GetProcAddress(hDLL, "ADL2_Workstation_EnableUnsupportedDisplayModes")
    )
    _ADL_Workstation_EnableUnsupportedDisplayModes = ADL_WORKSTATION_ENABLEUNSUPPORTEDDISPLAYMODES(
          GetProcAddress(hDLL, "ADL_Workstation_EnableUnsupportedDisplayModes")
    )
    _ADL2_Display_SLSRecords_Get = ADL2_DISPLAY_SLSRECORDS_GET(
          GetProcAddress(hDLL, "ADL2_Display_SLSRecords_Get")
    )
    _ADL_Display_SLSRecords_Get = ADL_DISPLAY_SLSRECORDS_GET(
          GetProcAddress(hDLL, "ADL_Display_SLSRecords_Get")
    )
    _ADL2_Adapter_AMDAndNonAMDDIsplayClone_Get = ADL2_ADAPTER_AMDANDNONAMDDISPLAYCLONE_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_AMDAndNonAMDDIsplayClone_Get")
    )
    _ADL2_Adapter_CloneTypes_Get = ADL2_ADAPTER_CLONETYPES_GET(
          GetProcAddress(hDLL, "ADL2_Adapter_CloneTypes_Get")
    )
    _ADL2_Adapter_CrossGPUClone_Disable = ADL2_ADAPTER_CROSSGPUCLONE_DISABLE(
          GetProcAddress(hDLL, "ADL2_Adapter_CrossGPUClone_Disable")
    )


__all__ = (
    '_ADL2_Adapter_Active_Set',
    '_ADL_Adapter_Active_Set',
    '_ADL2_Adapter_Active_SetPrefer',
    '_ADL_Adapter_Active_SetPrefer',
    '_ADL2_Adapter_Primary_Get',
    '_ADL_Adapter_Primary_Get',
    '_ADL2_Adapter_Primary_Set',
    '_ADL_Adapter_Primary_Set',
    '_ADL2_Adapter_ModeSwitch',
    '_ADL_Adapter_ModeSwitch',
    '_ADL2_Display_Modes_Get',
    '_ADL_Display_Modes_Get',
    '_ADL2_Display_Modes_Set',
    '_ADL_Display_Modes_Set',
    '_ADL2_Display_PossibleMode_Get',
    '_ADL_Display_PossibleMode_Get',
    '_ADL2_Display_ForcibleDisplay_Get',
    '_ADL_Display_ForcibleDisplay_Get',
    '_ADL2_Display_ForcibleDisplay_Set',
    '_ADL_Display_ForcibleDisplay_Set',
    '_ADL2_Adapter_NumberOfActivatableSources_Get',
    '_ADL_Adapter_NumberOfActivatableSources_Get',
    '_ADL2_Adapter_Display_Caps',
    '_ADL_Adapter_Display_Caps',
    '_ADL2_Display_DisplayMapConfig_Get',
    '_ADL_Display_DisplayMapConfig_Get',
    '_ADL2_Display_DisplayMapConfig_Set',
    '_ADL_Display_DisplayMapConfig_Set',
    '_ADL2_Display_PossibleMapping_Get',
    '_ADL_Display_PossibleMapping_Get',
    '_ADL2_Display_DisplayMapConfig_Validate',
    '_ADL_Display_DisplayMapConfig_Validate',
    '_ADL2_Display_DisplayMapConfig_PossibleAddAndRemove',
    '_ADL_Display_DisplayMapConfig_PossibleAddAndRemove',
    '_ADL2_Display_SLSGrid_Caps',
    '_ADL_Display_SLSGrid_Caps',
    '_ADL2_Display_SLSMapIndexList_Get',
    '_ADL_Display_SLSMapIndexList_Get',
    '_ADL2_Display_SLSMapIndex_Get',
    '_ADL_Display_SLSMapIndex_Get',
    '_ADL2_Display_SLSMapConfigX2_Get',
    '_ADL_Display_SLSMapConfigX2_Get',
    '_ADL2_Display_SLSMapConfig_Get',
    '_ADL_Display_SLSMapConfig_Get',
    '_ADL2_Display_SLSMapConfig_Create',
    '_ADL_Display_SLSMapConfig_Create',
    '_ADL2_Display_SLSMapConfig_Delete',
    '_ADL_Display_SLSMapConfig_Delete',
    '_ADL2_Display_SLSMapConfigX2_Delete',
    '_ADL2_Display_SLSMapConfig_SetState',
    '_ADL_Display_SLSMapConfig_SetState',
    '_ADL2_Display_SLSMapConfig_Rearrange',
    '_ADL_Display_SLSMapConfig_Rearrange',
    '_ADL2_Display_PossibleMode_WinXP_Get',
    '_ADL_Display_PossibleMode_WinXP_Get',
    '_ADL2_Display_BezelOffsetSteppingSize_Get',
    '_ADL_Display_BezelOffsetSteppingSize_Get',
    '_ADL2_Display_BezelOffset_Set',
    '_ADL_Display_BezelOffset_Set',
    '_ADL2_Display_BezelSupported_Validate',
    '_ADL_Display_BezelSupported_Validate',
    '_ADL2_Display_Overlap_Set',
    '_ADL_Display_Overlap_Set',
    '_ADL2_Display_SLSMiddleMode_Get',
    '_ADL_Display_SLSMiddleMode_Get',
    '_ADL2_Display_SLSMiddleMode_Set',
    '_ADL_Display_SLSMiddleMode_Set',
    '_ADL2_Workstation_EnableUnsupportedDisplayModes',
    '_ADL_Workstation_EnableUnsupportedDisplayModes',
    '_ADL2_Display_SLSRecords_Get',
    '_ADL_Display_SLSRecords_Get',
    '_ADL2_Adapter_AMDAndNonAMDDIsplayClone_Get',
    '_ADL2_Adapter_CloneTypes_Get',
    '_ADL2_Adapter_CrossGPUClone_Disable',
)


from .adapter_h import *  # NOQA
from .adl_sdk_h import ADL2_Main_Control_Create, AdapterBase  # NOQA
from .display_h import Display, _ADL2_Display_NumberOfDisplays_Get  # NOQA
from .crossdisplay_h import CrossDisplay  # NOQA


class Adapter(AdapterBase):

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
    def __adapter_info(self):
        lpInfo = AdapterInfo()
        lpInfo.iSize = ctypes.sizeof(AdapterInfo)
        iInputSize = INT(ctypes.sizeof(AdapterInfo))
        iAdapterIndex = INT(self._adapter_index)

        with ADL2_Main_Control_Create as context:
            if _ADL2_Adapter_AdapterInfo_Get(
                    context,
                    iAdapterIndex,
                    ctypes.byref(lpInfo),
                    iInputSize
            ) == ADL_OK:
                return lpInfo

    @property
    def udid(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strUDID)

    @property
    def bus_number(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return lpInfo.iBusNumber

    @property
    def device_number(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return lpInfo.iDeviceNumber

    @property
    def function_number(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return lpInfo.iFunctionNumber

    @property
    def vendor_id(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return lpInfo.iVendorID

    @property
    def adapter_name(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strAdapterName)

    @property
    def display_name(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strDisplayName)

    @property
    def is_present(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return lpInfo.iPresent == 1

    @property
    def exists(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return lpInfo.iExist == 1

    @property
    def driver_path(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strDriverPath)

    @property
    def driver_path_ext(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strDriverPathExt)

    @property
    def upnp_path(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return self._get_string(lpInfo.strPNPString)

    @property
    def display_index(self):
        lpInfo = self.__adapter_info
        if lpInfo is not None:
            return lpInfo.iOSDisplayIndex

    @property
    def driver_index(self):
        lpInfo = self.__adapter_info
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
