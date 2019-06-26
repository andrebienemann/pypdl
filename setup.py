import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypdl",
    version="0.2.0",
    author="André Bienemann",
    author_email="andre.bienemann@gmail.com",
    description="Python Probability Distributions Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrebienemann/pypdl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
