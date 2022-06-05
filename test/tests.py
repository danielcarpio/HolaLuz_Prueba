import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import unittest
from input_type_reading import csv
from input_type_reading import xml

class Testing(unittest.TestCase):

    def test_csv_file(self):
        csv_data = csv.read_csv('test/2016-readings.csv')
        result = [['583ef6329d7b9', '2016-09', 3564, 42798.5], ['583ef6329d89b', '2016-09', 162078, 59606.5], ['583ef6329d89b', '2016-10', 7759, 59606.5], ['583ef6329d916', '2016-09', 2479, 40956.0]]
        self.assertEqual(csv_data, result)

    def test_xml_file(self):
        xml_data = xml.read_xml('test/2016-readings.xml')
        result = [['583ef6329e237', '2016-11', 1379, 30132.5], ['583ef6329e271', '2016-10', 121208, 21661.0], ['583ef6329e3ab', '2016-11', 6440, 27867.5], ['583ef6329e41b', '2016-05', 133369, 32790.5]]
        self.assertEqual(xml_data, result)

    def test_csv_file_no_sus(self):
        csv_data = csv.read_csv('test/2016-readings_no_sus.csv')
        result = []
        self.assertEqual(csv_data, result)


if __name__ == '__main__':
    unittest.main()