import platform

name = "opensubdiv"

version = "3.5.0"

authors = [
    "Pixar Developers"
]

description = \
    """
    OpenSubdiv is a set of open source libraries that implement high performance
    subdivision surface (subdiv) evaluation on massively parallel CPU and GPU
    architectures. This code path is optimized for drawing deforming surfaces with
    static topology at interactive framerates.
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

uuid = "libs.opensubdiv"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")