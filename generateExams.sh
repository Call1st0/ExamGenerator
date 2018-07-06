#!/bin/bash
echo Generating exams, how much exams you need?
read numOfExams

#Generate random exams
python ExamGenerator.py --numExams $numOfExams

#Change folder and compile latex file
cd ExamLatex
pdflatex exam.tex

#Add handout-jednadzbe-tablica.pdf to every other page
pages="`pdftk exam.pdf dump_data | grep NumberOfPages | cut -d : -f2`"
numpages=`for ((a=1; a <= $pages; a++)); do echo -n "A$a B1 "; done`
pdftk A=exam.pdf B=handout-jednadzbe-tablica.pdf cat $numpages output exam-alternated.pdf

xdg-open exam-alternated.pdf 
exit 0

