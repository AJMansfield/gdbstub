from distutils.core import setup


setup(
    name="gdbstub",
    url="https://github.com/AJMansfield/gdbstub",
    author="Anson Mansfield",
    author_email="amansfield@mantaro.com",
    version="0.1",
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