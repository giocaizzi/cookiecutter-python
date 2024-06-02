"""test template"""

import pytest
from pytest_cookies.plugin import Result

# Bake Result
# cookies.bake() returns a result instance with a bunch of fields that hold useful information:

# exit_code: is the exit code of cookiecutter, 0 means successful termination
# exception: is the exception that happened if one did
# project_path: a Path object pointing to the rendered project
# context: is the rendered context

RECIPE = {
    "package_name": "pyprova",
    "short_description": "This is a prova.",
}

RECIPES = (
    None,
    RECIPE,
    {**RECIPE, "setup_workflows": "false"},
)


@pytest.fixture
def bake(cookies):
    def _bake(extra_context=None):
        if extra_context is None:
            # Use default parameters
            extra_context = RECIPE
        cookie = cookies.bake(extra_context=extra_context)
        return cookie

    return _bake


# ---- Test success of recepies ----
@pytest.mark.parametrize(
    "recipe",
    RECIPES,
)
def test_build_success(bake, recipe):
    """test that the recipes build successfully"""
    result = bake(recipe)

    # build success
    assert result.exit_code == 0
    assert result.exception is None


# ---- Test project structure ----
@pytest.mark.parametrize("recipe", RECIPES)
def test_folder_structure(bake, recipe):
    """test folder stru"""
    result = bake(recipe)

    # folder structuree
    assert result.project_path.name == "pyprova"
    assert result.project_path.is_dir()

    # license
    assert result.project_path.joinpath("LICENSE.md").is_file()
    # readme
    assert result.project_path.joinpath("README.md").is_file()
    # gitignore
    assert result.project_path.joinpath(".gitignore").is_file()
    # # workflows
    # assert result.project_path.joinpath(".github.is_dir()")
    # assert result.project_path.joinpath(".github/workflows").is_dir()


# ---- Test workflow choice ----

@pytest.mark.skip
@pytest.mark.parametrize(
    "recipe",
    [{**RECIPE, "setup_workflows": "false"}]
)
def test_workflow_choice(bake, recipe):
    result = bake(recipe)

    # workflows
    assert not result.project_path.joinpath(".github/workflows").is_dir()
