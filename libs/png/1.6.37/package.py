import platform

name = "png"

version = "1.6.37"

authors = [
    "Guy Eric Schalnat",
    "Andreas Dilger",
    "John Bowler",
    "Glenn Randers-Pehrson",
    "Cosmin Truta"
]

description = \
    """
    libpng is the official PNG reference library.
    """

build_requires = [
    "cmake"
]

requires = [

]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.png"


def commands():
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")