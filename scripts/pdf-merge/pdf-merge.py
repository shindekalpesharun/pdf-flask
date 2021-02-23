import PyPDF2

# Open the files that have to be merged one by one
pdf1File = open('os.pdf', 'rb')
pdf2File = open('outputans.pdf', 'rb')

# Read the files that you have opened
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()


for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)


for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)


pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

# Close all the files - Created as well as opened
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
