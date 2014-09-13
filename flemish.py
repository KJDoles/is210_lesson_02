#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
ONE_FISH = 'Spanish'
TWO_FISH = len(ONE_FISH)
SPANISH_FISHY = FISHY.index(ONE_FISH)
RED_FISH = FISHY[:SPANISH_FISHY]
BLUE_FISH = FISHY[SPANISH_FISHY + TWO_FISH:]
FLEMISH_INQUISITION = RED_FISH + 'Flemish' + BLUE_FISH
