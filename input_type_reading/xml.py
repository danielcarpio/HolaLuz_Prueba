from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def read_xml(file_name):
    suspicious = []

    with open(file_name, 'r') as f:
        data = f.read()
    
        client_id = 0
        month_data = []
        reading_data = []
        median = 0

        bs_data = BeautifulSoup(data, "xml")
        readings = bs_data.find_all('reading')

        for line in readings:
            client_id = line['clientID']
            month_data.append(line['period'])
            reading_data.append(int(line.get_text()))

            if len(month_data) == 12:
                sorted_reading_data = sorted(reading_data)
                median = (sorted_reading_data[5]+sorted_reading_data[6]) / 2;
                min_reading_allowed = median*0.5
                max_reading_allowed = median*1.5

                for i in range(0, 12):
                    if reading_data[i] < min_reading_allowed or reading_data[i] > max_reading_allowed:
                        suspicious.append([client_id, month_data[i], reading_data[i], median])

                client_id = 0
                month_data = []
                reading_data = []
                median = 0

    f.close()

    return suspicious