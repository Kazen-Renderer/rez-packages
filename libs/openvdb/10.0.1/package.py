import platform

name = "openvdb"

version = "10.0.1"

authors = [
    "DreamWorks Animation"
]

description = \
    """
    OpenVDB is an open source software library for working with
    sparse volumetric data. It provides a hierarchical data
    structure and related functions to help with calculating
    volumetric effects in CGI applications.
    """

build_requires = [
    "cmake"
]

requires = [
    "boost-1.80",
    "tbb-2020.3",
    "openexr-3.1",
    "png-1.6.37",
    "zlib-1.2.11",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.opensubdiv"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")