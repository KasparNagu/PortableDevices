#!/usr/bin/env python

import ctypes
import _ctypes
import comtypes
import comtypes.client
#uncomment this lines on first use and comment out the bad asserts
#comtypes.client.GetModule("portabledeviceapi.dll")
#comtypes.client.GetModule("portabledevicetypes.dll")

import comtypes.gen._1F001332_1A57_4934_BE31_AFFC99F4EE0A_0_1_0 as port;
import comtypes.gen._2B00BA2F_E750_4BEB_9235_97142EDE1D3E_0_1_0 as types;

WPD_OBJECT_NAME = comtypes.pointer(port._tagpropertykey());
WPD_OBJECT_NAME.contents.fmtid = comtypes.GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}");
WPD_OBJECT_NAME.contents.pid = 4;

WPD_OBJECT_ORIGINAL_FILE_NAME = comtypes.pointer(port._tagpropertykey());
WPD_OBJECT_ORIGINAL_FILE_NAME.contents.fmtid = comtypes.GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}");
WPD_OBJECT_ORIGINAL_FILE_NAME.contents.pid = 12;

WPD_OBJECT_SIZE =  comtypes.pointer(port._tagpropertykey());
WPD_OBJECT_SIZE.contents.fmtid = comtypes.GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}");
WPD_OBJECT_SIZE.contents.pid = 11;

WPD_OBJECT_PARENT_ID =  comtypes.pointer(port._tagpropertykey());
WPD_OBJECT_PARENT_ID.contents.fmtid = comtypes.GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}");
WPD_OBJECT_PARENT_ID.contents.pid = 3;
	
WPD_OBJECT_CONTENT_TYPE = comtypes.pointer(port._tagpropertykey());
WPD_OBJECT_CONTENT_TYPE.contents.fmtid = comtypes.GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}");
WPD_OBJECT_CONTENT_TYPE.contents.pid = 7;

WPD_RESOURCE_DEFAULT = comtypes.pointer(port._tagpropertykey());
WPD_RESOURCE_DEFAULT.contents.fmtid = comtypes.GUID("{E81E79BE-34F0-41BF-B53F-F1A06AE87842}")
WPD_RESOURCE_DEFAULT.contents.pid = 0; 

class PortableDeviceContent:
    def __init__(self,objectID,content,properties = None,propertiesToRead = None):
        self.objectID = objectID
        self.content = content
        self.name = None
        if properties:
            self.properties = properties
        else:
	    self.properties =  content.Properties()
        if propertiesToRead:
            self.propertiesToRead = propertiesToRead
        else:
            global WPD_OBJECT_NAME
            self.propertiesToRead = comtypes.client.CreateObject(types.PortableDeviceKeyCollection,
							  clsctx = comtypes.CLSCTX_INPROC_SERVER,
							  interface=port.IPortableDeviceKeyCollection);
	    self.propertiesToRead.Add(WPD_OBJECT_NAME)
	    self.propertiesToRead.Add(WPD_OBJECT_ORIGINAL_FILE_NAME)
	    self.propertiesToRead.Add(WPD_OBJECT_CONTENT_TYPE)
    def getName(self):
		if self.name:
			return self.name
		if self.objectID == None:
			return None
		global WPD_OBJECT_NAME,WPD_OBJECT_CONTENT_TYPE,WPD_OBJECT_ORIGINAL_FILE_NAME
		self.name = self.plain_name = self.properties.GetValues(self.objectID,self.propertiesToRead).GetStringValue(WPD_OBJECT_NAME)
		self.contentType = str(self.properties.GetValues(self.objectID,self.propertiesToRead).GetGuidValue(WPD_OBJECT_CONTENT_TYPE))
		if self.contentType != "{27E2E392-A111-48E0-AB0C-E17705A05F85}" and self.contentType != "{99ED0160-17FF-4C44-9D98-1D7A6F941921}":
				#its not a folder
				self.name = self.filename = self.properties.GetValues(self.objectID,self.propertiesToRead).GetStringValue(WPD_OBJECT_ORIGINAL_FILE_NAME)
		return self.name
    def getChildren(self):
        retObjs = []
        enumObjectIDs = self.content.EnumObjects(ctypes.c_ulong(0),
                    self.objectID,ctypes.POINTER(port.IPortableDeviceValues)())
	while True:
	    numObject=ctypes.c_ulong(16) #block size, so to speak
	    objectIDArray = (ctypes.c_wchar_p*numObject.value )()
	    numFetched = ctypes.pointer(ctypes.c_ulong(0))
	    #be sure to change the IEnumPortableDeviceObjectIDs 'Next' function in the generated code to have objectids as inout
	    enumObjectIDs.Next(numObject,ctypes.cast(objectIDArray,ctypes.POINTER(ctypes.c_wchar_p)),numFetched)
	    if numFetched.contents.value == 0:
                break
	    for i in range(0,numFetched.contents.value):
	      curObjectID = objectIDArray[i]
	      retObjs.append(PortableDeviceContent(curObjectID,self.content,self.properties,self.propertiesToRead))
#	enumObjectIDs.Release()
        return retObjs
    def getChild(self, name):
        matches = [c for c in self.getChildren() if c.getName() == name]
        if len(matches) == 0:
            #todo throw exception instead of returning none
            return None
        else:
            return matches[0]
    def getPath(self,path):
        cur = self
        for p in path.split("/"):
            cur = cur.getChild(p)
            if cur == None:
                return None
        return cur
    def __repr__(self):
        return "<PortableDeviceContent %s: %s>" % (self.objectID, self.getName())
    def uploadStream(self,fileName,inputStream,streamLen):
        global WPD_OBJECT_PARENT_ID,WPD_OBJECT_SIZE,WPD_OBJECT_ORIGINAL_FILE_NAME,WPD_OBJECT_NAME
        objectProperties=comtypes.client.CreateObject(types.PortableDeviceValues,
			clsctx = comtypes.CLSCTX_INPROC_SERVER,
			interface=port.IPortableDeviceValues)

        objectProperties.SetStringValue(WPD_OBJECT_PARENT_ID, self.objectID);
        objectProperties.SetUnsignedLargeIntegerValue(WPD_OBJECT_SIZE,streamLen);
        objectProperties.SetStringValue(WPD_OBJECT_ORIGINAL_FILE_NAME, fileName);
        objectProperties.SetStringValue(WPD_OBJECT_NAME, fileName);
        optimalTransferSizeBytes = ctypes.pointer(ctypes.c_ulong(0))
        pFileStream = ctypes.POINTER(port.IStream)();
		#be sure to change the IPortableDeviceContent 'CreateObjectWithPropertiesAndData' function in the generated code to have IStream ppData as 'in','out'
        fileStream = self.content.CreateObjectWithPropertiesAndData(objectProperties,
                                                        pFileStream,
                                                        optimalTransferSizeBytes,
                                                        ctypes.POINTER(ctypes.c_wchar_p)());
        fileStream = pFileStream.value
        blockSize = optimalTransferSizeBytes.contents.value
        curWritten = 0
        while True:
            toRead = streamLen - curWritten
            block = inputStream.read(toRead if toRead < blockSize else blockSize)
            if len(block)<=0:
                break
            stringBuf = ctypes.create_string_buffer(block)
            written = fileStream.RemoteWrite(ctypes.cast(stringBuf,ctypes.POINTER(ctypes.c_ubyte)),len(block))
            curWritten += written
            if(curWritten>=streamLen):
                break
        STGC_DEFAULT = 0
        fileStream.Commit(STGC_DEFAULT)
    def downloadStream(self,outputStream):
		global WPD_RESOURCE_DEFAULT
		resources = self.content.Transfer()
		STGM_READ = ctypes.c_uint(0)
		optimalTransferSizeBytes = ctypes.pointer(ctypes.c_ulong(0))
		pFileStream = ctypes.POINTER(port.IStream)();
		optimalTransferSizeBytes, pFileStream = resources.GetStream(self.objectID,
			WPD_RESOURCE_DEFAULT,
			STGM_READ,
			optimalTransferSizeBytes,
			pFileStream)
		blockSize = optimalTransferSizeBytes.contents.value
		fileStream = pFileStream.value
		buf = (ctypes.c_ubyte*blockSize)()
		#make sure all RemoteRead parameters are in
		while True:
			buf,len = fileStream.RemoteRead(buf, ctypes.c_ulong(blockSize))
			if len == 0:
				break
			outputStream.write(bytearray(buf))
		
class PortableDevice:
    def __init__(self,id):
        self.id = id
        self.desc = None
        self.device = None
    def getDescription(self):
        if self.desc:
            return self.desc
        
        global deviceManager
        nameLen = ctypes.pointer(ctypes.c_ulong(0))
        deviceManager.GetDeviceDescription(self.id,ctypes.POINTER(ctypes.c_ushort)(),nameLen)
        name = ctypes.create_unicode_buffer(nameLen.contents.value)
        deviceManager.GetDeviceDescription(self.id,ctypes.cast(
            name,ctypes.POINTER(ctypes.c_ushort)),nameLen)
        self.desc = name.value        
        return self.desc
    def getDevice(self):
        if self.device:
            return self.device
        clientInformation=comtypes.client.CreateObject(types.PortableDeviceValues,
			clsctx = comtypes.CLSCTX_INPROC_SERVER,
			interface=port.IPortableDeviceValues)
	self.device=comtypes.client.CreateObject(port.PortableDevice,
			clsctx = comtypes.CLSCTX_INPROC_SERVER,
			interface=port.IPortableDevice)
	self.device.Open(self.id,clientInformation)
	return self.device
    def releaseDevice(self):
        if self.device:
            self.device.Release()
            self.device = None
    def getContent(self):
        return PortableDeviceContent(ctypes.c_wchar_p("DEVICE"),self.getDevice().Content())
    def __repr__(self):
        return "<PortableDevice: %s>"%self.getDescription()
deviceManager = None
def getPortableDevices():
    global deviceManager
    if not deviceManager:
        deviceManager=comtypes.client.CreateObject(
            port.PortableDeviceManager,
            clsctx = comtypes.CLSCTX_INPROC_SERVER,
            interface=port.IPortableDeviceManager)
    pnpDeviceIDCount = ctypes.pointer(ctypes.c_ulong(0))
    deviceManager.GetDevices(ctypes.POINTER(ctypes.c_wchar_p)(),pnpDeviceIDCount)
    if(pnpDeviceIDCount.contents.value==0):
        return []
    pnpDeviceIDs = (ctypes.c_wchar_p*pnpDeviceIDCount.contents.value )()
    deviceManager.GetDevices(ctypes.cast(pnpDeviceIDs,ctypes.POINTER(ctypes.c_wchar_p)),pnpDeviceIDCount)
    return [PortableDevice(curId) for curId in pnpDeviceIDs]


def getContentFromDevicePath(path):
	path = path.split("/")
	for dev in getPortableDevices():
		if path[0] == dev.getDescription():			
			if len(path) > 1:
				cont = dev.getContent().getPath("/".join(path[1:]))
			else:
				cont = dev.getContent()
			return cont
	return None
	
if __name__ == "__main__":
	import sys
	import os
	if len(sys.argv)>1 and sys.argv[1] == 'ls':
		if len(sys.argv) == 2:
			print "Devices:"
			for d in getPortableDevices():
				print "  %s" % d.getDescription()
		else:
			path = sys.argv[2]
			cont = getContentFromDevicePath(path)
			if cont:
				print "%s contains:" % path
				for l in cont.getChildren():					
					print ("  %s" % l.getName()).encode("utf8")
			else:
				print "%s not found" % path
				exit(1)
	elif len(sys.argv) == 4 and sys.argv[1] == 'cp':
	#copy to target
		src = sys.argv[2]
		srcSize = os.path.getsize(src)
		tgt = sys.argv[3]
		cont = getContentFromDevicePath(tgt)
		if not cont:
				print "directory %s not found" % tgt
				exit(1)
		srcFile = open(src,"rb")
		cont.uploadStream(os.path.basename(src),srcFile,srcSize)
		srcFile.close()
	elif len(sys.argv) == 4 and sys.argv[1] == 'get':
	#copy to target
		src = sys.argv[2]
		tgt = sys.argv[3]
		cont = getContentFromDevicePath(src)
		if not cont:
				print "directory %s not found" % tgt
				exit(1)
		if tgt == "-":
			tgtFile = sys.stdout
		else:
			tgtFile = open(tgt,"wb")
		cont.downloadStream(tgtFile)
		if tgt != "-":
			tgtFile.close()
	else:
		print "usage: %s TODO" % sys.argv[0]
		exit(1)
