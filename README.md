liggghts-utils
==============

Various utilities for post-processing LIGGGHTS (www.liggghts.com) data files.

# dump2force

This python tool reads LIGGGHTS (http://www.liggghts.com) local dump files containing particle contact data and produces a VTK file for visualising contact chains and networks.

The visualisation is done simply by connecting the centres of particles in contact with a VTKLine which is coloured by the magnitude of the force. ParaView can be used to render this with tubes whose thickness is proportional to force if required.

PyEVTK is currently required to generate binary VTK files: https://bitbucket.org/pauloh/pyevtk

Future versions will fall back to a basic ASCII VTK file if this PyEVTK is not found.

The pizza.py bdump command is used to handle LIGGGHTS dump files and therefore PYTHONPATH must include the pizza/src location.

NOTE: bdump is NOT included in granular pizza, and should be taken from the standard LAMMPS pizza package!

NOTE: it is impossible to tell from the bdump header which values have been requested in the compute, so check that your compute
and dump match the format here - this will be checked in future!
