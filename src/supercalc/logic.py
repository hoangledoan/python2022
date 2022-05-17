# Copyright 2022  Projektpraktikum Python.
# SPDX-License-Identifier: Apache-2.0
"""Calculator logic."""

Stack = list[float | str]


class SupercalcExitError(Exception):
    """Signal that the processing is to be aborted."""


def add(left: float, right: float) -> float:
    """Add two operands.

    Args:
        left: First operand.
        right: Second operand.

    Returns:
        Sum of both operands.

    """
    return left + right


def process_last(stack: Stack) -> tuple[Stack, float | None]:
    """Check if the last item of the stack is a operator and execute.

    Args:
        stack: Current tokens.

    Returns:
        A tuple of the new stack and calculation result

    Raises:
        SupercalcExitError: If the quit operand is found.

    Note:
        The currently supported operands are:
            q: Quit the calculation.
            +: Calculate the sum.

    """
    if not stack or isinstance(stack[-1], float):
        return stack, None

    newstack = stack[:]
    operator = newstack.pop()
    if operator == 'q':
        raise SupercalcExitError

    right = newstack.pop()
    left = newstack.pop()

    assert operator == '+'
    assert isinstance(left, float)
    assert isinstance(right, float)

    value = add(left, right)
    newstack.append(value)

    return newstack, value
