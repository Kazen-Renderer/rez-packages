import platform

name = "yamlcpp"

version = "0.6.3"

authors = [
    "Jesse Beder"
]

description = \
    """
    yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec.
    """

build_requires = [
    "cmake"
]

requires = [
    "python-3.7.10",
    "boost-1.73",
    "zlib-1.2.11"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.yamlcpp"


def commands():
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/yaml-cpp")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")