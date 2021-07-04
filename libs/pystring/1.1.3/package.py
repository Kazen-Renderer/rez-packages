import platform

name = "pystring"

version = "1.1.3"

authors = [
    "Jesse Beder"
]

description = \
    """
    Pystring is a collection of C++ functions which match the interface
    and behavior of python's string class methods using std::string.
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

uuid = "libs.pystring"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")