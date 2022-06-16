import platform

name = "assimp"

version = "5.1.3"

authors = [
    "Kim Kulling and etc..."
]

description = \
    """
    A library to import and export various 3d-model-formats including
    scene-post-processing to generate missing render data.
    """

build_requires = [
    "cmake"
]

requires = [
    "zlib"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.assimp"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")