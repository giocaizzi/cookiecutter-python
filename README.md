# cookiecutter-python

[![Tests](https://github.com/giocaizzi/cookiecutter-python/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/giocaizzi/cookiecutter-python/actions/workflows/tests.yml)

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package with Documentation hosted on GitHub Pages.

Features:

- Python 3.x package with [setuptools](https://setuptools.readthedocs.io/en/latest/)
    - Formatting with [black](https://github.com/psf/black)
    - Linting with [flake8](https://flake8.pycqa.org/en/latest/)
- **Testing** with [pytest](https://docs.pytest.org/en/latest/)
    - Code coverage with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- **Documentation** with [Sphinx](http://www.sphinx-doc.org/en/master/)
    - Automatic API Reference from code docstrings with [autodoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)
        - Custom API Reference with [jinja2](https://jinja.palletsprojects.com)
    - Optimized for [GitHub Pages](https://pages.github.com/), with separate branches for `main` and `gh-pages`
    - Read the Docs theme with [sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)
    - Render jupyter notebooks with [nbsphinx](https://nbsphinx.readthedocs.io/en/latest/)
- **Continuous Integration** with [GitHub Actions](
    https://docs.github.com/en/actions)
    - Run tests on `main` for `push` and `pull_request` events
        - Upload code coverage to [codecov](https://codecov.io/)
    - Publish to [PyPI](https://pypi.org/) on `release` event
    - Build documentation on `push` and `pull_request` events on `gh-pages` branch
    - Lint with flake8 - using also [flake8-rst-docstrings](https://github.com/peterjc/flake8-rst-docstrings/tree/master) to catch RST formatting errors - on all `push` and `pull_request` events to `main`.
- MIT License

