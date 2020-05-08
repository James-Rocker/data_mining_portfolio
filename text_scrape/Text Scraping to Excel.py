import xlsxwriter
import re

filename = 'Dracula'

"""Search Text Logs"""
workbook = xlsxwriter.Workbook(filename.strftime('%d-%b-%Y') + " Analysis.xlsx")  # TODO: file needs to be output in working directory
worksheet = workbook.add_worksheet()

"""Analyse of text file here"""
try:
    filename = filename + ".txt"
    raised = len(re.findall('Vampire', file(filename).read()))  # TODO: add a function to actually open the file
    output1 = {
         "Vampire": ''
         }
    row = 0
    col = 0
    # TODO: add write to functionality

except:
    pass
