import openpyxl, os

os.chdir(r'C:\Users\herso\OneDrive\APython\Exercícios\Arquivos')

wb = openpyxl.load_workbook('prazo.xlsx')

#print(wb.get_sheet_names())
 #['Page 1', 'Page 2', 'Page 3']  Retorno do print acima.

sheet1 = wb.get_sheet_by_name('Page 1')

sheet2 = wb.get_sheet_by_name('Page 2')
