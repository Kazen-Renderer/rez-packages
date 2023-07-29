import os
import sys
import requests
import tarfile
import subprocess
import signal
import traceback
import functools


def build(source_path, build_path, install_path, targets):
    package_url = 'https://github.com/Kitware/CMake/releases/download/v3.25.1/cmake-3.25.1.tar.gz'
    package_name = os.path.basename(package_url)
    # extension name .tar.gz is kinda special, the following logic is specific
    # to this downloading url
    extension_idx = package_name.find('.tar.gz')
    folder_name = package_name[:extension_idx]

    def terminate_proc(proc, sig, frame):
        try:
            if proc:
                proc.terminate()
                proc.wait()
        except:
            traceback.print_exc()
        finally:
            sys.exit()

    def _build():
        os.chdir(build_path)
        if not os.path.exists(package_name):
            print("package doesn't exist, start downloading...")
            response = requests.get(package_url)
            open(package_name, 'wb').write(response.content)

        if not os.path.exists(folder_name):
            print('extracting package...')
            f = tarfile.open(package_name)
            f.extractall(build_path)

        os.chdir(os.path.join(build_path, folder_name))

        bootstrapped_path = os.path.join(build_path, folder_name, 'bootstrapped')
        if not os.path.exists(bootstrapped_path):
            print('package not configured, configure now...')
            bootstrap_proc = subprocess.Popen('./bootstrap --prefix=$REZ_BUILD_INSTALL_PATH', shell=True)
            handler = functools.partial(terminate_proc, bootstrap_proc)
            signal.signal(signal.SIGINT, handler)
            signal.signal(signal.SIGTERM, handler)
            bootstrap_proc.wait()
            print('bootstrap return code', bootstrap_proc.returncode)
            if (bootstrap_proc.returncode != 0):
                print('bootstrap failed, terminating...')
                return
            f = open('bootstrapped', 'wb')
            f.write('0')
            f.close()

        built_path = os.path.join(build_path, folder_name, 'built')
        if not os.path.exists(built_path):
            print('package not built, build now...')
            make_proc = subprocess.Popen('make -j{}'.format(os.cpu_count()), shell=True)
            handler = functools.partial(terminate_proc, make_proc)
            signal.signal(signal.SIGINT, handler)
            signal.signal(signal.SIGTERM, handler)
            make_proc.wait()
            if (make_proc.returncode != 0):
                print('make failed, terminating...')
                return
            f = open('built', 'wb')
            f.write('0')
            f.close()

        print('build done')

    def _install():
        print('installing package...')
        os.chdir(os.path.join(build_path, folder_name))
        install_proc = subprocess.Popen('make install', shell=True)
        handler = functools.partial(terminate_proc, install_proc)
        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)
        install_proc.wait()
        print('install done')

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