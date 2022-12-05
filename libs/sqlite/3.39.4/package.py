import platform

name = "sqlite"

version = "3.39.4"

authors = [
    "Dwayne Richard Hipp and etc.."
]

description = \
    """
    SQLite is an in-process library that implements a self-contained, serverless,
    zero-configuration, transactional SQL database engine.
    """

build_requires = []

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.sqlite"


def commands():
    env.PATH.append("{root}/bin")
    env.CPATH.append("{root}/include")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.SQLITE_ROOT_DIR.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")