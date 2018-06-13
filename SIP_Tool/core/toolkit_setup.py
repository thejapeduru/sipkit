import os
import json

def toolkit_files_setup():
    OOB_SUPPORT = False
    EDRIVE_SUPPORT = False
    # Copy c:\Toolkit\DefaultSettings.ps1 to c:\ToolkitUserFiles\Settings.ps1
    toolkit_settings_src = "C:\Toolkit\DefaultSettings.ps1"
    toolkit_settings_dest = "C:\ToolkitUserFiles"
    os.system("copy " + toolkit_settings_src + " " + toolkit_settings_dest)
    if "Settings.ps1" in os.listdir("C:\\ToolkitUserFiles"):
        os.system("del " "C:\ToolkitUserFiles\Settings.ps1")

    with open("C:\ToolkitUserFiles\config.json") as json_handler:
        data = json.load(json_handler)

        if data["edrive_support"] == "yes":
            EDRIVE_SUPPORT =True
        if data["oob_support"] == "yes":
            OOB_SUPPORT = True

        testdevice = data["device_name"]
        rack_uname = data["rack_manager_username"]
        rack_pwd = data["rack_manager_password"]
        server_uname = data["server_username"]
        server_pwd = data["server_password"]
    with open("C:\ToolkitUserFiles\DefaultSettings.ps1",'r')  as read_handler:
        with open("C:\ToolKitUserFiles\Settings.ps1",'w') as write_handler:
            for line in read_handler.readlines():

                if "SETTING_RACKMANAGER_CREDENTIALS" in line:
                    write_handler.write("Set-Variable  -Name SETTING_RACKMANAGER_CREDENTIALS      -Value  (new-object system.management.automation.pscredential('"+rack_uname+"',  (ConvertTo-SecureString '" + rack_pwd + "'  -asPlainText  -Force)))   -Option ReadOnly -Force -Scope Global \n")
                elif "SETTING_SERVER_CREDENTIALS" in line:
                    write_handler.write("Set-Variable  -Name SETTING_SERVER_CREDENTIALS           -Value  (new-object system.management.automation.pscredential('"+ server_uname +"',  (ConvertTo-SecureString '" + server_pwd + "'  -asPlainText  -Force)))   -Option ReadOnly -Force -Scope Global \n")
                elif "NVME_OOB_SUPPORT" in line and OOB_SUPPORT == True:
                    write_handler.write("Set-Variable  -Name NVME_OOB_SUPPORT                       -Value  @('HFS1T9GD0FEH-6410A BA') -Option ReadOnly -Force -Scope Global \n")
                elif "NVME_E_DRIVE_SUPPORT" in line and EDRIVE_SUPPORT == True:
                    #print(testdevice)
                    write_handler.write("Set-Variable  -Name NVME_E_DRIVE_SUPPORT                   -Value  @('"+testdevice+"') -Option ReadOnly -Force -Scope Global \n")
                else:
                    write_handler.write(line)