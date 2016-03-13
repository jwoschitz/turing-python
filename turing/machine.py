# -*- coding: utf-8 -*-

from __future__ import print_function

from turing.tape import Tape, TapeMotion
from turing.transition import TransitionTable, Transition


class UniversalTuringMachine(object):
    def __init__(self,
                 initial_state=None,
                 accepting_states=[],
                 blank_symbol=None,
                 tape_data="",
                 transition_data=[]):
        self._current_state = initial_state
        self._accepting_states = accepting_states
        self._tape = Tape(tape_data, blank_symbol)
        self._transitions = TransitionTable()
        for transition_string in transition_data:
            self._transitions.add_transition(Transition.from_data_string(transition_string))

    def run(self):
        while not self._current_state in self._accepting_states:
            symbol_at_head = self._tape.read_from_current_position()
            transition = self._transitions.get_transition_for(self._current_state, symbol_at_head)
            self._tape.write_to_current_position(transition.symbol_next)
            if transition.tape_motion == TapeMotion.RIGHT:
                self._tape.right()
            elif transition.tape_motion == TapeMotion.LEFT:
                self._tape.left()
            self._current_state = transition.state_next
        return self._tape
