import id3reader
import os
import shutil
filename="Ring My Bells.mp3"
id3r = id3reader.Reader(filename)
print str(id3r.getValue('mood'))
print str(id3r.getValue('tmoo'))

