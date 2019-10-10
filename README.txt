##########################################################################################
#################################                      ###################################                                  
#################################     PyMusiqMix       ###################################
#################################                      ###################################                     
##########################################################################################
# Copyright (c) 2015-20 PyMusiqMix Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

NAME:
-----

	PyMusiqMix - Constraints based Playlist generation using Genetic Algorithm.

AUTHOR:
-------

	Nimitha Liz Sunny
	Riya Mary Roly
	Tom Joseph - tom.jose.25@gmail.com

LATEST VERSION:
---------------

	1.0 - April 09th, 2015

SYNOPSIS:
--------

	A Player System which recommends you a playlist.
	No need of searching for songs in the database or recently or most played or favourites.
    
SOFTWARES REQUIRED:
------------------

	Python installer for windows - python-2.7.8.exe (Any version except 3 and above)
	Python Gui maker - PyQt-win-gpl-4.11.3.exe
	
ADDITIONAL LIBRARIES:
--------------------
	ID3 tag reader for mp3 - id3reader

PROGRAM FILES:
-------------
	
	PyMusiqMix.py - Main module for running the system
	main.py - The Genetic algorithm file
	const.py - Form for giving constraints as input
	songextracter.py - For extracting files supported by player i.e mp3 having meta data
	
	log.txt - To maintain log of current users
	database.txt - To maintain list of songs details
	
DESCRIPTION:
-----------

	With a huge amount of music collections, it might be difficult for users to find favourite music.
	Therefore, a variety of emerging music services is proposed, such as recommendation and playlist generation. 
	In apple iTunes or Windows Media player we see that the user has to manually add songs to the playlist. 
	To get away from all the tedious work involved with this, lots of playlist generation techniques have come up. 

	Genetic algorithm is a very promising technique on which lots of research is being done.
	Genetic algorithms implement optimization strategies by simulating evolution in species through natural selection.

	In our problem, we need to generate a playlist (set of songs) according to the likes of the user.
	Initially we generate a random population. Each individual in a population represents a solution or playlist.
	We then evaluate the fitness of each solution by checking the no of constraints each song in the playlist satisfies.
	Now we apply the genetic operators: Selection, Crossover and Mutation. Then calculate fitness of new generation.
	And the process goes on. After a few hundred or thousand generations we see that the best solution in the population will have a very high fitness value.
	We intend to create a music player system for creating a good playlist using Python named PyMusicMix
    
	
INSTRUCTIONS:
------------
	
	Change location of song folder in main.py
	You have to set source and location in songextractor.py

DISCUSSION:
-----------
	
	Discussions are currently held in the GitHub

CREDITS:
--------

	People who have helped/contributed:

	Mr.Jayarajan Jayan
	Mr.Febin Jacob
	Miss.Sneha Anthony

	Anyone We missed, drop me a line!

