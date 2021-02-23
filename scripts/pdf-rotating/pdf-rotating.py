import PyPDF2

origFileName = 'os.pdf'
newFileName = 'rotated_example.pdf'
rotation = 270
pdfFileObj = open(origFileName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfWriter = PyPDF2.PdfFileWriter()
for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    pageObj.rotateClockwise(rotation)
    pdfWriter.addPage(pageObj)
newFile = open(newFileName, 'wb')
pdfWriter.write(newFile)
pdfFileObj.close()
newFile.close()
