#!/usr/bin/env python

import os, platform
import os.path
import shutil
import sys
import stat
import subprocess
import urllib.request
import tarfile


def build(source_path, build_path, install_path, targets):

    file_path = os.path.join(build_path, 'openssl.tar.gz')
    extracted_path = os.path.join(build_path, 'openssl-OpenSSL_1_1_1k')

    def _download():
        
        if not os.path.exists(file_path):
            url = 'https://github.com/openssl/openssl/archive/refs/tags/OpenSSL_1_1_1k.tar.gz'
            downloaded_file = urllib.request.urlopen('https://github.com/openssl/openssl/archive/refs/tags/OpenSSL_1_1_1k.tar.gz').read()
            open(file_path, 'wb').write(downloaded_file)
        else:
            print('File already exists')

    def _decompress():
        if not os.path.exists(extracted_path):
            f = tarfile.open(file_path)
            f.extractall(build_path)
            f.close()

    def _build():

        _decompress()        

        _download()

        # In source build
        os.chdir(extracted_path)

        # Configure & Make
        if platform.system() == "Windows":
            os.system('call C:/"Program Files (x86)/Microsoft Visual Studio"/2019/Community/VC/Auxiliary/Build/vcvarsall.bat amd64')
            os.environ['PATH'] = ';'.join([os.environ['PATH'], 'C:/Program Files (x86)/Windows Kits/10/bin/10.0.19041.0/x64'])
            subprocess.run('perl Configure VC-WIN64A --prefix={0}'.format(os.path.abspath(os.getenv("REZ_BUILD_INSTALL_PATH"))), shell=True)
            subprocess.run('nmake', shell=True)
        else:
            subprocess.run('./config --prefix=$REZ_BUILD_INSTALL_PATH --openssldir=$REZ_BUILD_INSTALL_PATH', shell=True)
            subprocess.run('make', shell=True)

    def _install():
        # Make install
        if platform.system() == "Windows":
            #os.mkdir(os.getenv("REZ_BUILD_INSTALL_PATH"))
            subprocess.run('nmake install', shell=True)
        else:
            subprocess.run('make install', shell=True)

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
