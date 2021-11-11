#!/usr/bin/env python

import os
import os.path
import shutil
import sys
import stat


def build(source_path, build_path, install_path, targets):

    def _build():
        # python source
        pass

    def _install():
        pass

    _build()

    if "install" in (targets or []):
        _install()


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:]
    )
