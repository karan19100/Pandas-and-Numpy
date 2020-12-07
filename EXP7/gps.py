import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(19.04013, 72.925454,17)

gmap.coloricom = 'http://www.googlemapmarkers.com/v1/%s/' 

with open('data.csv','r') as f:
    reader = csv.reader(f)
    k = 0

    for row in reader:
        lat = float(row[0]) 
        long = float(row[1]) 
        if (k==0):
            gmap.marker(lat, long, 'yellow')
            k = 1
        else:
            gmap.marker(lat, long, 'blue')
gmap.marker(lat, long, 'red')
gmap.draw('mymap.html')

