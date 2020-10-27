#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from run import *

@pytest.mark.parametrize(
    ["n_queens", "expected"],
    [
        # Input 1
        (5,[(2, 4, 1, 3), (3, 1, 4, 2)]),
        # Input 2
        (6,[(2, 4, 6, 1, 3, 5), (3, 6, 2, 5, 1, 4), (4, 1, 5, 2, 6, 3), (5, 3, 1, 6, 4, 2)]),
        # Input 3
        (7,[(1, 3, 5, 7, 2, 4, 6), (1, 4, 7, 3, 6, 2, 5), (1, 5, 2, 6, 3, 7, 4), (1, 6, 4, 2, 7, 5, 3), (2, 4, 1, 7, 5, 3, 6), (2, 4, 6, 1, 3, 5, 7), (2, 5, 1, 4, 7, 3, 6), (2, 5, 3, 1, 7, 4, 6), (2, 5, 7, 4, 1, 3, 6), (2, 6, 3, 7, 4, 1, 5), (2, 7, 5, 3, 1, 6, 4), (3, 1, 6, 2, 5, 7, 4), (3, 1, 6, 4, 2, 7, 5), (3, 5, 7, 2, 4, 6, 1), (3, 6, 2, 5, 1, 4, 7), (3, 7, 2, 4, 6, 1, 5), (3, 7, 4, 1, 5, 2, 6), (4, 1, 3, 6, 2, 7, 5), (4, 1, 5, 2, 6, 3, 7), (4, 2, 7, 5, 3, 1, 6), (4, 6, 1, 3, 5, 7, 2), (4, 7, 3, 6, 2, 5, 1), (4, 7, 5, 2, 6, 1, 3), (5, 1, 4, 7, 3, 6, 2), (5, 1, 6, 4, 2, 7, 3), (5, 2, 6, 3, 7, 4, 1), (5, 3, 1, 6, 4, 2, 7), (5, 7, 2, 4, 6, 1, 3), (5, 7, 2, 6, 3, 1, 4), (6, 1, 3, 5, 7, 2, 4), (6, 2, 5, 1, 4, 7, 3), (6, 3, 1, 4, 7, 5, 2), (6, 3, 5, 7, 1, 4, 2), (6, 3, 7, 4, 1, 5, 2), (6, 4, 2, 7, 5, 3, 1), (6, 4, 7, 1, 3, 5, 2), (7, 2, 4, 6, 1, 3, 5), (7, 3, 6, 2, 5, 1, 4), (7, 4, 1, 5, 2, 6, 3), (7, 5, 3, 1, 6, 4, 2)]),
    ],
)

def test_check_n_queens(n_queens, expected):
    actual = check_n_queens(n_queens)
    assert actual == expected
