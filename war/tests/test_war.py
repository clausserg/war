"""
Unit and regression test for the war package.
"""

# Import package, test suite, and other packages as needed
import war
import pytest
import sys

def test_war_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "war" in sys.modules
