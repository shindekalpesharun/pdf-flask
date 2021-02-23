# ui *
# pdf compress word, powerpoint, excel, page number add
# powerpoint - pdf
# excel - pdf
# pdf to PDF/A

# TODO: Encrypt and decrypt PDF files with passwords

# pdf -jpg/
# jpg to pdf/
# html - pdf/
# merge/ split/ rotaing watermark word - pdf
import pdfFunction as pdf
import os
from flask import Flask, render_template, request, send_file


dir_path = os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__)


@app.route('/')
def home():
    pdf.filDel()
    return render_template('index.html')


# @app.route('/pdf_to_jpg.html', methods=['GET', 'POST'])
# def PdfToJpg():
#     pass


@app.route('/jpg_to_pdf.html', methods=['GET', 'POST'])
def JpgToPdf():
    pass


@app.route('/rotate_pdf.html', methods=['GET', 'POST'])
def Rotate():
    return pdf.rotatePdf()


@app.route('/html_to_pdf.html', methods=['GET', 'POST'])
def HtmlToPdf():
    pdf.htmlPdf()


@app.route('/marge_pdf.html', methods=['GET', 'POST'])
def margePdf():
    return pdf.margePdf()   # function calling throw pdfFunction module


# @app.route('/split_pdf.html', methods=['GET', 'POST'])
# def splitPdf():
#     pass


# @app.route('/compress_pdf.html', methods=['GET', 'POST'])
# def compressPdf():
#     pass


# @app.route('/pdf_to_word.html', methods=['GET', 'POST'])
# def pdfToWord():
#     pass


# @app.route('/pdf_to_powerpoint.html', methods=['GET', 'POST'])
# def pdfToPowerpoint():
#     pass


# @app.route('/pdf_to_excel.html', methods=['GET', 'POST'])
# def PdfToExcel():
#     pass


# @app.route('/word_to_pdf.html', methods=['GET', 'POST'])
# def WordToPdf():
#     pass


# @app.route('/powerpoint_to_pdf.html', methods=['GET', 'POST'])
# def PowerpointToPdf():
#     pass


# @app.route('/excel_to_pdf.html', methods=['GET', 'POST'])
# def ExcelToPdf():
#     pass


# @app.route('/page_number.html', methods=['GET', 'POST'])
# def PageNumber():
#     pass


# @app.route('/watermark.html', methods=['GET', 'POST'])
# def watermark():
#     pass


if __name__ == '__main__':
    app.run(debug=True)
