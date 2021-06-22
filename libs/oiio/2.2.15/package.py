import platform

name = "oiio"

version = "2.2.15"

authors = [
    "Larry Gritz"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and 
    a bunch of related classes, utilities, and applications.
    """

build_requires = [
    "cmake"
]

requires = [
    "openexr-2.4.3",
    "boost-1.73",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.oiio"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")