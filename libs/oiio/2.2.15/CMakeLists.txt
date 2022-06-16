CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/OpenImageIO/oiio/archive/refs/tags/v2.2.15.1.tar.gz)
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
    PATCH_COMMAND cd ../${name} && patch -p1 < $ENV{REZ_BUILD_SOURCE_PATH}/oiio.patch
    CONFIGURE_COMMAND cmake
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON
        -DCMAKE_FIND_USE_CMAKE_PATH=FALSE
        -DCMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY=FALSE
        -DCMAKE_BUILD_TYPE=Debug
        -DBoost_ROOT=$ENV{REZ_BOOST_ROOT}
        -DPython_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python3
        -Dpybind11_ROOT=$ENV{REZ_PYBIND11_ROOT}
        -DTBB_ROOT=$ENV{REZ_TBB_ROOT}
        -DOpenEXR_ROOT=$ENV{REZ_OPENEXR_ROOT}
        -DOpenColorIO_ROOT=$ENV{REZ_OCIO_ROOT}
        -DOpenJpeg_ROOT=$ENV{REZ_OPENJPEG_ROOT}
        -DTIFF_ROOT=$ENV{REZ_TIFF_ROOT}
        -DPNG_ROOT=$ENV{REZ_PNG_ROOT}
        -DJPEGTurbo_ROOT=$ENV{REZ_JPEG_ROOT}
        -DGIF_ROOT=$ENV{REZ_GIF_ROOT}
        -DZLIB_ROOT=$ENV{REZ_ZLIB_ROOT}
        -DOIIO_BUILD_TESTS=OFF
        -DOIIO_BUILD_TOOLS=ON
        #-DUSE_QT=OFF
        #-DUSE_OPENGL=OFF
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
