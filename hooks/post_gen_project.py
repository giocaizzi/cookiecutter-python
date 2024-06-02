import os
import shutil


# https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html#example-conditional-files-directories#conditional-file/directory-removal
REMOVE_PATHS = [
    '{% if cookiecutter.setup_workflows != "true" %}./.github/workflows{% endif %}',
    '{% if cookiecutter.setup_docs != "true" %}./docsrc{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)
