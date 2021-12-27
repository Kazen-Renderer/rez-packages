CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/archive/refs/tags/v1.11.14.2.tar.gz)
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
    CONFIGURE_COMMAND cmake
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON
        -DCMAKE_CXX_STANDARD=14
        -DCMAKE_BUILD_TYPE=Debug
        -DBoost_ROOT=$ENV{REZ_BOOST_ROOT}
        -DZLIB_ROOT=$ENV{REZ_ZLIB_ROOT}
        -DOpenEXR_ROOT=$ENV{REZ_OPENEXR_ROOT}
        -DOpenImageIO_ROOT=$ENV{REZ_OIIO_ROOT}
        -Dpugixml_ROOT=$ENV{REZ_PUGIXML_ROOT}
        -Dpybind11_ROOT=$ENV{REZ_PYBIND11_ROOT}
        -DPython_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python
        -DBUILD_TESTING=OFF
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
