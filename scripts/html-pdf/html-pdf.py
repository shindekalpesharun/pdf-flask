import weasyprint
pdf = weasyprint.HTML('http://www.google.com').write_pdf()
len(pdf)
open('google.pdf', 'wb').write(pdf)
