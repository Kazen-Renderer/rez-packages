import platform

name = "expat"

version = "2.5.0"

authors = [
    "James Clark"
]

description = \
    """
    Expat is a stream-oriented XML parser.
    """

build_requires = [
    "cmake"
]

requires = [
    "zlib-1.2.11"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.expat"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/{name}-{version}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")