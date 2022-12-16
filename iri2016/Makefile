run-iri: libiri.so run-iri.o
	gcc -g -o run-iri run-iri.o -L. -liri

run-iri.o: run-iri.c
	gcc -c -g run-iri.c

libiri.so: irisub.o irifun.o iritec.o iridreg.o igrf.o cira.o iriflip.o
	f77 -shared -g -o libiri.so  $^ -fPIC

%.o: %.for
	f77 -g -c $< -fPIC

iri: iritest.for
	f77 -g -o iri iritest.for irisub.for irifun.for iritec.for iridreg.for igrf.for cira.for iriflip.for 
clean:
	rm -f libiri.so *.o run-iri iri
