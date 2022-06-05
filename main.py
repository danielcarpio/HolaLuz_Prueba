#!/usr/bin/env python

from input_type_reading import csv, xml
from print_output import print_output
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('No file provided')


    # Finding extension of the given file 
    file_name = sys.argv[1]
    extension = file_name.split('.')[-1]
    
    suspicious = [] 
    
    # According to the extension, we call the function
    if extension == 'csv':
        suspicious = csv.read_csv(file_name=file_name)
    elif extension == 'xml':
        suspicious = xml.read_xml(file_name=file_name)
    else:
        print('File type not supported')

    print_output(suspicious)