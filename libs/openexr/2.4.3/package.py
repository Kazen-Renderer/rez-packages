import platform

name = "openexr"

version = "2.4.3"

authors = [
    "ILM"
]

description = \
    """
    OpenEXR provides the specification and reference implementation of
    the EXR file format, the professional-grade image storage format of
    the motion picture industry.
    """

build_requires = [
    "cmake"
]

requires = [
    "python-3.7",
    "boost-1.73",
    "zlib-1.2.11"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
    requires.append("gettext-0.21")
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.openexr"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/IlmBase")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/OpenEXR")
    env.OPENEXR_ROOT.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
