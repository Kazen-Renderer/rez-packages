name = "python"

version = "3.7.10"

authors = [
    "Guido van Rossum"
]

description = \
    """
    Python is an interpreted high-level general-purpose programming 
    language.
    """

build_requires = [

]

requires = [
    "zlib-1.2.11",
    "openssl-1.1.1"
]

variants = [
    ["platform-osx", "arch-x86_64"]
]

uuid = "softwares.python"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")