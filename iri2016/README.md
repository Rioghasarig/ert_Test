# IRI 2016

## Description
The International Reference Ionosphere is a project aimed at producing an empirical standard model of the ionosphere based. For given location, time and data IRI provides various statistics about the ionosphere, such as electron density and temperature. This repository provides a command line interface for accessing this electron density data. 

## Instructions

 1. Compile the program run 'make'. This compiles both the shared library libiri.so and the C interface run-iri.
 2. Move the shared library libiri.so to a folder in the LD_LIBRARY_PATH so the shared library can be found. 
 3. Execute the run-iri program and input the parameters to produce the edp.dat file containing the
    electron density table
 4. Run gnuplot make_plot.gp to produce the plot as a pdf file
