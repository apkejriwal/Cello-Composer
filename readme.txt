My program, Cello Composer, is an interactive educational tool written in Python that teaches the user how to play the cello by showing what fingers to put on what string based on the note. The program has two major components: a reader function and then a user function. The user function is where the user draws their staff with the notes and rests they want: they have the option to draw any note or rest with any duration specified in the program. Once the user is done drawing their staff, they can press "Go!" and then the reader funcion will take the staff the user created, analyze it, and then generate the same staff along with a cello fingerboard. Most importantly, the reader function creates several dictionaries of the pitches, locations, number of fingers for each note. All of this information is then stored with one list that contains objects which contain individual attributes of pitch, location, number of fingers, and any other supporting data. 

To run this program, an individual must download eventBasedAnimation and simpleAudio, python files developed by David Kosbie of Carnegie Mellon University. 

http://www.cs.cmu.edu/~112/notes/notes-event-based-animations.html#BackgroundAudioDemo
Website above contains both files created by David Kosbie. 


Next, one must also download music21, an external python module developed by MIT that is  geared towards musical analysis.

To do this, one must visit this website and follow the instructions as noted by the OS of your computer. 

http://web.mit.edu/music21/doc/installing/install.html

The installation is very simple and is automated and does not require the user to have to move libraries manually. 

To run this program, run CelloComposer.py
