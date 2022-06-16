import platform

name = "catch2"

version = "2.13.7"

authors = [
    "Martin Hořeňovský"
]

description = \
    """
    A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14, C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x branch)OpenEXR provides the specification and reference implementation of
    the EXR file format, the professional-grade image storage format of
    the motion picture industry.
    """

build_requires = [
    "cmake"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.catch2"


def commands():
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/Catch2")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")