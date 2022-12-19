import platform

name = "llvm"

version = "15.0.6"

authors = [
    "Vikram Adve",
    "Chris Lattner",
    "LLVM Developer Group"
]

description = \
    """
    The LLVM Project is a collection of modular and reusable compiler and toolchain
    technologies. Despite its name, LLVM has little to do with traditional virtual
    machines. The name "LLVM" itself is not an acronym; it is the full name of the
    project.
    """

build_requires = [
    "cmake"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.llvm"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/clang")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/llvm")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")