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
    "boost-1.73",
    "python-3.7",
    "tbb-2020.2",
    "openexr-2.4.3",
    "ocio-2.0.1",
    "openjpeg-2.4.0",
    "jpeg-2.1.0",
    "tiff-4.3.0",
    "gif-4.2.2",
    "png-1.6.37",
    "zlib-1.2.11",
    "fmt-8.0.1",
    "pybind11-2.6.2"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.oiio"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/OpenImageIO")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
