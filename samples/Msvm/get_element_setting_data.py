# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_ElementCapabilities") #OK 
for obj in objs: 
    print(obj)


# PS D:\vscode> & C:/Python38/python.exe d:/vscode/python/hyperv/Msvm/get_element_capabilities.py

# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:06FF76FA-2D58-4BAF-9F8D-455773824F37\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Synth3dVideoPool.InstanceID=\"Microsoft:06FF76FA-2D58-4BAF-9F8D-455773824F37\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:146C56A0-3546-469B-9737-FCBCF82428F4\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:146C56A0-3546-469B-9737-FCBCF82428F4\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:698F2285-28DC-4438-A147-82D7432C5254\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:698F2285-28DC-4438-A147-82D7432C5254\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:19839BFF-6F04-4B24-B4B5-1AFCCBE729DE\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:19839BFF-6F04-4B24-B4B5-1AFCCBE729DE\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:353B3BE8-310C-4CF4-839E-4E1B14616136\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:4EA4F71F-16E6-4250-99A8-A2315332CC64\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4EA4F71F-16E6-4250-99A8-A2315332CC64\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:6A45335D-4C3A-44B7-B61F-C9808BBDF8ED\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:6A45335D-4C3A-44B7-B61F-C9808BBDF8ED\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:70BB60D2-A9D3-46AA-B654-3DE53004B4F8\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:70BB60D2-A9D3-46AA-B654-3DE53004B4F8\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:72027ECE-E44A-446E-AF2B-8D8C4B8A2279\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:72027ECE-E44A-446E-AF2B-8D8C4B8A2279\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:78AA0C27-B2BD-45BA-83D1-5F2A8C4C6656\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:78AA0C27-B2BD-45BA-83D1-5F2A8C4C6656\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:7951A5ED-8DC5-42D7-AA8C-9F14C54CEB84\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:7951A5ED-8DC5-42d7-AA8C-9F14C54CEB84\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:BDE5D4D6-E450-46D2-B925-976CA3E989B4\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:D45268DA-37C5-44DA-B827-B0C55CCB3BDC\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D45268DA-37C5-44da-B827-B0C55CCB3BDC\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:D92D268E-9AA8-49DD-8C7D-821CEFB5F597\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D92D268E-9AA8-49DD-8C7D-821CEFB5F597\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:DACDCF3F-6F67-4EB8-A4D0-5D93B48A2468\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:DACDCF3F-6F67-4EB8-A4D0-5D93B48A2468\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AllocationCapabilities.InstanceID=\"Microsoft:F6293891-F32F-4930-B2DB-1A8961D9CB75\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:F6293891-F32F-4930-B2DB-1A8961D9CB75\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationCapabilities.InstanceID=\"Microsoft:0CB7725C-9528-4CE7-8992-78E051454C0E\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemManagementCapabilities.InstanceID=\"Microsoft:VirtualSystemManagementCapabilities\"";
#         Characteristics = {2};
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemManagementService.CreationClassName=\"Msvm_VirtualSystemManagementService\",Name=\"vmms\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemMigrationCapabilities.InstanceID=\"Microsoft:MigrationCapabilities\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemMigrationService.CreationClassName=\"Msvm_VirtualSystemMigrationService\",Name=\"migrationwmi\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricServiceCapabilities.InstanceID=\"Microsoft:MetricServiceCapabilities\"";
#         Characteristics = {2};
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualEthernetSwitchManagementCapabilities.InstanceID=\"Microsoft:VirtualEthernetSwitchManagementCapabilities\"";     
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualEthernetSwitchManagementService.CreationClassName=\"Msvm_VirtualEthernetSwitchManagementService\",Name=\"nvspwmi\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPortCapabilities.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\{4397B43B-CA80-47D9-ACEE-C9061CED70F0}\"";  
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPort.CreationClassName=\"Msvm_ExternalEthernetPort\",DeviceID=\"Microsoft:{4397B43B-CA80-47D9-ACEE-C9061CED70F0}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPortCapabilities.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\{D92B05D7-7C34-4D27-93C7-51BFE6D200A5}\"";  
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPort.CreationClassName=\"Msvm_ExternalEthernetPort\",DeviceID=\"Microsoft:{D92B05D7-7C34-4D27-93C7-51BFE6D200A5}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPortCapabilities.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\{BD5A0381-FBB6-4EDA-900A-4EEBEF76748F}\"";  
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPort.CreationClassName=\"Msvm_ExternalEthernetPort\",DeviceID=\"Microsoft:{BD5A0381-FBB6-4EDA-900A-4EEBEF76748F}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPortCapabilities.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\{EB473ADB-0B3E-4748-A9CF-BCC641982C61}\"";  
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPort.CreationClassName=\"Msvm_ExternalEthernetPort\",DeviceID=\"Microsoft:{EB473ADB-0B3E-4748-A9CF-BCC641982C61}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPortCapabilities.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\{683922E8-DE84-4348-AAC4-597112DD14BC}\"";  
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPort.CreationClassName=\"Msvm_ExternalEthernetPort\",DeviceID=\"Microsoft:{683922E8-DE84-4348-AAC4-597112DD14BC}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPortCapabilities.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\{758ECB8C-8694-4751-8710-FFF0188D29EE}\"";  
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPort.CreationClassName=\"Msvm_ExternalEthernetPort\",DeviceID=\"Microsoft:{758ECB8C-8694-4751-8710-FFF0188D29EE}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPortCapabilities.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\{F18E14AA-0193-4857-BAFF-C531E73FC7A6}\"";  
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPort.CreationClassName=\"Msvm_ExternalEthernetPort\",DeviceID=\"Microsoft:{F18E14AA-0193-4857-BAFF-C531E73FC7A6}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPortCapabilities.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\{291B7538-6BAD-4506-B816-470934CDD75F}\"";  
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ExternalEthernetPort.CreationClassName=\"Msvm_ExternalEthernetPort\",DeviceID=\"Microsoft:{291B7538-6BAD-4506-B816-470934CDD75F}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemCapabilities.InstanceID=\"Microsoft:4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemCapabilities.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementCapabilities
# {
#         Capabilities = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemCapabilities.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\"";
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };
