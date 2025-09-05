from distutils.core import setup


setup(
    name="gdb-stubs",
    url="https://github.com/AJMansfield/gdb-stubs",
    author="Anson Mansfield",
    author_email="amansfield@mantaro.com",
    version="0.1",
    package_data={"_gdb": ['__init__.pyi']},
    packages=["_gdb"]
)