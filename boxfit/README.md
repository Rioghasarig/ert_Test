# Box Fitting Algorithm

This python script implements a box fitting algorithm which attempts to fit a
given list of packages into a container of given dimensions in such a way that
maximizes the percentage of the volume of the container used.

It is a brute-force approach that searches through all possible positions of
the container for position it can fit. The packages are sorted by volume
beforehand to help maximize the volume of the container used