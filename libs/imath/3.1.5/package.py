import platform

name = "imath"

version = "3.1.5"

authors = [
    "ILM"
]

description = \
    """
    Imath is a basic, light-weight, and efficient C++ representation of
    2D and 3D vectors and matrices and other simple but useful
    mathematical objects, functions, and data types common in computer
    graphics applications, including the “half” 16-bit floating-point
    type.
    """

build_requires = [
    "cmake"
]

requires = [
    "boost-1.80",
    "python-3.10",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.oiio"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/Imath")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
