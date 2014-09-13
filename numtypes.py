#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Expresses differences between integer, fraction, and decimal number types.
'''

import decimal
import fractions
FLOATVAR = 0.1
DECIMALVAR = decimal.Decimal('0.1')
FRACTIONVAR = fractions.Fraction(1, 10)
DF_EQUALITY = DECIMALVAR == FRACTIONVAR
ARE_INEQUAL = FLOATVAR != DECIMALVAR != FRACTIONVAR
