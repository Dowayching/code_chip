import sys
from PyPDF4 import PdfFileReader, PdfFileWriter


def encrypt_pdf(input_path, output_path):
    with open(input_path, 'rb') as input_stream:
        reader = PdfFileReader(input_stream)
        writer = PdfFileWriter()
        #writer.appendPagesFromReader(reader)
        for page in range(reader.getNumPages()):
            writer.addPage(reader.getPage(page))
        writer.encrypt("a")
        for page in range(reader.getNumPages()):
            a = writer.getPage(page)
            a.scaleTo(480, 270)
        with open(output_path, 'wb') as output_stream:
            writer.write(output_stream)


if __name__ == '__main__':
    print(sys.argv[1])
    print(sys.argv[2])
    #encrypt_pdf('input.pdf', 'output.pdf')
    #encrypt_pdf(sys.argv[1], sys.argv[2])
