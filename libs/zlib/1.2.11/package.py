name = "zlib"

version = "1.2.11"

authors = [
    "Jean-loup Gailly",
    "Mark Adler"
]

description = \
    """
    zlib is designed to be a free, general-purpose, legally 
    unencumbered -- that is, not covered by any patents -- lossless 
    data-compression library for use on virtually any computer 
    hardware and operating system. 
    """

build_requires = [
    "cmake"
]

requires = [

]

variants = [
    ["platform-osx", "arch-x86_64"]
]

uuid = "libs.zlib"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")