#***********************
#
# Copyright (c) 2021-2023, Operation Technology, Inc.
#
# THIS PROGRAM IS CONFIDENTIAL AND PROPRIETARY TO OPERATION TECHNOLOGY, INC. 
# ANY USE OF THIS PROGRAM IS SUBJECT TO THE PROGRAM SOFTWARE LICENSE AGREEMENT, 
# EXCEPT THAT THE USER MAY MODIFY THE PROGRAM FOR ITS OWN USE. 
# HOWEVER, THE PROGRAM MAY NOT BE REPRODUCED, PUBLISHED, OR DISCLOSED TO OTHERS 
# WITHOUT THE PRIOR WRITTEN CONSENT OF OPERATION TECHNOLOGY, INC.
#
#***********************



__version__ = "2022.0.0"

# APPLICATION
application_filepaths       = "/etap/api/v1/application/filepaths" 
application_pid             = "/etap/api/v1/application/pid"
application_ping            = "/etap/api/v1/application/ping"
application_projectfile     = "/etap/api/v1/application/projectfile"
application_version         = "/etap/api/v1/application/version"
application_downloadfile    = "/etap/api/v1/application/downloadfile"
application_showhelp  = "/etap/api/v1/application/showhelp"
application_getcurrentuser = "/etap/api/v1/application/getcurrentuser"
application_getallusers = "/etap/api/v1/application/getallusers"
application_getlanguage = "/etap/api/v1/application/getlanguage"
application_getcurrentzoomlevel = "/etap/api/v1/application/getcurrentzoomlevel"
application_getactivescenario = "/etap/api/v1/application/getactivescenario"
application_getmessagelog = "/etap/api/v1/application/getmessagelog"
application_clearmessagelog = "/etap/api/v1/application/clearmessagelog"
application_hideetapapplication = "/etap/api/v1/application/hideetapapplication"
application_showetapapplication = "/etap/api/v1/application/showetapapplication"
application_hidemessagelog = "/etap/api/v1/application/hidemessagelog"
application_showmessagelog = "/etap/api/v1/application/showmessagelog"
application_savemessagelog = "/etap/api/v1/application/savemessagelog"
application_getstudymodes = "/etap/api/v1/application/getstudymodes"
application_setstudymode = "/etap/api/v1/application/setstudymode"
application_login = "/etap/api/v1/application/login"
application_getstudytypes = "/etap/api/v1/application/getstudytypes"
application_exitetap = "/etap/api/v1/application/exitetap"
application_validatetoken = "/etap/api/v1/application/validatetoken"


# DNP3 SLAVE
dnp3slave_getsampleaidiruntimejson = "/etap/api/v1/dnp3/getsampleaidiruntimejson"
dnp3slave_getsampleaodoruntimejson = "/etap/api/v1/dnp3/getsampleaodoruntimejson"
dnp3slave_getsampleinitjson = "/etap/api/v1/dnp3/getsampleinitjson"
dnp3slave_getslaveai = "/etap/api/v1/dnp3/getslaveai"
dnp3slave_getslaveao = "/etap/api/v1/dnp3/getslaveao"
dnp3slave_getslavechannelstate = "/etap/api/v1/dnp3/getslavechannelstate"
dnp3slave_getslavedb = "/etap/api/v1/dnp3/getslavedb"
dnp3slave_getslavedi = "/etap/api/v1/dnp3/getslavedi"
dnp3slave_getslavedo = "/etap/api/v1/dnp3/getslavedo"
dnp3slave_getslavesettings = "/etap/api/v1/dnp3/getslavesettings"
dnp3slave_start = "/etap/api/v1/dnp3/start"
dnp3slave_getslavestate = "/etap/api/v1/dnp3/getslavestate"
dnp3slave_dnp3ping = "/etap/api/v1/dnp3/ping"
dnp3slave_updateaidi = "/etap/api/v1/dnp3/updateaidi"
dnp3slave_updateaodo = "/etap/api/v1/dnp3/updateaodo"
dnp3slave_stop = "/etap/api/v1/dnp3/stop"
#dnp3slave_getsampleruntimejson = "/etap/api/v1/dnp3/getsampleruntimejson"

# PROJECT DATA
projectdata_getallelementdata  = "/etap/api/v1/projectdata/getallelementdata"
projectdata_getbusnames = "/etap/api/v1/projectdata/getbusnames"
projectdata_getconfigurations = "/etap/api/v1/projectdata/getconfigurations"
projectdata_getelementnames = "/etap/api/v1/projectdata/getelementnames"
projectdata_getrevisions = "/etap/api/v1/projectdata/getrevisions"
projectdata_getstudymodesandcases = "/etap/api/v1/projectdata/getstudymodesandcases"
projectdata_getxml = "/etap/api/v1/projectdata/xml"
projectdata_getelementprop = "/etap/api/v1/projectdata/getelementprop"
projectdata_setelementprop = "/etap/api/v1/projectdata/setelementprop"
projectdata_sendpdexml = "/etap/api/v1/projectdata/sendpdexml"
projectdata_createelementinold = "/etap/api/v1/projectdata/createelementinold"
projectdata_deleteelementinold = "/etap/api/v1/projectdata/deleteelementinold"
projectdata_iselementenergized= "/etap/api/v1/projectdata/iselementenergized"
projectdata_iselementhidden= "/etap/api/v1/projectdata/iselementhidden"
projectdata_iselementnode= "/etap/api/v1/projectdata/iselementnode"
projectdata_iselementoutofservice= "/etap/api/v1/projectdata/iselementoutofservice"
projectdata_getstudycasenames= "/etap/api/v1/projectdata/getstudycasenames"
projectdata_getstudycase= "/etap/api/v1/projectdata/getstudycase"
projectdata_setstudycase= "/etap/api/v1/projectdata/setstudycase"
projectdata_getelementpropertynamesxml= "/etap/api/v1/projectdata/getelementpropertynamesxml"
projectdata_getelementtypes= "/etap/api/v1/projectdata/getelementtypes"
projectdata_validatecredentials= "/etap/api/v1/projectdata/validatecredentials"
projectdata_xmldownload = "/etap/api/v1/projectdata/xmldownload"
projectdata_activateelement = "/etap/api/v1/projectdata/activateelement"
projectdata_isprojectauthenticationrequired = "/etap/api/v1/projectdata/isprojectauthenticationrequired"
projectdata_setelementsprops = "/etap/api/v1/projectdata/setelementsprops"



# SCENARIO XML
scenario_getxmlfilepath = "/etap/api/v1/scenario/getxmlfilepath"
scenario_getxml = "/etap/api/v1/scenario/getxml"
scenario_run = "/etap/api/v1/scenario/run"
scenario_createscenario = "/etap/api/v1/scenario/createscenario"
scenario_checkbeforeoperate = "/etap/api/v1/scenario/checkbeforeoperate"
scenario_whatif_buskvar = "/etap/api/v1/scenario/whatif/buskvar"
scenario_whatif_buskw = "/etap/api/v1/scenario/whatif/buskw"
scenario_whatif_close = "/etap/api/v1/scenario/whatif/close"
scenario_whatif_open = "/etap/api/v1/scenario/whatif/open"

# STUDIES
studies_runulf = "/etap/api/v1/studies/runulf"
studies_runlf = "/etap/api/v1/studies/runlf"
studies_runms = "/etap/api/v1/studies/runms"
studies_runtdlf = "/etap/api/v1/studies/runtdlf"
studies_runtdlfasync = "/etap/api/v1/studies/runtdlfasync"
studies_runtssync = "/etap/api/v1/studies/runtssync"
studies_runtsasync = "/etap/api/v1/studies/runtsasync"
studies_runvs = "/etap/api/v1/studies/runvs"
studies_runha = "/etap/api/v1/studies/runha"
studies_runstarsqop = "/etap/api/v1/studies/runstarsqop"
studies_runsc = "/etap/api/v1/studies/runsc"
studies_runstarz = "/etap/api/v1/studies/runstarz"
studies_runstarzasync = "/etap/api/v1/studies/runstarzasync"
# studies_runaf = "/etap/api/v1/studies/runaf"
studies_runca = "/etap/api/v1/studies/runca"
studies_runso = "/etap/api/v1/studies/runso"
studies_runubsc = "/etap/api/v1/studies/runubsc"

