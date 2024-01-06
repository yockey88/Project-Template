import project_settings 
import os , subprocess , sys
import shutil

args = project_settings.ProcessArguments(sys.argv)
print(args)
CONFIG = project_settings.GetArgValue(args , "c" , "debug")

print("Building {} in [{}] Configuration".format(project_settings.EXE_NAME , CONFIG))
print("\n")

ret = 0

first_build = False
if not os.path.exists("bin/{}/{}".format(CONFIG , project_settings.EXE_NAME)):
    first_build = True

MSBUILD = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\Community\\MSBuild\\Current\\Bin\\MSBuild.exe"
def find_msbuild():
    if project_settings.IsWindows():
        if os.path.exists(MSBUILD):
            return true
        else:
            MSBUILD.replace("2022" , "2019")
            if os.path.exists(MSBUILD):
                return true
            else:
                return false
    else:
        return false

if project_settings.IsWindows():
    if not find_msbuild():
        print("MSBuild.exe not found in default location")
        #print("Please specify the path to MSBuild.exe")
        #print("Example: python buildsln.py -msbuild \"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\MSBuild\\Current\\Bin\\MSBuild.exe\"")
        ret = 1
    else:
        ret = subprocess.call(
            [
                "cmd.exe" , "/c" , MSBUILD , 
                "{}.sln".format(project_settings.PROJECT_NAME) , 
                "/property:Configuration={}".format(CONFIG)
            ]
        )

if project_settings.IsLinux():
    ret = subprocess.call(["make" , "config={}".format(CONFIG)])

if project_settings.IsMac():
    ret = subprocess.call(["make" , "config={}".format(CONFIG)])

sys.exit(ret)

