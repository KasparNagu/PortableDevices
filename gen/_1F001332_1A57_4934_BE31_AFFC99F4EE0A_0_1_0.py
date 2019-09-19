# -*- coding: mbcs -*-
typelib_path = 'portabledeviceapi.dll'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
WSTRING = c_wchar_p
from comtypes.typeinfo import tagVARKIND
from comtypes.typeinfo import tagPARAMDESCEX
from ctypes.wintypes import _LARGE_INTEGER
from ctypes.wintypes import _ULARGE_INTEGER
from comtypes import IUnknown
from comtypes.automation import IDispatch
from comtypes.typeinfo import tagVARDESC
from comtypes import BSTR
from ctypes.wintypes import VARIANT_BOOL
from comtypes.automation import SCODE
from comtypes.automation import DECIMAL
STRING = c_char_p
from comtypes.typeinfo import tagSYSKIND
from ctypes.wintypes import _FILETIME
from ctypes.wintypes import _FILETIME
from comtypes.typeinfo import ITypeLib
from comtypes.typeinfo import tagSAFEARRAYBOUND
from ctypes.wintypes import _LARGE_INTEGER
from ctypes.wintypes import _ULARGE_INTEGER
from comtypes.typeinfo import tagFUNCDESC
from comtypes.typeinfo import tagTYPEDESC
from comtypes.typeinfo import tagTLIBATTR
from comtypes.typeinfo import IRecordInfo
from comtypes.typeinfo import tagELEMDESC
from comtypes.typeinfo import tagPARAMDESC
from comtypes.typeinfo import tagARRAYDESC
from comtypes.typeinfo import tagFUNCKIND
from comtypes.typeinfo import tagCALLCONV
from comtypes.typeinfo import tagSAFEARRAYBOUND
from comtypes.typeinfo import ITypeInfo
from comtypes.automation import VARIANT
from comtypes.typeinfo import tagIDLDESC
from ctypes.wintypes import DWORD
from comtypes.typeinfo import ULONG_PTR
from comtypes.typeinfo import tagTYPEATTR
from comtypes.automation import tagINVOKEKIND
from comtypes.typeinfo import ITypeComp
from comtypes.typeinfo import tagTYPEKIND
from comtypes.typeinfo import tagDESCKIND
from comtypes.automation import VARIANT


class ISequentialStream(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteRead',
              ( ['out'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'RemoteWrite',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]
################################################################
## code template for ISequentialStream implementation
##class ISequentialStream_Impl(object):
##    def RemoteRead(self, cb):
##        '-no docstring-'
##        #return pv, pcbRead
##
##    def RemoteWrite(self, pv, cb):
##        '-no docstring-'
##        #return pcbWritten
##

class PortableDevice(CoClass):
    u'PortableDevice Class'
    _reg_clsid_ = GUID('{728A21C5-3D9E-48D7-9810-864848F0F404}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1F001332-1A57-4934-BE31-AFFC99F4EE0A}', 1, 0)
class IPortableDevice(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDevice Interface'
    _iid_ = GUID('{625E2DF8-6392-4CF0-9AD1-3CFA5F17775C}')
    _idlflags_ = []
PortableDevice._com_interfaces_ = [IPortableDevice]

class IPortableDeviceManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceManager Interface'
    _iid_ = GUID('{A1567595-4C2F-4574-A6FA-ECEF917B9A40}')
    _idlflags_ = []
IPortableDeviceManager._methods_ = [
    COMMETHOD([], HRESULT, 'GetDevices',
              ( ['in', 'out'], POINTER(WSTRING), 'pPnPDeviceIDs' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pcPnPDeviceIDs' )),
    COMMETHOD([], HRESULT, 'RefreshDeviceList'),
    COMMETHOD([], HRESULT, 'GetDeviceFriendlyName',
              ( ['in'], WSTRING, 'pszPnPDeviceID' ),
              ( ['in', 'out'], POINTER(c_ushort), 'pDeviceFriendlyName' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pcchDeviceFriendlyName' )),
    COMMETHOD([], HRESULT, 'GetDeviceDescription',
              ( ['in'], WSTRING, 'pszPnPDeviceID' ),
              ( ['in', 'out'], POINTER(c_ushort), 'pDeviceDescription' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pcchDeviceDescription' )),
    COMMETHOD([], HRESULT, 'GetDeviceManufacturer',
              ( ['in'], WSTRING, 'pszPnPDeviceID' ),
              ( ['in', 'out'], POINTER(c_ushort), 'pDeviceManufacturer' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pcchDeviceManufacturer' )),
    COMMETHOD([], HRESULT, 'GetDeviceProperty',
              ( ['in'], WSTRING, 'pszPnPDeviceID' ),
              ( ['in'], WSTRING, 'pszDevicePropertyName' ),
              ( ['in', 'out'], POINTER(c_ubyte), 'pData' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pcbData' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwType' )),
    COMMETHOD([], HRESULT, 'GetPrivateDevices',
              ( ['in', 'out'], POINTER(WSTRING), 'pPnPDeviceIDs' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pcPnPDeviceIDs' )),
]
################################################################
## code template for IPortableDeviceManager implementation
##class IPortableDeviceManager_Impl(object):
##    def GetDeviceProperty(self, pszPnPDeviceID, pszDevicePropertyName):
##        '-no docstring-'
##        #return pData, pcbData, pdwType
##
##    def GetDeviceFriendlyName(self, pszPnPDeviceID):
##        '-no docstring-'
##        #return pDeviceFriendlyName, pcchDeviceFriendlyName
##
##    def GetDeviceDescription(self, pszPnPDeviceID):
##        '-no docstring-'
##        #return pDeviceDescription, pcchDeviceDescription
##
##    def GetDeviceManufacturer(self, pszPnPDeviceID):
##        '-no docstring-'
##        #return pDeviceManufacturer, pcchDeviceManufacturer
##
##    def RefreshDeviceList(self):
##        '-no docstring-'
##        #return 
##
##    def GetDevices(self):
##        '-no docstring-'
##        #return pPnPDeviceIDs, pcPnPDeviceIDs
##
##    def GetPrivateDevices(self):
##        '-no docstring-'
##        #return pPnPDeviceIDs, pcPnPDeviceIDs
##

class tagCAUL(Structure):
    pass
tagCAUL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ulong)),
]
assert sizeof(tagCAUL) == 16, sizeof(tagCAUL)
assert alignment(tagCAUL) == 8, alignment(tagCAUL)
class PortableDeviceService(CoClass):
    u'PortableDeviceService Class'
    _reg_clsid_ = GUID('{EF5DB4C2-9312-422C-9152-411CD9C4DD84}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1F001332-1A57-4934-BE31-AFFC99F4EE0A}', 1, 0)
class IPortableDeviceService(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceService Interface'
    _iid_ = GUID('{D3BD3A44-D7B5-40A9-98B7-2FA4D01DEC08}')
    _idlflags_ = []
PortableDeviceService._com_interfaces_ = [IPortableDeviceService]

class _BYTE_SIZEDARR(Structure):
    pass
_BYTE_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ubyte)),
]
assert sizeof(_BYTE_SIZEDARR) == 16, sizeof(_BYTE_SIZEDARR)
assert alignment(_BYTE_SIZEDARR) == 8, alignment(_BYTE_SIZEDARR)
class IPortableDeviceValues(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceValues Interface'
    _iid_ = GUID('{6848F6F2-3155-4F86-B6F5-263EEEAB3143}')
    _idlflags_ = []
class IPortableDeviceServiceCapabilities(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceServiceCapabilities Interface'
    _iid_ = GUID('{24DBD89D-413E-43E0-BD5B-197F3C56C886}')
    _idlflags_ = []
class IPortableDeviceContent(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceContent Interface'
    _iid_ = GUID('{6A96ED84-7C73-4480-9938-BF5AF477D426}')
    _idlflags_ = []
class IPortableDeviceContent2(IPortableDeviceContent):
    _case_insensitive_ = True
    u'IPortableDeviceContent2 Interface'
    _iid_ = GUID('{9B4ADD96-F6BF-4034-8708-ECA72BF10554}')
    _idlflags_ = []
class IPortableDeviceServiceMethods(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceServiceMethods Interface'
    _iid_ = GUID('{E20333C9-FD34-412D-A381-CC6F2D820DF7}')
    _idlflags_ = []
class IPortableDeviceEventCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceEventCallback Interface'
    _iid_ = GUID('{A8792A31-F385-493C-A893-40F64EB45F6E}')
    _idlflags_ = []
IPortableDeviceService._methods_ = [
    COMMETHOD([], HRESULT, 'Open',
              ( ['in'], WSTRING, 'pszPnPServiceID' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pClientInfo' )),
    COMMETHOD([], HRESULT, 'Capabilities',
              ( ['out'], POINTER(POINTER(IPortableDeviceServiceCapabilities)), 'ppCapabilities' )),
    COMMETHOD([], HRESULT, 'Content',
              ( ['out'], POINTER(POINTER(IPortableDeviceContent2)), 'ppContent' )),
    COMMETHOD([], HRESULT, 'Methods',
              ( ['out'], POINTER(POINTER(IPortableDeviceServiceMethods)), 'ppMethods' )),
    COMMETHOD([], HRESULT, 'Cancel'),
    COMMETHOD([], HRESULT, 'Close'),
    COMMETHOD([], HRESULT, 'GetServiceObjectID',
              ( ['out'], POINTER(WSTRING), 'ppszServiceObjectID' )),
    COMMETHOD([], HRESULT, 'GetPnPServiceID',
              ( ['out'], POINTER(WSTRING), 'ppszPnPServiceID' )),
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IPortableDeviceEventCallback), 'pCallback' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pParameters' ),
              ( ['out'], POINTER(WSTRING), 'ppszCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], WSTRING, 'pszCookie' )),
    COMMETHOD([], HRESULT, 'SendCommand',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pParameters' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppResults' )),
]
################################################################
## code template for IPortableDeviceService implementation
##class IPortableDeviceService_Impl(object):
##    def GetPnPServiceID(self):
##        '-no docstring-'
##        #return ppszPnPServiceID
##
##    def Methods(self):
##        '-no docstring-'
##        #return ppMethods
##
##    def GetServiceObjectID(self):
##        '-no docstring-'
##        #return ppszServiceObjectID
##
##    def Capabilities(self):
##        '-no docstring-'
##        #return ppCapabilities
##
##    def Content(self):
##        '-no docstring-'
##        #return ppContent
##
##    def Unadvise(self, pszCookie):
##        '-no docstring-'
##        #return 
##
##    def Cancel(self):
##        '-no docstring-'
##        #return 
##
##    def Close(self):
##        '-no docstring-'
##        #return 
##
##    def Advise(self, dwFlags, pCallback, pParameters):
##        '-no docstring-'
##        #return ppszCookie
##
##    def Open(self, pszPnPServiceID, pClientInfo):
##        '-no docstring-'
##        #return 
##
##    def SendCommand(self, dwFlags, pParameters):
##        '-no docstring-'
##        #return ppResults
##

class tagCACLIPDATA(Structure):
    pass
class tagCLIPDATA(Structure):
    pass
tagCACLIPDATA._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tagCLIPDATA)),
]
assert sizeof(tagCACLIPDATA) == 16, sizeof(tagCACLIPDATA)
assert alignment(tagCACLIPDATA) == 8, alignment(tagCACLIPDATA)
class tagCAH(Structure):
    pass
tagCAH._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_LARGE_INTEGER)),
]
assert sizeof(tagCAH) == 16, sizeof(tagCAH)
assert alignment(tagCAH) == 8, alignment(tagCAH)
class tagRemSNB(Structure):
    pass
tagRemSNB._pack_ = 4
tagRemSNB._fields_ = [
    ('ulCntStr', c_ulong),
    ('ulCntChar', c_ulong),
    ('rgString', POINTER(c_ushort)),
]
assert sizeof(tagRemSNB) == 16, sizeof(tagRemSNB)
assert alignment(tagRemSNB) == 4, alignment(tagRemSNB)
class _wireSAFEARR_BSTR(Structure):
    pass
class _FLAGGED_WORD_BLOB(Structure):
    pass
_wireSAFEARR_BSTR._fields_ = [
    ('Size', c_ulong),
    ('aBstr', POINTER(POINTER(_FLAGGED_WORD_BLOB))),
]
assert sizeof(_wireSAFEARR_BSTR) == 16, sizeof(_wireSAFEARR_BSTR)
assert alignment(_wireSAFEARR_BSTR) == 8, alignment(_wireSAFEARR_BSTR)
class _SHORT_SIZEDARR(Structure):
    pass
_SHORT_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ushort)),
]
assert sizeof(_SHORT_SIZEDARR) == 16, sizeof(_SHORT_SIZEDARR)
assert alignment(_SHORT_SIZEDARR) == 8, alignment(_SHORT_SIZEDARR)
class IEnumSTATSTG(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000D-0000-0000-C000-000000000046}')
    _idlflags_ = []
class tagSTATSTG(Structure):
    pass
IEnumSTATSTG._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(tagSTATSTG), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum' )),
]
################################################################
## code template for IEnumSTATSTG implementation
##class IEnumSTATSTG_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

class tagCAUH(Structure):
    pass
tagCAUH._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_ULARGE_INTEGER)),
]
assert sizeof(tagCAUH) == 16, sizeof(tagCAUH)
assert alignment(tagCAUH) == 8, alignment(tagCAUH)
class IPortableDeviceServiceMethodCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceServiceMethodCallback Interface'
    _iid_ = GUID('{C424233C-AFCE-4828-A756-7ED7A2350083}')
    _idlflags_ = []
IPortableDeviceServiceMethodCallback._methods_ = [
    COMMETHOD([], HRESULT, 'OnComplete',
              ( ['in'], HRESULT, 'hrStatus' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pResults' )),
]
################################################################
## code template for IPortableDeviceServiceMethodCallback implementation
##class IPortableDeviceServiceMethodCallback_Impl(object):
##    def OnComplete(self, hrStatus, pResults):
##        '-no docstring-'
##        #return 
##

class PortableDeviceWebControl(CoClass):
    u'Dispatch Class for Web Host Applications'
    _reg_clsid_ = GUID('{186DD02C-2DEC-41B5-A7D4-B59056FADE51}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1F001332-1A57-4934-BE31-AFFC99F4EE0A}', 1, 0)
class IPortableDeviceWebControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{94FC7953-5CA1-483A-8AEE-DF52E7747D00}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
PortableDeviceWebControl._com_interfaces_ = [IPortableDeviceWebControl]

class _LONG_SIZEDARR(Structure):
    pass
_LONG_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ulong)),
]
assert sizeof(_LONG_SIZEDARR) == 16, sizeof(_LONG_SIZEDARR)
assert alignment(_LONG_SIZEDARR) == 8, alignment(_LONG_SIZEDARR)
_FLAGGED_WORD_BLOB._pack_ = 4
_FLAGGED_WORD_BLOB._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('asData', POINTER(c_ushort)),
]
assert sizeof(_FLAGGED_WORD_BLOB) == 16, sizeof(_FLAGGED_WORD_BLOB)
assert alignment(_FLAGGED_WORD_BLOB) == 4, alignment(_FLAGGED_WORD_BLOB)
class tagCABSTRBLOB(Structure):
    pass
class tagBSTRBLOB(Structure):
    pass
tagCABSTRBLOB._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tagBSTRBLOB)),
]
assert sizeof(tagCABSTRBLOB) == 16, sizeof(tagCABSTRBLOB)
assert alignment(tagCABSTRBLOB) == 8, alignment(tagCABSTRBLOB)
class tagCAFLT(Structure):
    pass
tagCAFLT._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_float)),
]
assert sizeof(tagCAFLT) == 16, sizeof(tagCAFLT)
assert alignment(tagCAFLT) == 8, alignment(tagCAFLT)
class __MIDL_IOleAutomationTypes_0001(Union):
    pass
class _wireSAFEARR_UNKNOWN(Structure):
    pass
_wireSAFEARR_UNKNOWN._fields_ = [
    ('Size', c_ulong),
    ('apUnknown', POINTER(POINTER(IUnknown))),
]
assert sizeof(_wireSAFEARR_UNKNOWN) == 16, sizeof(_wireSAFEARR_UNKNOWN)
assert alignment(_wireSAFEARR_UNKNOWN) == 8, alignment(_wireSAFEARR_UNKNOWN)
class _wireSAFEARR_DISPATCH(Structure):
    pass
_wireSAFEARR_DISPATCH._fields_ = [
    ('Size', c_ulong),
    ('apDispatch', POINTER(POINTER(IDispatch))),
]
assert sizeof(_wireSAFEARR_DISPATCH) == 16, sizeof(_wireSAFEARR_DISPATCH)
assert alignment(_wireSAFEARR_DISPATCH) == 8, alignment(_wireSAFEARR_DISPATCH)
class _wireSAFEARR_VARIANT(Structure):
    pass
class _wireVARIANT(Structure):
    pass
_wireSAFEARR_VARIANT._fields_ = [
    ('Size', c_ulong),
    ('aVariant', POINTER(POINTER(_wireVARIANT))),
]
assert sizeof(_wireSAFEARR_VARIANT) == 16, sizeof(_wireSAFEARR_VARIANT)
assert alignment(_wireSAFEARR_VARIANT) == 8, alignment(_wireSAFEARR_VARIANT)
class _wireSAFEARR_BRECORD(Structure):
    pass
class _wireBRECORD(Structure):
    pass
_wireSAFEARR_BRECORD._fields_ = [
    ('Size', c_ulong),
    ('aRecord', POINTER(POINTER(_wireBRECORD))),
]
assert sizeof(_wireSAFEARR_BRECORD) == 16, sizeof(_wireSAFEARR_BRECORD)
assert alignment(_wireSAFEARR_BRECORD) == 8, alignment(_wireSAFEARR_BRECORD)
class _wireSAFEARR_HAVEIID(Structure):
    pass
_wireSAFEARR_HAVEIID._fields_ = [
    ('Size', c_ulong),
    ('apUnknown', POINTER(POINTER(IUnknown))),
    ('iid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
]
assert sizeof(_wireSAFEARR_HAVEIID) == 32, sizeof(_wireSAFEARR_HAVEIID)
assert alignment(_wireSAFEARR_HAVEIID) == 8, alignment(_wireSAFEARR_HAVEIID)
class _HYPER_SIZEDARR(Structure):
    pass
_HYPER_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_longlong)),
]
assert sizeof(_HYPER_SIZEDARR) == 16, sizeof(_HYPER_SIZEDARR)
assert alignment(_HYPER_SIZEDARR) == 8, alignment(_HYPER_SIZEDARR)
__MIDL_IOleAutomationTypes_0001._fields_ = [
    ('BstrStr', _wireSAFEARR_BSTR),
    ('UnknownStr', _wireSAFEARR_UNKNOWN),
    ('DispatchStr', _wireSAFEARR_DISPATCH),
    ('VariantStr', _wireSAFEARR_VARIANT),
    ('RecordStr', _wireSAFEARR_BRECORD),
    ('HaveIidStr', _wireSAFEARR_HAVEIID),
    ('ByteStr', _BYTE_SIZEDARR),
    ('WordStr', _SHORT_SIZEDARR),
    ('LongStr', _LONG_SIZEDARR),
    ('HyperStr', _HYPER_SIZEDARR),
]
assert sizeof(__MIDL_IOleAutomationTypes_0001) == 32, sizeof(__MIDL_IOleAutomationTypes_0001)
assert alignment(__MIDL_IOleAutomationTypes_0001) == 8, alignment(__MIDL_IOleAutomationTypes_0001)
class IPortableDeviceDispatchFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5E1EAFC3-E3D7-4132-96FA-759C0F9D1E0F}')
    _idlflags_ = []
IPortableDeviceDispatchFactory._methods_ = [
    COMMETHOD([], HRESULT, 'GetDeviceDispatch',
              ( ['in'], WSTRING, 'pszPnPDeviceID' ),
              ( ['out'], POINTER(POINTER(IDispatch)), 'ppDeviceDispatch' )),
]
################################################################
## code template for IPortableDeviceDispatchFactory implementation
##class IPortableDeviceDispatchFactory_Impl(object):
##    def GetDeviceDispatch(self, pszPnPDeviceID):
##        '-no docstring-'
##        #return ppDeviceDispatch
##

class PortableDeviceFTM(CoClass):
    u'PortableDeviceFTM Class'
    _reg_clsid_ = GUID('{F7C0039A-4762-488A-B4B3-760EF9A1BA9B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1F001332-1A57-4934-BE31-AFFC99F4EE0A}', 1, 0)
PortableDeviceFTM._com_interfaces_ = [IPortableDevice]

class PortableDeviceServiceFTM(CoClass):
    u'PortableDeviceServiceFTM Class'
    _reg_clsid_ = GUID('{1649B154-C794-497A-9B03-F3F0121302F3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1F001332-1A57-4934-BE31-AFFC99F4EE0A}', 1, 0)
PortableDeviceServiceFTM._com_interfaces_ = [IPortableDeviceService]

class IPortableDevicePropVariantCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDevicePropVariantCollection Interface'
    _iid_ = GUID('{89B2E422-4F1B-4316-BCEF-A44AFEA83EB3}')
    _idlflags_ = []
class _tagpropertykey(Structure):
    pass
class IPortableDeviceKeyCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceKeyCollection Interface'
    _iid_ = GUID('{DADA2357-E0AD-492E-98DB-DD61C53BA353}')
    _idlflags_ = []
class IPortableDeviceValuesCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceValuesCollection Interface'
    _iid_ = GUID('{6E3F2D79-4E07-48C4-8208-D8C2E5AF4A99}')
    _idlflags_ = []
IPortableDeviceServiceCapabilities._methods_ = [
    COMMETHOD([], HRESULT, 'GetSupportedMethods',
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppMethods' )),
    COMMETHOD([], HRESULT, 'GetSupportedMethodsByFormat',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Format' ),
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppMethods' )),
    COMMETHOD([], HRESULT, 'GetMethodAttributes',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Method' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppAttributes' )),
    COMMETHOD([], HRESULT, 'GetMethodParameterAttributes',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Method' ),
              ( ['in'], POINTER(_tagpropertykey), 'Parameter' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppAttributes' )),
    COMMETHOD([], HRESULT, 'GetSupportedFormats',
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppFormats' )),
    COMMETHOD([], HRESULT, 'GetFormatAttributes',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Format' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppAttributes' )),
    COMMETHOD([], HRESULT, 'GetSupportedFormatProperties',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Format' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceKeyCollection)), 'ppKeys' )),
    COMMETHOD([], HRESULT, 'GetFormatPropertyAttributes',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Format' ),
              ( ['in'], POINTER(_tagpropertykey), 'Property' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppAttributes' )),
    COMMETHOD([], HRESULT, 'GetSupportedEvents',
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppEvents' )),
    COMMETHOD([], HRESULT, 'GetEventAttributes',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Event' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppAttributes' )),
    COMMETHOD([], HRESULT, 'GetEventParameterAttributes',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Event' ),
              ( ['in'], POINTER(_tagpropertykey), 'Parameter' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppAttributes' )),
    COMMETHOD([], HRESULT, 'GetInheritedServices',
              ( ['in'], c_ulong, 'dwInheritanceType' ),
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppServices' )),
    COMMETHOD([], HRESULT, 'GetFormatRenderingProfiles',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Format' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValuesCollection)), 'ppRenderingProfiles' )),
    COMMETHOD([], HRESULT, 'GetSupportedCommands',
              ( ['out'], POINTER(POINTER(IPortableDeviceKeyCollection)), 'ppCommands' )),
    COMMETHOD([], HRESULT, 'GetCommandOptions',
              ( ['in'], POINTER(_tagpropertykey), 'Command' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppOptions' )),
    COMMETHOD([], HRESULT, 'Cancel'),
]
################################################################
## code template for IPortableDeviceServiceCapabilities implementation
##class IPortableDeviceServiceCapabilities_Impl(object):
##    def GetFormatPropertyAttributes(self, Format, Property):
##        '-no docstring-'
##        #return ppAttributes
##
##    def GetSupportedCommands(self):
##        '-no docstring-'
##        #return ppCommands
##
##    def GetFormatAttributes(self, Format):
##        '-no docstring-'
##        #return ppAttributes
##
##    def GetSupportedFormats(self):
##        '-no docstring-'
##        #return ppFormats
##
##    def GetSupportedEvents(self):
##        '-no docstring-'
##        #return ppEvents
##
##    def GetInheritedServices(self, dwInheritanceType):
##        '-no docstring-'
##        #return ppServices
##
##    def GetEventAttributes(self, Event):
##        '-no docstring-'
##        #return ppAttributes
##
##    def GetFormatRenderingProfiles(self, Format):
##        '-no docstring-'
##        #return ppRenderingProfiles
##
##    def GetMethodAttributes(self, Method):
##        '-no docstring-'
##        #return ppAttributes
##
##    def GetSupportedMethodsByFormat(self, Format):
##        '-no docstring-'
##        #return ppMethods
##
##    def GetSupportedFormatProperties(self, Format):
##        '-no docstring-'
##        #return ppKeys
##
##    def GetCommandOptions(self, Command):
##        '-no docstring-'
##        #return ppOptions
##
##    def Cancel(self):
##        '-no docstring-'
##        #return 
##
##    def GetEventParameterAttributes(self, Event, Parameter):
##        '-no docstring-'
##        #return ppAttributes
##
##    def GetMethodParameterAttributes(self, Method, Parameter):
##        '-no docstring-'
##        #return ppAttributes
##
##    def GetSupportedMethods(self):
##        '-no docstring-'
##        #return ppMethods
##

class _wireSAFEARRAY(Structure):
    pass
wirePSAFEARRAY = POINTER(POINTER(_wireSAFEARRAY))
class tagCALPWSTR(Structure):
    pass
tagCALPWSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(WSTRING)),
]
assert sizeof(tagCALPWSTR) == 16, sizeof(tagCALPWSTR)
assert alignment(tagCALPWSTR) == 8, alignment(tagCALPWSTR)
class tagCAI(Structure):
    pass
tagCAI._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_short)),
]
assert sizeof(tagCAI) == 16, sizeof(tagCAI)
assert alignment(tagCAI) == 8, alignment(tagCAI)
IPortableDeviceWebControl._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'method GetDeviceFromId')], HRESULT, 'GetDeviceFromId',
              ( ['in'], BSTR, 'deviceId' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDevice' )),
    COMMETHOD([dispid(2), helpstring(u'method GetDeviceFromIdAsync')], HRESULT, 'GetDeviceFromIdAsync',
              ( ['in'], BSTR, 'deviceId' ),
              ( ['in'], POINTER(IDispatch), 'pCompletionHandler' ),
              ( ['in'], POINTER(IDispatch), 'pErrorHandler' )),
]
################################################################
## code template for IPortableDeviceWebControl implementation
##class IPortableDeviceWebControl_Impl(object):
##    def GetDeviceFromId(self, deviceId):
##        u'method GetDeviceFromId'
##        #return ppDevice
##
##    def GetDeviceFromIdAsync(self, deviceId, pCompletionHandler, pErrorHandler):
##        u'method GetDeviceFromIdAsync'
##        #return 
##

class __MIDL_IOleAutomationTypes_0004(Union):
    pass
__MIDL_IOleAutomationTypes_0004._fields_ = [
    ('llVal', c_longlong),
    ('lVal', c_int),
    ('bVal', c_ubyte),
    ('iVal', c_short),
    ('fltVal', c_float),
    ('dblVal', c_double),
    ('boolVal', VARIANT_BOOL),
    ('scode', SCODE),
    ('cyVal', c_longlong),
    ('date', c_double),
    ('bstrVal', POINTER(_FLAGGED_WORD_BLOB)),
    ('punkVal', POINTER(IUnknown)),
    ('pdispVal', POINTER(IDispatch)),
    ('parray', POINTER(POINTER(_wireSAFEARRAY))),
    ('brecVal', POINTER(_wireBRECORD)),
    ('pbVal', POINTER(c_ubyte)),
    ('piVal', POINTER(c_short)),
    ('plVal', POINTER(c_int)),
    ('pllVal', POINTER(c_longlong)),
    ('pfltVal', POINTER(c_float)),
    ('pdblVal', POINTER(c_double)),
    ('pboolVal', POINTER(VARIANT_BOOL)),
    ('pscode', POINTER(SCODE)),
    ('pcyVal', POINTER(c_longlong)),
    ('pdate', POINTER(c_double)),
    ('pbstrVal', POINTER(POINTER(_FLAGGED_WORD_BLOB))),
    ('ppunkVal', POINTER(POINTER(IUnknown))),
    ('ppdispVal', POINTER(POINTER(IDispatch))),
    ('pparray', POINTER(POINTER(POINTER(_wireSAFEARRAY)))),
    ('pvarVal', POINTER(POINTER(_wireVARIANT))),
    ('cVal', c_char),
    ('uiVal', c_ushort),
    ('ulVal', c_ulong),
    ('ullVal', c_ulonglong),
    ('intVal', c_int),
    ('uintVal', c_uint),
    ('decVal', DECIMAL),
    ('pdecVal', POINTER(DECIMAL)),
    ('pcVal', STRING),
    ('puiVal', POINTER(c_ushort)),
    ('pulVal', POINTER(c_ulong)),
    ('pullVal', POINTER(c_ulonglong)),
    ('pintVal', POINTER(c_int)),
    ('puintVal', POINTER(c_uint)),
]
assert sizeof(__MIDL_IOleAutomationTypes_0004) == 16, sizeof(__MIDL_IOleAutomationTypes_0004)
assert alignment(__MIDL_IOleAutomationTypes_0004) == 8, alignment(__MIDL_IOleAutomationTypes_0004)
class Library(object):
    u'PortableDeviceApi 1.0 Type Library'
    name = u'PortableDeviceApiLib'
    _reg_typelib_ = ('{1F001332-1A57-4934-BE31-AFFC99F4EE0A}', 1, 0)

class tagCAC(Structure):
    pass
tagCAC._fields_ = [
    ('cElems', c_ulong),
    ('pElems', STRING),
]
assert sizeof(tagCAC) == 16, sizeof(tagCAC)
assert alignment(tagCAC) == 8, alignment(tagCAC)
class tagVersionedStream(Structure):
    pass
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
tagVersionedStream._fields_ = [
    ('guidVersion', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('pStream', POINTER(IStream)),
]
assert sizeof(tagVersionedStream) == 24, sizeof(tagVersionedStream)
assert alignment(tagVersionedStream) == 8, alignment(tagVersionedStream)
class tagCAPROPVARIANT(Structure):
    pass
class tag_inner_PROPVARIANT(Structure):
    pass
tagCAPROPVARIANT._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tag_inner_PROPVARIANT)),
]
assert sizeof(tagCAPROPVARIANT) == 16, sizeof(tagCAPROPVARIANT)
assert alignment(tagCAPROPVARIANT) == 8, alignment(tagCAPROPVARIANT)
class tagCASCODE(Structure):
    pass
tagCASCODE._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(SCODE)),
]
assert sizeof(tagCASCODE) == 16, sizeof(tagCASCODE)
assert alignment(tagCASCODE) == 8, alignment(tagCASCODE)
class tagCADBL(Structure):
    pass
tagCADBL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_double)),
]
assert sizeof(tagCADBL) == 16, sizeof(tagCADBL)
assert alignment(tagCADBL) == 8, alignment(tagCADBL)
class IEnumPortableDeviceObjectIDs(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IEnumPortableDeviceObjectIDs Interface'
    _iid_ = GUID('{10ECE955-CF41-4728-BFA0-41EEDF1BBF19}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

class IPortableDeviceProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceProperties Interface'
    _iid_ = GUID('{7F6D695C-03DF-4439-A809-59266BEEE3A6}')
    _idlflags_ = []
class IPortableDeviceResources(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceResources Interface'
    _iid_ = GUID('{FD8878AC-D841-4D17-891C-E6829CDB6934}')
    _idlflags_ = []
IPortableDeviceContent._methods_ = [
    COMMETHOD([], HRESULT, 'EnumObjects',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], WSTRING, 'pszParentObjectID' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pFilter' ),
              ( ['out'], POINTER(POINTER(IEnumPortableDeviceObjectIDs)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Properties',
              ( ['out'], POINTER(POINTER(IPortableDeviceProperties)), 'ppProperties' )),
    COMMETHOD([], HRESULT, 'Transfer',
              ( ['out'], POINTER(POINTER(IPortableDeviceResources)), 'ppResources' )),
    COMMETHOD([], HRESULT, 'CreateObjectWithPropertiesOnly',
              ( ['in'], POINTER(IPortableDeviceValues), 'pValues' ),
              ( ['in', 'out'], POINTER(WSTRING), 'ppszObjectID' )),
    COMMETHOD([], HRESULT, 'CreateObjectWithPropertiesAndData',
              ( ['in'], POINTER(IPortableDeviceValues), 'pValues' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppData' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwOptimalWriteBufferSize' ),
              ( ['in', 'out'], POINTER(WSTRING), 'ppszCookie' )),
    COMMETHOD([], HRESULT, 'Delete',
              ( ['in'], c_ulong, 'dwOptions' ),
              ( ['in'], POINTER(IPortableDevicePropVariantCollection), 'pObjectIDs' ),
              ( ['in', 'out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppResults' )),
    COMMETHOD([], HRESULT, 'GetObjectIDsFromPersistentUniqueIDs',
              ( ['in'], POINTER(IPortableDevicePropVariantCollection), 'pPersistentUniqueIDs' ),
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppObjectIDs' )),
    COMMETHOD([], HRESULT, 'Cancel'),
    COMMETHOD([], HRESULT, 'Move',
              ( ['in'], POINTER(IPortableDevicePropVariantCollection), 'pObjectIDs' ),
              ( ['in'], WSTRING, 'pszDestinationFolderObjectID' ),
              ( ['in', 'out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppResults' )),
    COMMETHOD([], HRESULT, 'Copy',
              ( ['in'], POINTER(IPortableDevicePropVariantCollection), 'pObjectIDs' ),
              ( ['in'], WSTRING, 'pszDestinationFolderObjectID' ),
              ( ['in', 'out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppResults' )),
]
################################################################
## code template for IPortableDeviceContent implementation
##class IPortableDeviceContent_Impl(object):
##    def Transfer(self):
##        '-no docstring-'
##        #return ppResources
##
##    def EnumObjects(self, dwFlags, pszParentObjectID, pFilter):
##        '-no docstring-'
##        #return ppenum
##
##    def Move(self, pObjectIDs, pszDestinationFolderObjectID):
##        '-no docstring-'
##        #return ppResults
##
##    def GetObjectIDsFromPersistentUniqueIDs(self, pPersistentUniqueIDs):
##        '-no docstring-'
##        #return ppObjectIDs
##
##    def Cancel(self):
##        '-no docstring-'
##        #return 
##
##    def CreateObjectWithPropertiesOnly(self, pValues):
##        '-no docstring-'
##        #return ppszObjectID
##
##    def CreateObjectWithPropertiesAndData(self, pValues):
##        '-no docstring-'
##        #return ppData, pdwOptimalWriteBufferSize, ppszCookie
##
##    def Copy(self, pObjectIDs, pszDestinationFolderObjectID):
##        '-no docstring-'
##        #return ppResults
##
##    def Properties(self):
##        '-no docstring-'
##        #return ppProperties
##
##    def Delete(self, dwOptions, pObjectIDs):
##        '-no docstring-'
##        #return ppResults
##

IPortableDeviceContent2._methods_ = [
    COMMETHOD([], HRESULT, 'UpdateObjectWithPropertiesAndData',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pProperties' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppData' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwOptimalWriteBufferSize' )),
]
################################################################
## code template for IPortableDeviceContent2 implementation
##class IPortableDeviceContent2_Impl(object):
##    def UpdateObjectWithPropertiesAndData(self, pszObjectID, pProperties):
##        '-no docstring-'
##        #return ppData, pdwOptimalWriteBufferSize
##

_wireVARIANT._fields_ = [
    ('clSize', c_ulong),
    ('rpcReserved', c_ulong),
    ('vt', c_ushort),
    ('wReserved1', c_ushort),
    ('wReserved2', c_ushort),
    ('wReserved3', c_ushort),
    ('DUMMYUNIONNAME', __MIDL_IOleAutomationTypes_0004),
]
assert sizeof(_wireVARIANT) == 32, sizeof(_wireVARIANT)
assert alignment(_wireVARIANT) == 8, alignment(_wireVARIANT)
class PortableDeviceDispatchFactory(CoClass):
    u'PortableDeviceDispatchFactory Class'
    _reg_clsid_ = GUID('{43232233-8338-4658-AE01-0B4AE830B6B0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1F001332-1A57-4934-BE31-AFFC99F4EE0A}', 1, 0)
PortableDeviceDispatchFactory._com_interfaces_ = [IPortableDeviceDispatchFactory]

class tagCACY(Structure):
    pass
tagCACY._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_longlong)),
]
assert sizeof(tagCACY) == 16, sizeof(tagCACY)
assert alignment(tagCACY) == 8, alignment(tagCACY)
class IPortableDeviceCapabilities(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPortableDeviceCapabilities Interface'
    _iid_ = GUID('{2C8C6DBF-E3DC-4061-BECC-8542E810D126}')
    _idlflags_ = []
IPortableDeviceCapabilities._methods_ = [
    COMMETHOD([], HRESULT, 'GetSupportedCommands',
              ( ['out'], POINTER(POINTER(IPortableDeviceKeyCollection)), 'ppCommands' )),
    COMMETHOD([], HRESULT, 'GetCommandOptions',
              ( ['in'], POINTER(_tagpropertykey), 'Command' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppOptions' )),
    COMMETHOD([], HRESULT, 'GetFunctionalCategories',
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppCategories' )),
    COMMETHOD([], HRESULT, 'GetFunctionalObjects',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Category' ),
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppObjectIDs' )),
    COMMETHOD([], HRESULT, 'GetSupportedContentTypes',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Category' ),
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppContentTypes' )),
    COMMETHOD([], HRESULT, 'GetSupportedFormats',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'ContentType' ),
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppFormats' )),
    COMMETHOD([], HRESULT, 'GetSupportedFormatProperties',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Format' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceKeyCollection)), 'ppKeys' )),
    COMMETHOD([], HRESULT, 'GetFixedPropertyAttributes',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Format' ),
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppAttributes' )),
    COMMETHOD([], HRESULT, 'Cancel'),
    COMMETHOD([], HRESULT, 'GetSupportedEvents',
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppEvents' )),
    COMMETHOD([], HRESULT, 'GetEventOptions',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Event' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppOptions' )),
]
################################################################
## code template for IPortableDeviceCapabilities implementation
##class IPortableDeviceCapabilities_Impl(object):
##    def GetFixedPropertyAttributes(self, Format, key):
##        '-no docstring-'
##        #return ppAttributes
##
##    def GetEventOptions(self, Event):
##        '-no docstring-'
##        #return ppOptions
##
##    def GetSupportedCommands(self):
##        '-no docstring-'
##        #return ppCommands
##
##    def GetFunctionalObjects(self, Category):
##        '-no docstring-'
##        #return ppObjectIDs
##
##    def GetSupportedEvents(self):
##        '-no docstring-'
##        #return ppEvents
##
##    def GetSupportedFormats(self, ContentType):
##        '-no docstring-'
##        #return ppFormats
##
##    def GetFunctionalCategories(self):
##        '-no docstring-'
##        #return ppCategories
##
##    def GetCommandOptions(self, Command):
##        '-no docstring-'
##        #return ppOptions
##
##    def GetSupportedContentTypes(self, Category):
##        '-no docstring-'
##        #return ppContentTypes
##
##    def GetSupportedFormatProperties(self, Format):
##        '-no docstring-'
##        #return ppKeys
##
##    def Cancel(self):
##        '-no docstring-'
##        #return 
##

class IStorage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000B-0000-0000-C000-000000000046}')
    _idlflags_ = []
wireSNB = POINTER(tagRemSNB)
IStorage._methods_ = [
    COMMETHOD([], HRESULT, 'CreateStream',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
    COMMETHOD([], HRESULT, 'RemoteOpenStream',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'cbReserved1' ),
              ( ['in'], POINTER(c_ubyte), 'reserved1' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
    COMMETHOD([], HRESULT, 'CreateStorage',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStorage)), 'ppstg' )),
    COMMETHOD([], HRESULT, 'OpenStorage',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(IStorage), 'pstgPriority' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], wireSNB, 'snbExclude' ),
              ( ['in'], c_ulong, 'reserved' ),
              ( ['out'], POINTER(POINTER(IStorage)), 'ppstg' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], c_ulong, 'ciidExclude' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'rgiidExclude' ),
              ( ['in'], wireSNB, 'snbExclude' ),
              ( ['in'], POINTER(IStorage), 'pstgDest' )),
    COMMETHOD([], HRESULT, 'MoveElementTo',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(IStorage), 'pstgDest' ),
              ( ['in'], WSTRING, 'pwcsNewName' ),
              ( ['in'], c_ulong, 'grfFlags' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'RemoteEnumElements',
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'cbReserved2' ),
              ( ['in'], POINTER(c_ubyte), 'reserved2' ),
              ( ['in'], c_ulong, 'reserved3' ),
              ( ['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'DestroyElement',
              ( ['in'], WSTRING, 'pwcsName' )),
    COMMETHOD([], HRESULT, 'RenameElement',
              ( ['in'], WSTRING, 'pwcsOldName' ),
              ( ['in'], WSTRING, 'pwcsNewName' )),
    COMMETHOD([], HRESULT, 'SetElementTimes',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(_FILETIME), 'pctime' ),
              ( ['in'], POINTER(_FILETIME), 'patime' ),
              ( ['in'], POINTER(_FILETIME), 'pmtime' )),
    COMMETHOD([], HRESULT, 'SetClass',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'clsid' )),
    COMMETHOD([], HRESULT, 'SetStateBits',
              ( ['in'], c_ulong, 'grfStateBits' ),
              ( ['in'], c_ulong, 'grfMask' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
]
################################################################
## code template for IStorage implementation
##class IStorage_Impl(object):
##    def RemoteOpenStream(self, pwcsName, cbReserved1, reserved1, grfMode, reserved2):
##        '-no docstring-'
##        #return ppstm
##
##    def MoveElementTo(self, pwcsName, pstgDest, pwcsNewName, grfFlags):
##        '-no docstring-'
##        #return 
##
##    def DestroyElement(self, pwcsName):
##        '-no docstring-'
##        #return 
##
##    def OpenStorage(self, pwcsName, pstgPriority, grfMode, snbExclude, reserved):
##        '-no docstring-'
##        #return ppstg
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def Revert(self):
##        '-no docstring-'
##        #return 
##
##    def SetElementTimes(self, pwcsName, pctime, patime, pmtime):
##        '-no docstring-'
##        #return 
##
##    def RemoteCopyTo(self, ciidExclude, rgiidExclude, snbExclude, pstgDest):
##        '-no docstring-'
##        #return 
##
##    def SetClass(self, clsid):
##        '-no docstring-'
##        #return 
##
##    def RemoteEnumElements(self, reserved1, cbReserved2, reserved2, reserved3):
##        '-no docstring-'
##        #return ppenum
##
##    def CreateStorage(self, pwcsName, grfMode, reserved1, reserved2):
##        '-no docstring-'
##        #return ppstg
##
##    def RenameElement(self, pwcsOldName, pwcsNewName):
##        '-no docstring-'
##        #return 
##
##    def CreateStream(self, pwcsName, grfMode, reserved1, reserved2):
##        '-no docstring-'
##        #return ppstm
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return 
##
##    def SetStateBits(self, grfStateBits, grfMask):
##        '-no docstring-'
##        #return 
##

IPortableDeviceEventCallback._methods_ = [
    COMMETHOD([], HRESULT, 'OnEvent',
              ( ['in'], POINTER(IPortableDeviceValues), 'pEventParameters' )),
]
################################################################
## code template for IPortableDeviceEventCallback implementation
##class IPortableDeviceEventCallback_Impl(object):
##    def OnEvent(self, pEventParameters):
##        '-no docstring-'
##        #return 
##

class tagCAUI(Structure):
    pass
tagCAUI._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ushort)),
]
assert sizeof(tagCAUI) == 16, sizeof(tagCAUI)
assert alignment(tagCAUI) == 8, alignment(tagCAUI)
IPortableDeviceServiceMethods._methods_ = [
    COMMETHOD([], HRESULT, 'Invoke',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Method' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pParameters' ),
              ( ['in', 'out'], POINTER(POINTER(IPortableDeviceValues)), 'ppResults' )),
    COMMETHOD([], HRESULT, 'InvokeAsync',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Method' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pParameters' ),
              ( ['in'], POINTER(IPortableDeviceServiceMethodCallback), 'pCallback' )),
    COMMETHOD([], HRESULT, 'Cancel',
              ( ['in'], POINTER(IPortableDeviceServiceMethodCallback), 'pCallback' )),
]
################################################################
## code template for IPortableDeviceServiceMethods implementation
##class IPortableDeviceServiceMethods_Impl(object):
##    def Cancel(self, pCallback):
##        '-no docstring-'
##        #return 
##
##    def Invoke(self, Method, pParameters):
##        '-no docstring-'
##        #return ppResults
##
##    def InvokeAsync(self, Method, pParameters, pCallback):
##        '-no docstring-'
##        #return 
##

class tagCAL(Structure):
    pass
tagCAL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_int)),
]
assert sizeof(tagCAL) == 16, sizeof(tagCAL)
assert alignment(tagCAL) == 8, alignment(tagCAL)
class _wireSAFEARRAY_UNION(Structure):
    pass
_wireSAFEARRAY_UNION._fields_ = [
    ('sfType', c_ulong),
    ('u', __MIDL_IOleAutomationTypes_0001),
]
assert sizeof(_wireSAFEARRAY_UNION) == 40, sizeof(_wireSAFEARRAY_UNION)
assert alignment(_wireSAFEARRAY_UNION) == 8, alignment(_wireSAFEARRAY_UNION)
_wireSAFEARRAY._fields_ = [
    ('cDims', c_ushort),
    ('fFeatures', c_ushort),
    ('cbElements', c_ulong),
    ('cLocks', c_ulong),
    ('uArrayStructs', _wireSAFEARRAY_UNION),
    ('rgsabound', POINTER(tagSAFEARRAYBOUND)),
]
assert sizeof(_wireSAFEARRAY) == 64, sizeof(_wireSAFEARRAY)
assert alignment(_wireSAFEARRAY) == 8, alignment(_wireSAFEARRAY)
class tagCACLSID(Structure):
    pass
tagCACLSID._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)),
]
assert sizeof(tagCACLSID) == 16, sizeof(tagCACLSID)
assert alignment(tagCACLSID) == 8, alignment(tagCACLSID)
class tagCADATE(Structure):
    pass
tagCADATE._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_double)),
]
assert sizeof(tagCADATE) == 16, sizeof(tagCADATE)
assert alignment(tagCADATE) == 8, alignment(tagCADATE)
IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], _LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], _ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbRead' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]
################################################################
## code template for IStream implementation
##class IStream_Impl(object):
##    def RemoteSeek(self, dlibMove, dwOrigin):
##        '-no docstring-'
##        #return plibNewPosition
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def UnlockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppstm
##
##    def Revert(self):
##        '-no docstring-'
##        #return 
##
##    def RemoteCopyTo(self, pstm, cb):
##        '-no docstring-'
##        #return pcbRead, pcbWritten
##
##    def LockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return 
##
##    def SetSize(self, libNewSize):
##        '-no docstring-'
##        #return 
##

class __MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001(Union):
    pass
tagBSTRBLOB._fields_ = [
    ('cbSize', c_ulong),
    ('pData', POINTER(c_ubyte)),
]
assert sizeof(tagBSTRBLOB) == 16, sizeof(tagBSTRBLOB)
assert alignment(tagBSTRBLOB) == 8, alignment(tagBSTRBLOB)
class tagBLOB(Structure):
    pass
tagBLOB._fields_ = [
    ('cbSize', c_ulong),
    ('pBlobData', POINTER(c_ubyte)),
]
assert sizeof(tagBLOB) == 16, sizeof(tagBLOB)
assert alignment(tagBLOB) == 8, alignment(tagBLOB)
class tagCAUB(Structure):
    pass
tagCAUB._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ubyte)),
]
assert sizeof(tagCAUB) == 16, sizeof(tagCAUB)
assert alignment(tagCAUB) == 8, alignment(tagCAUB)
class tagCABOOL(Structure):
    pass
tagCABOOL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(VARIANT_BOOL)),
]
assert sizeof(tagCABOOL) == 16, sizeof(tagCABOOL)
assert alignment(tagCABOOL) == 8, alignment(tagCABOOL)
class tagCAFILETIME(Structure):
    pass
tagCAFILETIME._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_FILETIME)),
]
assert sizeof(tagCAFILETIME) == 16, sizeof(tagCAFILETIME)
assert alignment(tagCAFILETIME) == 8, alignment(tagCAFILETIME)
class tagCABSTR(Structure):
    pass
tagCABSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(BSTR)),
]
assert sizeof(tagCABSTR) == 16, sizeof(tagCABSTR)
assert alignment(tagCABSTR) == 8, alignment(tagCABSTR)
class tagCALPSTR(Structure):
    pass
tagCALPSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(STRING)),
]
assert sizeof(tagCALPSTR) == 16, sizeof(tagCALPSTR)
assert alignment(tagCALPSTR) == 8, alignment(tagCALPSTR)
__MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001._fields_ = [
    ('cVal', c_char),
    ('bVal', c_ubyte),
    ('iVal', c_short),
    ('uiVal', c_ushort),
    ('lVal', c_int),
    ('ulVal', c_ulong),
    ('intVal', c_int),
    ('uintVal', c_uint),
    ('hVal', _LARGE_INTEGER),
    ('uhVal', _ULARGE_INTEGER),
    ('fltVal', c_float),
    ('dblVal', c_double),
    ('boolVal', VARIANT_BOOL),
    ('bool', VARIANT_BOOL),
    ('scode', SCODE),
    ('cyVal', c_longlong),
    ('date', c_double),
    ('filetime', _FILETIME),
    ('puuid', POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)),
    ('pClipData', POINTER(tagCLIPDATA)),
    ('bstrVal', BSTR),
    ('bstrblobVal', tagBSTRBLOB),
    ('blob', tagBLOB),
    ('pszVal', STRING),
    ('pwszVal', WSTRING),
    ('punkVal', POINTER(IUnknown)),
    ('pdispVal', POINTER(IDispatch)),
    ('pStream', POINTER(IStream)),
    ('pStorage', POINTER(IStorage)),
    ('pVersionedStream', POINTER(tagVersionedStream)),
    ('parray', wirePSAFEARRAY),
    ('cac', tagCAC),
    ('caub', tagCAUB),
    ('cai', tagCAI),
    ('caui', tagCAUI),
    ('cal', tagCAL),
    ('caul', tagCAUL),
    ('cah', tagCAH),
    ('cauh', tagCAUH),
    ('caflt', tagCAFLT),
    ('cadbl', tagCADBL),
    ('cabool', tagCABOOL),
    ('cascode', tagCASCODE),
    ('cacy', tagCACY),
    ('cadate', tagCADATE),
    ('cafiletime', tagCAFILETIME),
    ('cauuid', tagCACLSID),
    ('caclipdata', tagCACLIPDATA),
    ('cabstr', tagCABSTR),
    ('cabstrblob', tagCABSTRBLOB),
    ('calpstr', tagCALPSTR),
    ('calpwstr', tagCALPWSTR),
    ('capropvar', tagCAPROPVARIANT),
    ('pcVal', STRING),
    ('pbVal', POINTER(c_ubyte)),
    ('piVal', POINTER(c_short)),
    ('puiVal', POINTER(c_ushort)),
    ('plVal', POINTER(c_int)),
    ('pulVal', POINTER(c_ulong)),
    ('pintVal', POINTER(c_int)),
    ('puintVal', POINTER(c_uint)),
    ('pfltVal', POINTER(c_float)),
    ('pdblVal', POINTER(c_double)),
    ('pboolVal', POINTER(VARIANT_BOOL)),
    ('pdecVal', POINTER(DECIMAL)),
    ('pscode', POINTER(SCODE)),
    ('pcyVal', POINTER(c_longlong)),
    ('pdate', POINTER(c_double)),
    ('pbstrVal', POINTER(BSTR)),
    ('ppunkVal', POINTER(POINTER(IUnknown))),
    ('ppdispVal', POINTER(POINTER(IDispatch))),
    ('pparray', POINTER(wirePSAFEARRAY)),
    ('pvarVal', POINTER(tag_inner_PROPVARIANT)),
]
assert sizeof(__MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001) == 16, sizeof(__MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001)
assert alignment(__MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001) == 8, alignment(__MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001)
_wireBRECORD._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('pRecInfo', POINTER(IRecordInfo)),
    ('pRecord', POINTER(c_ubyte)),
]
assert sizeof(_wireBRECORD) == 24, sizeof(_wireBRECORD)
assert alignment(_wireBRECORD) == 8, alignment(_wireBRECORD)
IPortableDevicePropVariantCollection._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['in'], POINTER(c_ulong), 'pcElems' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_ulong, 'dwIndex' ),
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'pValue' )),
    COMMETHOD([], HRESULT, 'Add',
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetType',
              ( ['out'], POINTER(c_ushort), 'pvt' )),
    COMMETHOD([], HRESULT, 'ChangeType',
              ( ['in'], c_ushort, 'vt' )),
    COMMETHOD([], HRESULT, 'Clear'),
    COMMETHOD([], HRESULT, 'RemoveAt',
              ( ['in'], c_ulong, 'dwIndex' )),
]
################################################################
## code template for IPortableDevicePropVariantCollection implementation
##class IPortableDevicePropVariantCollection_Impl(object):
##    def Clear(self):
##        '-no docstring-'
##        #return 
##
##    def GetType(self):
##        '-no docstring-'
##        #return pvt
##
##    def Add(self, pValue):
##        '-no docstring-'
##        #return 
##
##    def GetAt(self, dwIndex, pValue):
##        '-no docstring-'
##        #return 
##
##    def RemoveAt(self, dwIndex):
##        '-no docstring-'
##        #return 
##
##    def GetCount(self, pcElems):
##        '-no docstring-'
##        #return 
##
##    def ChangeType(self, vt):
##        '-no docstring-'
##        #return 
##

class IPropertyStore(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Simple Property Store Interface'
    _iid_ = GUID('{886D8EEB-8CF2-4446-8D02-CDBA1DBDCF99}')
    _idlflags_ = []
IPropertyStore._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['out'], POINTER(c_ulong), 'cProps' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_ulong, 'iProp' ),
              ( ['out'], POINTER(_tagpropertykey), 'pKey' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(tag_inner_PROPVARIANT), 'pv' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'propvar' )),
    COMMETHOD([], HRESULT, 'Commit'),
]
################################################################
## code template for IPropertyStore implementation
##class IPropertyStore_Impl(object):
##    def Commit(self):
##        '-no docstring-'
##        #return 
##
##    def GetCount(self):
##        '-no docstring-'
##        #return cProps
##
##    def SetValue(self, key, propvar):
##        '-no docstring-'
##        #return 
##
##    def GetAt(self, iProp):
##        '-no docstring-'
##        #return pKey
##
##    def GetValue(self, key):
##        '-no docstring-'
##        #return pv
##

tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]
assert sizeof(tagSTATSTG) == 80, sizeof(tagSTATSTG)
assert alignment(tagSTATSTG) == 8, alignment(tagSTATSTG)
IPortableDeviceResources._methods_ = [
    COMMETHOD([], HRESULT, 'GetSupportedResources',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceKeyCollection)), 'ppKeys' )),
    COMMETHOD([], HRESULT, 'GetResourceAttributes',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppResourceAttributes' )),
    COMMETHOD([], HRESULT, 'GetStream',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], c_ulong, 'dwMode' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwOptimalBufferSize' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppStream' )),
    COMMETHOD([], HRESULT, 'Delete',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['in'], POINTER(IPortableDeviceKeyCollection), 'pKeys' )),
    COMMETHOD([], HRESULT, 'Cancel'),
    COMMETHOD([], HRESULT, 'CreateResource',
              ( ['in'], POINTER(IPortableDeviceValues), 'pResourceAttributes' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppData' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwOptimalWriteBufferSize' ),
              ( ['in', 'out'], POINTER(WSTRING), 'ppszCookie' )),
]
################################################################
## code template for IPortableDeviceResources implementation
##class IPortableDeviceResources_Impl(object):
##    def GetResourceAttributes(self, pszObjectID, key):
##        '-no docstring-'
##        #return ppResourceAttributes
##
##    def GetSupportedResources(self, pszObjectID):
##        '-no docstring-'
##        #return ppKeys
##
##    def GetStream(self, pszObjectID, key, dwMode):
##        '-no docstring-'
##        #return pdwOptimalBufferSize, ppStream
##
##    def CreateResource(self, pResourceAttributes):
##        '-no docstring-'
##        #return ppData, pdwOptimalWriteBufferSize, ppszCookie
##
##    def Cancel(self):
##        '-no docstring-'
##        #return 
##
##    def Delete(self, pszObjectID, pKeys):
##        '-no docstring-'
##        #return 
##

IPortableDevice._methods_ = [
    COMMETHOD([], HRESULT, 'Open',
              ( ['in'], WSTRING, 'pszPnPDeviceID' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pClientInfo' )),
    COMMETHOD([], HRESULT, 'SendCommand',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pParameters' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppResults' )),
    COMMETHOD([], HRESULT, 'Content',
              ( ['out'], POINTER(POINTER(IPortableDeviceContent)), 'ppContent' )),
    COMMETHOD([], HRESULT, 'Capabilities',
              ( ['out'], POINTER(POINTER(IPortableDeviceCapabilities)), 'ppCapabilities' )),
    COMMETHOD([], HRESULT, 'Cancel'),
    COMMETHOD([], HRESULT, 'Close'),
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IPortableDeviceEventCallback), 'pCallback' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pParameters' ),
              ( ['out'], POINTER(WSTRING), 'ppszCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], WSTRING, 'pszCookie' )),
    COMMETHOD([], HRESULT, 'GetPnPDeviceID',
              ( ['out'], POINTER(WSTRING), 'ppszPnPDeviceID' )),
]
################################################################
## code template for IPortableDevice implementation
##class IPortableDevice_Impl(object):
##    def Capabilities(self):
##        '-no docstring-'
##        #return ppCapabilities
##
##    def Content(self):
##        '-no docstring-'
##        #return ppContent
##
##    def Unadvise(self, pszCookie):
##        '-no docstring-'
##        #return 
##
##    def Cancel(self):
##        '-no docstring-'
##        #return 
##
##    def Close(self):
##        '-no docstring-'
##        #return 
##
##    def Advise(self, dwFlags, pCallback, pParameters):
##        '-no docstring-'
##        #return ppszCookie
##
##    def Open(self, pszPnPDeviceID, pClientInfo):
##        '-no docstring-'
##        #return 
##
##    def SendCommand(self, dwFlags, pParameters):
##        '-no docstring-'
##        #return ppResults
##
##    def GetPnPDeviceID(self):
##        '-no docstring-'
##        #return ppszPnPDeviceID
##

IPortableDeviceKeyCollection._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['in'], POINTER(c_ulong), 'pcElems' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_ulong, 'dwIndex' ),
              ( ['in'], POINTER(_tagpropertykey), 'pKey' )),
    COMMETHOD([], HRESULT, 'Add',
              ( ['in'], POINTER(_tagpropertykey), 'key' )),
    COMMETHOD([], HRESULT, 'Clear'),
    COMMETHOD([], HRESULT, 'RemoveAt',
              ( ['in'], c_ulong, 'dwIndex' )),
]
################################################################
## code template for IPortableDeviceKeyCollection implementation
##class IPortableDeviceKeyCollection_Impl(object):
##    def GetCount(self, pcElems):
##        '-no docstring-'
##        #return 
##
##    def Add(self, key):
##        '-no docstring-'
##        #return 
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##
##    def GetAt(self, dwIndex, pKey):
##        '-no docstring-'
##        #return 
##
##    def RemoveAt(self, dwIndex):
##        '-no docstring-'
##        #return 
##

class __MIDL_IOleAutomationTypes_0006(Union):
    pass
__MIDL_IOleAutomationTypes_0006._fields_ = [
    ('oInst', c_ulong),
    ('lpvarValue', POINTER(VARIANT)),
]
assert sizeof(__MIDL_IOleAutomationTypes_0006) == 8, sizeof(__MIDL_IOleAutomationTypes_0006)
assert alignment(__MIDL_IOleAutomationTypes_0006) == 8, alignment(__MIDL_IOleAutomationTypes_0006)
class PortableDeviceManager(CoClass):
    u'PortableDeviceManager Class'
    _reg_clsid_ = GUID('{0AF10CEC-2ECD-4B92-9581-34F6AE0637F3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1F001332-1A57-4934-BE31-AFFC99F4EE0A}', 1, 0)
PortableDeviceManager._com_interfaces_ = [IPortableDeviceManager]

IPortableDeviceValues._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['in'], POINTER(c_ulong), 'pcelt' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_ulong, 'index' ),
              ( ['in', 'out'], POINTER(_tagpropertykey), 'pKey' ),
              ( ['in', 'out'], POINTER(tag_inner_PROPVARIANT), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(tag_inner_PROPVARIANT), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetStringValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], WSTRING, 'Value' )),
    COMMETHOD([], HRESULT, 'GetStringValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(WSTRING), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetUnsignedIntegerValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], c_ulong, 'Value' )),
    COMMETHOD([], HRESULT, 'GetUnsignedIntegerValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_ulong), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetSignedIntegerValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'GetSignedIntegerValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetUnsignedLargeIntegerValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], c_ulonglong, 'Value' )),
    COMMETHOD([], HRESULT, 'GetUnsignedLargeIntegerValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_ulonglong), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetSignedLargeIntegerValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], c_longlong, 'Value' )),
    COMMETHOD([], HRESULT, 'GetSignedLargeIntegerValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_longlong), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetFloatValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], c_float, 'Value' )),
    COMMETHOD([], HRESULT, 'GetFloatValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_float), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetErrorValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], HRESULT, 'Value' )),
    COMMETHOD([], HRESULT, 'GetErrorValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(HRESULT), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetKeyValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(_tagpropertykey), 'Value' )),
    COMMETHOD([], HRESULT, 'GetKeyValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(_tagpropertykey), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetBoolValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'GetBoolValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetIUnknownValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(IUnknown), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetIUnknownValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppValue' )),
    COMMETHOD([], HRESULT, 'SetGuidValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Value' )),
    COMMETHOD([], HRESULT, 'GetGuidValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetBufferValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(c_ubyte), 'pValue' ),
              ( ['in'], c_ulong, 'cbValue' )),
    COMMETHOD([], HRESULT, 'GetBufferValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(c_ubyte)), 'ppValue' ),
              ( ['out'], POINTER(c_ulong), 'pcbValue' )),
    COMMETHOD([], HRESULT, 'SetIPortableDeviceValuesValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetIPortableDeviceValuesValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppValue' )),
    COMMETHOD([], HRESULT, 'SetIPortableDevicePropVariantCollectionValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(IPortableDevicePropVariantCollection), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetIPortableDevicePropVariantCollectionValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(IPortableDevicePropVariantCollection)), 'ppValue' )),
    COMMETHOD([], HRESULT, 'SetIPortableDeviceKeyCollectionValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(IPortableDeviceKeyCollection), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetIPortableDeviceKeyCollectionValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceKeyCollection)), 'ppValue' )),
    COMMETHOD([], HRESULT, 'SetIPortableDeviceValuesCollectionValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(IPortableDeviceValuesCollection), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetIPortableDeviceValuesCollectionValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValuesCollection)), 'ppValue' )),
    COMMETHOD([], HRESULT, 'RemoveValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' )),
    COMMETHOD([], HRESULT, 'CopyValuesFromPropertyStore',
              ( ['in'], POINTER(IPropertyStore), 'pStore' )),
    COMMETHOD([], HRESULT, 'CopyValuesToPropertyStore',
              ( ['in'], POINTER(IPropertyStore), 'pStore' )),
    COMMETHOD([], HRESULT, 'Clear'),
]
################################################################
## code template for IPortableDeviceValues implementation
##class IPortableDeviceValues_Impl(object):
##    def GetKeyValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def GetIPortableDeviceValuesValue(self, key):
##        '-no docstring-'
##        #return ppValue
##
##    def GetUnsignedLargeIntegerValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def GetFloatValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def SetKeyValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def GetErrorValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def GetValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def GetBoolValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def SetBoolValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def RemoveValue(self, key):
##        '-no docstring-'
##        #return 
##
##    def GetSignedLargeIntegerValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def SetUnsignedIntegerValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def GetUnsignedIntegerValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def GetSignedIntegerValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def GetBufferValue(self, key):
##        '-no docstring-'
##        #return ppValue, pcbValue
##
##    def GetGuidValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def GetIPortableDeviceKeyCollectionValue(self, key):
##        '-no docstring-'
##        #return ppValue
##
##    def GetIPortableDevicePropVariantCollectionValue(self, key):
##        '-no docstring-'
##        #return ppValue
##
##    def GetAt(self, index):
##        '-no docstring-'
##        #return pKey, pValue
##
##    def SetIUnknownValue(self, key, pValue):
##        '-no docstring-'
##        #return 
##
##    def SetErrorValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def SetIPortableDeviceValuesCollectionValue(self, key, pValue):
##        '-no docstring-'
##        #return 
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##
##    def SetFloatValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def SetSignedLargeIntegerValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def GetIPortableDeviceValuesCollectionValue(self, key):
##        '-no docstring-'
##        #return ppValue
##
##    def SetUnsignedLargeIntegerValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def SetIPortableDeviceValuesValue(self, key, pValue):
##        '-no docstring-'
##        #return 
##
##    def SetBufferValue(self, key, pValue, cbValue):
##        '-no docstring-'
##        #return 
##
##    def SetStringValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def SetValue(self, key, pValue):
##        '-no docstring-'
##        #return 
##
##    def SetIPortableDeviceKeyCollectionValue(self, key, pValue):
##        '-no docstring-'
##        #return 
##
##    def GetStringValue(self, key):
##        '-no docstring-'
##        #return pValue
##
##    def CopyValuesFromPropertyStore(self, pStore):
##        '-no docstring-'
##        #return 
##
##    def SetIPortableDevicePropVariantCollectionValue(self, key, pValue):
##        '-no docstring-'
##        #return 
##
##    def GetIUnknownValue(self, key):
##        '-no docstring-'
##        #return ppValue
##
##    def CopyValuesToPropertyStore(self, pStore):
##        '-no docstring-'
##        #return 
##
##    def GetCount(self, pcelt):
##        '-no docstring-'
##        #return 
##
##    def SetGuidValue(self, key, Value):
##        '-no docstring-'
##        #return 
##
##    def SetSignedIntegerValue(self, key, Value):
##        '-no docstring-'
##        #return 
##

tag_inner_PROPVARIANT._fields_ = [
    ('vt', c_ushort),
    ('wReserved1', c_ubyte),
    ('wReserved2', c_ubyte),
    ('wReserved3', c_ulong),
    ('__MIDL____MIDL_itf_PortableDeviceApi_0001_00000001', __MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001),
]
assert sizeof(tag_inner_PROPVARIANT) == 24, sizeof(tag_inner_PROPVARIANT)
assert alignment(tag_inner_PROPVARIANT) == 8, alignment(tag_inner_PROPVARIANT)
IEnumPortableDeviceObjectIDs._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cObjects' ),
              ( ['out'], POINTER(WSTRING), 'pObjIDs' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cObjects' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumPortableDeviceObjectIDs)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Cancel'),
]
################################################################
## code template for IEnumPortableDeviceObjectIDs implementation
##class IEnumPortableDeviceObjectIDs_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, cObjects):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Cancel(self):
##        '-no docstring-'
##        #return 
##
##    def Next(self, cObjects):
##        '-no docstring-'
##        #return pObjIDs, pcFetched
##

tagCLIPDATA._fields_ = [
    ('cbSize', c_ulong),
    ('ulClipFmt', c_int),
    ('pClipData', POINTER(c_ubyte)),
]
assert sizeof(tagCLIPDATA) == 16, sizeof(tagCLIPDATA)
assert alignment(tagCLIPDATA) == 8, alignment(tagCLIPDATA)
IPortableDeviceProperties._methods_ = [
    COMMETHOD([], HRESULT, 'GetSupportedProperties',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceKeyCollection)), 'ppKeys' )),
    COMMETHOD([], HRESULT, 'GetPropertyAttributes',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppAttributes' )),
    COMMETHOD([], HRESULT, 'GetValues',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['in'], POINTER(IPortableDeviceKeyCollection), 'pKeys' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppValues' )),
    COMMETHOD([], HRESULT, 'SetValues',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['in'], POINTER(IPortableDeviceValues), 'pValues' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppResults' )),
    COMMETHOD([], HRESULT, 'Delete',
              ( ['in'], WSTRING, 'pszObjectID' ),
              ( ['in'], POINTER(IPortableDeviceKeyCollection), 'pKeys' )),
    COMMETHOD([], HRESULT, 'Cancel'),
]
################################################################
## code template for IPortableDeviceProperties implementation
##class IPortableDeviceProperties_Impl(object):
##    def GetPropertyAttributes(self, pszObjectID, key):
##        '-no docstring-'
##        #return ppAttributes
##
##    def GetSupportedProperties(self, pszObjectID):
##        '-no docstring-'
##        #return ppKeys
##
##    def GetValues(self, pszObjectID, pKeys):
##        '-no docstring-'
##        #return ppValues
##
##    def Cancel(self):
##        '-no docstring-'
##        #return 
##
##    def SetValues(self, pszObjectID, pValues):
##        '-no docstring-'
##        #return ppResults
##
##    def Delete(self, pszObjectID, pKeys):
##        '-no docstring-'
##        #return 
##

class __MIDL_IOleAutomationTypes_0005(Union):
    pass
__MIDL_IOleAutomationTypes_0005._fields_ = [
    ('lptdesc', POINTER(tagTYPEDESC)),
    ('lpadesc', POINTER(tagARRAYDESC)),
    ('hreftype', c_ulong),
]
assert sizeof(__MIDL_IOleAutomationTypes_0005) == 8, sizeof(__MIDL_IOleAutomationTypes_0005)
assert alignment(__MIDL_IOleAutomationTypes_0005) == 8, alignment(__MIDL_IOleAutomationTypes_0005)
_tagpropertykey._fields_ = [
    ('fmtid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('pid', c_ulong),
]
assert sizeof(_tagpropertykey) == 20, sizeof(_tagpropertykey)
assert alignment(_tagpropertykey) == 4, alignment(_tagpropertykey)
IPortableDeviceValuesCollection._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['in'], POINTER(c_ulong), 'pcElems' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_ulong, 'dwIndex' ),
              ( ['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppValues' )),
    COMMETHOD([], HRESULT, 'Add',
              ( ['in'], POINTER(IPortableDeviceValues), 'pValues' )),
    COMMETHOD([], HRESULT, 'Clear'),
    COMMETHOD([], HRESULT, 'RemoveAt',
              ( ['in'], c_ulong, 'dwIndex' )),
]
################################################################
## code template for IPortableDeviceValuesCollection implementation
##class IPortableDeviceValuesCollection_Impl(object):
##    def GetCount(self, pcElems):
##        '-no docstring-'
##        #return 
##
##    def Add(self, pValues):
##        '-no docstring-'
##        #return 
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##
##    def GetAt(self, dwIndex):
##        '-no docstring-'
##        #return ppValues
##
##    def RemoveAt(self, dwIndex):
##        '-no docstring-'
##        #return 
##

__all__ = [ 'IStorage', 'IPortableDeviceManager',
           '__MIDL_IOleAutomationTypes_0004',
           '__MIDL_IOleAutomationTypes_0005', '_wireSAFEARRAY',
           '_wireSAFEARR_HAVEIID', 'tagBLOB',
           '__MIDL_IOleAutomationTypes_0001',
           'PortableDeviceDispatchFactory', '_wireSAFEARR_BSTR',
           'wirePSAFEARRAY', 'tagCAL', 'IPortableDevice',
           'tagBSTRBLOB', 'tagCAUB', 'tagCALPWSTR', 'IEnumSTATSTG',
           'IPortableDeviceService', 'tagSTATSTG', 'tagCLIPDATA',
           'tagCAUH', 'IPortableDeviceServiceCapabilities', 'tagCAUL',
           'PortableDeviceWebControl', '_wireSAFEARR_UNKNOWN',
           '_LONG_SIZEDARR', 'IPortableDeviceProperties',
           'IPortableDeviceContent2', 'tag_inner_PROPVARIANT',
           'tagCABOOL',
           '__MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001',
           'IPortableDeviceResources', '_wireBRECORD', 'tagCAFLT',
           'tagCABSTRBLOB', 'tagCAFILETIME', 'wireSNB',
           'PortableDeviceFTM', '_wireSAFEARR_DISPATCH', 'tagCADBL',
           'tagCACLIPDATA', 'tagCAUI', 'PortableDeviceManager',
           'PortableDeviceServiceFTM',
           'IPortableDevicePropVariantCollection',
           'tagVersionedStream', '_FLAGGED_WORD_BLOB',
           'PortableDeviceService', 'tagCASCODE',
           'IPortableDeviceServiceMethods', 'tagCAH', 'tagCAI',
           '_BYTE_SIZEDARR', 'tagCAC',
           '__MIDL_IOleAutomationTypes_0006', 'IPropertyStore',
           'tagRemSNB', '_SHORT_SIZEDARR', 'tagCACLSID',
           '_wireSAFEARRAY_UNION', 'ISequentialStream', 'tagCABSTR',
           'IPortableDeviceValuesCollection',
           'IPortableDeviceKeyCollection',
           'IPortableDeviceEventCallback', '_wireVARIANT',
           '_HYPER_SIZEDARR', 'tagCALPSTR',
           'IEnumPortableDeviceObjectIDs', 'tagCAPROPVARIANT',
           'IPortableDeviceWebControl', 'PortableDevice',
           'IPortableDeviceCapabilities',
           'IPortableDeviceDispatchFactory',
           'IPortableDeviceServiceMethodCallback', 'IStream',
           '_wireSAFEARR_BRECORD', 'IPortableDeviceValues',
           'IPortableDeviceContent', '_tagpropertykey', 'tagCADATE',
           '_wireSAFEARR_VARIANT', 'tagCACY']
from comtypes import _check_version; _check_version('')
