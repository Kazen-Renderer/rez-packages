CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tar.xz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd cd ../${name} && make install ${make_args} &&
        cd $ENV{REZ_BUILD_INSTALL_PATH}/bin && ln -sf python3 python && ln -sf pip3 pip)
else()
    set(install_cmd echo "skip install step")
endif()

ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    PATCH_COMMAND patch -p1 < $ENV{REZ_BUILD_SOURCE_PATH}/python.patch
    CONFIGURE_COMMAND cd ../${name} && ./configure 
        --prefix=$ENV{REZ_BUILD_INSTALL_PATH}
        --with-lto
        --with-openssl=$ENV{REZ_OPENSSL_ROOT}
        --without-pymalloc
        --enable-optimizations
        CPPFLAGS=-I$ENV{REZ_ZLIB_ROOT}/include
        LDFLAGS=-L$ENV{REZ_ZLIB_ROOT}/lib
    BUILD_COMMAND cd ../${name} &&  make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
