#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <math.h>

//#define M_PI 3.14159265358979323846264338327

int total_counter(FILE* fp);
//int alpha_calculator();
int yau_plot(char* fname,FILE* fp);
//float cos_calc(int pos);
//float sin_calc(int pos);
//float moment_of_inertia();
//float moment_of_inertia_calc(const char* fname, float x_avg, float y_avg, float* mi_x, float* mi_y);
//int char_by_char_read_write(FILE* in_fp, FILE* out_fp);

int count_total=0;
int count_a=0, count_g=0, count_t=0, count_c=0;
float tempx=0, tempy=0, sumx=0, sumy=0;
float mx=0.0, my=0.0, nx=0.0, ny=0.0, x_resultant=0.0, y_resultant=0.0;
float mewx=0.0, mewy=0.0, sqrGr=0.0, gr=0.0;

int main(int argc, char** argv)
{
  if(argc!=2)
  {
	perror("Command line arguments are not given properly\n");
	return -1;
  }
  else
  {
	FILE* fp=fopen(argv[1], "r");
	if(fp!=NULL)
	{
	  total_counter(fp);
	  fclose(fp);
	  //total_counter(fp);
	  //alpha_calculator();
	  //return(acgt_position_detector(argv[1],fp));
	}
	else
	{
	  perror("Requested file doesn't exist\n");
	  return -1;
	}
	//alpha_calculator();
	fp=fopen(argv[1], "r");
	if(fp!=NULL)
	{
	  //return(total_counter(fp));
	  yau_plot(argv[1],fp);
	  fclose(fp);
	}
	else
	{
	  perror("Requested file doesn't exist\n");
	  return -1;
	}
  }
}

int total_counter(FILE* fp)
{
  //int count_total=0;
  //static int count_total=0;
  char ch;
  while(1)
  {
	//fscanf(fp, "%c", &ch);
	ch=fgetc(fp);
	if(ch==65 || ch==67 || ch==71 || ch==84 || ch==97 || ch==99 || ch==103 || ch==116)
	  count_total++;
	else if(ch==EOF)
	  break;
  }
  printf("Total count is %d\n", count_total);
  //alpha_calculator();
}

int yau_plot(char* fname,FILE* fp)
{
  //char out_fname[100], ch;
  char ch, *out_fname, *f_str;
  int n, c;
  //static int count_a, count_g, count_t, count_c, count_total;
  //static const int r=100;
  //static long float a_x_avg, a_y_avg, c_x_avg, c_y_avg, g_x_avg, g_y_avg, t_x_avg, t_y_avg;
  //static long float a_x, a_y, c_x, c_y, g_x, g_y, t_x, t_y;
  //float rcos_tmp=0, rsin_tmp=0;
  long int byte_count;
  FILE *out_fp, *out_a, *out_c, *out_g, *out_t, *in_a, *in_c, *in_g, *in_t, *in_fp;
  out_fname = strtok (fname,".");
  //pch = strtok (fname,".");
  if (out_fname != NULL)
  {
	//strcat(out_fname, pch);
    strcat(out_fname, "_result.txt");
    //pch = strtok (NULL, " ,.-");
  }
  else
  {
	perror("Invalid input file format\n");
	return -1;
  }
  out_fp=fopen(out_fname, "w");
  out_a=fopen("a.txt", "w");
  out_c=fopen("c.txt", "w");
  out_g=fopen("g.txt", "w");
  out_t=fopen("t.txt", "w");
  if (feof(fp))
  {
	perror("Input file is empty\n");
	return -1;
  }
  count_total=0;
  count_a=0;
  count_c=0;
  count_g=0;
  count_t=0;
  c=0;
  n=0;
  //fprintf(out_a, "a:\n");
  //fprintf(out_c, "c:\n");
  //fprintf(out_g, "g:\n");
  //fprintf(out_t, "t:\n");
  
  
  
  while(1)
  {
	ch=fgetc(fp);
	if(ch==EOF)
	  break;
	else if(ch=='g'||ch=='G')
	{
	  count_g++;
	  count_total++;
	  fprintf(out_a, "%d\n", count_total);
	  tempx=tempx+0.8660254;
	  sumx=sumx+tempx;
	  tempy=tempy-0.5;
	  sumy=sumy+tempy;
	  /*rcos_tmp=r*cos_calc(count_total);
	  rsin_tmp=r*sin_calc(count_total);
	  a_x=a_x+rcos_tmp;
	  a_y=a_y+rsin_tmp;*/
	}
	else if(ch=='c'||ch=='C')
	{
	  count_c++;
	  count_total++;
	  fprintf(out_g, "%d\n", count_total);
	  tempx=tempx+0.8660254;
	  sumx=sumx+tempx;
	  tempy=tempy+0.5;
	  sumy=sumy+tempy;
	  /*rcos_tmp=r*cos_calc(count_total);
	  rsin_tmp=r*sin_calc(count_total);
	  g_x=g_x+rcos_tmp;
	  g_y=g_y+rsin_tmp;*/
	}
	else if(ch=='a'||ch=='A')
	{
	  count_a++;
	  count_total++;
	  fprintf(out_t, "%d\n", count_total);
	  tempx=tempx+0.5;
	  sumx=sumx+tempx;
	  tempy=tempy-0.8660254;
	  sumy=sumy+tempy;
	  /*rcos_tmp=r*cos_calc(count_total);
	  rsin_tmp=r*sin_calc(count_total);
	  t_x=t_x+rcos_tmp;
	  t_y=t_y+rsin_tmp;*/
	}
	else if(ch=='t'||ch=='T')
	{
	  count_t++;
	  count_total++;
	  fprintf(out_c, "%d\n", count_total);
	  tempx=tempx+0.5;
	  sumx=sumx+tempx;
	  tempy=tempy+0.8660254;
	  sumy=sumy+tempy;
	  /*rcos_tmp=r*cos_calc(count_total);
	  rsin_tmp=r*sin_calc(count_total);
	  c_x=c_x+rcos_tmp;
	  c_y=c_y+rsin_tmp;*/
	}
  }
  fclose(out_a);
  fclose(out_c);
  fclose(out_g);
  fclose(out_t);
  
  mx=((count_a*0.5)+(count_t*0.5));
  my=((count_g*0.8660254)+(count_c*0.8660254));
  nx=((count_g*0.5)+(count_c*0.5));
  ny=((count_a*0.8660254)+(count_t*0.8660254));
  x_resultant=(mx+(my*1.7320508))/2;
  y_resultant=(nx+(ny*1.7320508))/2;
  mewx=(float)sumx/(float)count_total;
  mewy=(float)sumy/(float)count_total;
  //mewx=(float)tempx/count_total;
  //mewy=(float)tempy/count_total;
  sqrGr=(float)((mewx*mewx)+(mewy*mewy));
  gr=(float)sqrt(sqrGr);
  //moment_of_inertia();
  /*moment_of_inertia_calc("a.txt", a_x_avg, a_y_avg, &a_mi_x, &a_mi_y);
  moment_of_inertia_calc("c.txt", c_x_avg, c_y_avg, &c_mi_x, &c_mi_y);
  moment_of_inertia_calc("g.txt", g_x_avg, g_y_avg, &g_mi_x, &g_mi_y);
  moment_of_inertia_calc("t.txt", t_x_avg, t_y_avg, &t_mi_x, &t_mi_y);*/
  
  fprintf(out_fp, "count of a: %d\ncount of c: %d\ncount of g: %d\ncount of t: %d\ntotal count: %d\n", count_a, count_c, count_g, count_t, count_total);
  fprintf(out_fp, "mx: %f\nmy: %f\nnx: %f\nny: %f\nx_resultant: %f\ny_resultant: %f\n", mx, my, nx, ny, x_resultant, y_resultant);
  fprintf(out_fp, "mewx: %f\nmewy: %f\nsqrGr: %f\ngr: %f\n", mewx, mewy, sqrGr, gr);
  //printf("gr: %f\n", gr);
  return 0;
}


