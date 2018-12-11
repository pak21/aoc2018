#!/usr/bin/python3

import sys

def parse_node(segment):
    metadata_count = segment[1]
    offset = 2
    metadata_sum = 0
    for i in range(segment[0]):
        more_offset, more_sum = parse_node(segment[offset:])
        offset += more_offset
        metadata_sum += more_sum
    metadata_values = segment[offset:offset + metadata_count]
    offset += metadata_count
    metadata_sum += sum(metadata_values)

    return offset, metadata_sum

with open(sys.argv[1]) as f:
    print(parse_node([int(x) for x in f.readline().split()])[1])
