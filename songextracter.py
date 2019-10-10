import id3reader
import os
import shutil
filename=""
flag=0
src ='E:\musiq'
#C:\Users\TMZ\Music
songs = []
with open("database.txt","w") as c:
   for root, dirs, files in os.walk(src):
      for f in files:
         list =[]
         filename = os.path.join(root, f)
         if filename.endswith('.mp3'):
            #print filename
            id3r = id3reader.Reader(filename)
            try:
               if str(id3r.getValue('title'))!= "None" and str(id3r.getValue('performer'))!="None" and str(id3r.getValue('album'))!="None" and str(id3r.getValue('year'))!="None" and str(id3r.getValue('genre')) !="None":
                  list.append(str(id3r.getValue('title')))
                  list.append(str(id3r.getValue('performer')))
                  list.append(str(id3r.getValue('album')))
                  list.append(str(id3r.getValue('year')))
                  list.append(str(id3r.getValue('genre')))
                  dest = "E:\songs\\" + f
                  shutil.copy(filename,dest)
            except:
               print filename
            else:
               #print list
               if list not in songs:
                  songs.append(list)
                  songs.sort()
   for list in songs:
      c.writelines(str(list)+"\n")
print "Database updated"


   
      

