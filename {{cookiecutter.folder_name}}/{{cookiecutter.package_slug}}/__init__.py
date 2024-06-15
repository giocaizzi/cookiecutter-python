"""{{cookiecutter.package_slug}}"""
{% if cookiecutter.package_specs == "setup.py" %}
__author__ = "{{cookiecutter.author_name}}"
__email__ = "{{cookiecutter.author_email}}"
__license__ = "{{cookiecutter.license}}"
__copyright__ = "Copyright (c) {% now 'utc', '%Y' %} {{cookiecutter.author_name}}"
__url__ = (
    "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug}}"
)
__version__ = "{{cookiecutter.version}}"
{% endif %}
__all__ = []
