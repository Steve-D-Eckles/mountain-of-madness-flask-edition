import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="madness"
    version="0.0.1",
    author="Steve Eckles",
    author_email="steve.d.eckles@gmail.com",
    url="https://github.com/Steve-D-Eckles/madness",
    description="what does madness do?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

