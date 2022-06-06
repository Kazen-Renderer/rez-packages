import platform

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

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])


uuid = "libs.zlib"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.LDFLAGS.append('-L{root}/lib'.replace('\~', '\\\~'))
        env.CPPFLAGS.append("-I{root}/include")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")