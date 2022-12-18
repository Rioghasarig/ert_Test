#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897
#define EARTH_RADIUS 6371000
// Formulas taken from: https://www.movable-type.co.uk/scripts/latlong.html


// Compute the range and bearing from between two GIS coordinates 
void GIS2Radar(double *range_out,
	       double *bearing_out,
	       double glonInit,
	       double glatInit,
	       double glonFinal,
	       double glatFinal) {

  double phiInit = (PI/180)*glatInit;
  double lambdaInit = (PI/180)*glonInit;
  
  double phiFinal = (PI/180)*glatFinal;
  double lambdaFinal = (PI/180)*glonFinal;

  double deltaLambda = lambdaFinal - lambdaInit;

  *range_out = acos(sin(phiInit)*sin(phiFinal) +
		  cos(phiInit)*cos(phiFinal)*cos(deltaLambda))*EARTH_RADIUS;

  *bearing_out = 180/PI*atan2(sin(deltaLambda)*cos(phiFinal),
		       cos(phiInit)*sin(phiFinal) - sin(phiInit)*cos(phiFinal)*cos(deltaLambda));
}


// Compute the result GIS coordinates from a starting coordinates and a range and bearing
void Radar2GIS(double range,
	       double bearing,
	       double glonInit,
	       double glatInit,
	       double *glonFinal,
	       double *glatFinal) {

  double phiInit = (PI/180)*glatInit;
  double lambdaInit = (PI/180)*glonInit;


  double phiFinal = asin(sin(phiInit)*cos(range/EARTH_RADIUS) + cos(phiInit)*sin(range/EARTH_RADIUS)*cos(bearing*PI/180));
  double lambdaFinal = lambdaInit + atan2(sin(bearing*PI/180)*sin(range/EARTH_RADIUS)*cos(phiInit),
				cos(range/EARTH_RADIUS)-sin(phiInit)*sin(phiFinal));

  *glatFinal = (180/PI)*phiFinal;
  *glonFinal = (180/PI)*lambdaFinal;
}


int main() {
  double range;
  double bearing;

  double glatInit = 37;
  double glonInit = -75;

  double glatFinal = 18;
  double glonFinal = -66;
  
  GIS2Radar(&range,&bearing,glonInit,glatInit,glonFinal,glatFinal);
  printf("Range: %f Bearing: %f\n", range, bearing);
  Radar2GIS(range, bearing,  glonInit, glatInit, &glonFinal, &glatFinal);
  printf("Final Latitude: %f Final Longitude: %f\n", glatFinal,glonFinal);

}
