"""
war
War card game written for fun while following the 'Complete Python Developer Certification Course' by Imtiaz Ahmad, on Udemy.
"""

# Add imports here
from card_class import Card
from .deck_class import Deck
from .table_class import Table
from .functions import get_players


# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
