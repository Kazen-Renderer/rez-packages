CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://boostorg.jfrog.io/artifactory/main/release/1.73.0/source/boost_1_73_0.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd cd ../${name} && ./b2 install)
else()
    set(install_cmd echo "skip install step")
endif()

ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND echo ${REZ_PYTHON_ROOT} && cd ../${name} && ./bootstrap.sh --prefix=$ENV{REZ_BUILD_INSTALL_PATH}
        --with-python=$ENV{REZ_PYTHON_ROOT}/bin/python
        --with-python-root=$ENV{REZ_PYTHON_ROOT}
        --with-python-version=3.7
    BUILD_COMMAND cd ../${name} && ./b2 -j$ENV{REZ_BUILD_THREAD_COUNT}
        --build-dir=$ENV{REZ_BUILD_PATH}
    INSTALL_COMMAND ${install_cmd}
)