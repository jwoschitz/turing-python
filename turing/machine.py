# -*- coding: utf-8 -*-

from __future__ import print_function


class TapeMotion(object):
    LEFT = "L"
    RIGHT = "R"
    STAY = "N"

    @staticmethod
    def is_valid(char):
        return char in [TapeMotion.LEFT, TapeMotion.RIGHT, TapeMotion.STAY]


class Tape(object):
    def __init__(self, input, blank_symbol):
        self._blank_symbol = blank_symbol
        self._tape = {}
        self._position = 0
        for index, item in enumerate(input):
            self._tape[index] = item

    def left(self):
        self._position -= 1

    def right(self):
        self._position += 1

    def read_from_current_position(self):
        if self._position in self._tape:
            return self._tape[self._position]
        return self._blank_symbol

    def write_to_current_position(self, value):
        self._tape[self._position] = value

    def __str__(self):
        str = ""
        for value in self._tape.values():
            str += value
        return str


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
