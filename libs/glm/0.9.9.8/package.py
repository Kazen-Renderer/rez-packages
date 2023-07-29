import platform

name = "glm"

version = "0.9.9.8"

authors = [
    "Christophe and etc..."
]

description = \
    """
    OpenGL Mathematics (GLM) is a header only C++ mathematics library
    for graphics software based on the OpenGL Shading Language (GLSL)
    specifications.
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

uuid = "libs.glm"


def commands():
    env.GLM_ROOT.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")