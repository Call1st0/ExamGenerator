# ExamGenerator is a python script for generation of exam with random questions from question bank
# The txt file generated is created for further typesetting using LaTeX
#
# Author: Ante Poljicak
# Version: 0.1 Initial version
import string
from random import choice, randrange, sample

def main(NumOfExams):
    #Name of the files used
    QuestionsFileName = "QuestionBank.txt"
    ExamFileName = "Exam01.txt"
    #NumOfExams = 3

    # Generate ID for the exam
    SecurityString=id_generator()

    # Read all lines in question bank
    QuestionsFile = open(QuestionsFileName, 'r')
    lines = QuestionsFile.readlines()

    # Create a file
    ExamFile = open(ExamFileName, "w")

    # Here add lines as needed e.g. First Last name or additional information if not already added in main latex file
    for count in range(1,NumOfExams+1):
        ExamFile.write('\\begin{enumerate}\n')

        ListOfLines=QuestionChooser(QuestionsFileName) #Chose random questions
        for counter, value in enumerate(ListOfLines):
            ExamFile.write(lines[value-1])

        ExamFile.write('\\end{enumerate}\n')
        ExamFile.write('\\vspace{10mm}\n')
        ExamFile.write('\\large ID: ' + SecurityString+'\n')
        ExamFile.write('\\newpage')

    ExamFile.close()

# Method for generation of security string to protect the exam from counterfeiting
def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(choice(chars) for _ in range(size))


def QuestionChooser(FileName): #TODO change method to return list of strings with questions instead of list of ints
    """From question bank chose a list of questions and return list of line numbers belonging to this questions

    Args:
    QuestionsFileName (str): QuestionFileName must have latex formatting where questions are formatted
        in itemized or enumerated lists and separated in sections

    Returns:
        list of ints where each int is a line number for chosen question

    """
    QuestionsFile=open(FileName,"r")
    # variable for counting numbers of questions in a section, each item in a list is another section
    NumOfQuestionsInSection=0
    NumOfLineWhereSectionStart=[]
    ListOfQuestions=[]
    CurrentLine=0
    for line in QuestionsFile:
        CurrentLine=CurrentLine+1
        if "section" in line: # when section is found
            NumOfQuestionsInSection=0 #reset counter
            NumOfLineWhereSectionStart.append(CurrentLine)
        elif "item" in line:
            NumOfQuestionsInSection=NumOfQuestionsInSection+1
        elif "end{enumerate}" in line:
            ListOfQuestions.append(NumOfQuestionsInSection)
    QuestionsFile.close()

    #Create list of lines to extract questions from
    Sections = sample(range(len(ListOfQuestions)-1), k = 5) #Careful, number of sections start from 0
    ListOfLines=[]
    for SectionNumber in Sections:
        # Generate list using num of line where section start add random number to chose question in that section and
        # add 2 to jump to first question in section
        ListOfLines.append(NumOfLineWhereSectionStart[SectionNumber]+randrange(ListOfQuestions[SectionNumber])+2)
    ListOfLines.append(NumOfLineWhereSectionStart[-1]+randrange(ListOfQuestions[-1])+2) #Questions in last section are always included

    return ListOfLines


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Number of exams')

    parser.add_argument('--numExams', type=int, metavar='N', required=True, help='Number of needed Exams')
    args = parser.parse_args()

    main(NumOfExams=args.numExams)
