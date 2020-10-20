from setuptools import setup, find_packages

setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.4",
    install_requires=["requests"]
)
