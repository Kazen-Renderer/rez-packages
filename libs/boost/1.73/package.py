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
    "python-3.7.10"
]

variants = [
    ["platform-osx", "arch-x86_64"]
]

uuid = "libs.boost"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")