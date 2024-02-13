local project = {}

project.name = "project"
project.kind = "ConsoleApp"
project.cppdialect = "C++latest"
project.staticruntime = "on"

project.files = function()
  files {
    "./src/**.cpp",
    "./include/**.hpp"
  }
end

project.includedirs = function()
  includedirs { "include/" }
end

AddProject(project)
