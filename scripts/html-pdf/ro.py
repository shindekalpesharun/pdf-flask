import PyPDF2


def PDFrotate(origFileName, newFileName, rotation):
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


def main():
    origFileName = 'Git_Cheat_Sheet.pdf'
    newFileName = 'Day 2.pdf'
    rotation = 270
    PDFrotate(origFileName, newFileName, rotation)


if __name__ == "__main__":
    main()
