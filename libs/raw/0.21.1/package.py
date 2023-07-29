import platform

name = "raw"

version = "0.21.1"

authors = [
    "Iliah Borg",
    "Alex Tutubalin"
]

description = \
    """
    LibRaw is a free and open-source software library for reading raw
    files from digital cameras.
    """

build_requires = []

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.raw"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")