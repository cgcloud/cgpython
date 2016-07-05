CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)

FILE(GLOB_RECURSE py_files "src/*.py")

rez_install_python(
    py
    FILES ${py_files}
	RELATIVE src
	DESTINATION .
)


file(GLOB package_files "package.yaml" "CMakeLists.txt")

rez_install_files(
    ${package_files}
    DESTINATION .
)
