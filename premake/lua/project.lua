include "lua/externals.lua"

local function ProjectHeader(project_data)
  project (project_data.name)
    kind (project_data.kind)
    language "C++"

    if project_data.cppdialect ~= nil then
      cppdialect (project_data.cppdialect)
    else
      cppdialect "C++latest"
    end

    if project_data.kind == "StaticLib" then
      staticruntime "On"
    elseif project_data.kind ~= "DynamicLib" and project_data.staticruntime ~= nil then
      staticruntime (project_data.staticruntime)
    elseif project_data.kind ~= "DynamicLib" then
      staticruntime "On"
    end

    targetdir (tdir)
    objdir (odir)
end

local function ProcessProjectComponents(project)
end

local function ProcessConfigurations(project)
    filter "system:windows"
      if project.windows_configuration ~= nil then
          project.windows_configuration()
      else
          systemversion "latest"
      end

    filter { "system:windows", "configurations:Debug" }
      if project.windows_debug_configuration ~= nil then
        project.windows_debug_configuration()
      else
        editandcontinue "Off"
        flags { "NoRuntimeChecks" }
        defines { "NOMINMAX" }
      end

    filter { "system:windows", "configurations:Release" }
      if project.windows_release_configuration ~= nil then
        project.windows_release_configuration()
      end

    filter "system:linux"
      if project.linux_configuration ~= nil then
        project.linux_configuration()
      end

    filter "configurations:Debug"
      if project.debug_configuration ~= nil then
        project.debug_configuration()
      else
        debugdir "."
        optimize "Off"
        symbols "On"
      end
      ProcessDependencies("Debug")

    filter "configurations:Release"
      if project.release_configuration ~= nil then
        project.release_configuration()
      else
        optimize "On"
        symbols "Off"
      end
      ProcessDependencies("Release")
end

function AddProject(project)
  if project == nil then
    print("AddProject: project is nil")
    return
  end

  if project.name == nil then
    print("ProjectHeader: project.name is nil")
    return
  end

  if project.kind == nil then
    print("ProjectHeader: project.kind is nil")
    return
  end

  if project.files == nil then
    print("AddProject: project.files is nil")
    return
  end

  project.include_dir = project.include_dir or function() end

  print(" -- Adding project : " .. project.name)
  ProjectHeader(project)
    project.files()
    project.include_dir()

    ProcessProjectComponents(project)

    if project.defines ~= nil then
      project.defines()
    end

    ProcessConfigurations(project)
    RunPostBuildCommands()
end
