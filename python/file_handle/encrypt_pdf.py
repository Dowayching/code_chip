# -*- coding: UTF-8 -*-
""" PDF Encryption Module
    
This module include encrypt pdf functions & run it directly to encrypt all
pdf files in specified folder

Usage:
    python encrypt_pdf.py -i input_path -o output_path -p password

Args:
    input: folder path of input pdf file 
    output: folder path of output pdf file
    password: password used when encryption

Author: Anto Tu
"""

import os
import sys
import glob
import argparse
from PyPDF4 import PdfFileReader, PdfFileWriter


def encrypt_single_pdf(input_file, output_file, password):
    """Encrypt single pdf as another file

    Args:
        input_file: input file path name
        output_file: output file path name
        password: password used when encryption 

    Return: None
    """
    with open(input_file, 'rb') as input_stream:
        reader = PdfFileReader(input_stream)
        writer = PdfFileWriter()
        #writer.appendPagesFromReader(reader)
        for page in range(reader.getNumPages()):
            writer.addPage(reader.getPage(page))
        writer.encrypt(password)
        for page in range(reader.getNumPages()):
            a = writer.getPage(page)
            #a.scaleTo(480, 270)
        with open(output_file, 'wb') as output_stream:
            writer.write(output_stream)
           

def encrypt_pdf_in_folder(input_path, output_path, password):
    """Encrypt all pdf in specified folder to another folder.

    Args:
        input_path: folder path of input pdf files
        output_path: folder path of output pdf files
        password: password used when encryption

    Return: None
    """
    # get all pdf files
    files = [f for f in glob.glob(input_path + "/*.pdf", recursive=False)] 
    
# encrypt all pdf files
    if len(files) == 0:
        print('Find no PDF files!')
    for input_file in files:
        file_name = os.path.basename(input_file)
        output_file = output_path + file_name 
        print('Input file: {}'.format(input_file))
        encrypt_single_pdf(input_file, output_file, password)
        print('Output file: {}'.format(output_file))
 

def main():
    """main function"""   

    # parse input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input_path', help='Input PDF file path')
    parser.add_argument('-o', dest='output_path', help='Output PDF file path')
    parser.add_argument('-p', dest='password', 
                        help='Password used when encryption')
    args = parser.parse_args()

   # encrypt each PDf files
    print('Encypt PDF...')
    args.output_path += '/'  # prevent user forget it
    encrypt_pdf_in_folder(args.input_path, 
                          args.output_path, 
                          args.password)
    print('Encypt Done!')


if __name__ == '__main__':
    main()

