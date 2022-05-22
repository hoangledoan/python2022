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


def sub(left: float, right: float) -> float:
    """Subtract one operand from one operand.

    Args:
        left: Minuend.
        right: Subtrahend.

    Returns:
        Difference between 2 operands.

    """
    return left - right


def mul(left: float, right: float) -> float:
    """Multiply two operands.

    Args:
        left:  Multiplier.
        right: Multiplicand.

    Returns:
        Product of both operands.

    """
    return left * right


def div(left: float, right: float) -> float | bool:
    """Divide a operand by a operand.

    Args:
        left:  Numerator.
        right: Denominator.

    Returns:
        A natural Quotient, followed behind the dot with a remainder.
        If the Denominator(right) = 0, it will return False.

    """
    if right:
        return left / right
    return False


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
            -: Calculate the subtraction
            *: Calculate the multiplcation
            /: Calculate the division

    """
    if not stack or isinstance(stack[-1], float):
        return stack, None

    newstack = stack[:]
    operator = newstack.pop()
    if operator == 'q':
        raise SupercalcExitError

    right = newstack.pop()
    left = newstack.pop()

    if operator == '+':
        assert isinstance(left, float)
        assert isinstance(right, float)
        value = add(left, right)
        newstack.append(value)

    if operator == '-':
        assert isinstance(left, float)
        assert isinstance(right, float)
        value = sub(left, right)
        newstack.append(value)

    if operator == '*':
        assert isinstance(left, float)
        assert isinstance(right, float)
        value = mul(left, right)
        newstack.append(value)

    if operator == '/':
        assert isinstance(left, float)
        assert isinstance(right, float)
        value = div(left, right)
        newstack.append(value)

    if operator == 'x':
        assert isinstance(left, float)
        assert isinstance(right, float)
        newstack.append(right)
        newstack.append(left)

    return newstack, value
