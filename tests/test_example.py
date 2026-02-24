"""Example tests for devcontainer_smoke_test."""


def test_example():
    """Example test that always passes."""
    assert True


def test_import():
    """Test that the package can be imported."""
    import devcontainer_smoke_test  # noqa: F401 - renamed to project name by init-workspace.sh

    assert devcontainer_smoke_test.__version__ == "0.1.0"
