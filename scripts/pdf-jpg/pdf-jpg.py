from pdf2image import convert_from_path
pages = convert_from_path('os.pdf', 500)
for page in pages:
    page.save('out.jpg', 'JPEG')
