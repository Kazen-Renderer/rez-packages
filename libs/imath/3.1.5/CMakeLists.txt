CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v3.1.5.tar.gz)
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
    CONFIGURE_COMMAND cmake -DILMBASE_BUILD_BOTH_STATIC_SHARED=ON 
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
        -DBoost_NO_SYSTEM_PATHS=ON
        -DZLIB_ROOT=$ENV{REZ_ZLIB_ROOT}
        -DIMATH_INTERNAL_NAMESPACE=Imath
        # From https://github.com/AcademySoftwareFoundation/openexr/issues/684
        -DPython_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python
        -DPython3_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
