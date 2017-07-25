# ExamGenerator
Simple python script for generation of unique exams using randomized questions from a question bank. 
Script draws questions from the Question bank and generates .txt file with LaTeX syntax. 
Main LaTeX file is used to control the layout of the exam.

I was tired of deciding on which questions to use in written exams I give to my students, 
and wanted to enforce objective tests where all questions have the same probability of occurrence. 
Therefore, I wrote the simple python script for generation of unique exams by randomly 
choosing questions from the question bank. Script draws questions from the Question bank and generates 
.txt file with LaTeX syntax. Then the main LaTeX file is used to control the layout of the exam.

## Main LaTeX file
The main latex file is used to define look and feel of the exam by setting arbitrary latex class 
in the preamble. Additional information such as date of the exam or name of the course can be included directly in main file.  

## Question bank
Question bank should be latex formated and each question itemized (or enumerated). Questions are grouped in
sections and the script by default uses only one question per section. If the number of questions needed for the
exam is less than the number of questions script randomly choses sections, with the exception of last section
which is by default always included.

## Generated exam file
Generated exam is included in main file by *\input{...}* LaTeX command. When exam file is generated, a random security ID
is also generated and included in the exam. This way you can make all questions available to students while still be certain 
that they can't cheat.   

## TODO list 
This script is far from complete. There are numerous features that are missing.
* Enable explicit choice of any section to be or not to be included
* Simplify structure of the question bank
* Create LaTeX class specially for this script
* Enable use of multi-choice questions
* Enable option to chose question by its difficulty level
