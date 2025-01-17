from setuptools import setup, find_packages

setup(
    name="WonderPeaks_preprocessing",
    version="0.2.3",  # Match the version in pyproject.toml
    description="Preprocessing functions for ChIP-seq and RNA-seq in Fungi with WonderPeaks",
    author="Megan E. Garber",
    author_email="mgarber21@gmail.com",
    url="https://github.com/mgarber21/WonderPeaks_preprocessing",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,  # Enables MANIFEST.in
    install_requires=[
        "deepTools==3.5.1",
        "deeptoolsintervals==0.1.9",
        "multiqc==1.10.1",
        ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)