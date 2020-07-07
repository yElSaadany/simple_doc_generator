from setuptools import setup, find_packages


setup(
    name="SimpleDocGenerator",
    version="0.1.1",
    packages_dir={"package": "simpledoc"},
    author="Youssef El Saadany",
    author_email="youssef.saadany@gmail.com",
    description="This package can be used to easily generate documention in markdown for Python projects",
    url="https://github.com/yElSaadany/simple_doc_generator/",
    keywords="documentation markdown python project simple",
    project_urls={"Source Code": "https://github.com/yElSaadany/simple_doc_generator"},
    install_requires=["docstring-parser==0.3", "setuptools==41.0.1",],
    extras_requires={"dev": ["flake8"]},
    entry_points={"console_scripts": ["generate-doc = simpledoc.main:main"]},
)
