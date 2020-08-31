# Program_to_mark_attendence

# Code 1 ( code1.py )
This program will read data from the input file line by line and search for the names in the excel sheet and mark present
against there names in the excel sheet on the same date column.
Input file will contain data in the form :  Name | Roll no. | Present
The program reads line and match name and roll no. in the excel sheet and mark Present agaist his name under the same date column.

# Code 2 ( code2.py )
This program will read data from the input file line by line and copy it into an excel sheet under three columns:[ Name , Roll No. , Date = today ]
Input file will contain data in the form :  Name | Roll no. | Present
The program reads line and write name and roll no. in the excel sheet forming a list of all the students present in the class.

# Input text file ( chat.txt )
This is the input text file containing chats.
Input file will contain data in the form :  Name | Roll no. | Present
And rest chats will be neglected.

# Excel workbook 1 ( SE_class.xlsx )
This excel workbook will contain different sheets representing different months and now it contains one sheet named 'sept' for attendence of the month september.
It contains the list of all students with their name and roll number.
'P' will be marked against the name of the present students after running code1.py python file.

# Excel workbook 2 ( SE_class_sept.xlsx )
This is empty workbook which will contain the list of present students on any day after running code2.py python file.
