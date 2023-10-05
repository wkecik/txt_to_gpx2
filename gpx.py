# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime

def split(name):
    with open("GPSData000001.txt", "r") as filestream:
        with open("output.gpx", "w") as filestreamtwo:


    for line in filestream:
                currentline = line.split(",")
                dt = datetime.datetime.fromtimestamp(int(currentline[0]))
                lat = currentline[2]
                long = currentline[3]
                print(str(dt) + " - " + lat + " - " + long + "\n")
                filestreamtwo.write((str(dt) + " - " + lat + " - " + long + "\n"))


if __name__ == '__main__':

    split('PyCharm')
