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


GETAMDADAPTERINDEX = int(
    POINTER(ADL_CONTEXT_HANDLE)
)
ADL2_APPLICATIONPROFILES_SYSTEM_RELOAD = int(
    ADL_CONTEXT_HANDLE
)
ADL_APPLICATIONPROFILES_SYSTEM_RELOAD = int(

)
ADL2_APPLICATIONPROFILES_USER_LOAD = int(
    ADL_CONTEXT_HANDLE
)
ADL_APPLICATIONPROFILES_USER_LOAD = int(

)
ADL2_APPLICATIONPROFILES_USER_UNLOAD = int(
    ADL_CONTEXT_HANDLE
)
ADL_APPLICATIONPROFILES_USER_UNLOAD = int(

)
ADL2_APPLICATIONPROFILES_PROFILEOFANAPPLICATION_SEARCH = int(
    ADL_CONTEXT_HANDLE,
    POINTER(CHAR),
    POINTER(CHAR),
    POINTER(CHAR),
    POINTER(CHAR),
    POINTER(POINTER(ADLApplicationProfile))
)
ADL_APPLICATIONPROFILES_PROFILEOFANAPPLICATION_SEARCH = int(
    POINTER(CHAR),
    POINTER(CHAR),
    POINTER(CHAR),
    POINTER(CHAR),
    POINTER(POINTER(ADLApplicationProfile))
)
ADL2_APPLICATIONPROFILES_HITLISTS_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLApplicationData))
)
ADL_APPLICATIONPROFILES_HITLISTS_GET = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLApplicationData))
)
ADL2_APPLICATIONPROFILES_HITLISTSX3_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLApplicationDataX3))
)
ADL2_APPLICATIONPROFILES_HITLISTSX2_GET = int(
    ADL_CONTEXT_HANDLE,
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLApplicationDataX2))
)
ADL_APPLICATIONPROFILES_HITLISTSX2_GET = int(
    INT,
    POINTER(INT),
    POINTER(POINTER(ADLApplicationDataX2))
)

_GetAMDAdapterIndex = GETAMDADAPTERINDEX

# Function to Reload System appprofiles.
_ADL2_ApplicationProfiles_System_Reload = ADL2_APPLICATIONPROFILES_SYSTEM_RELOAD

# Function to Reload System appprofiles.
_ADL_ApplicationProfiles_System_Reload = ADL_APPLICATIONPROFILES_SYSTEM_RELOAD

# Function to Load User appprofiles.
_ADL2_ApplicationProfiles_User_Load = ADL2_APPLICATIONPROFILES_USER_LOAD

# Function to Load User appprofiles.
_ADL_ApplicationProfiles_User_Load = ADL_APPLICATIONPROFILES_USER_LOAD

# Function to Unload User appprofiles.
_ADL2_ApplicationProfiles_User_Unload = ADL2_APPLICATIONPROFILES_USER_UNLOAD

# Function to Unload User appprofiles.
_ADL_ApplicationProfiles_User_Unload = ADL_APPLICATIONPROFILES_USER_UNLOAD

# Function to retrieve the profile of an application defined in driver.
_ADL2_ApplicationProfiles_ProfileOfAnApplication_Search = ADL2_APPLICATIONPROFILES_PROFILEOFANAPPLICATION_SEARCH

# Function to retrieve the profile of an application defined in driver.
_ADL_ApplicationProfiles_ProfileOfAnApplication_Search = ADL_APPLICATIONPROFILES_PROFILEOFANAPPLICATION_SEARCH

# Function to retrieve the recent application list from registry.
_ADL2_ApplicationProfiles_HitLists_Get = ADL2_APPLICATIONPROFILES_HITLISTS_GET

# Function to retrieve the recent application list from registry.
_ADL_ApplicationProfiles_HitLists_Get = ADL_APPLICATIONPROFILES_HITLISTS_GET

# Function to retrieve the recent application list from registry.
_ADL2_ApplicationProfiles_HitListsX3_Get = ADL2_APPLICATIONPROFILES_HITLISTSX3_GET

# Function to retrieve the recent application list from registry.
_ADL2_ApplicationProfiles_HitListsX2_Get = ADL2_APPLICATIONPROFILES_HITLISTSX2_GET

# Function to retrieve the recent application list from registry.
_ADL_ApplicationProfiles_HitListsX2_Get = ADL_APPLICATIONPROFILES_HITLISTSX2_GET


def Init(hDLL):
    global _GetAMDAdapterIndex
    global _ADL2_ApplicationProfiles_System_Reload
    global _ADL_ApplicationProfiles_System_Reload
    global _ADL2_ApplicationProfiles_User_Load
    global _ADL_ApplicationProfiles_User_Load
    global _ADL2_ApplicationProfiles_User_Unload
    global _ADL_ApplicationProfiles_User_Unload
    global _ADL2_ApplicationProfiles_ProfileOfAnApplication_Search
    global _ADL_ApplicationProfiles_ProfileOfAnApplication_Search
    global _ADL2_ApplicationProfiles_HitLists_Get
    global _ADL_ApplicationProfiles_HitLists_Get
    global _ADL2_ApplicationProfiles_HitListsX3_Get
    global _ADL2_ApplicationProfiles_HitListsX2_Get
    global _ADL_ApplicationProfiles_HitListsX2_Get

    _GetAMDAdapterIndex = GETAMDADAPTERINDEX(
        GetProcAddress(hDLL, "GetAMDAdapterIndex")
    )
    _ADL2_ApplicationProfiles_System_Reload = ADL2_APPLICATIONPROFILES_SYSTEM_RELOAD(
        GetProcAddress(hDLL, "ADL2_ApplicationProfiles_System_Reload")
    )
    _ADL_ApplicationProfiles_System_Reload = ADL_APPLICATIONPROFILES_SYSTEM_RELOAD(
        GetProcAddress(hDLL, "ADL_ApplicationProfiles_System_Reload")
    )
    _ADL2_ApplicationProfiles_User_Load = ADL2_APPLICATIONPROFILES_USER_LOAD(
        GetProcAddress(hDLL, "ADL2_ApplicationProfiles_User_Load")
    )
    _ADL_ApplicationProfiles_User_Load = ADL_APPLICATIONPROFILES_USER_LOAD(
        GetProcAddress(hDLL, "ADL_ApplicationProfiles_User_Load")
    )
    _ADL2_ApplicationProfiles_User_Unload = ADL2_APPLICATIONPROFILES_USER_UNLOAD(
        GetProcAddress(hDLL, "ADL2_ApplicationProfiles_User_Unload")
    )
    _ADL_ApplicationProfiles_User_Unload = ADL_APPLICATIONPROFILES_USER_UNLOAD(
        GetProcAddress(hDLL, "ADL_ApplicationProfiles_User_Unload")
    )
    _ADL2_ApplicationProfiles_ProfileOfAnApplication_Search = ADL2_APPLICATIONPROFILES_PROFILEOFANAPPLICATION_SEARCH(
        GetProcAddress(hDLL, "ADL2_ApplicationProfiles_ProfileOfAnApplication_Search")
    )
    _ADL_ApplicationProfiles_ProfileOfAnApplication_Search = ADL_APPLICATIONPROFILES_PROFILEOFANAPPLICATION_SEARCH(
        GetProcAddress(hDLL, "ADL_ApplicationProfiles_ProfileOfAnApplication_Search")
    )
    _ADL2_ApplicationProfiles_HitLists_Get = ADL2_APPLICATIONPROFILES_HITLISTS_GET(
        GetProcAddress(hDLL, "ADL2_ApplicationProfiles_HitLists_Get")
    )
    _ADL_ApplicationProfiles_HitLists_Get = ADL_APPLICATIONPROFILES_HITLISTS_GET(
        GetProcAddress(hDLL, "ADL_ApplicationProfiles_HitLists_Get")
    )
    _ADL2_ApplicationProfiles_HitListsX3_Get = ADL2_APPLICATIONPROFILES_HITLISTSX3_GET(
        GetProcAddress(hDLL, "ADL2_ApplicationProfiles_HitListsX3_Get")
    )
    _ADL2_ApplicationProfiles_HitListsX2_Get = ADL2_APPLICATIONPROFILES_HITLISTSX2_GET(
        GetProcAddress(hDLL, "ADL2_ApplicationProfiles_HitListsX2_Get")
    )
    _ADL_ApplicationProfiles_HitListsX2_Get = ADL_APPLICATIONPROFILES_HITLISTSX2_GET(
        GetProcAddress(hDLL, "ADL_ApplicationProfiles_HitListsX2_Get")
    )


__all__ = (
    '_GetAMDAdapterIndex',
    '_ADL2_ApplicationProfiles_System_Reload',
    '_ADL_ApplicationProfiles_System_Reload',
    '_ADL2_ApplicationProfiles_User_Load',
    '_ADL_ApplicationProfiles_User_Load',
    '_ADL2_ApplicationProfiles_User_Unload',
    '_ADL_ApplicationProfiles_User_Unload',
    '_ADL2_ApplicationProfiles_ProfileOfAnApplication_Search',
    '_ADL_ApplicationProfiles_ProfileOfAnApplication_Search',
    '_ADL2_ApplicationProfiles_HitLists_Get',
    '_ADL_ApplicationProfiles_HitLists_Get',
    '_ADL2_ApplicationProfiles_HitListsX3_Get',
    '_ADL2_ApplicationProfiles_HitListsX2_Get',
    '_ADL_ApplicationProfiles_HitListsX2_Get',
)
