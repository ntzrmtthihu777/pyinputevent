import setuptools

readme = open("README").read()
setuptools.setup(
    name="PyInputEvent",
    version="0.1b0",
    description="PyInputEvent provides a python interface to Linux's input subsystem",
    url="https://github.com/ntzrmtthihu777/pyinputevent.git",
    author="rmt",
    license="MIT",
    long_description=readme,
    package_dir={"": "src"},
    packages=setuptools.find_packages("src")
)
