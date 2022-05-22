# Copyright 2022  Projektpraktikum Python.
# SPDX-License-Identifier: Apache-2.0
"""Logic tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from supercalc.logic import SupercalcExitError, add, div, mul, process_last, sub

if TYPE_CHECKING:
    from supercalc.logic import Stack


def test_add_calculates_correct_result() -> None:
    """Test add operator calculates correctly."""
    assert add(2, 3) == 5
    assert add(4.5, 5) == 9.5


def test_sub_calculates_correct_result() -> None:
    """Test sub operator calculates correctly."""
    assert sub(7, 5) == 2
    assert sub(12.5, 5.5) == 7


def test_mul_calculates_correct_result() -> None:
    """Test mul operator calculates correctly."""
    assert mul(7, 5) == 35
    assert mul(12.5, 5.5) == 68.75


def test_div_calculates_correct_result() -> None:
    """Test sub operator calculates correctly."""
    assert div(7, 5) == 1.4
    assert div(35, 5) == 7
    assert div(5, 0) is False


def test_process_last_ignores_empty_stack() -> None:
    """Test process_last does not change empty stack."""
    stack: Stack = []
    newstack, value = process_last(stack)
    assert newstack is stack
    assert not newstack
    assert value is None


def test_process_last_ignores_float_top() -> None:
    """Test process_last does not stack if top element is a float."""
    stack: Stack = [4.5]
    newstack, value = process_last(stack)
    assert newstack is stack
    assert newstack == [4.5]
    assert value is None


def test_process_last_executes_quit_operation() -> None:
    """Test process_last executes quit operation."""
    stack: Stack = ['q']
    with pytest.raises(SupercalcExitError):
        process_last(stack)


def test_process_last_executes_add_operation() -> None:
    """Test process_last executes add operation."""
    stack: Stack = [4.5, 5., '+']
    newstack, value = process_last(stack)
    assert newstack is not stack
    assert newstack == [9.5]
    assert value == 9.5


def test_process_last_executes_sub_operation() -> None:
    """Test process_last executes sub operation."""
    stack: Stack = [4.5, 5., '-']
    newstack, value = process_last(stack)
    assert newstack is not stack
    assert newstack == [-0.5]
    assert value == -0.5


def test_process_last_executes_mul_operation() -> None:
    """Test process_last executes mul operation."""
    stack: Stack = [2., 3., '*']
    newstack, value = process_last(stack)
    assert newstack is not stack
    assert newstack == [6.]
    assert value == 6.


def test_process_last_executes_div_operation() -> None:
    """Test process_last executes sub operation."""
    stack: Stack = [6., 3., '/']
    newstack, value = process_last(stack)
    assert newstack is not stack
    assert newstack == [2.]
    assert value == 2.


def test_process_last_executes_x_operation() -> None:
    """Test process_last executes sub operation."""
    stack: Stack = [6., 3., 4., 5., 'x']
    newstack, value = process_last(stack)
    assert newstack is not stack
    assert newstack == [6., 3., 5., 4.]
    assert value is None
