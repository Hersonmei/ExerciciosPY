# Esse aquivo consegui gerar um arquivo txt, mas ele vem desconfigurado, por isso fica difícil trabalhar com eles no momento.

import PyPDF2, os, sys

sys.stdout = open("prazo.txt", "w")
os.chdir(r'C:\Users\herso\OneDrive\APython\Exercícios\Arquivos')
pdfFileObj = open('prazo.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

#print(pageObj)

page_1_text = pageObj.extractText()
print(page_1_text)
sys.stdout.close()


