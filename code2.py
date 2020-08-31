import openpyxl                      #install openpyxl using code: pip install openpyxl
from datetime import date

wb= openpyxl.Workbook()

sheet=wb.active

today=date.today()
# print(today)

sheet.append(['Name','Roll No','Date = '+str(today)])    #give header to the worksheet

fh=open("chat.txt","r+")            #open file containing data
data=fh.readlines()
for line in data:
    line=line.strip()
    print("Input Line: ",line)
    nrp=line.split('|')             #separate name, roll no. and Present from the input line
    # print(nrp)
    try:
        roll=int(nrp[1].strip())
    except:
        continue
    if(len(nrp)==3 and nrp[2].strip()=="Present"):
        sheet.append([nrp[0].strip(),nrp[1].strip(),''])

        #append data to the excel sheet


wb.save('C:/Users/Deepanshu/Desktop/program_to_save_attendence/SE_class_sept.xlsx')

#save the excel sheet