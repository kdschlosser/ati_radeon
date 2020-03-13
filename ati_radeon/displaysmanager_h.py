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


ADL2_ADAPTER_ACTIVE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_ADAPTER_ACTIVE_SET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_ACTIVE_SETPREFER = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT)
)
ADL_ADAPTER_ACTIVE_SETPREFER = _int(
    INT,
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT)
)
ADL2_ADAPTER_PRIMARY_GET = _int(
    ADL_CONTEXT_HANDLE,
    POINTER(INT)
)
ADL_ADAPTER_PRIMARY_GET = _int(
    POINTER(INT)
)
ADL2_ADAPTER_PRIMARY_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_ADAPTER_PRIMARY_SET = _int(
    INT
)
ADL2_ADAPTER_MODESWITCH = _int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_ADAPTER_MODESWITCH = _int(
    INT
)
ADL2_DISPLAY_MODES_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL_DISPLAY_MODES_GET = _int(
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL2_DISPLAY_MODES_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLMode)
)
ADL_DISPLAY_MODES_SET = _int(
    INT,
    INT,
    INT,
    POINTER(ADLMode)
)
ADL2_DISPLAY_POSSIBLEMODE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL_DISPLAY_POSSIBLEMODE_GET = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL2_DISPLAY_FORCIBLEDISPLAY_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_DISPLAY_FORCIBLEDISPLAY_GET = _int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_FORCIBLEDISPLAY_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_FORCIBLEDISPLAY_SET = _int(
    INT,
    INT,
    INT
)
ADL2_ADAPTER_NUMBEROFACTIVATABLESOURCES_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLActivatableSource))
)
ADL_ADAPTER_NUMBEROFACTIVATABLESOURCES_GET = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLActivatableSource))
)
ADL2_ADAPTER_DISPLAY_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLAdapterDisplayCap))
)
ADL_ADAPTER_DISPLAY_CAPS = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLAdapterDisplayCap))
)
ADL2_DISPLAY_DISPLAYMAPCONFIG_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayMap)),
    POINTER(INT),
    POINTER(POINTER(ADLDisplayTarget)),
    INT
)
ADL_DISPLAY_DISPLAYMAPCONFIG_GET = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLDisplayMap)),
    POINTER(INT),
    POINTER(POINTER(ADLDisplayTarget)),
    INT
)
ADL2_DISPLAY_DISPLAYMAPCONFIG_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayMap),
    INT,
    POINTER(ADLDisplayTarget)
)
ADL_DISPLAY_DISPLAYMAPCONFIG_SET = _int(
    INT,
    INT,
    POINTER(ADLDisplayMap),
    INT,
    POINTER(ADLDisplayTarget)
)
ADL2_DISPLAY_POSSIBLEMAPPING_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLPossibleMapping),
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLPossibleMapping))
)
ADL_DISPLAY_POSSIBLEMAPPING_GET = _int(
    INT,
    INT,
    POINTER(ADLPossibleMapping),
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLPossibleMapping))
)
ADL2_DISPLAY_DISPLAYMAPCONFIG_VALIDATE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLPossibleMap),
    POINTER(INT),
    POINTER(POINTER(ADLPossibleMapResult))
)
ADL_DISPLAY_DISPLAYMAPCONFIG_VALIDATE = _int(
    INT,
    INT,
    POINTER(ADLPossibleMap),
    POINTER(INT),
    POINTER(POINTER(ADLPossibleMapResult))
)
ADL2_DISPLAY_DISPLAYMAPCONFIG_POSSIBLEADDANDREMOVE = _int(
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
ADL_DISPLAY_DISPLAYMAPCONFIG_POSSIBLEADDANDREMOVE = _int(
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
ADL2_DISPLAY_SLSGRID_CAPS = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLSLSGrid)),
    INT
)
ADL_DISPLAY_SLSGRID_CAPS = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLSLSGrid)),
    INT
)
ADL2_DISPLAY_SLSMAPINDEXLIST_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(INT)),
    INT
)
ADL_DISPLAY_SLSMAPINDEXLIST_GET = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(INT)),
    INT
)
ADL2_DISPLAY_SLSMAPINDEX_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT)
)
ADL_DISPLAY_SLSMAPINDEX_GET = _int(
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    POINTER(INT)
)
ADL2_DISPLAY_SLSMAPCONFIGX2_GET = _int(
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
ADL_DISPLAY_SLSMAPCONFIGX2_GET = _int(
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
ADL2_DISPLAY_SLSMAPCONFIG_GET = _int(
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
ADL_DISPLAY_SLSMAPCONFIG_GET = _int(
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
ADL2_DISPLAY_SLSMAPCONFIG_CREATE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLSLSMap,
    INT,
    POINTER(ADLSLSTarget),
    INT,
    POINTER(INT),
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_CREATE = _int(
    INT,
    ADLSLSMap,
    INT,
    POINTER(ADLSLSTarget),
    INT,
    POINTER(INT),
    INT
)
ADL2_DISPLAY_SLSMAPCONFIG_DELETE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_DELETE = _int(
    INT,
    INT
)
ADL2_DISPLAY_SLSMAPCONFIGX2_DELETE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL2_DISPLAY_SLSMAPCONFIG_SETSTATE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_SETSTATE = _int(
    INT,
    INT,
    INT
)
ADL2_DISPLAY_SLSMAPCONFIG_REARRANGE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLSLSTarget),
    ADLSLSMap,
    INT
)
ADL_DISPLAY_SLSMAPCONFIG_REARRANGE = _int(
    INT,
    INT,
    INT,
    POINTER(ADLSLSTarget),
    ADLSLSMap,
    INT
)
ADL2_DISPLAY_POSSIBLEMODE_WINXP_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL_DISPLAY_POSSIBLEMODE_WINXP_GET = _int(
    INT,
    INT,
    POINTER(ADLDisplayTarget),
    INT,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLMode))
)
ADL2_DISPLAY_BEZELOFFSETSTEPPINGSIZE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLBezelOffsetSteppingSize))
)
ADL_DISPLAY_BEZELOFFSETSTEPPINGSIZE_GET = _int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLBezelOffsetSteppingSize))
)
ADL2_DISPLAY_BEZELOFFSET_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    LPADLSLSOffset,
    ADLSLSMap,
    INT
)
ADL_DISPLAY_BEZELOFFSET_SET = _int(
    INT,
    INT,
    INT,
    LPADLSLSOffset,
    ADLSLSMap,
    INT
)
ADL2_DISPLAY_BEZELSUPPORTED_VALIDATE = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    LPADLPossibleSLSMap,
    POINTER(INT),
    POINTER(LPADLPossibleMapResult)
)
ADL_DISPLAY_BEZELSUPPORTED_VALIDATE = _int(
    INT,
    INT,
    LPADLPossibleSLSMap,
    POINTER(INT),
    POINTER(LPADLPossibleMapResult)
)
ADL2_DISPLAY_OVERLAP_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    LPADLSLSTargetOverlap,
    INT,
    LPADLSLSOffset,
    ADLSLSMap
)
ADL_DISPLAY_OVERLAP_SET = _int(
    INT,
    INT,
    INT,
    LPADLSLSTargetOverlap,
    INT,
    LPADLSLSOffset,
    ADLSLSMap
)
ADL2_DISPLAY_SLSMIDDLEMODE_GET = _int(
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
ADL_DISPLAY_SLSMIDDLEMODE_GET = _int(
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
ADL2_DISPLAY_SLSMIDDLEMODE_SET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLSLSMode),
    INT
)
ADL_DISPLAY_SLSMIDDLEMODE_SET = _int(
    INT,
    INT,
    INT,
    POINTER(ADLSLSMode),
    INT
)
ADL2_WORKSTATION_ENABLEUNSUPPORTEDDISPLAYMODES = _int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_WORKSTATION_ENABLEUNSUPPORTEDDISPLAYMODES = _int(
    INT
)
ADL2_DISPLAY_SLSRECORDS_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    ADLDisplayID,
    POINTER(INT),
    POINTER(POINTER(INT))
)
ADL_DISPLAY_SLSRECORDS_GET = _int(
    INT,
    ADLDisplayID,
    POINTER(INT),
    POINTER(POINTER(INT))
)
ADL2_ADAPTER_AMDANDNONAMDDISPLAYCLONE_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_CLONETYPES_GET = _int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL2_ADAPTER_CROSSGPUCLONE_DISABLE = _int(
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
