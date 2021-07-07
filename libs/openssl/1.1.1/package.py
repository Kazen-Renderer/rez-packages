import platform

name = "openssl"

version = "1.1.1"

authors = [
    "Mark Cox",
    "Ralf Engelschall",
    "Stephen Henson",
    "Ben Laurie",
    "Paul Sutton"
]

description = \
    """
    OpenSSL is a software library for applications that secure 
    communications over computer networks against eavesdropping 
    or need to identify the party at the other end. It is widely 
    used by Internet servers, including the majority of HTTPS 
    websites.
    """

build_requires = []

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86-64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.openssl"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")