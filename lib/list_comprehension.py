#!/usr/bin/env python3


def return_evens(num_list):
    evens_list = [n for n in num_list if n % 2 == 0]
    return evens_list if evens_list else []
    pass


def make_exclamation(sentence_list):
    new_list = [s + "!" for s in sentence_list]
    return new_list
    pass
