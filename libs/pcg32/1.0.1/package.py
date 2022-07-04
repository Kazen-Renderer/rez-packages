import platform

name = "pcg32"

version = "1.0.1"

authors = [
    "Wenzel Jacob"
]

description = \
    """
    libpng is the official PNG reference library.This is a tiny self-contained
    C++ implementation of the PCG32 random number based on code by Melissa O'Neill
    available at http://www.pcg-random.org.
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

uuid = "libs.pcg32"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")