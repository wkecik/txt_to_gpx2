import folium
import gpxpy
from selenium import webdriver

with open('myfile.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

map = folium.Map(location=[52.222823, 21.1], zoom_start=11, tiles='OpenStreetMap')

points = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            points.append(tuple([point.latitude, point.longitude]))
polyline = folium.PolyLine(locations=points, weight=5, color='blue')
map.add_child(polyline)

map.save('nazwa_mapy.html')
map.save('nazwa_mapy.png')

#browser = webdriver.Chrome()  # utwórz obiekt przeglądarki Chrome
#map.save('nazwa_mapy.html')

#browser.get('nazwa_mapy.html')  # otwórz plik HTML z mapą w przeglądarce
#browser.save_screenshot('nazwa_mapy.png')  # zapisz zrzut ekranu jako plik PNG
#browser.quit()  # zamknij przeglądarkę

