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

]

variants = [
    ["platform-osx", "arch-x86_64"]
]

uuid = "libs.openexr"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")