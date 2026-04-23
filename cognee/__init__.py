"""
Cognee - A knowledge graph and memory layer for AI applications.

This package provides tools for building, querying, and managing
knowledge graphs powered by LLMs.
"""

from cognee.api.v1.add import add
from cognee.api.v1.cognify import cognify
from cognee.api.v1.search import search
from cognee.api.v1.prune import prune
from cognee.api.v1.config import config

__version__ = "0.1.0"
__author__ = "Cognee Contributors"

__all__ = [
    "add",
    "cognify",
    "search",
    "prune",
    "config",
    "__version__",
]
