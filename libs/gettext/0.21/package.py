import platform

name = "gettext"

version = "0.21"

authors = [
    "Daiki Ueno"
]

description = \
    """
    GNU gettext is an important step for the GNU Translation Project,
    as it is an asset on which we may build many other steps. This
    package offers to programmers, translators, and even users, a well
    integrated set of tools and documentation. Specifically, the GNU
    gettext utilities are a set of tools that provides a framework to
    help other GNU packages produce multi-lingual messages. These tools
    include a set of conventions about how programs should be written
    to support message catalogs, a directory and file naming
    organization for the message catalogs themselves, a runtime library
    supporting the retrieval of translated messages, and a few
    stand-alone programs to massage in various ways the sets of
    translatable strings, or already translated strings. A special
    GNU Emacs mode also helps interested parties in preparing these
    sets, or bringing them up to date.
    """

build_requires = []

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])


uuid = "libs.gettext"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.LDFLAGS.append('-L{root}/lib')
        env.CPPFLAGS.append("-I{root}/include")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")