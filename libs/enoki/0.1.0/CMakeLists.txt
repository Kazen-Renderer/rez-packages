CMAKE_MINIMUM_REQUIRED(VERSION 3.17)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/mitsuba-renderer/enoki.git)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd  ${CMAKE_COMMAND} -E copy_directory <SOURCE_DIR> $ENV{REZ_BUILD_INSTALL_PATH})
else()
    set(install_cmd echo "skip install step")
endif()


ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND cmake
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")