import platform

name = "enoki"

version = "0.1.0"

authors = [
    "Wenzel Jakob"
]

description = \
    """
    Enoki is a C++ template library that enables automatic transformations of numerical code, 
    for instance to create a "wide" vectorized variant of an algorithm that runs on the CPU or GPU, 
    or to compute gradients via transparent forward/reverse-mode automatic differentation.
    """

build_requires = [
    "cmake"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "enoki-0.1.0"


def commands():
    # NOTICE: 
    # User should add these 2 lines in their own cmake file
    #
    # target_compile_features(YOUR_TARGET_NAME PUBLIC cxx_std_17)
    # target_include_directories(YOUR_TARGET_NAME PUBLIC
    #     $ENV{REZ_ENOKI_ROOT}/include  
    # )

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")