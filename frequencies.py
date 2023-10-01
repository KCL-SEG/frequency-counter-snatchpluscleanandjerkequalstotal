"""Frequencies function."""
import itertools

def frequencies(items):
    frequencies = {}
    keys = [] # the keys of the dictionary
    groups = [] # this will be a list of lists where each list is the elements grouped by string value
    # convert everything to strings and then sort them for the grouping stage
    for k,g in itertools.groupby(sorted([str(x) for x in items])):
        keys.append(k)
        groups.append(list(g)) # g is an iterable, hence why we need to call list()
    frequencies = {x[0]: len(x[1]) for x in zip(keys, groups)}
    # note that frequencies = {x[0]: len(x) for x in groups works just the same}
    return frequencies
