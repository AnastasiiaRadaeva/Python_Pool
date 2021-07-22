#!/bin/sh
head -n1 ../ex01/hh.csv > hh_sorted.csv
cat ../ex01/hh.csv | tail -n20 | sort -t"," -k2 -k1 >> hh_sorted.csv