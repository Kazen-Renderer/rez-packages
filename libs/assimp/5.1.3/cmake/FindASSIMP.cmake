find_path(ASSIMP_INCLUDE_DIR assimp/Importer.hpp
    NO_DEFAULT_PATH
    HINTS
        ${ASSIMP_ROOT}
        $ENV{REZ_ASSIMP_ROOT}
    PATH_SUFFIXES
        include)

find_library(ASSIMP_LIBRARY assimp
    NO_DEFAULT_PATH
    HINTS
        ${ASSIMP_ROOT}
        $ENV{REZ_ASSIMP_ROOT}
    PATH_SUFFIXES
        lib)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(ASSIMP DEFAULT_MSG
    ASSIMP_INCLUDE_DIR
    ASSIMP_LIBRARY)

if(ASSIMP_FOUND)
    set(ASSIMP_INCLUDE_DIRS ${ASSIMP_INCLUDE_DIR})
    set(ASSIMP_LIBRARIES ${ASSIMP_LIBRARY})
endif()