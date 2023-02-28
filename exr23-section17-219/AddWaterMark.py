import PyPDF2

file = open("exr23-section17-219/super.pdf", 'rb')
watermark_file = open("exr23-section17-219/wtr.pdf", 'rb')
file_pdf = PyPDF2.PdfFileReader(file)
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

watermark = watermark_pdf.getPage(0)

output = PyPDF2.PdfFileWriter()

for page in range(file_pdf.getNumPages()):
    file_page = file_pdf.getPage(page)
    file_page.mergePage(watermark)
    output.addPage(file_page)

with open("exr23-section17-219/merged.pdf", 'wb') as merged_file:
    output.write(merged_file)

file.close()
watermark_file.close()
