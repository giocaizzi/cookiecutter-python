import pytest
from pytest_cookies.plugin import Result

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
    def _bake(extra_context=None)-> Result:
        if extra_context is None:
            # Use default parameters
            extra_context = RECIPE
        cookie = cookies.bake(extra_context=extra_context)
        return cookie

    return _bake


