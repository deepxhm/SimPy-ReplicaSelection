#!/bin/bash
awk -f test.awk TLL-seed1inter10_99thlatency.txt >> inter10 
awk -f test.awk TLL-seed16inter10_99thlatency.txt >> inter10 
awk -f test.awk TLL-seed128inter10_99thlatency.txt >> inter10 
awk -f test.awk TLL-seed1024inter10_99thlatency.txt >> inter10 
awk -f test.awk TLL-seed20480inter10_99thlatency.txt >> inter10 


awk -f test.awk TLL-seed1inter200_99thlatency.txt >> inter200
awk -f test.awk TLL-seed16inter200_99thlatency.txt >> inter200
awk -f test.awk TLL-seed128inter200_99thlatency.txt >> inter200
awk -f test.awk TLL-seed1024inter200_99thlatency.txt >> inter200
awk -f test.awk TLL-seed20480inter200_99thlatency.txt >> inter200

awk -f test.awk TLL-seed1inter500_99thlatency.txt >> inter500
awk -f test.awk TLL-seed16inter500_99thlatency.txt >> inter500
awk -f test.awk TLL-seed128inter500_99thlatency.txt >> inter500
awk -f test.awk TLL-seed1024inter500_99thlatency.txt >> inter500
awk -f test.awk TLL-seed20480inter500_99thlatency.txt >> inter500




python testaverage.py
