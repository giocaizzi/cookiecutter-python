from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.short_description}}",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}",
    author="{{cookiecutter.author_name}}",
    author_email=f"{{cookiecutter.author_email}}",
    license="{{cookiecutter.license}}",
    packages=find_packages(
        include=["{{cookiecutter.package_name}}", "{{cookiecutter.package_name}}/*"]
    ),
    setup_requires=[],
    tests_require=[],
    install_requires=[],
    extras_require={
        "docs": [],
        "dev": [],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    project_urls={
        "Documentation": "https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.package_name}}/",
        "Bug Reports": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/issues",
        "Source": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}",
    },
)
