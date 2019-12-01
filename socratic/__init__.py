# -*- coding: utf-8 -*-
#
# Socratic - very simple question-answer dialogue system based on python generators.
#
# Daniil Volynkin
# foxezzz@gmail.com
#
# License: MIT
#
from .__version__ import (
    __title__,
    __license__,
    __version__,
    __author__,
    __contact__,
    __url__,
    __description__,
)

from .dialogue import Dialogue

__all__ = [
    Dialogue,
    __title__,
    __license__,
    __version__,
    __author__,
    __contact__,
    __url__,
    __description__,
]
