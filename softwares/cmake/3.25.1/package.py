import platform

name = "cmake"

version = "3.25.1"

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

build_requires = [
    "gcc-12"
]

requires = [
    "openssl-1.1.1"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "softwares.cmake"

build_command = 'python {root}/build.py {install}'


def commands():
    env.PATH.append("{root}/bin")
    env.C_INCLUDE_PATH.append("{root}/include")
    env.CPLUS_INCLUDE_PATH.append("{root}/include")
    env.LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/share/cmake-3.25/Modules")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")