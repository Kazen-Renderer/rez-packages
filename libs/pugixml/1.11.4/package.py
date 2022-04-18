import platform

name = "pugixml"

version = "1.11.4"

authors = [
    "Arseny Kapoulkine"
]

description = \
    """
    pugixml is a light-weight C++ XML processing library.
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


uuid = "libs.pugixml"


def commands():
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")