# Copyright 2022  Projektpraktikum Python.
# SPDX-License-Identifier: Apache-2.0
"""Calculator cli."""

from __future__ import annotations

from contextlib import suppress
from typing import TYPE_CHECKING

from .logic import SupercalcExitError, process_last

if TYPE_CHECKING:
    from .logic import Stack


def main() -> float | None:
    """Interact with user on the cli."""
    stack: Stack = []
    value: float | None = None
    while True:
        token: str | float = input('Token: ').strip()
        if not token:
            continue

        with suppress(ValueError):
            token = float(token)
        stack.append(token)

        try:
            stack, value = process_last(stack)
        except SupercalcExitError:
            return value

        print(f'Stack: {stack!r}')
        if value is not None:
            print(f'Result: {value!r}')
