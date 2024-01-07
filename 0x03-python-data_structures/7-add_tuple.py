#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_a[0] if len(tuple_a) > 0 else 0
    tuple_2 = tuple_a[1] if len(tuple_a) > 1 else 0
    tuple_3 = tuple_b[0] if len(tuple_b) > 0 else 0
    tuple_4 = tuple_b[1] if len(tuple_b) > 1 else 0

    new_tuple = (tuple_1 + tuple_2, tuple_3 + tuple_4)

    return new_tuple
