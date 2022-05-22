# Copyright 2022  Projektpraktikum Python.
# SPDX-License-Identifier: Apache-2.0
"""Cli tests."""

from unittest.mock import patch

from supercalc.cli import main


def test_main_function_processes_inputs() -> None:
    """Test main function processes inputs."""
    with patch('builtins.input', side_effect=['q']):
        res = main()
    assert res is None

    with patch('builtins.input', side_effect=['  ', 'q']):
        res = main()
    assert res is None

    # Operator: '+'
    with patch('builtins.input', side_effect=['4', '5.5', '+', 'q']):
        res = main()
    assert res == 9.5

    with patch('builtins.input', side_effect=['4', '5.5', ' ', '+', 'q']):
        res = main()
    assert res == 9.5

    # Operator: '-'
    with patch('builtins.input', side_effect=['9', '5.5', '-', 'q']):
        res = main()
    assert res == 3.5

    with patch('builtins.input', side_effect=['9', '5.5', ' ', '-', 'q']):
        res = main()
    assert res == 3.5

    # Operator: '*'
    with patch('builtins.input', side_effect=['4', '5', '*', 'q']):
        res = main()
    assert res == 20

    with patch('builtins.input', side_effect=['4', '5', ' ', '*', 'q']):
        res = main()
    assert res == 20

    # Operator: '/'
    with patch('builtins.input', side_effect=['9', '3', '/', 'q']):
        res = main()
    assert res == 3

    with patch('builtins.input', side_effect=['9', '3', ' ', '/', 'q']):
        res = main()
    assert res == 3

    # Operator: 'x'
    with patch('builtins.input', side_effect=['9', '3', '5', 'x', 'q']):
        res = main()
    assert res == ['9', '5', '3']

    with patch('builtins.input', side_effect=['9', '3', ' ', '5', 'x', 'q']):
        res = main()
    assert res == ['9', '3', '5', '']
