import PyPDF2

def add_watermark(wmFile, pageObj):
    wmFileObj = open(wmFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(wmFileObj)
    pageObj.mergePage(pdfReader.getPage(0))
    wmFileObj.close()
    return pageObj


def main():
    mywatermark = 'watermark.pdf'
    origFileName = 'example.pdf'

    newFileName = 'watermarked_example.pdf'
    pdfFileObj = open(origFileName, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pdfWriter = PyPDF2.PdfFileWriter()

    for page in range(pdfReader.numPages):
        wmpageObj = add_watermark(mywatermark, pdfReader.getPage(page))

        pdfWriter.addPage(wmpageObj)

    newFile = open(newFileName, 'wb')

    pdfWriter.write(newFile)

    pdfFileObj.close()

    newFile.close()


if __name__ == "__main__":
    main()
