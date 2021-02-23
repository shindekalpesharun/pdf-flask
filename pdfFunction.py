import os
from flask import request, render_template, send_file


def filDel():
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    test = os.listdir(dir_path)

    for item in test:
        if item.endswith(".jpg"):
            os.remove(os.path.join(dir_path, item))
        if item.endswith(".pdf"):
            os.remove(os.path.join(dir_path, item))


def margePdf():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if request.method == 'POST':
        file0 = request.files['pdf0']
        file1 = request.files['pdf1']

        import PyPDF2
        pdf1Reader = PyPDF2.PdfFileReader(file0)
        pdf2Reader = PyPDF2.PdfFileReader(file1)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        for pageNum in range(pdf2Reader.numPages):
            pageObj = pdf2Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        pdfOutputFile = open(dir_path+'/MergedFiles.pdf', 'wb')
        pdfWriter.write(pdfOutputFile)
        pdfOutputFile.close()
        return send_file(dir_path+'/MergedFiles.pdf')
    else:
        return render_template('pdf-files/marge_pdf.html')


def jpgPdf(dir_path):
    pass


def pdfJpg(dir_path):
    # from pdf2image import convert_from_path
    # pages = convert_from_path('os.pdf', 500)
    # for page in pages:
    #     page.save('out.jpg', 'JPEG')

    # while pages:
    #     pages.save
    pass


def rotatePdf():
    import PyPDF2
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if request.method == 'POST':
        file0 = request.files['pdf0']
        file0.save(file0.filename)
        # rotatePdfAngle = request.form['rotatePdfAngle']

        origFileName = file0
        rotation = 270
        pdfFileObj = open(origFileName, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pdfWriter = PyPDF2.PdfFileWriter()
        for page in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(page)
            pageObj.rotateClockwise(rotation)
            pdfWriter.addPage(pageObj)
        newFile = open(origFileName, 'wb')
        pdfWriter.write(newFile)
        pdfFileObj.close()
        newFile.close()
        return send_file(dir_path+"/Backlog Exam _ Summer 2020 (1).pdf")
        # return dir_path
    else:
        return render_template('pdf-files/rotate_pdf.html')


def htmlPdf():
    import weasyprint

    # dir_path = os.path.dirname(os.path.realpath(__file__))
    pdf = weasyprint.HTML('http://www.google.com').write_pdf()
    len(pdf)
    open('google.pdf', 'wb').write(pdf)
