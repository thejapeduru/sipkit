import os
import pexpect
import json
def run_suite():
    # update OOB-validation.xls and smart-validation.xls



    with open("C:\ToolkitUserFiles\config.json") as json_handler:
        data = json.load(json_handler)

        if data["oob_support"] == "yes":
            OOB_SUPPORT = True

        if data["edrive_support"] == "yes":
            EDRIVE_SUPPORT = True
        testdevice = data["device_name"]

        if data["shortsuite"] == "yes":
            short_switch = "$True"
        else:
            short_switch = "$False"
        suite = data["suite"]

    os.system( " powershell \"(Get-Content C:\TestController\TestSuites\\Nvme.ps1).replace('FriendlyName', '" + testdevice + "') | Set-Content C:\TestController\TestSuites\\Nvme.ps1\"")
    os.system(" powershell \"(Get-Content C:\TestController\TestSuites\\Nvme-Setup.ps1).replace('FriendlyName', '" + testdevice + "') | Set-Content C:\TestController\TestSuites\\Nvme-Setup.ps1\"")
    if EDRIVE_SUPPORT == True:
        os.system( "powershell \"(Get-Content C:\TestController\TestSuites\\Nvme.ps1).replace('$NvmeEdriveSupport         = $FALSE', '$NvmeEdriveSupport         = $True') | Set-Content C:\TestController\TestSuites\\Nvme.ps1\"")
        os.system("powershell \"(Get-Content C:\TestController\TestSuites\\Nvme-Setup.ps1).replace('$NvmeEdriveSupport         = $FALSE', '$NvmeEdriveSupport         = $True') | Set-Content C:\TestController\TestSuites\\Nvme-Setup.ps1\"")
    if OOB_SUPPORT ==True:
        os.system("powershell \"(Get-Content C:\TestController\TestSuites\\Nvme.ps1).replace('$NvmeOobSupport            = $FALSE', '$NvmeOobSupport            = $True') | Set-Content C:\TestController\TestSuites\\Nvme.ps1\"")
        os.system("powershell \"(Get-Content C:\TestController\TestSuites\\Nvme-Setup.ps1).replace('$NvmeOobSupport            = $FALSE', '$NvmeOobSupport            = $True') | Set-Content C:\TestController\TestSuites\\Nvme-Setup.ps1\"")
        os.system(" powershell \"(Get-Content C:\ToolkitUserFiles\Library\ProductSpecific\C2010.ps1).replace('$FALSE', '$True') | Set-Content C:\ToolkitUserFiles\Library\ProductSpecific\C2010.ps1 \"")
        #os.system(" powershell \"(Get-Content C:\ToolkitUserFiles\Library\ProductSpecific\C2010.ps1).replace('$False', '$True') | Set-ContentC:\ToolkitUserFiles\Library\ProductSpecific\C2010.ps1\"")

    os.system("del " "C:\TestController\StartController.ps1")
    os.system("copy C:\ToolkitUserFiles\StartController.ps1 C:\TestController")

    os.system("powershell -noexit \"C:\TestController\StartController.ps1 -Name " + suite + " -ServerList TestSystems -TestPlan 678123 -Shortsuite \"" + short_switch  )
