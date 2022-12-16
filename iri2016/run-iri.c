#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void iri_sub_(int* jf, int* jmag, float* alati, float* along, int* iyyyy,
	      int* mmdd, float* dhour, float* heibeg, float* heiend,
	      float* heistp, float* outf, float* oarr); 

void read_ig_rz_();
void readapf107_();

char* months[] = {"Janurary", "Februrary", "March", "April", "May",
		"June", "July", "August", "September", "October",
		"November", "December"};

int month_days[] = {31, 28, 31, 30, 31, 30, 31, 31, 31, 31, 30, 31};
int main() {
  read_ig_rz_();
  readapf107_();
  int jf[50];

  for(int i = 0; i < 50; i++)
    jf[i] = 1.0;
  int jmag = 0;

  int iyyyy, month, day, mmdd;
  float alati, along, dhour;
  float heibeg, heiend, heistp;

  printf("Year (1958-2020): ");
  scanf("%d", &iyyyy);
  assert(iyyyy>=1958 && iyyyy<=2020);

  printf("Month (1-12): ");
  scanf("%d", &month);
  assert(month>=1 && month <=12);

  printf("Day (1-%d): ", month_days[month-1]);
  scanf("%d", &day);
  assert(day>=1 && day <= month_days[month-1]);  
  mmdd = 100*month + day;

  printf("Latitude (-90.0-90.0): ");
  scanf("%f", &alati);
  assert(alati>=-90.0 && alati<=90.0);
  
  printf("Longitude (0-360): ");
  scanf("%f", &along);
  assert(along>=0 && along<=360.0);


  printf("Hour (0.0-24.0): ");
  scanf("%f", &dhour);
  assert(dhour>=0 && dhour<=24.0);

  printf("Altitude Min (60.0-200.0): ");
  scanf("%f", &heibeg);
  assert(heibeg>=60.0 && heibeg<=200.0);
  

  printf("Altitude Max (%.2f-200.0): ", heibeg);
  scanf("%f", &heiend);
  assert(heiend>=heibeg && heiend<=200.0);
  
  printf("Altitude Step (>0): ");
  scanf("%f", &heistp);
  assert(heistp>0);

  float outf[20000];
  float oarr[100];

  iri_sub_(jf, &jmag, &alati, &along, &iyyyy, &mmdd, &dhour, &heibeg,
	   &heiend, &heistp, outf, oarr); 
  
  FILE* outfile = fopen("edp.dat","w");

  // Output the Title
  fprintf(outfile, "EDP for %s %d, %d at %d UTC\n",
	  months[month-1],
	  day,
	  iyyyy,
	  (int)(dhour*100));
  
  fprintf(outfile,"Altitude        Electron Density\n");

  // Output Data Table
  for(int j = 0; heibeg+j*heistp <= heiend; j++) {
    int r = outf[20*j]/1E6;
    fprintf(outfile, "%10f\t%16d\n", heibeg+j*heistp, r);
  }
  fclose(outfile); 
  return 0;
}
