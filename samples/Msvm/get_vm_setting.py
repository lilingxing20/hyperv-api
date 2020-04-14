# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

vms_obj = client.query("SELECT * FROM Msvm_VirtualSystemSettingData")
for vm in vms_obj: 
    print(vm)

# instance of Msvm_VirtualSystemSettingData
# {
#         AdditionalRecoveryInformation = NULL;
#         AllowFullSCSICommandSet = FALSE;
#         AllowReducedFcRedundancy = FALSE;
#         AutomaticRecoveryAction = 3;
#         AutomaticShutdownAction = 3;
#         AutomaticStartupAction = 3;
#         AutomaticStartupActionDelay = "00000000000000.000000:000";
#         AutomaticStartupActionSequenceNumber = NULL;
#         BaseBoardSerialNumber = "8835-1574-8377-3065-0179-1569-03";
#         BIOSGUID = "{9ECB1BA8-0048-4AE5-9891-431EDFBD6F02}";
#         BIOSNumLock = FALSE;
#         BIOSSerialNumber = "8835-1574-8377-3065-0179-1569-03";
#         BootOrder = {1, 2, 3, 0};
#         BootSourceOrder = {};
#         Caption = "虚拟机设置";
#         ChassisAssetTag = "8835-1574-8377-3065-0179-1569-03";
#         ChassisSerialNumber = "8835-1574-8377-3065-0179-1569-03";
#         ConfigurationDataRoot = "C:\\ProgramData\\Microsoft\\Windows\\Hyper-V";
#         ConfigurationFile = "Virtual Machines\\4EA7033C-356C-4EBA-9F77-1A3399CFCD72.xml";
#         ConfigurationID = "4EA7033C-356C-4EBA-9F77-1A3399CFCD72";
#         CreationTime = "16010101000000.000000-000";
#         DebugChannelId = NULL;
#         DebugPort = NULL;
#         DebugPortEnabled = NULL;
#         Description = "虚拟机的活动设置。";
#         ElementName = "centos7";
#         IncrementalBackupEnabled = FALSE;
#         InstanceID = "Microsoft:4EA7033C-356C-4EBA-9F77-1A3399CFCD72";
#         IsSaved = FALSE;
#         LogDataRoot = NULL;
#         LowMmioGapSize = "128";
#         NetworkBootPreferredProtocol = 4096;
#         Notes = {""};
#         Parent = NULL;
#         PauseAfterBootFailure = FALSE;
#         RecoveryFile = NULL;
#         SecureBootEnabled = FALSE;
#         SnapshotDataRoot = "C:\\ProgramData\\Microsoft\\Windows\\Hyper-V";
#         SuspendDataRoot = "Virtual Machines\\4EA7033C-356C-4EBA-9F77-1A3399CFCD72";
#         SwapFileDataRoot = "C:\\ProgramData\\Microsoft\\Windows\\Hyper-V";
#         Version = "5.0";
#         VirtualNumaEnabled = TRUE;
#         VirtualSystemIdentifier = "4EA7033C-356C-4EBA-9F77-1A3399CFCD72";
#         VirtualSystemSubType = "Microsoft:Hyper-V:SubType:1";
#         VirtualSystemType = "Microsoft:Hyper-V:System:Realized";
# };