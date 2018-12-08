#!/usr/bin/python3

import sys

def parse_node(segment):
    metadata_count = segment[1]
    offset = 2
    child_values = []
    for i in range(segment[0]):
        more_offset, child_value = parse_node(segment[offset:])
        offset += more_offset
        child_values.append(child_value)
    metadata_values = segment[offset:offset + metadata_count]
    offset += metadata_count

    if child_values:
        node_value = sum([child_values[x-1] for x in metadata_values if x >= 1 and x <= len(child_values)])
    else:
        node_value = sum(metadata_values)

    return offset, node_value

with open(sys.argv[1]) as f:
    print(parse_node([int(x) for x in f.readline().split()])[1])
