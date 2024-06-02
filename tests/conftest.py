import pytest
from pytest_cookies.plugin import Result

RECIPE = {
    "name": "pyprova",
    "short_description": "This is a prova.",
}

RECIPES = (
    None,
    RECIPE,
    {**RECIPE, "setup_workflows": "false"},
)

# Bake Result
# cookies.bake() returns a result instance with a bunch of fields that hold useful information:

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
