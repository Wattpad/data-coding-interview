import pytest
import os.path

from pathlib import Path


@pytest.fixture
def test_files_path() -> Path:
    """Returns a Path to the test_files directory."""
    return Path(os.path.dirname(__file__)) / "test_files"
