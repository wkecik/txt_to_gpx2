# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import datetime
import folium


def txt_gpx():


    # Use a breakpoint in the code line below to debug your script.

    f = open("myfile.gpx", "w")
    f.write(

"""<?xml version="1.0" encoding="UTF-8"?>
<gpx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.topografix.com/GPX/1/1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.topografix.com/GPX/gpx_style/0/2 http://www.topografix.com/GPX/gpx_style/0/2/gpx_style.xsd" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:gpx_style="http://www.topografix.com/GPX/gpx_style/0/2" version="1.1" creator="https://gpx.studio">
<metadata>
    <name>new</name>
    <author>
        <name>gpx.studio</name>
        <link href="https://gpx.studio"></link>
    </author>
</metadata>
<trk>
    <name>new</name>
    <type>Cycling</type>
    <trkseg>\n""")

    dt_from = datetime.datetime(2023, 2, 5, 8, 50, 00)
    dt_from_min = (dt_from.time().hour*60 + dt_from.time().minute)
    dt_from_sec = (dt_from.time().hour*3600 + dt_from.time().minute)*60 + dt_from.time().second

    dt_to = datetime.datetime(2023, 2, 5, 9, 21, 11)
    dt_to_min = (dt_to.time().hour * 60 + dt_to.time().minute)
    dt_to_sec = (dt_to.time().hour*3600 + dt_to.time().minute)*60 + dt_to.time().second


    with open("GPSData000001.txt.orig", "r") as filestream:

        for line in filestream:
            if (line.find("$V02")<0):
                currentline = line.split(",")
                dt0 = datetime.datetime.utcfromtimestamp(int(currentline[0]))
                dt = datetime.datetime.utcfromtimestamp(int(currentline[0])+32400)
                dt_min = (dt.time().hour * 60 + dt.time().minute)
                dt_sec = (dt.time().hour * 3600 + dt.time().minute) * 60 + dt_from.time().second
                dtcx = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                lat = currentline[2]
                long = currentline[3]
                ele = currentline[7]

                if  (dt_from.date() == dt.date()) and (dt_to_sec >= dt_sec >= dt_from_sec) :
                    print(dt_from , dt , dt_to)
                    
                    f.write("    <trkpt ")
                    f.write("lat=\"" + str(lat) + "\" lon=\"" +str(long) +  "\">\n")
                    f.write("        <ele>" + str(ele) + "</ele>\n")
                    f.write("        <time>" + dtcx + "</time>\n")
                    f.write(
            """        <extensions>
        <gpxtpx:TrackPointExtension>
        <gpxtpx:Extensions>
            <surface>asphalt</surface>
        </gpxtpx:Extensions>
        </gpxtpx:TrackPointExtension>
        </extensions>
    </trkpt>
""")

    f.write("""</trkseg>
</trk>
</gpx>""" )

    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    txt_gpx()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
