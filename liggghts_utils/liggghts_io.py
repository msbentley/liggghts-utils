#!/usr/bin/python
"""
A set of routines to read and manipulate LIGGGHTS output files
"""

import pandas as pd

local_cols = [
    'pos1_x', 'pos1_y', 'pos1_z', 'pos2_x', 'pos2_y', 'pos2_z',
    'vel_x', 'vel_y', 'vel_z',
    'id_1', 'id_2', 'periodic',
    'f_x', 'f_y', 'f_z',
    'f_normal', 'f_tangential',
    'torque', 'history', 'contactArea', 'heatFlux', 'contactPointq']


def read_local(filename, cols=local_cols):
    """Reads an ASCII LIGGGHTS dump file produced from a computer/gran/local.
    Returns as a pandas DataFrame"""

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
    data = pd.read_table(filename, skiprows=skiplines, delim_whitespace=True, header=None)

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
    startline = []

    start = 'ITEM: ATOMS'
    time = 'ITEM: TIMESTEP'

    lines = f.readlines()  # all in one go

    for idx, line in enumerate(lines):
        if line.startswith(time):
            timesteps.append(int(lines[idx+1].strip()))
            startline.append(idx+1)
        elif line.startswith(start):
            skiplines.append(idx+1)
            cols = line.split(start)[1].split()

    if len(timesteps) == 0:
        print('LIGGGHTS ASCII dump file not recognised')
        return None

    f.close()

    data = []
    for idx, skip in enumerate(skiplines):

        if idx < (len(skiplines) - 1):
            # nrows = skiplines[idx + 1] - skiplines[idx] - startline[0]-1
            nrows = startline[idx+1] - skiplines[idx] - 1
        else:
            nrows = len(lines) - skip
        data.append(pd.read_table(filename, skiprows=skip, delim_whitespace=True, header=None, names=cols, nrows=nrows))

    return timesteps, data


def vtk_to_csv(in_file, out_file):

    data = read_vtk(in_file)
    data.to_csv(out_file, index=False)

    return


def read_vtk(filename):
    """Reads a VTK file output from LIGGGHTS and loads the data into 
    a Pandas DataFrame"""

    # import vtk
    # 
    # reader = vtk.vtkPolyDataReader()
    # reader.SetFileName(filename)
    # reader.ReadAllScalarsOn()
    # reader.Update()
    # vtkdata = reader.GetOutput()
    # pointData = vtkdata.GetPointData()
    # scalar_names = [reader.GetScalarsNameInFile(i) for i in range(0, reader.GetNumberOfScalarsInFile())]
    # print(scalar_names)

    flatten = lambda l: [item for sublist in l for item in sublist]

    import pyevtk
    import pandas as pd
    import numpy as np

    data = pyevtk.VtkData(filename)
    coords = np.array(data.structure.points)
    field = data.point_data.data[0]
    cols = field.data.keys()

    if coords.shape[1] == 2:
        coord_cols = ['x', 'y']
    elif coords.shape[1] == 3:
        coord_cols = ['x', 'y', 'z']
    else:
        print("ERROR: can only process 2D or 3D data")
        return None

    cols = coord_cols + cols
    skipped = []
    data = pd.DataFrame([], columns=cols)


    for col in cols:
        if col == 'x':
            col_vals = np.array(coords[:,0])
        elif col == 'y':
            col_vals = np.array(coords[:,1])
        elif col == 'z':
            col_vals = np.array(coords[:,2])
        else:
            if len(field.data[col][0]) > 1:
                print("WARNING: skipping vector value %s" % col)
                skipped.append(col)
                continue
            col_vals = np.array(flatten(field.data[col]))
            
        data[col] = col_vals
    data.dropna(axis=1, inplace=True)
    data.sort_values(by='id', inplace=True)

    return data
    
    

def nat_sort(l):
    """Performs a natural sort of a list of strings. This is particularly
    useful for LIGGGHTS filenames!"""

    from re import compile, split    
    dre = compile(r'(\d+)')
    l.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in split(dre, l)])

    return