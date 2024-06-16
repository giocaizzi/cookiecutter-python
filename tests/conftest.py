import pytest
from pytest_cookies.plugin import Result

# ---- RECIPES ----
# minimal recipe
RECIPE = {}
RECIPE.update(
    {
        "name": "py prova",
        "short_description": "This is a prova.",
    }
)

# TODO: exahustive combination of choices
RECIPES = [
    RECIPE,
    {**RECIPE, "package_specs": "pyproject.toml"},
    {**RECIPE, "package_specs": "setup.py"},
    {**RECIPE, "setup_docs": "true"},
    {**RECIPE, "setup_docs": "false"},
    {**RECIPE, "setup_workflows": "true"},
    {**RECIPE, "setup_workflows": "false"},
    {**RECIPE, "package_specs": "pyproject.toml", "setup_docs": "true"},
    {**RECIPE, "package_specs": "pyproject.toml", "setup_docs": "false"},
    {**RECIPE, "package_specs": "pyproject.toml", "setup_workflows": "true"},
    {**RECIPE, "package_specs": "pyproject.toml", "setup_workflows": "false"},
    {**RECIPE, "package_specs": "setup.py", "setup_docs": "true"},
    {**RECIPE, "package_specs": "setup.py", "setup_docs": "false"},
    {**RECIPE, "package_specs": "setup.py", "setup_workflows": "true"},
    {**RECIPE, "package_specs": "setup.py", "setup_workflows": "false"},
]


# ---- BAKING ----
# Bake Result
# cookies.bake() returns a result instance with a bunch
# of fields that hold useful information:

# exit_code: is the exit code of cookiecutter, 0 means successful termination
# exception: is the exception that happened if one did
# project_path: a Path object pointing to the rendered project
# context: is the rendered context


@pytest.fixture
def bake(cookies):
    def _bake(extra_context=None) -> Result:
        if extra_context is None:
            # Use default parameters
            extra_context = RECIPE
        cookie = cookies.bake(extra_context=extra_context)
        return cookie

    return _bake
