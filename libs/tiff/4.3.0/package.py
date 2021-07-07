import platform

name = "tiff"

version = "4.3.0"

authors = [
    "Sam Leffler",
    "Silicon Graphics"
]

description = \
    """
    This software provides support for the Tag Image File Format (TIFF),
    a widely used format for storing image data.
    """

build_requires = [
    "cmake"
]

requires = [
    "jpeg-2.1.0",
    "zlib-1.2.11"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.tiff"


def commands():
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")