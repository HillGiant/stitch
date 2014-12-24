import urllib.request
import os

CURRENTDIR = os.path.dirname(__file__)
print (CURRENTDIR)
TILEFOLDER = os.path.join(CURRENTDIR, 'Tiles')
print (TILEFOLDER)

def DownloadTile(url, filename):
    filepath = os.path.join(TILEFOLDER, filename)
    urllib.request.urlretrieve(url, filepath)

def CollectTiles():
    print ("Collecting Tiles")
    DownloadTile("https://maps.googleapis.com/maps/api/staticmap?center=South+Lake+Union&zoom=15&size=640x640&scale=2", "Tile1.png")

def StitchTiles():
    print ("Stitching tiles together")

print ("Hello World")

CollectTiles()
StitchTiles()
