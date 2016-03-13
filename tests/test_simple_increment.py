# -*- coding: utf-8 -*-

from .context import turing
from turing.machine import UniversalTuringMachine

import unittest


class SimpleIncrementTest(unittest.TestCase):
    """Naive increment"""

    def test_absolute_truth_and_meaning(self):
        utm = UniversalTuringMachine(
            initial_state="q0",
            accepting_states=["qf"],
            tape_data="111",
            blank_symbol="B",
            transition_data=[
                "q0 1 q0 1 R",
                "q0 B qf 1 N",
            ]
        )
        tape_on_halt = utm.run()
        self.assertEquals(str(tape_on_halt), "1111")

if __name__ == '__main__':
    unittest.main()
