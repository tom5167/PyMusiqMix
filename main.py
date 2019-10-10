import random
from operator import itemgetter
import id3reader
import os

global pop
global playlist
global song
global l
global c
global flag
global thf
global top
global count

pop = []
playlist = []
flag = 0
thf = 20
top = 0
cs = []
css = []
count = 0           
gen = 100
c=[]
song = []
fit = 5
loc = 'D:\songs'

def valid():
    global pop
    pop1 = []
    for play in pop:
        list = []
        for x in xrange(0,5):
            if play[x] not in list:
                list.append(play[x])

        if len(list) != 5:
            for y in xrange (5-len(list)):
                list.append(random.randint(0,l))
        list.append(0)
        pop1.append(list)
    pop.pop()
    pop.pop()
    pop.pop() 
    pop.pop()
    pop.pop()
    pop = pop1
    return

def selection():
    global pop
    global c
    
    for play in pop:
        play[fit]=0
        for x in c:
            for item in range(0,fit):
                if x[0] == '0' or x[0] == '1':
                    if x[2:].lower() in song[int(play[item])][int(x[1])].lower():
                        play[fit] = play[fit]+1
                try:
                    if x[0] == '3' and x[1] == '0':
                        if int(x[2:5]) <= int(song[int(play[item])][int(x[1])]) and int(song[int(play[item])][int(x[1])]) <= int(x[6:]):
                            play[fit] = play[fit]+1
                    if x[0] == '3' and x[1] == '1':
                        if not(int(x[2:5]) <= int(song[int(play[item])][int(x[1])]) and int(song[int(play[item])][int(x[1])]) <= int(x[6:])):
                            play[fit] = play[fit]+1
                except:
                    pass
    #sort
    pop = sorted(pop,key=itemgetter(5),reverse=True)
    pop.pop()
    pop.pop()
    return

def crossover():
    x=random.randint(0,2)
    y=random.randint(0,2)
    p1=pop[x]
    p2=pop[y]
    pt=3
    temp1=p1[pt:]
    temp2=p2[:pt]
    pp1=temp2+temp1
    pp2=p1[:pt]+p2[pt:]
    #for fitness value
    pp1.pop()
    pp2.pop()
    pp1.append(0)
    pp2.append(0)
    pop.extend([pp1,pp2])
    return

def mutate():
    x=random.randint(0,4)
    y=random.randint(0,4)
    pop[x][y]=random.randint(0,l)
    return

def music(user):
    global l
    global c
    #################################### song databse #####################################
    with open("database.txt","w") as c:
        for root, dirs, files in os.walk(loc):
            for f in files:
                filename = os.path.join(root, f)
                if filename.endswith('.mp3'):
                    list =[]
                    
                    id3r = id3reader.Reader(filename)
                    list.append(str(id3r.getValue('title')))
                    list.append(str(id3r.getValue('performer')))
                    list.append(str(id3r.getValue('album')))
                    list.append(str(id3r.getValue('year')))
                    list.append(str(id3r.getValue('genre')))

                    c.write(str(list)+"\n")
                    if list not in song:
                        song.append(list)
                        song.sort()
    #################################### song database #####################################
    l=len(song)-1
    ####################################  constraints  #####################################
    with open(user+".txt","r") as f:
        lines=f.readlines()
        c=[(e.strip()) for e in lines]
    ####################################  constraints  #####################################
      
    ####################################     GA        #####################################
    for i in range(0,5):
        playlist=[random.randint(0,l),random.randint(0,l),random.randint(0,l),random.randint(0,l),random.randint(0,l),0]
        pop.append(playlist)
    cur_gen = 0
    selection()
    while cur_gen < gen:
        crossover()
        mutate()
        valid()
        selection()
        cur_gen = cur_gen+1
    ####################################     GA        #####################################
    result = pop[flag]
    result = result[:-1]
    ################################# return song address ##################################
    set = []
    for x in result:
        for root, dirs, files in os.walk(loc):
            for f in files:
                filename = os.path.join(root, f)
                if filename.endswith('.mp3'):                
                    id3r = id3reader.Reader(filename)
                    if song[x][0] == str(id3r.getValue('title')):
                        set.append(str(filename))
    ################################# return song address ##################################
    return set

if __name__ == "__main__":
    list = music() 
