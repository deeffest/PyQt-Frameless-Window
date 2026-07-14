import setuptools

setuptools.setup(
    name="PySide6-Frameless-Window",
    version="0.8.1+20260714",
    packages=setuptools.find_packages(),
    install_requires=[
        "pywin32;platform_system=='Windows'",
        "pyobjc;platform_system=='Darwin'",
        "PyCocoa;platform_system=='Darwin'",
    ],
)
