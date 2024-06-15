from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="{{cookiecutter.package_slug}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.short_description}}",
    long_description_content_type="text/markdown",
    long_description=long_description,
    {% if cookiecutter.add_urls == "true" %}
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug}}",
    {% endif %}
    author="{{cookiecutter.author_name}}",
    author_email=f"{{cookiecutter.author_email}}",
    license="{{cookiecutter.license}}",
    packages=find_packages(
        include=["{{cookiecutter.package_slug}}", "{{cookiecutter.package_slug}}/*"]
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
    {% if cookiecutter.add_urls == "true" %}
    project_urls={
        "Documentation": "https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.package_slug}}/",
        "Bug Reports": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug}}/issues",
        "Source": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug}}",
    },
    {% endif %}
)
