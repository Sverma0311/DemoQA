import csv


class DataReader:
    def read_data_from_csv(filename):
        # create empty list

        datalist = []

        # open csv file

        csvdata = open(filename, 'r')

        reader = csv.reader(csvdata)

        next(reader)

        # Add csv rows into list

        for rows in reader:
            datalist.append(rows)

        return datalist