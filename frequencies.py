"""Frequencies function."""
import itertools

def frequencies(items):
    frequencies = {}
    groups = []
    for k,g in itertools.groupby(sorted([str(x) for x in items])):
        groups.append(list(g))
    keys = [k for k, g in itertools.groupby(sorted([str(x) for x in items]))]
    frequencies = {x[0]: len(x[1]) for x in zip(keys, groups)}
    # note that frequencies = {x[0]: len(x) for x in groups works just the same}
    return frequencies
