CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v2.4.3.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd "cd ${name} && make install ${make_args}")
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND cmake -DILMBASE_BUILD_BOTH_STATIC_SHARED=ON 
        -DOPENEXR_BUILD_BOTH_STATIC_SHARED=ON 
        -DOPENEXR_VIEWERS_ENABLE=OFF
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        ../${name}
    BUILD_COMMAND cd ${name} &&  make ${make_args}
    INSTALL_COMMAND cd ${install_cmd}
)

rez_install_files(
    cmake/openexr.cmake
    DESTINATION .
)