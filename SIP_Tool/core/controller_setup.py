import os
import json

def controller_files_setup(kit_location):
    with open("C:\ToolkitUserFiles\config.json") as json_handler:
        data = json.load(json_handler)

        if data["edrive_support"] == "yes":
            EDRIVE_SUPPORT = True
        if data["oob_support"] == "yes":
            OOB_SUPPORT = True

        testdevice = data["device_name"]
        rack_uname = data["rack_manager_username"]
        rack_pwd = data["rack_manager_password"]
        server_uname = data["server_username"]
        server_pwd = data["server_password"]

        # Copy c:\TestController\DefaultControllerSettings.ps1 to c:\TestControllerUserFiles\ControllerSettings.ps1
    controller_settings_src = "C:\TestController\DefaultControllerSettings.ps1"
    controller_settings_dest = "C:\TestControllerUserFiles"
    os.system("copy " + controller_settings_src + " " + controller_settings_dest)
    if "ControllerSettings.ps1" in os.listdir("C:\\TestControllerUserFiles"):
        os.system("del " "C:\TestControllerUserFiles\ControllerSettings.ps1")

    with open("C:\TestControllerUserFiles\DefaultControllerSettings.ps1",'r')  as read_handler:
        with open("C:\TestControllerUserFiles\ControllerSettings.ps1",'w') as write_handler:
            for line in read_handler.readlines():

                if "SETTING_RACKMANAGER_CREDENTIALS" in line:
                    write_handler.write("Set-Variable  -Name SETTING_RACKMANAGER_CREDENTIALS      -Value  (new-object system.management.automation.pscredential('"+rack_uname+"',  (ConvertTo-SecureString '" + rack_pwd + "'  -asPlainText  -Force)))   -Option ReadOnly -Force -Scope Global \n")
                elif "SETTING_SERVER_CREDENTIALS" in line:
                    write_handler.write("Set-Variable  -Name SETTING_SERVER_CREDENTIALS           -Value  (new-object system.management.automation.pscredential('"+ server_uname +"',  (ConvertTo-SecureString '" + server_pwd + "'  -asPlainText  -Force)))   -Option ReadOnly -Force -Scope Global \n")
                else:
                    write_handler.write(line)

        # create friendlyname and copy fw binaries

    if testdevice in os.listdir("C:\ToolkitUserFiles\FilesForTests"):
        os.system("powershell Remove-Item C:\ToolkitUserFiles\FilesForTests\\*" "'"+testdevice+"'" " -Recurse")

    os.rename("C:\ToolkitUserFiles\FilesForTests\FriendlyName", "C:\ToolkitUserFiles\FilesForTests\\"+testdevice)

    # copy fw
    for item in os.listdir(kit_location):
        if item.endswith(".bin"):
            fw_src = kit_location +"\\"+ item

    #print(fw_src)
    fw_dest2 = "\"C:\\ToolkitUserFiles\\FilesForTests\\"+testdevice+"\\CurrentFirmware\""
    fw_dest1 = "\"C:\\ToolkitUserFiles\\FilesForTests\\"+testdevice+"\\PriorFirmware\""
    #print(fw_dest1)
    fw_cmd1 = "copy " + fw_src + " " + fw_dest1
    #print(fw_cmd1)
    fw_cmd2 = "copy " + fw_src + " " + fw_dest2
    os.system(fw_cmd1)
    os.system(fw_cmd2)

    #update OOB-validation.xls and smart-validation.xls

    os.system("powershell \"(Get-Content C:\ToolkitUserFiles\FilesForTests\OOB-Validation-Limits.csv).replace('FriendlyName', '"+testdevice+"') | Set-Content C:\ToolkitUserFiles\FilesForTests\OOB-Validation-Limits.csv\"")
    os.system("powershell \"(Get-Content C:\ToolkitUserFiles\FilesForTests\SMART-Validation-Limits.csv).replace('FriendlyName', '" + testdevice + "') | Set-Content C:\ToolkitUserFiles\FilesForTests\SMART-Validation-Limits.csv\"")
