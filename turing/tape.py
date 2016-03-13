# -*- coding: utf-8 -*-


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
