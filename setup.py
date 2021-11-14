from setuptools import setup, find_packages

setup(
    name='piter',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'typer',
        'toml',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'piter = piter:app',
        ],
    },
)