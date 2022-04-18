import platform

name = "boost"

version = "1.73.0"

authors = [
    "Boost community"
]

description = \
    """
    Boost is a set of libraries for the C++ programming language 
    that provides support for tasks and structures such as linear 
    algebra, pseudorandom number generation, multithreading,
    image processing, regular expressions, and unit testing.
    """

build_requires = [

]

requires = [
    "python-3.7"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.boost"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")