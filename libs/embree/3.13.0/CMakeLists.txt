CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/embree/embree/archive/refs/tags/v3.13.0.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd echo "skip install step")
endif()

ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND cmake
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        -DEMBREE_TBB_ROOT=$ENV{REZ_TBB_ROOT}
        -DEMBREE_TUTORIALS=OFF
        -DEMBREE_RAY_MASK=ON
        -DEMBREE_ISPC_SUPPORT=OFF # NOTICE: disable ispc for now. This line should be removed after ispc rez package add in.
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)
# # static lib
# ExternalProject_add(
#     ${name}
#     URL ${url}
#     PREFIX ${name}
#     CONFIGURE_COMMAND cmake
#         -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
#         -DEMBREE_TBB_ROOT=$ENV{REZ_TBB_ROOT}
#         -DEMBREE_STATIC_LIB=ON
#         -DEMBREE_TUTORIALS=OFF
#         -DEMBREE_RAY_MASK=ON
#         ../${name}
#     BUILD_COMMAND make ${make_args}
#     INSTALL_COMMAND ${install_cmd}
# )


install(CODE "message(STATUS Dummy Install Target)")
