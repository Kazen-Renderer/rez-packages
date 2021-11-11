import platform

name = "frozen"

version = "1.0.1"

authors = [
    "Serge Sans Paille"
]

description = \
    """
    Header-only library that provides 0 cost initialization for immutable
    containers, fixed-size containers, and various algorithms.
    """

build_requires = [
    "cmake"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.frozen"


def commands():
    env.FROZEN_ROOT.append("{root}")
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")