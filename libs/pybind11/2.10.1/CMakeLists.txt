CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/pybind/pybind11/archive/refs/tags/v2.10.1.tar.gz)
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
        -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
        -DBoost_NO_SYSTEM_PATHS=ON
        -DPython_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python
        # These definitions are set for find PythonInterp
        -DPYTHON_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python
        -DPYTHON_LIBRARY=$ENV{REZ_PYTHON_ROOT}/lib
        -DPYTHON_INCLUDE_DIR=$ENV{REZ_PYTHON_ROOT}/include
        -DPYBIND11_TEST=OFF
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
