name = "vfx_reference_platform"

version = "2021"

authors = [
    "Visual Effects Society Technology Committee (VES)"
]

description = \
    """
    Bundle for VFX Reference Platform.
    """

requires = [
    # TODO: non-std, however is convenient for development. Move these to other suite in final commit. 
    "cmake-3.20",
    "oiio-2.2.15",
    
    # CY2021 standard
    "boost-1.73",
    "python-3.7",
    "openexr-2.4.3",
    "tbb-2020.2",
    "ocio-2.0.1"
]

uuid = "vfx_reference_platform_2021"