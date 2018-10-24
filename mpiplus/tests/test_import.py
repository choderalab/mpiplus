"""
Unit and regression test for the mpiplus package.
"""

# Import package, test suite, and other packages as needed
import mpiplus
import pytest
import sys

def test_mpiplus_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mpiplus" in sys.modules
