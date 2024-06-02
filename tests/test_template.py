"""test template"""

import pytest

from tests.conftest import RECIPE, RECIPES

# Bake Result
# cookies.bake() returns a result instance with a bunch of fields that hold useful information:

# exit_code: is the exit code of cookiecutter, 0 means successful termination
# exception: is the exception that happened if one did
# project_path: a Path object pointing to the rendered project
# context: is the rendered context


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

# ------------------------------
# FOLDER STRUCTURE
# ------------------------------
# ---- Test minimum project structure ----
@pytest.mark.parametrize("recipe", RECIPES)
def test_minimum_folder_structure(bake, recipe):
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


def test_default_folders(bake):
    result = bake()
    # docs is not a default folder
    assert not result.project_path.joinpath("docsrc").is_dir()
    # workflows are a default folder
    assert result.project_path.joinpath(".github/workflows").is_dir()


# ------------------------------
# CHOICESS
# ------------------------------
# ---- Test workflow choice ----
def test_workflow_choice(bake):
    result = bake({**RECIPE, "setup_workflows": "false"})
    assert not result.project_path.joinpath(".github/workflows").is_dir()


# ---- Test docs choice ----
def test_docs_choice(bake):
    result = bake({**RECIPE, "setup_docs": "false"})
    assert not result.project_path.joinpath("docsrc").is_dir()
