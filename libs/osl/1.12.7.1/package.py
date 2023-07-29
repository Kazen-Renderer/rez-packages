import platform

name = "osl"

version = "1.12.7.1"

authors = [
    "Larry Gritz",
]

description = \
    """
    Open Shading Language (OSL) is a small but rich language for
    programmable shading in advanced renderers and other applications,
    ideal for describing materials, lights, displacement, and pattern
    generation.
    """

build_requires = [
    "cmake"
]

requires = [
    "llvm-13.0",
    "boost-1.80",
    "python-3.10",
    "zlib-1.2.11",
    "openexr-3.1",
    "oiio-2.4",
    "pugixml-1.11.4",
    "pybind11-2.10",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])


uuid = "libs.osl"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/OSL")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")