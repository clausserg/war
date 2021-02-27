"""
war
War card game written for fun while following the 'Complete Python Developer Certification Course' by Imtiaz Ahmad, on Udemy.
"""

# Add imports here
from .war import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
