import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hostlink-python",
    version="0.0.1",
    author="Josh",
    author_email="68728513+joshlin5900@users.noreply.github.com",
    description="Host Link protocol stack of Omron PLCs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshlin5900/hostlink-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
