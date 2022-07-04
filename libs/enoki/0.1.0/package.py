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
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.enoki"


def commands():
    # NOTICE: 
    # User should add these 2 lines in their own cmake file
    #
    # # C++17
    # include(CheckCXXCompilerFlag)
    # if (CMAKE_CXX_COMPILER_ID MATCHES "^(GNU|Clang|Emscripten|Intel)$")
    # CHECK_CXX_COMPILER_FLAG("-std=c++17" HAS_CPP17_FLAG)
    #
    # if (HAS_CPP17_FLAG)
    #     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")
    # else()
    #     CHECK_CXX_COMPILER_FLAG("-std=c++1z" HAS_CPP1Z_FLAG)
    #     if (HAS_CPP1Z_FLAG)
    #     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1z")
    #     else()
    #     message(FATAL_ERROR "Unsupported compiler -- nanogui requires C++17 support!")
    #     endif()
    # endif()
    # elseif(MSVC)
    # set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++17")
    # endif()
    #
    # # enoki
    # add_subdirectory($ENV{REZ_ENOKI_ROOT} ext_build)
    # enoki_set_compile_flags()
    # enoki_set_native_flags()
    # include_directories($ENV{REZ_ENOKI_ROOT}/include)

    env.CMAKE_PREFIX_PATH.append("{root}")
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")