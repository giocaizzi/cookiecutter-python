"""building"""

import pytest
from .conftest import RECIPES

# ------------------------------
# README
# ------------------------------
# All these tests are parametrized with RECIPES
# which is a list of dictionaries that represent
# different combinations of choices that can be made
# when baking the template.
# If the key is not present in the dictionary
# the default value is used


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
