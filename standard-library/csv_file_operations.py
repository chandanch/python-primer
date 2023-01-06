"""
    Using csv module to read and write data from to CSV file
"""
import csv

# writing data to CSV file
# open the file using open() in write mode
with open("orders.csv", "w") as csv_file:
    # create an instance of csv writer to write to csv file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Id", "Value", "UserId", "TransactionId"])
    csv_writer.writerow([123223, 134.23, "CADQ1232", "TR123911"])
    csv_writer.writerow([119001, 120, "CADQ1232", "TR00923"])

# Reading csv file
with open("orders.csv", encoding="utf-8") as orders_file:
    # create an instance of csv reader, 
    # the reader is iterable and extracts each row from the csv file
    csv_reader = csv.reader(orders_file)
    