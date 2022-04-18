import platform

name = "gif"

version = "4.2.2"

authors = [
    "Michael Brown",
    "Daniel Eisenbud",
    "etc"
]

description = \
    """
    The GIFLIB project maintains the giflib service library,
    which has been pulling images out of GIFs since 1989. 
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

uuid = "libs.gif"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
