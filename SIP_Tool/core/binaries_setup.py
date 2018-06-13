import os
import zipfile

def list_cmp(list1,list2):
    result = 0
    for item in list1:
        if item in list2:
            result = 1
        else:
            result = -1
    return result


def binaries_setup(kit_location):

    if(not os.path.exists(kit_location)):
        print("binaries location is incorrect")
        print ("press 'q' to exit and come back")
        close = input()
        if close == 'q' or close == 'Q':
            return 0

    kit_location = kit_location
    if kit_location.endswith("\\"):
        kit_location = kit_location
    else:
        kit_location = kit_location + "\\"
    all_files = os.listdir(kit_location)
    count = 0
    tc_zip = ''
    for item in all_files:
        if item.endswith(".zip"):
            tc_zip = item
            count += 1
    if count == 0:
        print("No test kit zip in the provided location, copy it and run the program again ")
        os.sleep(2)
        return 0
    must_list = ["diskspd.exe", 'diskspd.xsd', 'Dynamo.exe', 'fio.exe', 'IOmeter.exe', 'PsExec64.exe', 'smartctl.exe', 'StorageTool.exe']
    #print(all_files)
    if list_cmp(must_list,all_files) != 1:
        print("Something is missing copy items before you move forward ")
        print("Required : 'diskspd.exe', 'diskspd.xsd', 'Dynamo.exe', 'fio.exe', 'IOmeter.exe', 'PsExec64.exe', 'smartctl.exe', 'StorageTool.exe'")

    # unzip Tc file in C:\
    #copyfile(kit_location + tc_zip , "C:")
    zip_ref = zipfile.ZipFile(kit_location + tc_zip , 'r')
    zip_ref.extractall("C:\\")

    # change directory and file permissions
    #change_permission()

    # copy psexec file to C:\TestControllerUserFiles\Binaries
    PsExec_src = kit_location + "PsExec64.exe"
    PsExec_dst = "C:\TestControllerUserFiles\Binaries"
    copy_cmd = "copy " + PsExec_src + " " + PsExec_dst
    os.system(copy_cmd)

    #create SMART directory
    if "SMART" in os.listdir("C:\ToolkitUserFiles\Binaries"):
        os.system("powershell Remove-Item C:\ToolkitUserFiles\Binaries\SMART  -Recurse")
    smart_cmd = "mkdir C:\ToolkitUserFiles\Binaries\SMART"
    os.system(smart_cmd)
    #copy smartctl and storagetool to smart directory
    smart_src = kit_location + "smartctl.exe"
    storage_src = kit_location + "StorageTool.exe"
    smart_dest = "C:\ToolkitUserFiles\Binaries\SMART"
    os.system("copy "+smart_src + " " + smart_dest)
    os.system("copy " +storage_src + " " + smart_dest)

    #create fio directory
    if "fio" in os.listdir("C:\ToolkitUserFiles\Binaries"):
        os.system("powershell Remove-Item C:\ToolkitUserFiles\Binaries\\fio  -Recurse")
    fio_cmd = "mkdir C:\ToolkitUserFiles\Binaries\\fio"
    os.system(fio_cmd)
    #copy fio
    fio_src = kit_location + "fio.exe"
    fio_dst = "C:\ToolkitUserFiles\Binaries\\fio"
    fio_cmd = "copy " + fio_src + " " + fio_dst
    os.system(fio_cmd)

    #crete IOmeter directory
    if "Iometer" in os.listdir("C:\ToolkitUserFiles\Binaries"):
        os.system("powershell Remove-Item C:\ToolkitUserFiles\Binaries\Iometer  -Recurse")
    IOmeter_cmd = "mkdir C:\ToolkitUserFiles\Binaries\Iometer"
    os.system(IOmeter_cmd)
    # copy Iometer and dynamo to iomter directory
    iometer_src = kit_location + "IOmeter.exe"
    dynamo_src = kit_location + "Dynamo.exe"
    iometer_dest = "C:\ToolkitUserFiles\Binaries\Iometer"
    os.system("copy " + iometer_src + " " + iometer_dest)
    os.system("copy " + dynamo_src + " " + iometer_dest)

   # crete Diskspd directory
    if "DiskSpd" in os.listdir("C:\ToolkitUserFiles\Binaries"):
        os.system("powershell Remove-Item C:\ToolkitUserFiles\Binaries\DiskSpd  -Recurse")
    DiskSpd_cmd = "mkdir C:\ToolkitUserFiles\Binaries\DiskSpd"
    os.system(DiskSpd_cmd)
    # copy disksdp exe and xsd directory
    DiskSpd_src = kit_location + "diskspd.exe"
    DiskSpd_xsd_src = kit_location + "diskspd.xsd"
    DiskSpd_dest = "C:\ToolkitUserFiles\Binaries\DiskSpd"
    os.system("copy " + DiskSpd_src + " " + DiskSpd_dest)
    os.system("copy " + DiskSpd_xsd_src + " " + DiskSpd_dest)

   #copy json file to C:\Toolkituserfiles
    json_src = kit_location + "config.json"
    json_dst = "C:\ToolkitUserFiles"
    copy_cmd = "copy " + json_src + " " + json_dst
    os.system(copy_cmd)

    #copy change startconrtoller file
    startfile_src = kit_location + "StartController.ps1"
    startfile_dest = "C:\ToolkitUserFiles"
    startfile_copy_cmd = "copy " + startfile_src + " " + startfile_dest
    os.system(startfile_copy_cmd)
