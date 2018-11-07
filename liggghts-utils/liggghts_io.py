#!/usr/bin/python
"""
A set of routines to read and manipulate LIGGGHTS output files
"""

import pandas as pd
import os

local_cols = ['pos1_x', 'pos1_y', 'pos1_z', 'pos2_x', 'pos2_y', 'pos2_z',
    'vel_x', 'vel_y', 'vel_z',
    'id_1', 'id_2', 'periodic',
    'f_x', 'f_y', 'f_z',
    'f_normal', 'f_tangential',
     'torque', 'history', 'contactArea', 'heatFlux', 'contactPointq']

def read_local(filename, cols=local_cols):
    """Reads an ASCII LIGGGHTS dump file produced from a computer/gran/local And
    returns as a pandas DataFrame"""

    # if the file exists, read some header info, find the length of the header
    # and use this to read all subsequent data.

    try:
        f = open(filename)
    except IOError:
        print('Cannot open file %s' % filename)
        return None

    skiplines = 0

    for idx, line in enumerate(f.readlines()):
        if line.startswith('ITEM: ENTRIES'):
            skiplines = idx+1
            break

    if skiplines == 0:
        print('LIGGGHTS ASCII dump file not recognised')
        return None

    f.close()
    data = pd.read_table(filename, skiprows=skiplines, delim_whitespace=True, header=None )

    if len(data.columns) != len(cols):
        print('Warning: %d columns read from file and %d specified. Not labelling!' % (len(data.columns), len(cols)))
    else:
        data.columns = cols

    return data


def read_dump(filename):
    """Reads an ASCII LIGGGHTS dump file into a pandas DataFrame. The file is first indexed
    to find the timesteps contained, and each timestep is then read into a pandas DataFrame."""

    try:
        f = open(filename)
    except IOError:
        print('Cannot open file %s' % filename)
        return None

    timesteps = []
    skiplines = []

    start = 'ITEM: ATOMS'
    time = 'ITEM: TIMESTEP'

    lines = f.readlines() # all in one go

    for idx, line in enumerate(lines):
        if line.startswith(time):
            timesteps.append(int(lines[idx+1].strip()))
        elif line.startswith(start):
            skiplines.append(idx+1)
            cols = line.split(start)[1].split()

    if len(timesteps) == 0:
        print('LIGGGHTS ASCII dump file not recognised')
        return None

    f.close()

    data = []
    for idx, skip in enumerate(skiplines):
        nrows = skiplines[idx+1]-skiplines[idx] if idx<(len(skiplines)-1) else len(lines)-skip
        data.append(pd.read_table(filename, skiprows=skip, delim_whitespace=True, header=None, names=cols, nrows=nrows ))
    # use nrows to get each timestep

    return timesteps, data
