CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/AcademySoftwareFoundation/openvdb/archive/refs/tags/v10.0.1.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if($ENV{REZ_BUILD_INSTALL})
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
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON
        -DBoost_ROOT=$ENV{REZ_BOOST_ROOT}
        -DTBB_ROOT=$ENV{REZ_TBB_ROOT}
        -DTbb_INCLUDE_DIR=$ENV{REZ_TBB_ROOT}/include
        -DOpenEXR_ROOT=$ENV{REZ_OPENEXR_ROOT}
        -DPNG_ROOT=$ENV{REZ_PNG_ROOT}
        -DZLIB_ROOT=$ENV{REZ_ZLIB_ROOT}
        -DUSE_EXR=ON
        -DUSE_PNG=ON
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
