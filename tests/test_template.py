"""test template"""

import pytest

# Bake Result
# cookies.bake() returns a result instance with a bunch of fields that hold useful information:

# exit_code: is the exit code of cookiecutter, 0 means successful termination
# exception: is the exception that happened if one did
# project_path: a Path object pointing to the rendered project
# context: is the rendered context


@pytest.fixture
def bake(cookies):
    result = cookies.bake(
        extra_context={
            "package_name": "pyprova",
            "short_description": "This is a prova.",
        }
    )
    return result


def test_build_success(bake):
    result = bake

    # build success
    assert result.exit_code == 0
    assert result.exception is None


def test_folder_structure(bake):
    result = bake

    # folder structuree
    assert result.project_path.name == "pyprova"
    assert result.project_path.is_dir()
