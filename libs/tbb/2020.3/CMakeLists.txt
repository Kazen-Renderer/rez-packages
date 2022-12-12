CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/oneapi-src/oneTBB/archive/refs/tags/v2020.3.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd python build/build.py
        --prefix $ENV{REZ_BUILD_INSTALL_PATH} --install-devel --install-libs)
else()
    set(install_cmd echo "skip install step")
endif()

# TBB 2020 update 2 only got a Makefile in the release tarball
# No install target included, cannot configure it..
ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND echo "Dummy configure command"
    BUILD_COMMAND cd ../${name} && echo | pwd && python build/build.py
        --prefix $ENV{REZ_BUILD_INSTALL_PATH}
    INSTALL_COMMAND cd ../${name} && ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
