import platform

name = "gcc"

version = "12.3.0"

authors = [
    "Richard Stallman and others"
]

description = \
    """
    The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages (libstdc++,...).Header-only library that provides 0 cost initialization for immutable
    containers, fixed-size containers, and various algorithms.
    """

build_requires = []

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "softwares.gcc"


def commands():
    env.PATH.append("{root}/bin")
    env.CC = "{root}/bin/gcc"
    env.CXX = "{root}/bin/g++"
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")