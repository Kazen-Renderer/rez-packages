import platform

name = "spirvcross"

version = "2021.1.15"

authors = [
    "Hans-Kristian Arntzen and etc..."
]

description = \
    """
    SPIRV-Cross is a tool designed for parsing and converting SPIR-V to
    other shader languages.
    """

build_requires = [
    "cmake"
]

requires = [
    "python-3.10"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.spirvcross"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.SPIRVCROSS_ROOT.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
