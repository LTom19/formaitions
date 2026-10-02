"""Formes connues des généraux. Le simulateur ne les importe pas."""

from enum import Enum


class Shape(Enum):
    CIRCLE = "circle"
    LINE = "line"
    BLOCK_DENSE = "block_dense"
    BLOCK_LOOSE = "block_loose"
