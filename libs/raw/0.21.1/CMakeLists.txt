CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url http://download.osgeo.org/libtiff/tiff-4.3.0.tar.gz)
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
    CONFIGURE_COMMAND cd ../${name} &&
        ./configure --prefix=$ENV{REZ_BUILD_INSTALL_PATH}
    BUILD_COMMAND cd ../${name} && make ${make_args}
    INSTALL_COMMAND cd ../${name} && ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
