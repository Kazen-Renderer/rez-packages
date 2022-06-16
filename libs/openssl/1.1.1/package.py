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
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])
elif platform.system() == "Windows":
    variants.append(["platform-windows", "arch-AMD64"])

uuid = "libs.openssl"

if platform.system() == "Windows":
    build_requires.append("python-3")
    build_requires.append("winenv-0.0.1")
    build_command = "python {root}/build.py {install}"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.OPENSSL_ROOT_DIR.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")