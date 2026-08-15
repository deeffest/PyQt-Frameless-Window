import setuptools

setuptools.setup(
    name="PyQt5-Frameless-Window",
    version="0.8.2+20260815",
    packages=setuptools.find_packages(),
    install_requires=[
        "pywin32;platform_system=='Windows'",
        "xcffib;platform_system=='Linux'",
        "pyobjc;platform_system=='Darwin'",
        "PyCocoa;platform_system=='Darwin'",
    ],
)
