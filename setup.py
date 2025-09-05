from distutils.core import setup

def calc_git_version():
    import subprocess
    import os
    try:
        version = subprocess.run(['git', 'describe', '--tags'], check=True, capture_output=True, encoding='utf-8').stdout
        assert version[0] == "v"
        version = version.strip().removeprefix("v").replace("-",".post",1).replace("-","+")
    except subprocess.CalledProcessError as e:
        version = os.path.basename(os.path.dirname(__file__)).split("-", maxsplit=1)[1]
    return version

setup(
    name="gdbstub",
    url="https://github.com/AJMansfield/gdbstub",
    author="Anson Mansfield",
    author_email="amansfield@mantaro.com",
    version=calc_git_version(),
    package_data={"_gdb": ['__init__.pyi']},
    packages=["_gdb"],
    license="GPL-2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Debuggers",
        "Typing :: Stubs Only",
    ]
)