"""test template"""

import pytest

from tests.conftest import RECIPES, RECIPE

# ------------------------------
# README
# ------------------------------
# All these tests are parametrized with RECIPES
# which is a list of dictionaries that represent
# different combinations of choices that can be made
# when baking the template.
# If the key is not present in the dictionary
# the default value is used.

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
    # license
    assert result.project_path.joinpath("LICENSE.md").is_file()
    # readme
    assert result.project_path.joinpath("README.md").is_file()
    # gitignore
    assert result.project_path.joinpath(".gitignore").is_file()


# ---- Test default folders----
def test_composition_of_default_folders(bake):
    """test default composition of folders

    All features are enabled by default
    """
    result = bake()
    # pyproject.toml is a default file
    assert result.project_path.joinpath("pyproject.toml").is_file()
    # docs is not a default folder
    assert result.project_path.joinpath("docsrc").is_dir()
    # workflows are a default folder
    assert result.project_path.joinpath(".github/workflows").is_dir()


# ---- test package_specs choice ----
@pytest.mark.parametrize("recipe", RECIPES)
def test_package_specs_choice(bake, recipe):
    result = bake(recipe)
    print(recipe)
    # if default (not specified)
    if "package_specs" not in recipe:
        # default is pyproject.toml
        assert result.project_path.joinpath("pyproject.toml").is_file()
    # else if specified
    else:
        if recipe["package_specs"] == "pyproject.toml":
            # pyproject.toml is there
            assert result.project_path.joinpath("pyproject.toml").is_file()
            # not required
            assert not result.project_path.joinpath("setup.py").is_file()
        elif recipe["package_specs"] == "setup.py":
            # required
            assert result.project_path.joinpath("setup.py").is_file()
            # not required
            assert not result.project_path.joinpath("pyproject.toml").is_file()


@pytest.mark.parametrize("recipe", RECIPES)
def test_setup_docs_choice(bake, recipe):
    result = bake(recipe)
    # if default (not specified)
    if "setup_docs" not in recipe:
        # docs is a default folder
        assert result.project_path.joinpath("docsrc").is_dir()
    # else if specified
    else:
        if recipe["setup_docs"] == "true":
            assert result.project_path.joinpath("docsrc").is_dir()
        elif recipe["setup_docs"] == "false":
            assert not result.project_path.joinpath("docsrc").is_dir()


@pytest.mark.parametrize("recipe", RECIPES)
def test_setup_workflows_choice(bake, recipe):
    result = bake(recipe)
    # if default (not specified)
    if "setup_workflows" not in recipe:
        # workflows are a default folder
        assert result.project_path.joinpath(".github/workflows").is_dir()
    # else if specified
    else:
        if recipe["setup_workflows"] == "true":
            # workflows are a default folder
            assert result.project_path.joinpath(".github/workflows").is_dir()
        elif recipe["setup_workflows"] == "false":
            # workflows are not a default folder
            assert not result.project_path.joinpath(".github/workflows").is_dir()
