import platform

name = "cmake"

version = "3.20.4"

authors = [
    "Andy Cedilnik",
    "Bill Hoffman",
    "Brad King",
    "Ken Martin",
    "Alexander Neundorf"
]

description = \
    """
    CMake is cross-platform free and open-source software for build
    automation, testing, packaging and installation of software by using
    a compiler-independent method.
    """

build_requires = []

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "softwares.cmake"


def commands():
    env.PATH.append("{root}/bin")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")