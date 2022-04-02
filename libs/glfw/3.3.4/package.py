import platform

name = "glfw"

version = "3.3.4"

authors = [
    "Copyright © 2002-2006 Marcus Geelnard",
    "Copyright © 2006-2019 Camilla Löwy"
]

description = \
    """
    GLFW is an Open Source, multi-platform library for OpenGL, 
    OpenGL ES and Vulkan development on the desktop.
    """

build_requires = [
    "cmake"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "~arch==x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.glfw"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/glfw3")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")