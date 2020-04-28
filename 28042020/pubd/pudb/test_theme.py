#!/usr/bin/env python3
'''
'''

from pudb.theme import get_palette

def test_get_palette():
	p = get_palette(True)
	assert len(p) == 90
