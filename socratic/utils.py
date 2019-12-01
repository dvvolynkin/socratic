# -*- coding: utf-8 -*-
#
# Socratic - very simple question-answer dialogue system based on python generators.
#
# Daniil Volynkin
# foxezzz@gmail.com
#
# License: MIT
#


def generator_start_wrapper(generator):
    """
    Need for using generator.send() for first message instead next(generator).
    """
    yield

    yield from generator
