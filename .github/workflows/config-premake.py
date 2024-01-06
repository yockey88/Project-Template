## premake5.lua
 ## project -> repo name
 ## Project -> repo name

## project_settings.py
 ## project -> repo name

import os , sys 

if len(sys.argv) < 2:
    print("Usage: python3 create-premake.py <project name>")
    exit(1)

repo_name = sys.argv[1]

if not os.path.exisists("../../premake5.lua"):
    print("premake5.lua not found!")
    exit(1)
else:
    print("premake5.lua found!")
    premake_contents = open("../../premake5.lua", "r").read()
    premake_contents = premake_contents.replace("project", repo_name)
    premake_contents = premake_contents.replace("Project", repo_name)

    open("../../premake5.lua", "w").write(premake_contents)

if not os.path.exisists("../../tools/project_settings.py"):
    print("project_settings.py not found!")
    exit(1)
else:
    print("project_settings.py found!")
    project_settings_contents = open("../../tools/project_settings.py", "r").read()
    project_settings_contents = project_settings_contents.replace("project", repo_name)

    open("../../tools/project_settings.py", "w").write(project_settings_contents)
