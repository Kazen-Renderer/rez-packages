import platform

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
    "openssl-1.1.1",
    "sqlite-3"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "softwares.python"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.append("{root}/bin")
    env.Python_ROOT_DIR = "{root}"

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")