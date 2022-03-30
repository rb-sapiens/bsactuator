import setuptools

setuptools.setup(
    name="bsactuator", # Replace with your own username
    version="0.0.1",
    install_requires=[
        "pyserial",
    ],
    author="Shun Nagao",
    author_email="nagao@rb-sapiens.com",
    description="A serial operator for BambooShoot Actuator",
    long_description_content_type="text/markdown",
    url="https://github.com/rb-sapiens/bsactuator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)