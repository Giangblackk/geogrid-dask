"""Test cases for the __main__ module."""

from geogrid_dask.server import main


def test_inc() -> None:
    """Test increment function."""
    assert main.inc(1) == 2
