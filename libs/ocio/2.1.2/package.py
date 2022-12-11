import platform

name = "ocio"

version = "2.2.0"

authors = [
    "Sony Pictures Imageworks team"
]

description = \
    """
    A complete color management solution geared towards motion picture
    production with an emphasis on visual effects and computer animation.
    """

build_requires = [
    "cmake"
]

requires = [
    "openexr-2.4.3",
    "expat-2.2.8",
    "yamlcpp-0.6.3",
    "pystring-1.1.3",
    "pybind11-2.6.2",
    "python-3.7",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.ocio"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.OCIO_ROOT.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")