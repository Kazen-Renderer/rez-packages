import platform

name = "osl"

version = "1.11.14"

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
    "boost-1.73.0",
    "python-3.7.10",
    "zlib-1.2.11",
    "openexr-2.4.3",
    "oiio-2.2.15",
    "pugixml-1.11.4",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])


uuid = "libs.osl"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")