CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://sourceforge.net/projects/giflib/files/latest/download)
set(make_args VERBOSE=1)

if($ENV{REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd echo "skip install step")
endif()

ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    PATCH_COMMAND cd ../${name} && patch -p1 < $ENV{REZ_BUILD_SOURCE_PATH}/gif.patch
    CONFIGURE_COMMAND cmake -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH} ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
