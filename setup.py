from setuptools import setup, find_packages

setup(
    name='proxy-tools',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'alabaster==0.7.12',
    ],
)
