setup(
    name="PyQr",
    version="1.0.0",
    description="fast creating qr code with this tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DanteAlighierin/PyQr",
    author="DanteAlighierin",
    license="GPL-3",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["pyqrode"],
    include_package_data=True,
    install_requires=[
        "pyqrcode" ],
    entry_points={"console_scripts": ["choise.py=reader.__main__:main"]},
)

