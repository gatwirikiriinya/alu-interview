#!/usr/bin/python3

"""
Rain square program
"""


def rain(walls):

    result = 0
    if len(walls) == 0:
        return 0
    for i in range(1, len(walls) - 1):
        awalls = walls[i]
        bwalls = walls[i]
        for j in range(i):
            awalls = max(awalls, walls[j])
        for j in range(i + 1, len(walls)):
            bwalls = max(bwalls, walls[j])
        result = result + (min(awalls, bwalls) - walls[i])
    return result