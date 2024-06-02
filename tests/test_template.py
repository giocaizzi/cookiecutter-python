"""test template"""

import pytest

from .conftest import RECIPE, RECIPES


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
# NAMING
# ------------------------------
# test package_slug with respect 
# to naming conventions regarding "-" and "_" and " "
# in python package names
# controlled in cookiecutter.json
WRONG_NAMING_RECIPES = [
    # recipe, expected folder name, expected slug
    ({**RECIPE, "name": "py prova"}, "py-prova", "py_prova"),
    ({**RECIPE, "name": "py_prova"}, "py-prova", "py_prova"),
]

@pytest.mark.parametrize("recipe, expected_folder, expected_slug", WRONG_NAMING_RECIPES)
def test_package_slug(bake, recipe, expected_folder, expected_slug):
    result = bake(recipe)
    assert result.project_path.name == expected_folder
    assert (result.project_path / expected_slug).is_dir()


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


# ---- Test default folders ----
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
