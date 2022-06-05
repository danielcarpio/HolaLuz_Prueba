def read_csv(file_name):
    suspicious = []

    with open(file_name, 'r') as f:
        f.readline() #Skip column names row

        client_id = 0
        month_data = []
        reading_data = []
        median = 0

        while True:
            line = f.readline()
            if not line:
                break
            
            data = line.rstrip().split(',')
            client_id = data[0]
            month_data.append(data[1])
            reading_data.append(int(data[2]))

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