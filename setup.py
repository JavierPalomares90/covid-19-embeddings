import setuptools


def readme():
    with open("README.md") as readme_file:
        return readme_file.read()


setuptools.setup(
    name="cord-19-embeddings",
    version="0.0.1",
    description="CORD 19 embeddings tools",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/JavierPalomares90/covid-19-embeddings",
    maintainer="Javier Palomares",
    maintainer_email="javier.palomares.90@gmail.com",
    packages=["embeddings","scorings"],
    license="GPL version 3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL version 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["cord-19-tools"],
 )