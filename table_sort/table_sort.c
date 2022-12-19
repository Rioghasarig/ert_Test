#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct table_entry {

  int year;
  int month;
  int day;
  
  int ddd;
  int hour;
  int minute;
  int second;
  int c_score;
  
  float foF2;
  float foF1;
  float foE;
  float foEs;
  float hEs;
  float hmF2;
  float hmF1;
  float hmE;
  float b0;
  float b1;
} table_entry;

// Read in a float while taking into account the possibility that
// it is omitted (set equal to '---')

float str_to_float(char* float_str)
{

  if(strcmp(float_str,"---") == 0) {
    return NAN;
  } else {
    return atof(float_str);
  }

}

void float_to_str(float value, char* str) {
  if (isnan(value)) {
    strcpy(str, "---");
  } else {
    sprintf(str, "%.3f", value);
  }
}

void read_line(table_entry* entry, char* line)
{

  char foF2[20], foF1[20], foE[20];
  char foEs[20], hEs[20], hmF2[20];
  char hmF1[20], hmE[20], b0[20];
  char b1[20];
  sscanf(line, "%d.%d.%d (%d) %d:%d:%d %d %s %s %s %s %s %s %s %s %s %s",
	 &entry->year, &entry->month, &entry->day, &entry->ddd,
	 &entry->hour, &entry->minute, &entry->second, &entry->c_score,
	 foF2, foF1, foE, foEs, hEs, hmF2, hmF1,
	 hmE, b0, b1);


  
  entry->foF2 = str_to_float(foF2);
  entry->foF1 = str_to_float(foF1);
  entry->foE  = str_to_float(foE);
  entry->foEs = str_to_float(foEs);
  entry->hEs = str_to_float(hEs);
  entry->hmF2 = str_to_float(hmF2);
  entry->hmF1 = str_to_float(hmF1);
  entry->hmE = str_to_float(hmE);
  entry->b0 = str_to_float(b0);
  entry->b1 = str_to_float(b1);

}

void write_table(FILE* fp_out, table_entry* data, int num_entries)
{
  fprintf(fp_out, "yyyy.MM.dd (DDD) HH:mm:ss C-score   foF2    foF1   foE   foEs   h`Es    hmF2    hmF1    hmE     B0     B1\n\n");

  for(int i = 0; i < num_entries; i++) {
  char foF2[20], foF1[20], foE[20];
  char foEs[20], hEs[20], hmF2[20];
  char hmF1[20], hmE[20], b0[20];
  char b1[20];
  float_to_str(data[i].foF2,foF2);
  float_to_str(data[i].foF1,foF1);
  float_to_str(data[i].foE,foE);
  float_to_str(data[i].foEs,foEs);
  float_to_str(data[i].hEs, hEs);
  float_to_str(data[i].hmF2, hmF2);
  float_to_str(data[i].hmF1, hmF1);
  float_to_str(data[i].hmE, hmE);
  float_to_str(data[i].b0, b0);
  float_to_str(data[i].b1, b1);
  

  fprintf(fp_out, "%d.%.2d.%.2d (%.3d) %.2d:%.2d:%.2d %7d %6s %6s %6s %6s %6s %6s %6s %6s %6s %6s\n",
	  data[i].year, data[i].month, data[i].day, data[i].ddd,
	  data[i].hour, data[i].minute,data[i].second, data[i].c_score,
	  foF2, foF1, foE, foEs, hEs, hmF2, hmF1, hmE, b0, b1); 
  }

  
}
// Comparison function for qsort. Compares the foF2 fields of two table_entry structs.
int compare_foF2(const void* a, const void* b) {
  const table_entry* ta = (const table_entry*)a;
  const table_entry* tb = (const table_entry*)b;
  if (ta->foF2 < tb->foF2) return -1;
  if (ta->foF2 > tb->foF2) return 1;
  return 0;
}

int main(int argc, char *argv[]) {
  FILE *fp;

  
  char line[1000];
  table_entry data[1000];

  // Open the file for reading
  fp = fopen("AU930_ROAM.TXT", "r");
  if (fp == NULL) {
    perror("Error opening file");
    return 1;
  }
  //Ignore header line
  fgets(line, 1000, fp);
  fgets(line,1000,fp);
  // Read each line of the file
  int num_entries = 0;
  while (fgets(line, 1000, fp) != NULL) {

    // Parse the data from the line
    read_line(data+num_entries, line);
    num_entries++;
  }
  qsort(data, num_entries, sizeof(table_entry), compare_foF2);
  // Close the file
  fclose(fp);

  // Output sorted file
  FILE *fp_out;
  fp_out = fopen("sorted_table.txt","w");
  write_table(fp_out,data,num_entries);

  // Output Median
  printf("Median foF2: %f\n ", data[num_entries/2].foF2);
  fclose(fp_out);
  return 0;
}
