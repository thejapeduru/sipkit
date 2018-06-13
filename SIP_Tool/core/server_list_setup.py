import json
import os

def create_server_list():

    with open("C:\ToolkitUserFiles\config.json") as json_handler:
        data = json.load(json_handler)

        if data["oob_support"] == "yes":
            OOB_SUPPORT = True

    print(len(data["Servers"]))
    servers = data["Servers"]
    if data["rack_manager_type"] == "gen6":
        mgr_type = 'M2010'
    elif data["rack_manager_type"] == "legacy":
        mgr_type = 'Legacy'
    else:
        mgr_type = 'None'

    if "TestSystems.ps1" in os.listdir("C:\TestControllerUserFiles\ServerLists"):
        os.system("del " "C:\TestControllerUserFiles\ServerLists\TestSystems.ps1")
    #print("cjeck")

    with open("C:\TestControllerUserFiles\ServerLists\Template.ps1", 'r')  as read_handler:
        with open("C:\TestControllerUserFiles\ServerLists\TestSystems.ps1", 'w') as write_handler:
            for line in read_handler.readlines():
                if "$ServerList_NvmeOobSupport" in line and OOB_SUPPORT == True:
                    write_handler.write("$ServerList_NvmeOobSupport        = $FALSE \n")
                elif "$ServerList_NvmeTempSensorSupport = $FALSE" in line and OOB_SUPPORT == True:
                    write_handler.write("$ServerList_NvmeTempSensorSupport = $FALSE \n")
                elif "WCSMTS13QPVT001" in line:
                    i = 0
                    while( i < len(data["Servers"])):
                        write_handler.write(" @{ slot = "+str(servers[i]['slot'])+ ";   Address = '" +str(servers[i]['IP'])+ "'  ; Name = '" +str(servers[i]["hostname"]) + "' } \n")
                        i += 1
                elif " @{ slot" in line:
                        write_handler.write("")
                elif "$WcsTestRemoteMgrType" in line :
                    write_handler.write("$WcsTestRemoteMgrType            = '"+mgr_type+"'\n" )
                elif "$WcsTestRemoteMgr                = 'CMMTF1PVT022' " in line:
                    write_handler.write("$WcsTestRemoteMgr                = '" +data["rack_manager_ip"] + "'\n")

                else:
                    write_handler.write(line)