PortableDevices
===============

Python code to access devices using the Windows Portable Devices API  (e.g. Media Transfer Protocol - MTP - devices)

For now, only directory listing and transfer to the device is implemented.

Installation and Usage
----------------------

-Get [comtypes](https://pypi.python.org/pypi/comtypes).
-Next you need let comtypes build the interfaces. I needed to fiddle around the generated code, to get it working:
 -comment-in the `comtypes.client.GetModule(...)` lines (or call both from Python console)
 -remove all bad asserts from the generated files (`_1F001332_1A57_4934_BE31_AFFC99F4EE0A_0_1_0.py` and `_2B00BA2F_E750_4BEB_9235_97142EDE1D3E_0_1_0.py`)
 -Don't know if it was just me not understanding the interface or if there is a bug in comtypes, but I had to define some parameters as in-out that were just out parameters. In `_1F001332_1A57_4934_BE31_AFFC99F4EE0A_0_1_0.py` :
  -In `IEnumPortableDeviceObjectIDs`, in function `Next` change the parameter `pObjIDs` to in-out
  -In `IPortableDeviceContent`, in function `CreateObjectWithPropertiesAndData` change the parameter `ppData` to in-out
-Now you can:
 -List devices with `PortableDevices.py ls`
 -List directory contents with `PortableDevices.py ls [Device]/directory`
 -Upload files with `PortableDevices.py cp source [Device]/directory`
