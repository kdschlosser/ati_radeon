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
from .adl_sdk_h import ADL_MAIN_MALLOC_CALLBACK

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


ADL_MAIN_CONTROLX2_CREATE = _int(
    ADL_MAIN_MALLOC_CALLBACK,
    INT,
    ADLThreadingModel
)
ADL2_MAIN_CONTROLX2_CREATE = _int(
    ADL_MAIN_MALLOC_CALLBACK,
    INT,
    POINTER(ADL_CONTEXT_HANDLE),
    ADLThreadingModel
)
ADL_MAIN_CONTROL_CREATE = _int(
    ADL_MAIN_MALLOC_CALLBACK,
    INT
)
ADL2_MAIN_CONTROL_CREATE = _int(
    ADL_MAIN_MALLOC_CALLBACK,
    INT,
    POINTER(ADL_CONTEXT_HANDLE)
)
ADL2_MAIN_CONTROL_REFRESH = _int(
    ADL_CONTEXT_HANDLE
)
ADL_MAIN_CONTROL_REFRESH = _int(

)
ADL_MAIN_CONTROL_DESTROY = _int(

)
ADL2_MAIN_CONTROL_DESTROY = _int(
    ADL_CONTEXT_HANDLE
)
ADL2_GRAPHICS_VERSIONS_GET = _int(
    ADL_CONTEXT_HANDLE,
    POINTER(ADLVersionsInfo)
)
ADL_GRAPHICS_VERSIONS_GET = _int(
    POINTER(ADLVersionsInfo)
)
ADL2_GRAPHICS_VERSIONSX2_GET = _int(
    ADL_CONTEXT_HANDLE,
    POINTER(ADLVersionsInfoX2)
)

# Function to initialize the ADL interface. This function should be called first.
_ADL_Main_ControlX2_Create = ADL_MAIN_CONTROLX2_CREATE

# Function to initialize the ADL2 interface and issue client's context handle.
_ADL2_Main_ControlX2_Create = ADL2_MAIN_CONTROLX2_CREATE

# Function to initialize the ADL interface. This function should be called first.
_ADL_Main_Control_Create = ADL_MAIN_CONTROL_CREATE

# Function to initialize the ADL2 interface and to obtain client's context handle.
_ADL2_Main_Control_Create = ADL2_MAIN_CONTROL_CREATE

# Function to refresh adapter information. This function generates an adapter index
# value for all logical adapters that have ever been present in the system.
_ADL2_Main_Control_Refresh = ADL2_MAIN_CONTROL_REFRESH

# Function to refresh adapter information. This function generates an adapter index
# value for all logical adapters that have ever been present in the system.
_ADL_Main_Control_Refresh = ADL_MAIN_CONTROL_REFRESH

# Function to destroy ADL global pointers. This function should be called last.
_ADL_Main_Control_Destroy = ADL_MAIN_CONTROL_DESTROY

# Destroy client's ADL context. void * 	ADL2_Main_Control_GetProcAddress
# (ADL_CONTEXT_HANDLE context, void *lpModule, char *lpProcName) ADL local interface.
# Function to determine the validity of and retrieve the function pointer
# (similar to the GetProcAdress API) for a specified function. void *
# ADL_Main_Control_GetProcAddress (void *lpModule, char *lpProcName) ADL local interface.
# Function to determine the validity of and retrieve the function pointer
# (similar to the GetProcAdress API) for a specified function.
_ADL2_Main_Control_Destroy = ADL2_MAIN_CONTROL_DESTROY

# Function to retrieve version information.
_ADL2_Graphics_Versions_Get = ADL2_GRAPHICS_VERSIONS_GET

# Function to retrieve version information.
_ADL_Graphics_Versions_Get = ADL_GRAPHICS_VERSIONS_GET

# Function to retrieve s version information.
_ADL2_Graphics_VersionsX2_Get = ADL2_GRAPHICS_VERSIONSX2_GET


def Init(hDLL):
    global _ADL_Main_ControlX2_Create
    global _ADL2_Main_ControlX2_Create
    global _ADL_Main_Control_Create
    global _ADL2_Main_Control_Create
    global _ADL2_Main_Control_Refresh
    global _ADL_Main_Control_Refresh
    global _ADL_Main_Control_Destroy
    global _ADL2_Main_Control_Destroy
    global _ADL2_Graphics_Versions_Get
    global _ADL_Graphics_Versions_Get
    global _ADL2_Graphics_VersionsX2_Get

    _ADL_Main_ControlX2_Create = ADL_MAIN_CONTROLX2_CREATE(
        GetProcAddress(hDLL, "ADL_Main_ControlX2_Create")
    )
    _ADL2_Main_ControlX2_Create = ADL2_MAIN_CONTROLX2_CREATE(
        GetProcAddress(hDLL, "ADL2_Main_ControlX2_Create")
    )
    _ADL_Main_Control_Create = ADL_MAIN_CONTROL_CREATE(
        GetProcAddress(hDLL, "ADL_Main_Control_Create")
    )
    _ADL2_Main_Control_Create = ADL2_MAIN_CONTROL_CREATE(
        GetProcAddress(hDLL, "ADL2_Main_Control_Create")
    )
    _ADL2_Main_Control_Refresh = ADL2_MAIN_CONTROL_REFRESH(
        GetProcAddress(hDLL, "ADL2_Main_Control_Refresh")
    )
    _ADL_Main_Control_Refresh = ADL_MAIN_CONTROL_REFRESH(
        GetProcAddress(hDLL, "ADL_Main_Control_Refresh")
    )
    _ADL_Main_Control_Destroy = ADL_MAIN_CONTROL_DESTROY(
        GetProcAddress(hDLL, "ADL_Main_Control_Destroy")
    )
    _ADL2_Main_Control_Destroy = ADL2_MAIN_CONTROL_DESTROY(
        GetProcAddress(hDLL, "ADL2_Main_Control_Destroy")
    )
    _ADL2_Graphics_Versions_Get = ADL2_GRAPHICS_VERSIONS_GET(
        GetProcAddress(hDLL, "ADL2_Graphics_Versions_Get")
    )
    _ADL_Graphics_Versions_Get = ADL_GRAPHICS_VERSIONS_GET(
        GetProcAddress(hDLL, "ADL_Graphics_Versions_Get")
    )
    _ADL2_Graphics_VersionsX2_Get = ADL2_GRAPHICS_VERSIONSX2_GET(
        GetProcAddress(hDLL, "ADL2_Graphics_VersionsX2_Get")
    )


__all__ = (
    '_ADL_Main_ControlX2_Create',
    '_ADL2_Main_ControlX2_Create',
    '_ADL_Main_Control_Create',
    '_ADL2_Main_Control_Create',
    '_ADL2_Main_Control_Refresh',
    '_ADL_Main_Control_Refresh',
    '_ADL_Main_Control_Destroy',
    '_ADL2_Main_Control_Destroy',
    '_ADL2_Graphics_Versions_Get',
    '_ADL_Graphics_Versions_Get',
    '_ADL2_Graphics_VersionsX2_Get',
)
