CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.tar.gz)


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
        -DCMAKE_BUILD_TYPE=Release
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
