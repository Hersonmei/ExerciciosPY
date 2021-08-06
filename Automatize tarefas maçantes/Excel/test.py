import openpyxl, os

os.chdir(r'C:\Users\herso\OneDrive\APython\Exercícios\Arquivos')

wb = openpyxl.load_workbook('prazo.xlsx')

sheet1 = wb['Page 1'] 

#print(tuple(sheet1['F12': 'F28']))

for rowOfCelObj in sheet1['D12': 'F28']:
    for cellObj in rowOfCelObj:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')