CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url  https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/refs/tags/v2.2.0.tar.gz)
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
    PATCH_COMMAND cd ../${name} && patch -p1 < $ENV{REZ_BUILD_SOURCE_PATH}/ocio.patch
    CONFIGURE_COMMAND cmake
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        -DPython_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python
        -Dpybind11_ROOT=$ENV{REZ_PYBIND11_ROOT}
        -Dexpat_ROOT=$ENV{REZ_EXPAT_ROOT}
        -Dyaml-cpp_ROOT=$ENV{REZ_YAMLCPP_ROOT}
        -Dpystring_ROOT=$ENV{REZ_PYSTRING_ROOT}
        -DHalf_ROOT=$ENV{REZ_OPENEXR_ROOT}
        -DOpenEXR_ROOT=$ENV{REZ_OPENEXR_ROOT}
        -Dminizip-ng_ROOT=$ENV{REZ_MINIZIP_ROOT}
        -Dminizip-ng_DIR=$ENV{REZ_MINIZIP_ROOT}/lib/cmake/minizip
        -DPYBIND11_TEST=OFF
        -DBUILD_TESTING=OFF
        -DOCIO_BUILD_APPS=OFF
        -DOCIO_BUILD_TESTS=OFF
        -DOCIO_BUILD_GPU_TESTS=OFF
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
