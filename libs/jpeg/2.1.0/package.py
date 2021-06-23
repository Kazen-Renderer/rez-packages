import platform

name = "jpeg"

version = "2.1.0"

authors = [
    "libjpeg-turbo team",
]

description = \
    """
    libjpeg-turbo is a JPEG image codec that uses SIMD instructions
    (MMX, SSE2, AVX2, Neon, AltiVec) to accelerate baseline JPEG
    compression and decompression.
    """

build_requires = [
    "cmake"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.jpeg"


def commands():
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")