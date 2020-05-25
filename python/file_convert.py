# Not-tested yet

import docx2pdf



def doc2pdf(src, dst):
    docx2pdf.convert(src, dst)


if __name__ == '__main__':
    doc2pdf("src.docx", "dst.pdf")
