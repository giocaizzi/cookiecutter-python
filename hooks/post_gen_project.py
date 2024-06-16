import os
import shutil

# https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html#example-conditional-files-directories#conditional-file/directory-removal
REMOVE_PATHS = [
    # ---- FEATURES ----
    # workflows
    '{% if cookiecutter.setup_workflows != "true" %}./.github/workflows{% endif %}',
    # docs
    '{% if cookiecutter.setup_docs != "true" %}./docsrc{% endif %}',
    # ---- PYTHON PACKAGING ----
    # if using pyproject.toml
    '{% if cookiecutter.package_specs == "pyproject.toml" %}./setup.py{% endif %}',
    '{% if cookiecutter.package_specs == "pyproject.toml" %}./pytest.ini{% endif %}',
    # if using setup.py
    '{% if cookiecutter.package_specs == "setup.py" %}./pyproject.toml{% endif %}',
]


for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)
