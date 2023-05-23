#!/usr/bin/env python3
import pytest

from os import path
import runpy
import io
import sys
from app import *

class TestAppPy:
    '''app.py'''
    def test_combine_sequences(self):
        '''combine_sequences() returns a single sequence of the elements of seq1 followed by the elements of seq2.'''
        seq1 = [1, 2, 3]
        seq2 = ['a', 'b', 'c']
        assert(combine_sequences(seq1, seq2) == [1, 2, 3, 'a', 'b', 'c'])

    def test_sequence_n_times(self):
        '''sequence_n_times() returns a single sequence of seq repeated n times.'''
        seq = [7, 14, 21]
        assert(sequence_n_times(seq, 3) == [7, 14, 21, 7, 14, 21, 7, 14, 21])

    def test_average(self):
        '''average() returns the average of the numbers in the input sequence.'''
        seq = [1, 2, 4, 8, 16, 32]
        assert(average(seq) == 10.5)

    def test_append_n_times(self):
        '''append_n_times() returns a list with an element appended n times.'''
        seq = ['f', 'l', 'a', 't', 'i', 'r', 'o', 'n']
        assert(append_n_times(seq, 'a', 4) == ['f', 'l', 'a', 't', 'i', 'r', 'o', 'n', 'a', 'a', 'a', 'a'])