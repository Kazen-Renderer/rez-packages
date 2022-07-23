import platform

name = "eigen"

version = "3.4.0"

authors = [
    "Benoît Jacob",
    "Gaël Guennebaud"
]

description = \
    """
    Eigen is a C++ template library for linear algebra: matrices, vectors,
    numerical solvers, and related algorithms.
    """

build_requires = []

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.eigen"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/share/eigen3/cmake")
    env.EIGEN3_ROOT.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
