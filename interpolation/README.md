# 2D Interpolation


Continains code to compute the 2D interpolation of the example data provided. Simply execute with `python interp2d.py`.

Given a function f: R^2->R and a list of pointx x_1,...,x_n in R^2 and values z_1,...,z_n in R such that f(x_i) = z_i we compute a linear interpolation F that satisfies F(x_i) = z_i. F is computed as a linear combination F(x_i) = Sum_i a_i phi_(x) of functions of the form phi_i(x) = |x-x_i|. 