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


ADL2_WORKSTATION_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_CAPS = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_STEREO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_STEREO_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_STEREO_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_WORKSTATION_STEREO_SET = int(
    INT,
    INT
)
ADL2_WORKSTATION_ADAPTERNUMOFGLSYNCCONNECTORS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_WORKSTATION_ADAPTERNUMOFGLSYNCCONNECTORS_GET = int(
    INT,
    POINTER(INT)
)
ADL2_WORKSTATION_DISPLAYGENLOCKCAPABLE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT)
)
ADL_WORKSTATION_DISPLAYGENLOCKCAPABLE_GET = int(
    INT,
    INT,
    POINTER(INT)
)
ADL2_WORKSTATION_GLSYNCMODULEDETECT_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLGLSyncModuleID)
)
ADL_WORKSTATION_GLSYNCMODULEDETECT_GET = int(
    INT,
    INT,
    POINTER(ADLGLSyncModuleID)
)
ADL2_WORKSTATION_GLSYNCMODULEINFO_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLGLSyncPortCaps))
)
ADL_WORKSTATION_GLSYNCMODULEINFO_GET = int(
    INT,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(POINTER(ADLGLSyncPortCaps))
)
ADL2_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    POINTER(ADLGLSyncGenlockConfig)
)
ADL_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_GET = int(
    INT,
    INT,
    INT,
    POINTER(ADLGLSyncGenlockConfig)
)
ADL2_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    ADLGLSyncGenlockConfig
)
ADL_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_SET = int(
    INT,
    INT,
    ADLGLSyncGenlockConfig
)
ADL2_WORKSTATION_GLSYNCPORTSTATE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT,
    INT,
    POINTER(ADLGlSyncPortInfo),
    POINTER(POINTER(INT))
)
ADL_WORKSTATION_GLSYNCPORTSTATE_GET = int(
    INT,
    INT,
    INT,
    INT,
    POINTER(ADLGlSyncPortInfo),
    POINTER(POINTER(INT))
)
ADL2_WORKSTATION_GLSYNCPORTSTATE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    ADLGlSyncPortControl
)
ADL_WORKSTATION_GLSYNCPORTSTATE_SET = int(
    INT,
    INT,
    ADLGlSyncPortControl
)
ADL2_WORKSTATION_DISPLAYGLSYNCMODE_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLGlSyncMode)
)
ADL_WORKSTATION_DISPLAYGLSYNCMODE_GET = int(
    INT,
    INT,
    POINTER(ADLGlSyncMode)
)
ADL2_WORKSTATION_DISPLAYGLSYNCMODE_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    ADLGlSyncMode
)
ADL_WORKSTATION_DISPLAYGLSYNCMODE_SET = int(
    INT,
    INT,
    ADLGlSyncMode
)
ADL2_WORKSTATION_GLSYNCSUPPORTEDTOPOLOGY_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    POINTER(ADLGlSyncMode2),
    POINTER(INT),
    POINTER(POINTER(ADLGlSyncMode2))
)
ADL_WORKSTATION_GLSYNCSUPPORTEDTOPOLOGY_GET = int(
    INT,
    INT,
    POINTER(ADLGlSyncMode2),
    POINTER(INT),
    POINTER(POINTER(ADLGlSyncMode2))
)
ADL2_WORKSTATION_LOADBALANCING_GET = int(
    ADL_CONTEXT_HANDLE,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_LOADBALANCING_GET = int(
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_LOADBALANCING_SET = int(
    ADL_CONTEXT_HANDLE,
    INT
)
ADL_WORKSTATION_LOADBALANCING_SET = int(
    INT
)
ADL2_WORKSTATION_LOADBALANCING_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_LOADBALANCING_CAPS = int(
    INT,
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_DEEPBITDEPTH_GET = int(
    ADL_CONTEXT_HANDLE,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_DEEPBITDEPTH_GET = int(
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_DEEPBITDEPTH_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT,
    INT
)
ADL_WORKSTATION_DEEPBITDEPTH_SET = int(
    INT,
    INT,
    INT
)
ADL2_WORKSTATION_ECC_CAPS = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT)
)
ADL_WORKSTATION_ECC_CAPS = int(
    INT,
    POINTER(INT)
)
ADL2_WORKSTATION_ECC_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_ECC_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_ECCX2_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL_WORKSTATION_ECCX2_GET = int(
    INT,
    POINTER(INT),
    POINTER(INT),
    POINTER(INT),
    POINTER(INT)
)
ADL2_WORKSTATION_ECCDATA_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(ADLECCData)
)
ADL_WORKSTATION_ECCDATA_GET = int(
    INT,
    POINTER(ADLECCData)
)
ADL2_WORKSTATION_ECC_SET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    INT
)
ADL_WORKSTATION_ECC_SET = int(
    INT,
    INT
)


# Function to retrieve current workstation capabilities.
_ADL2_Workstation_Caps = ADL2_WORKSTATION_CAPS

# Function to retrieve current workstation capabilities.
_ADL_Workstation_Caps = ADL_WORKSTATION_CAPS

# Function to retreive the worstation stereo mode.
_ADL2_Workstation_Stereo_Get = ADL2_WORKSTATION_STEREO_GET

# Function to retreive the worstation stereo mode.
_ADL_Workstation_Stereo_Get = ADL_WORKSTATION_STEREO_GET

# Function to set the workstation stereo mode.
_ADL2_Workstation_Stereo_Set = ADL2_WORKSTATION_STEREO_SET

# Function to set the workstation stereo mode.
_ADL_Workstation_Stereo_Set = ADL_WORKSTATION_STEREO_SET

# Function to retrieve the number of GL-Sync connectors on an adapter.
_ADL2_Workstation_AdapterNumOfGLSyncConnectors_Get = ADL2_WORKSTATION_ADAPTERNUMOFGLSYNCCONNECTORS_GET

# Function to retrieve the number of GL-Sync connectors on an adapter.
_ADL_Workstation_AdapterNumOfGLSyncConnectors_Get = ADL_WORKSTATION_ADAPTERNUMOFGLSYNCCONNECTORS_GET

# Function to determine whether or not a display is capable of Genlock functionality.
_ADL2_Workstation_DisplayGenlockCapable_Get = ADL2_WORKSTATION_DISPLAYGENLOCKCAPABLE_GET

# Function to determine whether or not a display is capable of Genlock functionality.
_ADL_Workstation_DisplayGenlockCapable_Get = ADL_WORKSTATION_DISPLAYGENLOCKCAPABLE_GET

# Function to detect the GL-Sync module.
_ADL2_Workstation_GLSyncModuleDetect_Get = ADL2_WORKSTATION_GLSYNCMODULEDETECT_GET

# Function to detect the GL-Sync module.
_ADL_Workstation_GLSyncModuleDetect_Get = ADL_WORKSTATION_GLSYNCMODULEDETECT_GET

# Function to describe the GL-Sync module caps.
_ADL2_Workstation_GLSyncModuleInfo_Get = ADL2_WORKSTATION_GLSYNCMODULEINFO_GET

# Function to describe the GL-Sync module caps.
_ADL_Workstation_GLSyncModuleInfo_Get = ADL_WORKSTATION_GLSYNCMODULEINFO_GET

# Function to retrieve the GL-Sync Genlock configuration settings.
_ADL2_Workstation_GLSyncGenlockConfiguration_Get = ADL2_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_GET

# Function to retrieve the GL-Sync Genlock configuration settings.
_ADL_Workstation_GLSyncGenlockConfiguration_Get = ADL_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_GET

# Function to set the GL-Sync Genlock configuration settings.
_ADL2_Workstation_GLSyncGenlockConfiguration_Set = ADL2_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_SET

# Function to set the GL-Sync Genlock configuration settings.
_ADL_Workstation_GLSyncGenlockConfiguration_Set = ADL_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_SET

# Function to retrieve GL-Sync port information.
_ADL2_Workstation_GLSyncPortState_Get = ADL2_WORKSTATION_GLSYNCPORTSTATE_GET

# Function to retrieve GL-Sync port information.
_ADL_Workstation_GLSyncPortState_Get = ADL_WORKSTATION_GLSYNCPORTSTATE_GET

# Function to perform GL-Sync port control.
_ADL2_Workstation_GLSyncPortState_Set = ADL2_WORKSTATION_GLSYNCPORTSTATE_SET

# Function to perform GL-Sync port control.
_ADL_Workstation_GLSyncPortState_Set = ADL_WORKSTATION_GLSYNCPORTSTATE_SET

# Function to retrieve the GL-Sync mode for a display.
_ADL2_Workstation_DisplayGLSyncMode_Get = ADL2_WORKSTATION_DISPLAYGLSYNCMODE_GET

# Function to retrieve the GL-Sync mode for a display.
_ADL_Workstation_DisplayGLSyncMode_Get = ADL_WORKSTATION_DISPLAYGLSYNCMODE_GET

# Function to set the GL-Sync mode for a display.
_ADL2_Workstation_DisplayGLSyncMode_Set = ADL2_WORKSTATION_DISPLAYGLSYNCMODE_SET

# Function to set the GL-Sync mode for a display.
_ADL_Workstation_DisplayGLSyncMode_Set = ADL_WORKSTATION_DISPLAYGLSYNCMODE_SET

# Function to get the supported GL-Sync topology.
_ADL2_Workstation_GLSyncSupportedTopology_Get = ADL2_WORKSTATION_GLSYNCSUPPORTEDTOPOLOGY_GET

# Function to get the supported GL-Sync topology.
_ADL_Workstation_GLSyncSupportedTopology_Get = ADL_WORKSTATION_GLSYNCSUPPORTEDTOPOLOGY_GET

# Function to get the load balancing state of the specified adapter.
_ADL2_Workstation_LoadBalancing_Get = ADL2_WORKSTATION_LOADBALANCING_GET

# Function to get the load balancing state of the specified adapter.
_ADL_Workstation_LoadBalancing_Get = ADL_WORKSTATION_LOADBALANCING_GET

# Function to set the load balancing state of the specified adapter.
_ADL2_Workstation_LoadBalancing_Set = ADL2_WORKSTATION_LOADBALANCING_SET

# Function to set the load balancing state of the specified adapter.
_ADL_Workstation_LoadBalancing_Set = ADL_WORKSTATION_LOADBALANCING_SET

# Function to set the load balancing capabilities for the specified adapter.
_ADL2_Workstation_LoadBalancing_Caps = ADL2_WORKSTATION_LOADBALANCING_CAPS

# Function to set the load balancing capabilities for the specified adapter.
_ADL_Workstation_LoadBalancing_Caps = ADL_WORKSTATION_LOADBALANCING_CAPS

# Function to get current requested state of Deep Bit Depth and related settings.
_ADL2_Workstation_DeepBitDepth_Get = ADL2_WORKSTATION_DEEPBITDEPTH_GET

# Function to get current requested state of Deep Bit Depth and related settings.
_ADL_Workstation_DeepBitDepth_Get = ADL_WORKSTATION_DEEPBITDEPTH_GET

# Function to set requested state of Deep Bit Depth and related settings.
_ADL2_Workstation_DeepBitDepth_Set = ADL2_WORKSTATION_DEEPBITDEPTH_SET

# Function to set requested state of Deep Bit Depth and related settings.
_ADL_Workstation_DeepBitDepth_Set = ADL_WORKSTATION_DEEPBITDEPTH_SET

# Function to get ECC (Error Correction Code) Capabilities on the specified adapter. This function implements the CI call to get ECC (Error Correction Code) Capabilities on the specified adapter.
_ADL2_Workstation_ECC_Caps = ADL2_WORKSTATION_ECC_CAPS

# Function to get ECC (Error Correction Code) Capabilities on the specified adapter. This function implements the CI call to get ECC (Error Correction Code) Capabilities on the specified adapter.
_ADL_Workstation_ECC_Caps = ADL_WORKSTATION_ECC_CAPS

# Function to get ECC (Error Correction Code) current and desired states on the specified adapter. This function implements the CI call to get ECC (Error Correction Code) current mode(driver applied mode) and the desired mode (user requested mode) on the specified adapter.
_ADL2_Workstation_ECC_Get = ADL2_WORKSTATION_ECC_GET

# Function to get ECC (Error Correction Code) current and desired states on the specified adapter. This function implements the CI call to get ECC (Error Correction Code) current mode(driver applied mode) and the desired mode (user requested mode) on the specified adapter.
_ADL_Workstation_ECC_Get = ADL_WORKSTATION_ECC_GET

# Function to get ECC (Error Correction Code) current and desired states on the specified adapter. This function implements the CI call to get ECC (Error Correction Code) current mode(driver applied mode) and the desired mode (user requested mode) on the specified adapter.
_ADL2_Workstation_ECCX2_Get = ADL2_WORKSTATION_ECCX2_GET

# Function to get ECC (Error Correction Code) current and desired states on the specified adapter. This function implements the CI call to get ECC (Error Correction Code) current mode(driver applied mode) and the desired mode (user requested mode) on the specified adapter.
_ADL_Workstation_ECCX2_Get = ADL_WORKSTATION_ECCX2_GET

# Function to get ECC statistics on the specified adapter. This function implements the CI call to get SEC(Single Error Correct) and DED(Double Error Detect) Counts on the specified adapter.
_ADL2_Workstation_ECCData_Get = ADL2_WORKSTATION_ECCDATA_GET

# Function to get ECC statistics on the specified adapter. This function implements the CI call to get SEC(Single Error Correct) and DED(Double Error Detect) Counts on the specified adapter.
_ADL_Workstation_ECCData_Get = ADL_WORKSTATION_ECCDATA_GET

# Function to set ECC Mode on the specified adapter This function implements the CI call to set ECC (Error Correction Code) to turn on and off this feature on the specified adapter.
_ADL2_Workstation_ECC_Set = ADL2_WORKSTATION_ECC_SET

# Function to set ECC Mode on the specified adapter This function implements the CI call to set ECC (Error Correction Code) to turn on and off this feature on the specified adapter.
_ADL_Workstation_ECC_Set = ADL_WORKSTATION_ECC_SET


def Init(hDLL):
    global _ADL2_Workstation_Caps
    global _ADL_Workstation_Caps
    global _ADL2_Workstation_Stereo_Get
    global _ADL_Workstation_Stereo_Get
    global _ADL2_Workstation_Stereo_Set
    global _ADL_Workstation_Stereo_Set
    global _ADL2_Workstation_AdapterNumOfGLSyncConnectors_Get
    global _ADL_Workstation_AdapterNumOfGLSyncConnectors_Get
    global _ADL2_Workstation_DisplayGenlockCapable_Get
    global _ADL_Workstation_DisplayGenlockCapable_Get
    global _ADL2_Workstation_GLSyncModuleDetect_Get
    global _ADL_Workstation_GLSyncModuleDetect_Get
    global _ADL2_Workstation_GLSyncModuleInfo_Get
    global _ADL_Workstation_GLSyncModuleInfo_Get
    global _ADL2_Workstation_GLSyncGenlockConfiguration_Get
    global _ADL_Workstation_GLSyncGenlockConfiguration_Get
    global _ADL2_Workstation_GLSyncGenlockConfiguration_Set
    global _ADL_Workstation_GLSyncGenlockConfiguration_Set
    global _ADL2_Workstation_GLSyncPortState_Get
    global _ADL_Workstation_GLSyncPortState_Get
    global _ADL2_Workstation_GLSyncPortState_Set
    global _ADL_Workstation_GLSyncPortState_Set
    global _ADL2_Workstation_DisplayGLSyncMode_Get
    global _ADL_Workstation_DisplayGLSyncMode_Get
    global _ADL2_Workstation_DisplayGLSyncMode_Set
    global _ADL_Workstation_DisplayGLSyncMode_Set
    global _ADL2_Workstation_GLSyncSupportedTopology_Get
    global _ADL_Workstation_GLSyncSupportedTopology_Get
    global _ADL2_Workstation_LoadBalancing_Get
    global _ADL_Workstation_LoadBalancing_Get
    global _ADL2_Workstation_LoadBalancing_Set
    global _ADL_Workstation_LoadBalancing_Set
    global _ADL2_Workstation_LoadBalancing_Caps
    global _ADL_Workstation_LoadBalancing_Caps
    global _ADL2_Workstation_DeepBitDepth_Get
    global _ADL_Workstation_DeepBitDepth_Get
    global _ADL2_Workstation_DeepBitDepth_Set
    global _ADL_Workstation_DeepBitDepth_Set
    global _ADL2_Workstation_ECC_Caps
    global _ADL_Workstation_ECC_Caps
    global _ADL2_Workstation_ECC_Get
    global _ADL_Workstation_ECC_Get
    global _ADL2_Workstation_ECCX2_Get
    global _ADL_Workstation_ECCX2_Get
    global _ADL2_Workstation_ECCData_Get
    global _ADL_Workstation_ECCData_Get
    global _ADL2_Workstation_ECC_Set
    global _ADL_Workstation_ECC_Set

    _ADL2_Workstation_Caps = ADL2_WORKSTATION_CAPS(
          GetProcAddress(hDLL, "ADL2_Workstation_Caps")
    )
    _ADL_Workstation_Caps = ADL_WORKSTATION_CAPS(
          GetProcAddress(hDLL, "ADL_Workstation_Caps")
    )
    _ADL2_Workstation_Stereo_Get = ADL2_WORKSTATION_STEREO_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_Stereo_Get")
    )
    _ADL_Workstation_Stereo_Get = ADL_WORKSTATION_STEREO_GET(
          GetProcAddress(hDLL, "ADL_Workstation_Stereo_Get")
    )
    _ADL2_Workstation_Stereo_Set = ADL2_WORKSTATION_STEREO_SET(
          GetProcAddress(hDLL, "ADL2_Workstation_Stereo_Set")
    )
    _ADL_Workstation_Stereo_Set = ADL_WORKSTATION_STEREO_SET(
          GetProcAddress(hDLL, "ADL_Workstation_Stereo_Set")
    )
    _ADL2_Workstation_AdapterNumOfGLSyncConnectors_Get = ADL2_WORKSTATION_ADAPTERNUMOFGLSYNCCONNECTORS_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_AdapterNumOfGLSyncConnectors_Get")
    )
    _ADL_Workstation_AdapterNumOfGLSyncConnectors_Get = ADL_WORKSTATION_ADAPTERNUMOFGLSYNCCONNECTORS_GET(
          GetProcAddress(hDLL, "ADL_Workstation_AdapterNumOfGLSyncConnectors_Get")
    )
    _ADL2_Workstation_DisplayGenlockCapable_Get = ADL2_WORKSTATION_DISPLAYGENLOCKCAPABLE_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_DisplayGenlockCapable_Get")
    )
    _ADL_Workstation_DisplayGenlockCapable_Get = ADL_WORKSTATION_DISPLAYGENLOCKCAPABLE_GET(
          GetProcAddress(hDLL, "ADL_Workstation_DisplayGenlockCapable_Get")
    )
    _ADL2_Workstation_GLSyncModuleDetect_Get = ADL2_WORKSTATION_GLSYNCMODULEDETECT_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_GLSyncModuleDetect_Get")
    )
    _ADL_Workstation_GLSyncModuleDetect_Get = ADL_WORKSTATION_GLSYNCMODULEDETECT_GET(
          GetProcAddress(hDLL, "ADL_Workstation_GLSyncModuleDetect_Get")
    )
    _ADL2_Workstation_GLSyncModuleInfo_Get = ADL2_WORKSTATION_GLSYNCMODULEINFO_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_GLSyncModuleInfo_Get")
    )
    _ADL_Workstation_GLSyncModuleInfo_Get = ADL_WORKSTATION_GLSYNCMODULEINFO_GET(
          GetProcAddress(hDLL, "ADL_Workstation_GLSyncModuleInfo_Get")
    )
    _ADL2_Workstation_GLSyncGenlockConfiguration_Get = ADL2_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_GLSyncGenlockConfiguration_Get")
    )
    _ADL_Workstation_GLSyncGenlockConfiguration_Get = ADL_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_GET(
          GetProcAddress(hDLL, "ADL_Workstation_GLSyncGenlockConfiguration_Get")
    )
    _ADL2_Workstation_GLSyncGenlockConfiguration_Set = ADL2_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_SET(
          GetProcAddress(hDLL, "ADL2_Workstation_GLSyncGenlockConfiguration_Set")
    )
    _ADL_Workstation_GLSyncGenlockConfiguration_Set = ADL_WORKSTATION_GLSYNCGENLOCKCONFIGURATION_SET(
          GetProcAddress(hDLL, "ADL_Workstation_GLSyncGenlockConfiguration_Set")
    )
    _ADL2_Workstation_GLSyncPortState_Get = ADL2_WORKSTATION_GLSYNCPORTSTATE_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_GLSyncPortState_Get")
    )
    _ADL_Workstation_GLSyncPortState_Get = ADL_WORKSTATION_GLSYNCPORTSTATE_GET(
          GetProcAddress(hDLL, "ADL_Workstation_GLSyncPortState_Get")
    )
    _ADL2_Workstation_GLSyncPortState_Set = ADL2_WORKSTATION_GLSYNCPORTSTATE_SET(
          GetProcAddress(hDLL, "ADL2_Workstation_GLSyncPortState_Set")
    )
    _ADL_Workstation_GLSyncPortState_Set = ADL_WORKSTATION_GLSYNCPORTSTATE_SET(
          GetProcAddress(hDLL, "ADL_Workstation_GLSyncPortState_Set")
    )
    _ADL2_Workstation_DisplayGLSyncMode_Get = ADL2_WORKSTATION_DISPLAYGLSYNCMODE_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_DisplayGLSyncMode_Get")
    )
    _ADL_Workstation_DisplayGLSyncMode_Get = ADL_WORKSTATION_DISPLAYGLSYNCMODE_GET(
          GetProcAddress(hDLL, "ADL_Workstation_DisplayGLSyncMode_Get")
    )
    _ADL2_Workstation_DisplayGLSyncMode_Set = ADL2_WORKSTATION_DISPLAYGLSYNCMODE_SET(
          GetProcAddress(hDLL, "ADL2_Workstation_DisplayGLSyncMode_Set")
    )
    _ADL_Workstation_DisplayGLSyncMode_Set = ADL_WORKSTATION_DISPLAYGLSYNCMODE_SET(
          GetProcAddress(hDLL, "ADL_Workstation_DisplayGLSyncMode_Set")
    )
    _ADL2_Workstation_GLSyncSupportedTopology_Get = ADL2_WORKSTATION_GLSYNCSUPPORTEDTOPOLOGY_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_GLSyncSupportedTopology_Get")
    )
    _ADL_Workstation_GLSyncSupportedTopology_Get = ADL_WORKSTATION_GLSYNCSUPPORTEDTOPOLOGY_GET(
          GetProcAddress(hDLL, "ADL_Workstation_GLSyncSupportedTopology_Get")
    )
    _ADL2_Workstation_LoadBalancing_Get = ADL2_WORKSTATION_LOADBALANCING_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_LoadBalancing_Get")
    )
    _ADL_Workstation_LoadBalancing_Get = ADL_WORKSTATION_LOADBALANCING_GET(
          GetProcAddress(hDLL, "ADL_Workstation_LoadBalancing_Get")
    )
    _ADL2_Workstation_LoadBalancing_Set = ADL2_WORKSTATION_LOADBALANCING_SET(
          GetProcAddress(hDLL, "ADL2_Workstation_LoadBalancing_Set")
    )
    _ADL_Workstation_LoadBalancing_Set = ADL_WORKSTATION_LOADBALANCING_SET(
          GetProcAddress(hDLL, "ADL_Workstation_LoadBalancing_Set")
    )
    _ADL2_Workstation_LoadBalancing_Caps = ADL2_WORKSTATION_LOADBALANCING_CAPS(
          GetProcAddress(hDLL, "ADL2_Workstation_LoadBalancing_Caps")
    )
    _ADL_Workstation_LoadBalancing_Caps = ADL_WORKSTATION_LOADBALANCING_CAPS(
          GetProcAddress(hDLL, "ADL_Workstation_LoadBalancing_Caps")
    )
    _ADL2_Workstation_DeepBitDepth_Get = ADL2_WORKSTATION_DEEPBITDEPTH_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_DeepBitDepth_Get")
    )
    _ADL_Workstation_DeepBitDepth_Get = ADL_WORKSTATION_DEEPBITDEPTH_GET(
          GetProcAddress(hDLL, "ADL_Workstation_DeepBitDepth_Get")
    )
    _ADL2_Workstation_DeepBitDepth_Set = ADL2_WORKSTATION_DEEPBITDEPTH_SET(
          GetProcAddress(hDLL, "ADL2_Workstation_DeepBitDepth_Set")
    )
    _ADL_Workstation_DeepBitDepth_Set = ADL_WORKSTATION_DEEPBITDEPTH_SET(
          GetProcAddress(hDLL, "ADL_Workstation_DeepBitDepth_Set")
    )
    _ADL2_Workstation_ECC_Caps = ADL2_WORKSTATION_ECC_CAPS(
          GetProcAddress(hDLL, "ADL2_Workstation_ECC_Caps")
    )
    _ADL_Workstation_ECC_Caps = ADL_WORKSTATION_ECC_CAPS(
          GetProcAddress(hDLL, "ADL_Workstation_ECC_Caps")
    )
    _ADL2_Workstation_ECC_Get = ADL2_WORKSTATION_ECC_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_ECC_Get")
    )
    _ADL_Workstation_ECC_Get = ADL_WORKSTATION_ECC_GET(
          GetProcAddress(hDLL, "ADL_Workstation_ECC_Get")
    )
    _ADL2_Workstation_ECCX2_Get = ADL2_WORKSTATION_ECCX2_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_ECCX2_Get")
    )
    _ADL_Workstation_ECCX2_Get = ADL_WORKSTATION_ECCX2_GET(
          GetProcAddress(hDLL, "ADL_Workstation_ECCX2_Get")
    )
    _ADL2_Workstation_ECCData_Get = ADL2_WORKSTATION_ECCDATA_GET(
          GetProcAddress(hDLL, "ADL2_Workstation_ECCData_Get")
    )
    _ADL_Workstation_ECCData_Get = ADL_WORKSTATION_ECCDATA_GET(
          GetProcAddress(hDLL, "ADL_Workstation_ECCData_Get")
    )
    _ADL2_Workstation_ECC_Set = ADL2_WORKSTATION_ECC_SET(
          GetProcAddress(hDLL, "ADL2_Workstation_ECC_Set")
    )
    _ADL_Workstation_ECC_Set = ADL_WORKSTATION_ECC_SET(
          GetProcAddress(hDLL, "ADL_Workstation_ECC_Set")
    )


__all__ = (
    '_ADL2_Workstation_Caps',
    '_ADL_Workstation_Caps',
    '_ADL2_Workstation_Stereo_Get',
    '_ADL_Workstation_Stereo_Get',
    '_ADL2_Workstation_Stereo_Set',
    '_ADL_Workstation_Stereo_Set',
    '_ADL2_Workstation_AdapterNumOfGLSyncConnectors_Get',
    '_ADL_Workstation_AdapterNumOfGLSyncConnectors_Get',
    '_ADL2_Workstation_DisplayGenlockCapable_Get',
    '_ADL_Workstation_DisplayGenlockCapable_Get',
    '_ADL2_Workstation_GLSyncModuleDetect_Get',
    '_ADL_Workstation_GLSyncModuleDetect_Get',
    '_ADL2_Workstation_GLSyncModuleInfo_Get',
    '_ADL_Workstation_GLSyncModuleInfo_Get',
    '_ADL2_Workstation_GLSyncGenlockConfiguration_Get',
    '_ADL_Workstation_GLSyncGenlockConfiguration_Get',
    '_ADL2_Workstation_GLSyncGenlockConfiguration_Set',
    '_ADL_Workstation_GLSyncGenlockConfiguration_Set',
    '_ADL2_Workstation_GLSyncPortState_Get',
    '_ADL_Workstation_GLSyncPortState_Get',
    '_ADL2_Workstation_GLSyncPortState_Set',
    '_ADL_Workstation_GLSyncPortState_Set',
    '_ADL2_Workstation_DisplayGLSyncMode_Get',
    '_ADL_Workstation_DisplayGLSyncMode_Get',
    '_ADL2_Workstation_DisplayGLSyncMode_Set',
    '_ADL_Workstation_DisplayGLSyncMode_Set',
    '_ADL2_Workstation_GLSyncSupportedTopology_Get',
    '_ADL_Workstation_GLSyncSupportedTopology_Get',
    '_ADL2_Workstation_LoadBalancing_Get',
    '_ADL_Workstation_LoadBalancing_Get',
    '_ADL2_Workstation_LoadBalancing_Set',
    '_ADL_Workstation_LoadBalancing_Set',
    '_ADL2_Workstation_LoadBalancing_Caps',
    '_ADL_Workstation_LoadBalancing_Caps',
    '_ADL2_Workstation_DeepBitDepth_Get',
    '_ADL_Workstation_DeepBitDepth_Get',
    '_ADL2_Workstation_DeepBitDepth_Set',
    '_ADL_Workstation_DeepBitDepth_Set',
    '_ADL2_Workstation_ECC_Caps',
    '_ADL_Workstation_ECC_Caps',
    '_ADL2_Workstation_ECC_Get',
    '_ADL_Workstation_ECC_Get',
    '_ADL2_Workstation_ECCX2_Get',
    '_ADL_Workstation_ECCX2_Get',
    '_ADL2_Workstation_ECCData_Get',
    '_ADL_Workstation_ECCData_Get',
    '_ADL2_Workstation_ECC_Set',
    '_ADL_Workstation_ECC_Set',
)
