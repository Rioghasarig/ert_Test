set terminal pdf
set output "plot.pdf"
set title system("head -1 edp.dat")
set xlabel "Electron Density (cm^{-3})"
set ylabel "Altitude (km)"
plot "edp.dat" using 2:1 with lines notitle