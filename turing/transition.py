# -*- coding: utf-8 -*-
from turing.tape import TapeMotion


class TransitionNotFoundError(Exception):
    pass


class TransitionParseError(Exception):
    pass


class Transition(object):
    def __init__(self, state_current, symbol_current, state_next, symbol_next, tape_motion):
        self.expected_state_symbol_pair = (state_current, symbol_current)
        self.state_next = state_next
        self.symbol_next = symbol_next
        self.tape_motion = tape_motion

    @staticmethod
    def from_data_string(transition_as_string):
        splitted = transition_as_string.split()
        if len(splitted) != 5:
            raise TransitionParseError("Transition '{}' has incorrect number of arguments".format(transition_as_string))
        if not TapeMotion.is_valid(splitted[4]):
            raise TransitionParseError(
                "Transition '{}' has invalid tape motion '{}'".format(transition_as_string, splitted[4]))
        return Transition(splitted[0], splitted[1], splitted[2], splitted[3], splitted[4])


class TransitionTable(object):
    def __init__(self):
        self._transitions = {}

    def add_transition(self, transition):
        self._transitions[transition.expected_state_symbol_pair] = transition

    def get_transition_for(self, state_current, symbol_current):
        current_state_symbol_pair = (state_current, symbol_current)
        if current_state_symbol_pair in self._transitions:
            return self._transitions[current_state_symbol_pair]
        raise TransitionNotFoundError(
            "No transition found for state {} and symbol {}".format(state_current, symbol_current))