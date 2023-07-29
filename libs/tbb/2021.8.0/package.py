import platform

name = "tbb"

version = "2021.8.0"

authors = [
    "James Reinders",
    "Rafael Asenjo",
    "Michael J. Voss"
]

description = \
    """
    Intel® Threading Building Blocks (Intel® TBB) is a library that
    supports scalable parallel programming using standard ISO C++ code.
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

uuid = "libs.tbb"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/TBB")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")