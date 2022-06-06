import platform

name = "openjpeg"

version = "2.4.0"

authors = [
    "Hervé Drolon",
    "François-Olivier Devaux",
    "Antonin Descampe",
    "Yannick Verschueren",
    "David Janssens, Benoît Macq"
]

description = \
    """
    OpenJPEG is an open-source library to encode and decode JPEG 2000 images.
    """

build_requires = [
    "cmake"
]

requires = [

]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.openjpeg"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")