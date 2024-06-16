# cookiecutter-python

[![Deploy Ubunut](https://github.com/giocaizzi/cookiecutter-python/actions/workflows/deployment.yml/badge.svg)](https://github.com/giocaizzi/cookiecutter-python/actions/workflows/deployment.yml)
[![Deploy Windows](https://github.com/giocaizzi/cookiecutter-python/actions/workflows/deployment-win.yml/badge.svg)](https://github.com/giocaizzi/cookiecutter-python/actions/workflows/deployment-win.yml)

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python packages.

## Usage

```bash
pipx run cookiecutter gh:giocaizzi/cookiecutter-python [--config-file <path_to_config>]
```

### User configuration

Specify user configuration in YAML file.

```yaml
default_context:
  author_name: "Mario Rossi"
  author_email: "mario@rossi.com"
  github_username: "mariorrossi"
```

Set default configuration, adding the `COOKIECUTTER_CONFIG` environment variable.
```bash
export COOKIECUTTER_CONFIG=/home/mariorossi/my-custom-config.yaml
```

## 🍬 Features:

- 🛠 **Set up Python 3.x package** with [poetry]() or [setuptools](https://setuptools.readthedocs.io/en/latest/)
    - Choosing between `pyproject.toml` configuration or legacy `setup.py` script
    - *Formatting* with [black](https://github.com/psf/black)
    - *Linting* with [flake8](https://flake8.pycqa.org/en/latest/) and [flake8-rst-docstrings](https://github.com/peterjc/flake8-rst-docstrings/tree/master) to catch RST formatting errors.
- ⚙️ **Testing** with [pytest](https://docs.pytest.org/en/latest/)
    - Code *coverage* with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- 📚 **Documentation** with [Sphinx](http://www.sphinx-doc.org/en/master/)
    - *Automatic API Reference* from code docstrings with [autodoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)
        - Custom API Reference with [jinja2](https://jinja.palletsprojects.com)
    - Optimized for [GitHub Pages](https://pages.github.com/), with separate branches for `main` and `gh-pages`
    - Read the Docs theme with [sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)
    - Render jupyter notebooks with [nbsphinx](https://nbsphinx.readthedocs.io/en/latest/)
- ♻️ **Continuous Integration** with [GitHub Actions](
    https://docs.github.com/en/actions)
    - Utilize standardized reusable workflows from [python-dev-actions](https://github.com/giocaizzi/python-dev-actions) to maintain a consistent CI/CD pipeline across projects.
- ⚖️ MIT License

