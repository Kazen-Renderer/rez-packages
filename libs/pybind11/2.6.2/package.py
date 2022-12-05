import platform

name = "pybind11"

version = "2.6.2"

authors = [
    "Wenzel Jacob"
]

description = \
    """
    pybind11 is a lightweight header-only library that exposes C++ types
    in Python and vice versa, mainly to create Python bindings of existing
    C++ code.
    """

build_requires = [
    "cmake"
]

requires = [
    "python-3.7",
    "boost-1.73",
    "zlib-1.2.11"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.pybind11"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/share/cmake/pybind11")
    env.CMAKE_MODULE_PATH.append("{root}/share/cmake/pybind11")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")