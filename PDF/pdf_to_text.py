import PyPDF2

pdf_name = 'poem.pdf'
pdfObj = open(pdf_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
    print(text)
    
