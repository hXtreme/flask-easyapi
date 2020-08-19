#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Harsh Parekh",
    author_email="harsh_parekh@outlook.com",
    python_requires=">=3.6",
    classifiers=[
        "Framework :: Flask",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Rest API on Flask made a little too easy.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="flask_easyapi",
    name="flask_easyapi",
    packages=find_packages(include=["flask_easyapi", "flask_easyapi.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/hXtreme/flask_easyapi",
    version="0.0.1",
    zip_safe=False,
)
