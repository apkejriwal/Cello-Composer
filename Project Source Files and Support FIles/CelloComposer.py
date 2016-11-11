from music21 import * 
from Tkinter import * 
import eventBasedAnimation
import simpleAudio 

"""
Music21 is a python module developed by MIT researchers. 
eventBasedAnimation and simpleAudio are modules developed by David Kosbie, CMU 

Images of notes, rests provided by
https://www.iconfinder.com/

Image background of Cello is provided by 
http://pixshark.com/abstract-cello-art.htm

Samples of Cello Notes provided by University of Iowa:
http://theremin.music.uiowa.edu/MIS.html

musicxml files of Bach Cello suites provided by:
http://kern.ccarh.org/

"""

class Page(object): pass 

class Staff(object):
	def __init__(self,x0,y0,x1,y1):
		self.margin = 50 
		self.x0, self.y0 = x0, y0 + self.margin * 3 
		self.x1, self.y1 = x1, self.y0 + self.margin * 2
		self.dy = float(self.y1 - self.y0) / 4
		self.spacing = (float(self.x1 - self.x0) / 5) / 3
		filename = "bassclef_final2.gif"
		self.photo = PhotoImage(file = filename)
		
	def draw(self,canvas, numerator, denominator, offset):
		x0,y0,x1,y1 = self.x0, self.y0, self.x1, self.y1
		dy = self.dy
		spacing = self.spacing
		canvas.create_rectangle(x0,y0,x1,y1, width = 3)

		left = spacing * 1.5 - offset

		canvas.create_image(self.spacing / 2 - offset,(y1+y0) / 2, image = self.photo)

		canvas.create_text(left, y0 + dy, text = str(numerator), font = "Arial " + str(int(spacing) / 2))
		canvas.create_text(left, y1 - dy, text = str(denominator), font = "Arial " + str(int(spacing) / 2))

		for i in xrange(1,4):
			newY = y0 + (dy * i) 								  
			canvas.create_line(x0,newY,x1,newY, width = 2)

class vLine(object):
	def __init__(self,left,top,right,bottom):
		self.left = left 
		self.right = right
		self.top = top
		self.bottom = bottom 

	def draw(self,canvas,offset,width):
		left, right = self.left - offset, self.right - offset,
		top, bottom = self.top, self.bottom

		if left <= 0:
			return
		if left >= width:
			return
		else:
			canvas.create_line(left,top,right,bottom, width = 2)

class Note(object):
	def __init__(self,left,right,top,bottom,duration,pitch,r,num):
		self.left = left
		self.right = right 
		self.top = top 
		self.bottom = bottom
		self.duration = duration 
		self.pitch = pitch
		self.r = r 
		self.num = num

		qRest = "quarter_rest.gif"
		self.qRest = PhotoImage(file = qRest)
		sRest = "sixteenth_rest.gif"
		self.sRest = PhotoImage(file = sRest)
		eRest = "eighth_rest.gif"
		self.eRest = PhotoImage(file = eRest)

	def draw(self,canvas,offset,highlight, width,num):
		r = self.r
		left = self.left - r - offset
		right = self.left + r - offset
		top, bottom = self.top, self.bottom
		middle = (top + bottom) / 2.0
		vOff = middle + 100 - r
		vOffD = middle - 100 + r
		self.color = "black"
		dy = float(top-bottom)

		time = self.duration 

		if left <= 0:
			return
		elif left >= width:
			return
		else:
			if self.pitch == 73:
				if self.duration == 2.0:
					canvas.create_rectangle(left,top,right,middle, fill = "black")
				if self.duration == 4.0:
					canvas.create_rectangle(left + 162.5,middle,right + 162.5,bottom, fill = "black")
				if self.duration == 1.0:
					canvas.create_image((left+right)/2.0,top,image = self.qRest)
				if self.duration == .50:
					canvas.create_image((left+right) / 2.0, top, image = self.eRest)
				if self.duration == .25:
					canvas.create_image((left+right) / 2.0, top, image = self.sRest)

			if self.pitch in [36,37]:
				canvas.create_line(left - r,middle,right + r ,middle,width = 1.5)
				canvas.create_line(left-r,middle+dy,right+r,middle+dy,width = 1.5)
			if self.pitch == 38:
				canvas.create_line(left-r,middle+dy/2,right+r,middle+dy/2,width = 1.5)
			if self.pitch in [39,40]:
				canvas.create_line(left - r,middle,right + r ,middle,width = 1.5)

			if self.pitch in [60,61]:
				canvas.create_line(left - r,middle,right + r ,middle,width = 1.5)
			if self.pitch == 62:
				canvas.create_line(left - r,middle - dy/2,right + r ,middle-dy/2,width = 1.5)
			if self.pitch in [63,64]:
				canvas.create_line(left-r,middle,right+r,middle,width = 1.5)
				canvas.create_line(left-r,middle-dy,right+r,middle-dy,width = 1.5)
			if self.pitch in [65,66]:
				canvas.create_line(left-r,middle-(1.5 *dy),right+r,middle-(1.5*dy),width = 1.5)
				canvas.create_line(left-r,middle-dy/2,right+r,middle-dy/2,width = 1.5)
			if self.pitch in [67,68]:
				canvas.create_line(left-r,middle,right+r,middle,width = 1.5)
				canvas.create_line(left-r,middle-dy,right+r,middle-dy,width = 1.5)
				canvas.create_line(left-r,middle-dy*2,right+r,middle-dy*2,width = 1.5)
			if self.pitch == 69:
				canvas.create_line(left-r,middle-(1.5 *dy),right+r,middle-(1.5*dy),width = 1.5)
				canvas.create_line(left-r,middle-dy/2,right+r,middle-dy/2,width = 1.5)
				canvas.create_line(left-r,middle-(2.5 *dy),right+r,middle-(2.5*dy),width = 1.5)
			if self.pitch in [70,71]:
				canvas.create_line(left-r,middle,right+r,middle,width = 1.5)
				canvas.create_line(left-r,middle-dy,right+r,middle-dy,width = 1.5)
				canvas.create_line(left-r,middle-dy*2,right+r,middle-dy*2,width = 1.5)
				canvas.create_line(left-r,middle-dy*3,right+r,middle-dy*3,width = 1.5)
			if self.pitch == 72:
				canvas.create_line(left-r,middle-dy/2,right+r,middle-dy/2,width = 1.5)
				canvas.create_line(left-r,middle-(1.5 *dy),right+r,middle-(1.5*dy),width = 1.5)
				canvas.create_line(left-r,middle-(2.5 *dy),right+r,middle-(2.5*dy),width = 1.5)
				canvas.create_line(left-r,middle-(3.5 *dy),right+r,middle-(3.5*dy),width = 1.5)

			if self.pitch != 73:
				if self.pitch % 12 == 1 or self.pitch % 12 == 6 or self.pitch % 12 == 8:
					canvas.create_line(left-r-5,top,left-r-5,bottom,width = 2)
					canvas.create_line(left-r + 5,top,left-r + 5, bottom, width = 2)
					canvas.create_line(left-r*2,middle+5,left,middle+5, width = 2)
					canvas.create_line(left-r*2,middle-5,left,middle-5, width = 2)
				if self.pitch % 12 == 3 or self.pitch % 12 == 10:
					canvas.create_text(left-r, middle, text = "b", font = "Arial 20 bold ")

			if time == .50 and self.pitch < 73:
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)
				if self.pitch <= 50:
					canvas.create_line(right,vOffD,right,middle, width = 3)
					x1,y1 = right + 20, vOffD + 25 
					canvas.create_line(right,vOffD,x1,y1, width = 3) #slanted 
					canvas.create_line(x1,y1,x1,y1+20, width = 3)  #vertical line down 
				else:
					canvas.create_line(left,middle,left,vOff, width = 3)
					x1,y1 = left + 20, vOff - 25
					canvas.create_line(left,vOff,x1,y1,width = 3)  #slanted 
					canvas.create_line(x1,y1,x1,y1-20,width = 3)   #vertical line down 

			if time == .25 and self.pitch < 73:
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)
				if self.pitch <= 50:
					canvas.create_line(right,vOffD,right,middle, width = 3)
					x1,y1 = right + 15, vOffD + 25 
					canvas.create_line(right,vOffD,x1,y1, width = 3)
					canvas.create_line(x1,y1,x1,y1+20, width = 3)

					x2, y2 = x1 - 5, y1 + 5
					canvas.create_line(right, vOffD + 15, x2, y2, width = 3)
					canvas.create_line(x2,y2,x2,y2 + 15, width = 3)

				else:
					canvas.create_line(left,middle,left,vOff, width = 3)
					x1,y1 = left + 15, vOff - 25
					canvas.create_line(left,vOff,x1,y1,width = 3)
					canvas.create_line(x1,y1,x1,y1-20,width = 3)

					x2, y2 = x1 - 5, y1 - 5

					canvas.create_line(left,vOff - 15, x2, y2, width = 3)
					canvas.create_line(x2,y2,x2,y2 - 15, width = 3)

			if time == 1.0 and self.pitch < 73:
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)
				if self.pitch <= 50: 
					canvas.create_line(right,vOffD,right,middle, width = 3)
				else:
					canvas.create_line(left,middle,left,vOff, width = 3)
			if time == 2.0 and self.pitch < 73:
				if self.color == "black":
					self.color = None
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)
				if self.pitch <= 50: #D3
					canvas.create_line(right,vOffD,right,middle, width = 3)
				else:
					canvas.create_line(left,middle,left,vOff, width = 3)
			if time == 4.0 and self.pitch < 73:
				if self.color == "black":
					self.color = None
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)

		if highlight == self.num and self.pitch != 73:
			canvas.create_oval(left,top,right,bottom, fill = "red")

class Fingerboard(object):
	def __init__(self,x0,y0,x1,y1,frets,strings):
		self.margin = 50 
		self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
		self.frets = frets
		self.strings = strings
		self.color = "red"
		self.on = 0 

	def draw(self,canvas):
		y0 = self.y0 + self.margin * 5
		self.dy = 50 
		y1 = y0 + self.dy * 3
		x0 = float(self.x0)
		x1 = float(self.x1)
		string_list = []

		self.height = 400
		self.width = float(x1-x0)
		self.dx = self.width / float(self.frets + 1)

		canvas.create_rectangle(x0,y0,x1,y1, width = 3, fill = "black")

		for i in xrange(self.strings):
			yPos = y0 + i * self.dy
			left = x0
			right = x1
			color = self.color
			canvas.create_line(left,yPos,right,yPos, fill = color, width = 8)
			string_list.append((right,yPos))

		count = 0 
		for i in xrange(65,72,3):
			midX, midY = string_list[count]
			canvas.create_text(midX + 15,midY,text = chr(i), fill = "white", font = "Arial 20")
			count += 1 
			if i == 71:
				canvas.create_text(midX +15, midY + self.dy, text = "C", fill = "white", font = "Arial 20")

		if self.on % 2 == 1:
			for i in xrange(1,self.frets + 1):
				xPos = self.margin + self.dx * i
				canvas.create_line(xPos,y0,xPos,y1, fill = "yellow")


class Sound(object):
	def __init__(self,filename,num):
		self.filename = filename
		self.num = num

	def play(self,highlight,num):
		filename = self.filename
		if highlight == self.num:
			simpleAudio.startSound(filename,async = True, loop = False)

class Position(object):
	def __init__(self,midX,midY,fingers,space,line,x0,x1,num):
		self.midX = midX
		self.midY = midY

		self.fingers = fingers 
		self.space = space 

		self.margin = 50 
		self.strings = 4 
		self.frets = 14

		self.num = num 
		self.line = line
		self.x0 = x0 
		self.x1 = x1

		self.width = float(self.x1-self.x0)
		self.dx = self.width / float(self.frets + 1)

		self.radius = self.dx / 2.0 

	def draw(self,canvas,highlight,num):
		radius = self.radius 

		left = self.midX - radius 
		right  = self.midX + radius

		top = self.midY - radius 
		bottom = self.midY + radius 

		fingers = self.fingers 
		dx = self.dx 

		if highlight == self.num:
			if self.line == False:
				if self.space == True:
					left += dx
					right += dx 
					canvas.create_oval(left,top,right,bottom,fill = "yellow")
					left += dx 
					right += dx
					for i in xrange(self.fingers - 1):
						left += dx 
						right += dx
						canvas.create_oval(left,top,right,bottom, fill = "yellow")
				else:
					for i in xrange(fingers):
						left += dx 
						right += dx
						canvas.create_oval(left,top,right,bottom, fill = "yellow")
			else:
				canvas.create_line(self.x0,self.midY,self.x1,self.midY, fill = "yellow", width = 20)

	
class Button(object):
	def __init__(self,x0,y0,x1,y1, text):
		self.margin = 25 
		self.x0 = x0
		self.x1 = x1
		self.y0 = y0
		self.y1 = y1
		self.text = text 
		self.color = "orange"

	def draw(self,canvas):
		x0, x1, y0, y1 = self.x0, self.x1, self.y0, self.y1
		self.midX = (x1 + x0) / 2
		self.midY = (y1 + y0) / 2
		canvas.create_rectangle(x0,y0,x1,y1, fill = self.color, width = 2)
		canvas.create_text(self.midX, self.midY, text = self.text, fill = "black", font = "Arial 10 bold")

class Reader(Page):
	def __init__(self,width,height,path):
		self.storedPath = path 
		simpleAudio.stopSound()
		self.timerDelay = 300 
		self.width = width
		self.height = height
		self.aboutText = self.windowTitle = "Cello Composer"
		self.margin = 50 
		self.x0, self.y0, self.x1, self.y1 = 0, 0, self.width, self.height

		self.staff = Staff(self.x0, self.y0, self.x1, self.y1)
		self.path = converter.parse(path)

		self.fx0, self.fy0 = self.margin, self.margin * 3 
		self.fx1, self.fy1 = self.x1 - self.margin , self.fy0 + self.margin * 2

		self.strings = 4 
		self.frets = 14

		self.fingerboard = Fingerboard(self.fx0, self.fy0, self.fx1, self.fy1, self.frets, self.strings)
		
		self.numerator = self.path.flat.getElementsByClass("TimeSignature")[0].numerator
		self.denominator = self.path.flat.getElementsByClass("TimeSignature")[0].denominator

		self.notes = []
		self.positions = []
		self.pitches = []
		self.durations = []
		self.sounds = []
		self.vLines = []
		self.noteDict = dict()
		self.posDict = dict()
		self.soundDict = dict()

		self.dx = float(self.fx1-self.fx0) / 5
		self.dy = float(self.fy1-self.fy0) / 4 

		self.offset = 0
		self.durationCounter = 0 
		self.currDuration = 0 
		self.counter = 0
		self.num = 0 
		self.highlight = False
		self.timer = 0 

		self.r = self.dy / 2 
		self.lowY = self.fy1 + 2 * self.dy
		self.newI = 0 
		self.noteSpace = self.dx / 2.0
		self.left = self.fx0 + self.dx + self.noteSpace 
		self.play = None

		self.restartButton = Button(self.fx1-100,600,self.fx1,650, text = "Restart!")
		self.fretButton = Button(self.fx1-225,600,self.fx1-125,650, text = "Frets On/Off")

		self.restart = False 
		self.composition = False 
		self.preset = False 
		self.instructionsVal = False 
		self.presetFile = None
		self.home = False 

		fx0 = self.fx0 
		right = self.fx0 + 100 
		shift = 125 

		self.backButton = Button(self.fx0,25,right,75, text = "Home")
		self.playButton = Button(self.fx0,600,right,650, text = "")
		self.pauseButton = Button(self.fx0+shift,600,right + shift ,650, text = "")
		self.reverseButton = Button(self.fx0+shift*2,600,right + shift * 2,650, text = "")

		self.muteButton = Button(self.fx0+shift*3,600,right + shift*3 - 50, 650, text ="")
		self.unMuteButton = Button(self.fx0+shift*4 - 50,600,right+shift*4 - 100,650, text ="")
		end = right+shift*4 - 100

		self.slowButton = Button(end+25,600,end+shift,650,text = "")
		self.fastButton = Button(end + shift + 25, 600, end + shift * 2, 650, text = "")

		self.go = None
		self.stop = False
		self.volume = True
		self.reverse = False 

		mute = "mute.gif"
		unmute = "unmute.gif"
		play = "play.gif"
		pause = "pause.gif"
		play_reverse = "play_reverse.gif"
		slower = "slower.gif"
		faster = "faster.gif"
		back = "cello_home.gif"
		self.back = PhotoImage(file = back)
		self.slower = PhotoImage(file = slower)
		self.faster = PhotoImage(file = faster)
		self.mute = PhotoImage(file = mute)
		self.unmute = PhotoImage(file = unmute)
		self.playimg = PhotoImage(file = play)
		self.pauseimg = PhotoImage(file = pause)
		self.play_reverse = PhotoImage(file = play_reverse)

		listOfNotes = self.path.flat.getElementsByClass([note.Note, chord.Chord, note.Rest])

		def getPitches():
			for elem in listOfNotes:                            #pitches 
				if type(elem) != note.Note:
					if type(elem) == chord.Chord:
						pass
					if type(elem) == note.Rest:
						self.pitches.append(73)
				else:
					self.pitches.append(elem.midi)

		def getDurations():
			for elem in listOfNotes:
				self.durations.append(elem.quarterLength)   	#durations 

		def noteDictionary(): 
			r = self.r
			for i in xrange(36,73):  #C2 to C5 (cello range) 
				if i % 12 == 1: 
					self.noteDict[i] = self.noteDict[i-1]
				elif i % 12 == 3:
					self.noteDict[i] = self.noteDict[i-1]
				elif i % 12 == 6:
					self.noteDict[i] = self.noteDict[i-1]
				elif i % 12 == 8:
					self.noteDict[i] = self.noteDict[i-1]
				elif i % 12 == 10: 
					self.noteDict[i] = self.noteDict[i-1]
				else:
					self.noteDict[i] = ((self.lowY - r - r * self.newI), 
									   (self.lowY + r - r * self.newI))
					self.newI += 1 
			for i in xrange(36,73):
				if i % 12 == 3 or i % 12 == 10:
					self.noteDict[i] = self.noteDict[i+1]

			self.noteDict[73] = ((0,0))
			self.noteDict[73] = self.noteDict[50]

		def soundDictionary():
			filename = "cello_samples_midi_num/"
			for i in xrange(36,73):
				self.soundDict[i] = filename + str(i)
			self.soundDict[73] = "cello_samples_midi_num/nosound"

		def posDictionary():
			width = float(self.fx1 - self.fx0)
			dx = width / float(self.frets + 1)
			dy = self.margin
			yPos = self.fy1 + self.margin * 3

			self.posDict[73] = 0
			self.posDict[73] = (0,0,0,False,False,0,0)

			for i in xrange(36,64):
				if i >= 36 and i <= 42:
					midY = yPos + dy * 3 
				elif i >= 43 and i <= 49:
					midY = yPos + dy * 2 
				elif i >= 50 and i <= 56:
					midY = yPos + dy
				elif i >= 57:
					midY = yPos
									  		
				if i % 7 == 1:
					self.posDict[i] = (0,midY,1,False,True,self.fx0, self.fx1)
				if i % 7 == 2:
					self.posDict[i] = (self.margin,midY,1,False,False,self.fx0,self.fx1)
				if i % 7 == 3:
					self.posDict[i] = (self.margin + dx,midY,1,False,False,self.fx0,self.fx1)
				if i % 7 == 4:
					self.posDict[i] = (self.margin + dx,midY,2,False,False,self.fx0,self.fx1)
				if i % 7 == 5:
					self.posDict[i] = (self.margin + dx,midY,3,False,False,self.fx0,self.fx1)
				if i % 7 == 6:
					self.posDict[i] = (self.margin + dx,midY,4,False,False,self.fx0,self.fx1)
				if i % 7 == 0:
					self.posDict[i] = (self.margin + dx,midY,4,True,False,self.fx0,self.fx1)

			for i in xrange(64,69):
				midY, midX = yPos, self.margin + dx * 6
				if i % 7 == 1:
					self.posDict[i] = (midX, midY, 1, False, False, self.fx0, self.fx1)
				if i % 7 == 2:
					self.posDict[i] = (midX, midY, 2, False, False, self.fx0, self.fx1)
				if i % 7 == 3:
					self.posDict[i] = (midX, midY, 3, False, False, self.fx0, self.fx1)
				if i % 7 == 4:
					self.posDict[i] = (midX, midY, 4, False, False, self.fx0, self.fx1)
				if i % 7 == 5:
					self.posDict[i] = (midX, midY, 4, True, False, self.fx0, self.fx1)

			for i in xrange(69,73):
				midY, midX = yPos, self.margin + dx * 11
				if i % 7 == 6:
					self.posDict[i] = (midX, midY,1,False,False,self.fx0, self.fx1)
				if i % 7 == 0:
					self.posDict[i] = (midX, midY,2,False,False,self.fx0, self.fx1)
				if i % 7 == 1:
					self.posDict[i] = (midX, midY,2,True,False,self.fx0, self.fx1)
				if i % 7 == 2:
					self.posDict[i] = (midX, midY,3,True,False,self.fx0, self.fx1)

		getPitches()
		getDurations()
		noteDictionary()
		posDictionary()
		soundDictionary()


		def getNotesandPos():
			for i in xrange(len(self.pitches)):
				r = self.r
				top, bottom = self.noteDict[self.pitches[i]]
				duration = self.durations[i]
				self.durationCounter += duration
				pitch = self.pitches[i]

				midX,midY,fingers,space,line,x0,x1 = self.posDict[self.pitches[i]]
				num = self.num
				soundFile = self.soundDict[self.pitches[i]]

				self.notes.append(Note(self.left,self.left,top,bottom,duration,pitch,r,num))
											   # midX,midY,fingers,space,line,x0,x1,num
				self.positions.append(Position(midX,midY,fingers,space,line,x0,x1,num))
				self.sounds.append(Sound(soundFile,num))

				self.num += 1
				self.left += self.noteSpace * duration

				if self.durationCounter % self.numerator == 0:
					self.vLines.append(vLine(self.left,self.fy0,self.left,self.fy1))
					self.left += self.noteSpace

		getNotesandPos()
		self.currDuration = self.notes[0].duration 
		
		def playSound():
			soundFile = self.soundDict[self.pitches[self.counter]]
			simpleAudio.startSound(soundFile,async = True, loop = True)

		playSound()

	def onDraw(self,canvas):
		canvas.create_image(self.width / 2.0, self.height / 2.0, image = self.back)
		canvas.create_text(self.width / 2.0, self.margin / 2.0, text = "Learn to play your score!", font = "Arial 20", fill = "white")
		self.staff.draw(canvas, self.numerator, self.denominator,self.offset)
		self.fingerboard.draw(canvas)
		for elem in self.notes:
			elem.draw(canvas,self.offset, self.highlight,self.width, self.num)
		for elem in self.vLines:
			elem.draw(canvas,self.offset,self.width)
		for elem in self.positions:
			elem.draw(canvas,self.highlight,self.num)

		self.restartButton.draw(canvas)
		self.fretButton.draw(canvas)
		self.playButton.draw(canvas)
		self.pauseButton.draw(canvas)
		self.reverseButton.draw(canvas)
		self.muteButton.draw(canvas)
		self.unMuteButton.draw(canvas)
		self.slowButton.draw(canvas)
		self.fastButton.draw(canvas)
		self.backButton.draw(canvas)

		midX = self.fx0 + 50 
		shift = 125 
		canvas.create_image(midX,625, image = self.playimg)
		canvas.create_image(midX+shift,625, image = self.pauseimg)
		canvas.create_image(midX+shift*2,625, image = self.play_reverse)
		canvas.create_image(450,625, image = self.mute)
		canvas.create_image(525,625, image = self.unmute)
		canvas.create_image(midX+shift*4 + 25,625, image = self.slower)
		canvas.create_image(midX+shift*5+25,625,image = self.faster)


	def onKey(self,event):

		def playSound():
			if self.volume == True:
				if self.counter + 1 == len(self.notes):
					soundFile = self.soundDict[self.pitches[self.counter]]
					simpleAudio.startSound(soundFile,async = True, loop = False)
				elif self.counter == 0:
					soundFile = self.soundDict[self.pitches[self.counter]]
					simpleAudio.startSound(soundFile,async = True, loop = False)
				else:
					soundFile = self.soundDict[self.pitches[self.counter]]
					simpleAudio.startSound(soundFile,async = True, loop = True)
		
		if self.counter < len(self.notes) - 1:
			if event.keysym == "Right" and (self.currDuration) % self.numerator == 0:
				self.offset += self.noteSpace
				self.counter += 1 
				self.highlight += 1
				self.offset += self.noteSpace * self.notes[self.counter].duration
				self.currDuration += self.notes[self.counter].duration
				playSound()
				
			elif event.keysym == "Right":
				self.counter += 1 
				self.highlight += 1
				self.offset += self.noteSpace * self.notes[self.counter].duration
				self.currDuration += self.notes[self.counter].duration
				playSound()

		if self.counter > 0:
			if event.keysym == "Left":
				self.offset -= self.noteSpace * self.notes[self.counter].duration
				self.currDuration -= self.notes[self.counter].duration
				self.counter -= 1 
				self.highlight -= 1  
				
				playSound()
				if self.currDuration % self.numerator == 0:
					self.offset -= self.noteSpace
		
	def onStep(self):
		if self.stop == False:
			def playSound():
				if self.volume == True:
					if self.counter + 1 == len(self.notes) and self.reverse != True:
						self.stop = True
						soundFile = self.soundDict[self.pitches[self.counter]]
						simpleAudio.startSound(soundFile,async = True, loop = False)
					elif self.counter == 0:
						soundFile = self.soundDict[self.pitches[self.counter]]
						simpleAudio.startSound(soundFile,async = True, loop = False)
						self.stop = True 
					else:
						soundFile = self.soundDict[self.pitches[self.counter]]
						simpleAudio.startSound(soundFile,async = True, loop = True)

			def moveRight():
				self.timer += .25 
				if self.timer == self.notes[self.counter].duration:
					self.counter += 1
					self.highlight += 1 
					self.offset += self.noteSpace * self.notes[self.counter].duration
					self.currDuration += self.notes[self.counter].duration 
					self.timer = 0
					if self.currDuration % self.numerator == 0:
						self.offset += self.noteSpace
						self.currDuration += self.notes[self.counter].duration
						self.timer = 0 

			def moveLeft():
				self.timer -= .25
				if abs(self.timer) == self.notes[self.counter].duration:
					self.offset -= self.noteSpace * self.notes[self.counter].duration
					self.currDuration -= self.notes[self.counter].duration
					self.counter -= 1 
					self.highlight -= 1  
					self.timer = 0
					self.play = False 
					
				if self.currDuration % self.numerator == 0:
					self.offset -= self.noteSpace
					self.currDuration -= self.notes[self.counter].duration
					self.timer = 0

			if self.play == True:
				if self.counter < len(self.notes) - 1:
					moveRight()
				if self.timer == 0:
					playSound()

			elif self.play == False:
				if self.counter > 0:
					moveLeft()
				if self.timer == 0:
					playSound()

	def onMouse(self,event):
		xClick = event.x + self.offset

		if (xClick >= self.backButton.x0 + self.offset and xClick <= self.backButton.x1 + self.offset and 
			event.y >= self.backButton.y0 and event.y <= self.backButton.y1):
			self.home = True 

		def fretToggle():
			if (xClick >= self.fretButton.x0 + self.offset and xClick <= self.fretButton.x1 + self.offset and 
				event.y >= self.fretButton.y0 and event.y <= self.fretButton.y1):
				self.fingerboard.on += 1 

		def playback():
			if (xClick >= self.playButton.x0 + self.offset and xClick <= self.playButton.x1 + self.offset and 
				event.y >= self.playButton.y0 and event.y <= self.playButton.y1):
				self.play = True 
				self.reverse = False 
				self.stop = False 
			if (xClick >= self.pauseButton.x0 + self.offset and xClick <= self.pauseButton.x1 + self.offset and 
				event.y >= self.pauseButton.y0 and event.y <= self.pauseButton.y1):
				self.play = None
				simpleAudio.stopSound()
			if (xClick >= self.reverseButton.x0 + self.offset and xClick <= self.reverseButton.x1 + self.offset and 
				event.y >= self.reverseButton.y0 and event.y <= self.reverseButton.y1):
				self.play = False
				self.stop = False
				self.reverse = True 

		def mute():
			if (xClick >= self.muteButton.x0 + self.offset and xClick <= self.muteButton.x1 + self.offset and 
				event.y >= self.muteButton.y0 and event.y <= self.muteButton.y1):
				self.volume = False 
				simpleAudio.stopSound()

			if (xClick >= self.unMuteButton.x0 + self.offset and xClick <= self.unMuteButton.x1 + self.offset and 
				event.y >= self.unMuteButton.y0 and event.y <= self.unMuteButton.y1):
				self.volume = True 

		def tempo():
			if (xClick >= self.slowButton.x0 + self.offset and xClick <= self.slowButton.x1 + self.offset and 
				event.y >= self.slowButton.y0 and event.y <= self.slowButton.y1):
				self.timerDelay += 100 

			if (xClick >= self.fastButton.x0 + self.offset and xClick <= self.fastButton.x1 + self.offset and 
				event.y >= self.fastButton.y0 and event.y <= self.fastButton.y1):
				if self.timerDelay > 100:
					self.timerDelay -= 100 

		def restart():
			if (xClick >= self.restartButton.x0 + self.offset and xClick <= self.restartButton.x1 + self.offset and 
				event.y >= self.restartButton.y0 and event.y <= self.restartButton.y1):
				self.restart = True 

		fretToggle()
		playback()
		tempo()
		mute()
		restart()

	def onMouseMove(self,event):
		pass

	def onQuit(self):
		simpleAudio.stopSound()


class userNote(object):
	def __init__(self,left,right,top,bottom,duration,pitch,r):
		self.left = left
		self.right = right 
		self.top = top 
		self.bottom = bottom
		self.duration = duration 
		self.pitch = pitch
		self.r = r 

	def draw(self,canvas,offset,width):
		r = self.r
		left = self.left - r - offset
		right = self.left + r - offset
		top, bottom = self.top, self.bottom
		dy = float(top-bottom)
		middle = (top + bottom) / 2.0
		vOff = middle + 100 - r
		vOffD = middle - 100 + r
		time = self.duration 
		self.color = "black"

		qRest = "quarter_rest.gif"
		self.qRest = PhotoImage(file = qRest)
		sRest = "sixteenth_rest.gif"
		self.sRest = PhotoImage(file = sRest)
		eRest = "eighth_rest.gif"
		self.eRest = PhotoImage(file = eRest)

		if left <= 0:
			return
		elif left >= width:
			return
		else:
			if self.pitch == 73:
				if self.duration == 2.0:
					canvas.create_rectangle(left,top,right,middle, fill = "black")
				if self.duration == 4.0:
					canvas.create_rectangle(left + 162.5,middle,right + 162.5,bottom, fill = "black")
				if self.duration == 1.0:
					canvas.create_image((left+right)/2.0,top,image = self.qRest)
				if self.duration == .50:
					canvas.create_image((left+right) / 2.0, top, image = self.eRest)
				if self.duration == .25:
					canvas.create_image((left+right) / 2.0, top, image = self.sRest)

			if self.pitch in [36,37]:
				canvas.create_line(left - r,middle,right + r ,middle,width = 1.5)
				canvas.create_line(left-r,middle+dy,right+r,middle+dy,width = 1.5)
			if self.pitch == 38:
				canvas.create_line(left-r,middle+dy/2,right+r,middle+dy/2,width = 1.5)
			if self.pitch in [39,40]:
				canvas.create_line(left -r,middle,right + r ,middle,width = 1.5)

			if self.pitch in [60,61]:
				canvas.create_line(left - r,middle,right + r ,middle,width = 1.5)
			if self.pitch == 62:
				canvas.create_line(left - r,middle - dy/2,right + r ,middle-dy/2,width = 1.5)
			if self.pitch in [63,64]:
				canvas.create_line(left-r,middle,right+r,middle,width = 1.5)
				canvas.create_line(left-r,middle-dy,right+r,middle-dy,width = 1.5)
			if self.pitch in [65,66]:
				canvas.create_line(left-r,middle-(1.5 *dy),right+r,middle-(1.5*dy),width = 1.5)
				canvas.create_line(left-r,middle-dy/2,right+r,middle-dy/2,width = 1.5)
			if self.pitch in [67,68]:
				canvas.create_line(left-r,middle,right+r,middle,width = 1.5)
				canvas.create_line(left-r,middle-dy,right+r,middle-dy,width = 1.5)
				canvas.create_line(left-r,middle-dy*2,right+r,middle-dy*2,width = 1.5)
			if self.pitch == 69:
				canvas.create_line(left-r,middle-(1.5 *dy),right+r,middle-(1.5*dy),width = 1.5)
				canvas.create_line(left-r,middle-dy/2,right+r,middle-dy/2,width = 1.5)
				canvas.create_line(left-r,middle-(2.5 *dy),right+r,middle-(2.5*dy),width = 1.5)
			if self.pitch in [70,71]:
				canvas.create_line(left-r,middle,right+r,middle,width = 1.5)
				canvas.create_line(left-r,middle-dy,right+r,middle-dy,width = 1.5)
				canvas.create_line(left-r,middle-dy*2,right+r,middle-dy*2,width = 1.5)
				canvas.create_line(left-r,middle-dy*3,right+r,middle-dy*3,width = 1.5)
			if self.pitch == 72:
				canvas.create_line(left-r,middle-dy/2,right+r,middle-dy/2,width = 1.5)
				canvas.create_line(left-r,middle-(1.5 *dy),right+r,middle-(1.5*dy),width = 1.5)
				canvas.create_line(left-r,middle-(2.5 *dy),right+r,middle-(2.5*dy),width = 1.5)
				canvas.create_line(left-r,middle-(3.5 *dy),right+r,middle-(3.5*dy),width = 1.5)

			if self.pitch != 73:
				if self.pitch % 12 == 1 or self.pitch % 12 == 6 or self.pitch % 12 == 8:
					canvas.create_line(left-r-5,top,left-r-5,bottom,width = 2)
					canvas.create_line(left-r + 5,top,left-r + 5, bottom, width = 2)
					canvas.create_line(left-r*2,middle+5,left,middle+5, width = 2)
					canvas.create_line(left-r*2,middle-5,left,middle-5, width = 2)
				if self.pitch % 12 == 3 or self.pitch % 12 == 10:
					canvas.create_text(left-r, middle, text = "b", font = "Arial 20 bold ")

			if time == .50 and self.pitch < 73:
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)
				if self.pitch <= 50:
					canvas.create_line(right,vOffD,right,middle, width = 3)
					x1,y1 = right + 20, vOffD + 25 
					canvas.create_line(right,vOffD,x1,y1, width = 3) #slanted 
					canvas.create_line(x1,y1,x1,y1+20, width = 3)  #vertical line down 
				else:
					canvas.create_line(left,middle,left,vOff, width = 3)
					x1,y1 = left + 20, vOff - 25
					canvas.create_line(left,vOff,x1,y1,width = 3)  #slanted 
					canvas.create_line(x1,y1,x1,y1-20,width = 3)   #vertical line down 

			if time == .25 and self.pitch < 73:
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)
				if self.pitch <= 50:
					canvas.create_line(right,vOffD,right,middle, width = 3)
					x1,y1 = right + 15, vOffD + 25 
					canvas.create_line(right,vOffD,x1,y1, width = 3)
					canvas.create_line(x1,y1,x1,y1+20, width = 3)

					x2, y2 = x1 - 5, y1 + 5
					canvas.create_line(right, vOffD + 15, x2, y2, width = 3)
					canvas.create_line(x2,y2,x2,y2 + 15, width = 3)

				else:
					canvas.create_line(left,middle,left,vOff, width = 3)
					x1,y1 = left + 15, vOff - 25
					canvas.create_line(left,vOff,x1,y1,width = 3)
					canvas.create_line(x1,y1,x1,y1-20,width = 3)

					x2, y2 = x1 - 5, y1 - 5

					canvas.create_line(left,vOff - 15, x2, y2, width = 3)
					canvas.create_line(x2,y2,x2,y2 - 15, width = 3)

			if time == 1.0 and self.pitch < 73:
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)
				if self.pitch <= 50: #D3
					canvas.create_line(right,vOffD,right,middle, width = 3)
				else:
					canvas.create_line(left,middle,left,vOff, width = 3)
			if time == 2.0 and self.pitch < 73:
				if self.color == "black":
					self.color = None
				canvas.create_oval(left,top,right,bottom,width = 2,fill = self.color)
				if self.pitch <= 50: #D3
					canvas.create_line(right,vOffD,right,middle, width = 3)
				else:
					canvas.create_line(left,middle,left,vOff, width = 3)
			if time == 4.0 and self.pitch < 73:
				if self.color == "black":
					self.color = None
				canvas.create_oval(left,top,right,bottom,width = 2, fill = self.color)

class User(Page):
	def __init__(self,width,height):
		simpleAudio.stopSound()
		self.timerDelay = 500 
		self.width, self.height = width, height 
		self.aboutText = self.windowTitle = "User Cello Composer"
		self.margin = 50 
		self.x0, self.y0, self.x1, self.y1 = 0, 0, self.width, self.height

		self.staff = Staff(self.x0,self.y0,self.x1,self.y1)

		self.userPath = stream.Stream()
		self.time = meter.TimeSignature("4/4")
		self.userPath.append(self.time)

		self.numerator = self.userPath.flat.getElementsByClass("TimeSignature")[0].numerator
		self.denominator = self.userPath.flat.getElementsByClass("TimeSignature")[0].denominator

		self.fx0, self.fy0 = self.margin, self.margin * 3
		self.fx1, self.fy1 = self.x1 - self.margin, self.fy0 + self.margin * 2 

		self.notes = []
		self.vLines = []
		self.noteDict = dict()
		self.pathError = False 
		self.restart = None
		self.preset = None 
		self.instructionsVal = None 
		self.presetFile = None 
		self.home = False 

		self.dx = float(self.fx1-self.fx0) / 5
		self.dy = float(self.fy1-self.fy0) / 4 

		self.offset = 0
		self.durationCounter = 0 
		self.num = 0 

		self.r = self.dy / 2 
		self.lowY = self.fy1 + 2 * self.dy
		self.newI = 0 
		self.noteSpace = self.dx / 2.0
		self.left = self.fx0 + self.dx + self.noteSpace 
		self.prevLeft = self.fx0 + self.dx
		self.showKeys = 0
		self.accidental = 0 

		self.go = False 
		self.composition = False 
		self.GoButton = Button(50,350,150,400, text = "Go!")
		self.UndoButton = Button(50,425,150,475, text = "Undo")
		self.drawPad = Button(50,500,150,550, text = "Notepad")
		self.backButton = Button(50,575,150,625, text = "Home")

		self.sixteenthButton = Button(175,350,275,400, text = "")
		self.eightButton = Button(175,425,275,475, text = "")
		self.quarterButton = Button(300,350,400,400, text = "")
		self.halfButton = Button(300,425,400,475, text = "")
		self.sharpButton = Button(425,425,525,475, text = "Sharp/Flat")
		self.wholeButton = Button(175,500,275,550, text = "")
		self.restButton = Button(300,500,400,550, text = "Rest/Note")

		self.cButton = Button(850,350,900,400, text = "C")
		self.csharpButton = Button(900,350,950,400, text = "C#")
		self.dButton = Button(950,350,1000,400, text = "D")
		self.eflatButton = Button(1000,350,1050,400, text = "Eb")

		self.eButton = Button(850,400,900,450, text = "E")
		self.fButton = Button(900,400,950,450, text = "F")
		self.fsharpButton = Button(950,400,1000,450, text = "F#")
		self.gButton = Button(1000,400,1050,450, text = "G")

		self.gsharpButton = Button(850,450,900,500, text = "G#")
		self.aButton = Button(900,450,950,500, text = "A")
		self.bflatButton = Button(950,450,1000,500, text = "Bb")
		self.bButton = Button(1000,450,1050,500, text = "B")

		self.button2 = Button(750,350,800,400, text = "2")
		self.button3 = Button(750,400,800,450, text = "3")
		self.button4 = Button(750,450,800,500, text = "4")
		self.createRest = 0 

		self.currDuration = 1.0
		self.octave = 12
		self.pitch = 36 
		self.error = False

		self.hover = False
		self.hoverX = 0 
		self.hoverY = 0

		back = "cello_home.gif"
		self.back = PhotoImage(file = back)
		qRest = "quarter_rest.gif"
		self.qRest = PhotoImage(file = qRest)
		qNote = "qNote.gif"
		self.qNote = PhotoImage(file=qNote)
		sNote = "sixNote.gif"
		self.sNote = PhotoImage(file =sNote)
		wNote = "wNote.gif"
		self.wNote = PhotoImage(file=wNote)
		hNote = "hNote.gif"
		self.hNote = PhotoImage(file =hNote)
		eRest = "8note.gif"
		self.eRest = PhotoImage(file =eRest)

		def noteDictionary(): 
			r = self.r
			for i in xrange(36,73):  #C2 to C5 (cello range) 
				if i % 12 == 1: 
					self.noteDict[i] = self.noteDict[i-1]
				elif i % 12 == 3:
					self.noteDict[i] = self.noteDict[i-1]
				elif i % 12 == 6:
					self.noteDict[i] = self.noteDict[i-1]
				elif i % 12 == 8:
					self.noteDict[i] = self.noteDict[i-1]
				elif i % 12 == 10: 
					self.noteDict[i] = self.noteDict[i-1]
				else:
					self.noteDict[i] = ((self.lowY - r - r * self.newI), (self.lowY + r - r * self.newI))
					self.newI += 1 

			for i in xrange(36,73):
				if i % 12 == 3 or i % 12 == 10:
					self.noteDict[i] = self.noteDict[i+1]

			self.noteDict[73] = ((0,0))
			self.noteDict[73] = self.noteDict[50]

		noteDictionary()
				
	def onDraw(self,canvas):
		canvas.create_image(self.width / 2.0, self.height / 2.0, image = self.back)
		canvas.create_text(self.width / 2.0, self.margin / 2.0, text = "Create your own score!", font = "Arial 20", fill = "white")
		self.GoButton.draw(canvas)
		self.UndoButton.draw(canvas)

		self.sixteenthButton.draw(canvas)
		canvas.create_image(((self.sixteenthButton.x1 + self.sixteenthButton.x0) / 2.0), ((self.sixteenthButton.y0 + self.sixteenthButton.y1) / 2.0), image = self.sNote)
		self.eightButton.draw(canvas)
		canvas.create_image(((self.eightButton.x1 + self.eightButton.x0) / 2.0), ((self.eightButton.y0 + self.eightButton.y1) / 2.0), image = self.eRest)
		self.quarterButton.draw(canvas)
		canvas.create_image(((self.quarterButton.x1 + self.quarterButton.x0) / 2.0), ((self.quarterButton.y0 + self.quarterButton.y1) / 2.0), image = self.qNote)
		self.halfButton.draw(canvas)
		canvas.create_image(((self.halfButton.x1 + self.halfButton.x0) / 2.0), ((self.halfButton.y0 + self.halfButton.y1) / 2.0), image = self.hNote)
		self.wholeButton.draw(canvas)
		canvas.create_image(((self.wholeButton.x1 + self.wholeButton.x0) / 2.0), ((self.wholeButton.y0 + self.wholeButton.y1) / 2.0), image = self.wNote)
		self.drawPad.draw(canvas)
		self.restButton.draw(canvas)
		self.backButton.draw(canvas)

		if self.showKeys % 2 == 1:
			self.cButton.draw(canvas)
			self.csharpButton.draw(canvas)
			self.dButton.draw(canvas)
			self.eflatButton.draw(canvas)

			self.eButton.draw(canvas)
			self.fButton.draw(canvas)
			self.fsharpButton.draw(canvas)
			self.gButton.draw(canvas)

			self.gsharpButton.draw(canvas)
			self.aButton.draw(canvas)
			self.bButton.draw(canvas)
			self.bflatButton.draw(canvas)

			self.button2.draw(canvas)
			self.button3.draw(canvas)
			self.button4.draw(canvas)
			canvas.create_text(self.csharpButton.x1,self.csharpButton.y0 - 15, text = "Notepad", font = "Arial 20 bold", fill = "white")
			canvas.create_text(((self.button2.x1 + self.button2.x0) / 2.0), self.button2.y0 - 15, text = "Octave", font = "Arial 20 bold", fill = "white")
		
		elif self.showKeys % 2 == 0:
			self.sharpButton.draw(canvas)

		self.staff.draw(canvas, self.numerator, self.denominator,self.offset)

		for elem in self.notes:
			elem.draw(canvas,self.offset,self.width)
		for elem in self.vLines:
			elem.draw(canvas,self.offset,self.width)
		
		r = self.r 
		left = self.hoverX - r 
		right = self.hoverX + r 

		if self.hover == True:
			canvas.create_oval(left, self.hoverY - r,right, self.hoverY + r, fill = "yellow")
		if self.error == True:
			canvas.create_text(450,620,fill = "white", text = "Sum of notes in measure must be equal to time signature!", font = "Arial 20")
		if self.pathError == True:
			canvas.create_text(700,600,fill="white", text = "You must draw a note before clicking Go!", font = "Arial 20")

	def onMouse(self,event):
		xClick = event.x + self.offset
		self.error = False 

		if (xClick >= self.backButton.x0 + self.offset and xClick <= self.backButton.x1 + self.offset and 
			event.y >= self.backButton.y0 and event.y <= self.backButton.y1):
			self.home = True 

		def notePicker():
			if xClick >= self.cButton.x0 + self.offset and xClick <= self.cButton.x1 + self.offset:
				if event.y >= self.cButton.y0  and event.y <= self.cButton.y1 :
					self.pitch = 24 + self.octave
				elif event.y >= self.eButton.y0  and event.y <= self.eButton.y1 :
					self.pitch = 28 + self.octave
				elif event.y >= self.gsharpButton.y0  and event.y <= self.gsharpButton.y1 :
					self.pitch = 32 + self.octave

			elif xClick >= self.csharpButton.x0 + self.offset and xClick <= self.csharpButton.x1 + self.offset:
				if event.y >= self.cButton.y0  and event.y <= self.cButton.y1 :
					self.pitch = 25 + self.octave
				elif event.y >= self.eButton.y0  and event.y <= self.eButton.y1 :
					self.pitch = 29 + self.octave
				elif event.y >= self.gsharpButton.y0  and event.y <= self.gsharpButton.y1 :
					self.pitch = 33 + self.octave

			elif xClick >= self.dButton.x0 + self.offset and xClick <= self.dButton.x1 + self.offset:
				if event.y >= self.cButton.y0  and event.y <= self.cButton.y1 :
					self.pitch = 26 + self.octave
				elif event.y >= self.eButton.y0  and event.y <= self.eButton.y1 :
					self.pitch = 30 + self.octave
				elif event.y >= self.gsharpButton.y0  and event.y <= self.gsharpButton.y1 :
					self.pitch = 34 + self.octave

			elif xClick >= self.eflatButton.x0 + self.offset and xClick <= self.eflatButton.x1 + self.offset:
				if event.y >= self.cButton.y0  and event.y <= self.cButton.y1 :
						self.pitch = 27 + self.octave
				elif event.y >= self.eButton.y0  and event.y <= self.eButton.y1 :
					self.pitch = 31 + self.octave
				elif event.y >= self.gsharpButton.y0  and event.y <= self.gsharpButton.y1 :
					self.pitch = 35 + self.octave

		def octavePicker():
			if xClick >= self.button2.x0 + self.offset and xClick <= self.button2.x1 + self.offset:
				if event.y >= self.button2.y0 and event.y <= self.button2.y1:
					self.octave = 12
				elif event.y >= self.button3.y0 and event.y <= self.button3.y1:
					self.octave = 24 
				elif event.y >= self.button4.y0 and event.y <= self.button4.y1:
					self.octave = 36 

		def write():
			if xClick >= self.GoButton.x0 + self.offset and xClick <= self.GoButton.x1 + self.offset:
				if event.y >= self.GoButton.y0 and event.y <= self.GoButton.y1:
					if len(self.userPath) == 1:
						self.pathError = True 
					else:
						self.go = True
						self.show = False
						self.GoButton.color = "blue"
						self.listOfNotes = self.userPath.flat.getElementsByClass([note.Note, chord.Chord, note.Rest])
						self.newFile = self.userPath.write('musicxml')

		def changeDuration():
			if (xClick >= self.wholeButton.x0 + self.offset and xClick <= self.wholeButton.x1 + self.offset and
				event.y >= self.wholeButton.y0 and event.y <= self.wholeButton.y1):
					self.currDuration = 4.0

			if xClick >= self.sixteenthButton.x0 + self.offset and xClick <= self.sixteenthButton.x1 + self.offset:
				if event.y >= self.sixteenthButton.y0 and event.y <= self.sixteenthButton.y1:
					self.currDuration = .25
				elif event.y >= self.eightButton.y0 and event.y <= self.eightButton.y1:
					self.currDuration = .50

			elif xClick >= self.quarterButton.x0 + self.offset and xClick <= self.quarterButton.x1 + self.offset:
				if event.y >= self.quarterButton.y0 and event.y <= self.quarterButton.y1:
					self.currDuration = 1.0
				elif event.y >= self.halfButton.y0 and event.y <= self.halfButton.y1:
					self.currDuration = 2.0

		def drawNoteMouse():
			yTop = self.noteDict[72][0]
			yBot = self.noteDict[36][1]
			if len(self.notes) > 1:
				self.pathError = False 
			if self.showKeys % 2 == 1:
				if xClick >= self.prevLeft and xClick <= self.x1 + self.offset:
					if event.y >= yTop and event.y <= yBot:
						self.currNote = note.Note(self.pitch)
						self.currNote.quarterLength = self.currDuration
						self.duration = self.currDuration
						top, bottom = self.noteDict[self.pitch]
						if self.durationCounter + self.duration <= self.numerator:
							self.userPath.append(self.currNote)
							self.notes.append(userNote(self.left,self.left,top,bottom,self.duration,self.pitch,self.r))
							self.prevLeft = self.left 
							self.left += self.noteSpace * self.duration 
							self.durationCounter += self.duration
							self.offset += self.noteSpace * self.duration
						else:
							self.error = True 
						# if self.durationCounter % self.numerator == 0 and self.durationCounter != 0:
						# 	self.vLines.append(vLine(self.left,self.fy0,self.left,self.fy1))
						# 	self.left += self.noteSpace
						# 	self.offset += self.noteSpace 
						# 	self.durationCounter = 0
		def undo():
			if len(self.notes) > 0:
				if (xClick >= self.UndoButton.x0 + self.offset and xClick <= self.UndoButton.x1 + self.offset and
					event.y >= self.UndoButton.y0 and event.y <= self.UndoButton.y1):
					self.durationCounter -= self.duration 
					self.offset -= self.noteSpace * self.duration 
					self.left -= self.noteSpace * self.duration 

					if len(self.notes) > 0:
						if len(self.notes) > 2:
							self.prevLeft -= self.notes[-2].duration * self.noteSpace
						elif len(self.notes) == 2:
							self.prevLeft -= self.notes[1].duration * self.noteSpace
						else:
							self.prevLeft = self.fx0 + self.dx

					self.notes.pop(-1)
					self.userPath.pop(-1)

					if self.durationCounter % self.numerator == 0 and self.durationCounter != 0:
						self.prevLeft -= self.noteSpace
						self.left -= self.noteSpace
						self.offset -= self.noteSpace
						self.durationCounter = 0

		def drawDirect():
			if len(self.notes) > 1:
				self.pathError = False 
			if self.showKeys % 2 == 0:
				if self.accidental % 2 == 1:
					for key in self.noteDict:
						if key % 12 in [1,3,6,8,10]:
							top,bottom = self.noteDict[key]
							topCheck = top + 5 
							botCheck = bottom - 5 
							if xClick >= self.prevLeft and xClick <= self.x1 + self.offset and event.y >= topCheck and event.y <= botCheck:
								top, bottom = self.noteDict[key]
								currNote = note.Note(key)
								currNote.quarterLength = self.currDuration
								self.duration = currNote.quarterLength
								pitch = currNote.midi

								if self.durationCounter + self.duration <= self.numerator:
									self.userPath.append(currNote)
									self.notes.append(userNote(self.left,self.left,top,bottom,self.duration,pitch,self.r))
									self.prevLeft = self.left 
									self.left += self.noteSpace * self.duration 
									self.durationCounter += self.duration
									self.offset += self.noteSpace * self.duration
								else:
									self.error = True 

							# if self.durationCounter % self.numerator == 0 and self.durationCounter != 0:
							# 	self.vLines.append(vLine(self.left,self.fy0,self.left,self.fy1))
							# 	self.left += self.noteSpace
							# 	self.offset += self.noteSpace 
							# 	self.durationCounter = 0
				else:
					for key in self.noteDict:
						if key % 12 not in [1,3,6,8,10]:
							top,bottom = self.noteDict[key]
							topCheck = top + 5 
							botCheck = bottom - 5 
							if xClick >= self.prevLeft and xClick <= self.x1 + self.offset and event.y >= topCheck and event.y <= botCheck:
								top, bottom = self.noteDict[key]
								currNote = note.Note(key)
								currNote.quarterLength = self.currDuration
								self.duration = currNote.quarterLength
								pitch = currNote.midi

								if self.durationCounter + self.duration <= self.numerator:
									self.userPath.append(currNote)
									self.notes.append(userNote(self.left,self.left,top,bottom,self.duration,pitch,self.r))
									self.prevLeft = self.left 
									self.left += self.noteSpace * self.duration 
									self.durationCounter += self.duration
									self.offset += self.noteSpace * self.duration
								else:
									self.error = True 

							# if self.durationCounter % self.numerator == 0 and self.durationCounter != 0:
							# 	self.vLines.append(vLine(self.left,self.fy0,self.left,self.fy1))
							# 	self.left += self.noteSpace
							# 	self.offset += self.noteSpace 
							# 	self.durationCounter = 0

		def accidentalSelector():
			if (xClick >= self.sharpButton.x0 + self.offset and xClick <= self.sharpButton.x1 + self.offset and
			    event.y >= self.sharpButton.y0 and event.y <= self.sharpButton.y1):
					self.accidental += 1 

		def drawPad():
			if (xClick >= self.drawPad.x0 + self.offset and xClick <= self.drawPad.x1 + self.offset and
			    event.y >= self.drawPad.y0 and event.y <= self.drawPad.y1):
					self.showKeys += 1

		def restPicker():
			if (xClick >= self.restButton.x0 + self.offset and xClick <= self.restButton.x1 + self.offset and
			    event.y >= self.restButton.y0 and event.y <= self.restButton.y1):
					self.createRest += 1 

		def drawRest():
			yTop = self.noteDict[72][0]
			yBot = self.noteDict[36][1]
			if self.createRest % 2 == 1:
				if (xClick >= self.prevLeft and xClick <= self.x1 + self.offset and
					event.y >= yTop and event.y <= yBot):
					self.currRest = note.Rest()
					self.duration = self.currDuration
					self.currRest.quarterLength = self.duration
					pitch = 73 
					top, bottom = self.noteDict[50]

					if self.durationCounter + self.duration <= self.numerator:
						self.userPath.append(self.currRest)
						self.notes.append(userNote(self.left,self.left,top,bottom,self.duration,pitch,self.r))

						self.prevLeft = self.left 
						self.left += self.noteSpace * self.duration 
						self.durationCounter += self.duration
						self.offset += self.noteSpace * self.duration
					else:
						self.error = True 
				
		if self.durationCounter % self.numerator == 0 and self.durationCounter != 0:
			self.vLines.append(vLine(self.left,self.fy0,self.left,self.fy1))
			self.left += self.noteSpace
			self.offset += self.noteSpace 
			self.durationCounter = 0


		changeDuration()
		notePicker()
		octavePicker()
		octavePicker()
		notePicker()
		accidentalSelector()
		
		restPicker()
		write()
		undo()
		drawPad()

		if self.createRest % 2 == 1:
			drawRest()
		if self.createRest % 2 == 0:
			drawNoteMouse()
			drawDirect()
		
	def onKey(self,event):
		if event.keysym == "Right":
			self.offset += self.noteSpace 
			
		if event.keysym == "Left":
			self.offset -= self.noteSpace 
			
	def onMouseMove(self,event):
		xPos = event.x + self.offset
		yTop = self.noteDict[72][0]
		yBot = self.noteDict[36][1]

		if xPos >= self.prevLeft and xPos <= self.x1 + self.offset:
			if event.y > yTop and event.y < yBot:
				self.hoverX = event.x
				self.hoverY = event.y 
				self.hover = True 
			else:
				self.hover = False 
		else:
			self.hover = False

	def onStep(self):
		pass

	def onQuit(self):
		pass 

class Home(Page):
	def __init__(self,width,height):
		self.go = False
		self.preset = False 
		self.composition = False  
		self.instructionsVal = False 
		self.presetFile = None 
		self.timerDelay = 500
		self.restart = None
		self.home = False 
		self.width, self.height = width, height
		homepage = "cello_home.gif"  #cite pixshark.com 
		self.homepage = PhotoImage(file = homepage)

		r = 300
		self.presetsButton = Button(self.width/2.0 - r, self.height* 1.5 / 4.0 - r/8,
						 self.width/2.0 + r, self.height * 1.5 / 4.0 + r/8, text = "Play a preset!")

		self.compositionButton = Button(self.width/2.0 - r, (self.height * 2 / 4.0) - r/8, self.width/2.0 + r,
									 (self.height * 2 / 4.0) + r/8, text = "Write a Composition")

		self.instructions = Button(self.width/2.0 - r, (self.height * 2.5 / 4.0) - r/8, self.width/2.0 + r,
									 (self.height * 2.5 / 4.0) + r/8, text = "Instructions")

	def onMouse(self,event):
		xClick = event.x

		if (xClick >= self.compositionButton.x0 and xClick <= self.compositionButton.x1 and 
			event.y >= self.compositionButton.y0 and event.y <= self.compositionButton.y1):
			self.composition = True 

		if (xClick >= self.presetsButton.x0 and xClick <= self.presetsButton.x1 and 
			event.y >= self.presetsButton.y0 and event.y <= self.presetsButton.y1):
			self.preset = True 

		if (xClick >= self.instructions.x0 and xClick <= self.instructions.x1 and 
			event.y >= self.instructions.y0 and event.y <= self.instructions.y1):
			self.instructionsVal = True 

	def onKey(self,event):
		pass
	def onQuit(self):
		pass
	def onStep(self):
		pass
	def onMouseMove(self,event):
		pass
	def onDraw(self,canvas):

		canvas.create_image(550,350, image = self.homepage)
		canvas.create_text(self.width / 2.0, self.height / 8.0, text = "Cello Composer", fill = "white",
			font = "Arial 40 bold")
		canvas.create_text(self.width - 125, (self.height) - 25, text = "by: Akash Kejriwal", fill = "white", font = "Arial 20")
		self.compositionButton.draw(canvas)
		self.presetsButton.draw(canvas)
		self.instructions.draw(canvas)

class Instructions(Page):
	def __init__(self,width,height):
		self.go = False
		self.preset = False 
		self.composition = False  
		self.instructionsVal = False 
		self.presetFile = None 
		self.timerDelay = 500
		self.restart = None
		self.home = False 
		self.width, self.height = width, height
		homepage = "cello_home.gif"  #cite pixshark.com 
		self.homepage = PhotoImage(file = homepage)

		self.backButton = Button(self.width - 200,self.height / 8.0 - 25, self.width - 100,self.height / 8.0 + 25, text = "Back")

	def onMouse(self,event):
		xClick = event.x

		if (xClick >= self.backButton.x0 and xClick <= self.backButton.x1 and 
			event.y >= self.backButton.y0 and event.y <= self.backButton.y1):
			self.home = True 

	def onKey(self,event):
		pass
	def onQuit(self):
		pass
	def onStep(self):
		pass
	def onMouseMove(self,event):
		pass
	def onDraw(self,canvas):
		canvas.create_image(550,350, image = self.homepage)
		canvas.create_text(self.width / 2.0, self.height / 8.0, text = "Instructions", fill = "white",
			font = "Arial 40 bold")

		canvas.create_rectangle(100,150,1000,600, width = 15, outline = "white")
		canvas.create_text(550,185,text = "Composition", font = "Arial 20 bold underline", fill = "white")
		canvas.create_text(550,285,text = "Use the left and right key to slide the staff \n" +
			"Draw directly on the staff by clicking or by using the notepad option \n" +
			"Click on the sharp/flats toggle to draw sharps or flats \n" +
			"Click on any of the durations to change length of note \n" + 
			"Create a rest note by clicking on the note/rest toggle \n" + 
			"Undo button will undraw the previous note/rest"
			,font = "Arial 16 ", fill = "white", justify = CENTER)

		canvas.create_text(550,385,text = "Reader", font = "Arial 20 bold underline", fill = "white")
		canvas.create_text(550,485,text = "Use the left and right key to slide the staff \n" +
			"Play, pause, or reverse \n" +
			"Mute or unmute the sound \n" +
			"Speed up or slow down the tempo \n" + 
			"Restart from the beginning \n" + 
			"Turn frets on/off to see fingering positions \n"
			,font = "Arial 16 ", fill = "white", justify = CENTER)

		self.backButton.draw(canvas)

class Presets(Page):
	def __init__(self,width,height):
		self.go = False
		self.preset = False 
		self.composition = False  
		self.instructionsVal = False 
		self.timerDelay = 500
		self.restart = None
		self.width, self.height = width, height
		homepage = "cello_home.gif" 
		self.homepage = PhotoImage(file = homepage)
		self.home = False 

		self.presetFile = None 

		r = 300
		self.song1 = Button(self.width/2.0 - r, self.height* 1.5 / 4.0 - r/8,
						 self.width/2.0 + r, self.height * 1.5 / 4.0 + r/8, text = "Bach Cello Suite No 1, Prelude, G Major")

		self.song2 = Button(self.width/2.0 - r, (self.height * 2 / 4.0) - r/8, self.width/2.0 + r,
									 (self.height * 2 / 4.0) + r/8, text = "Bach Cello Suite No 1, Courante, G Major")

		self.song3 = Button(self.width/2.0 - r, (self.height * 2.5 / 4.0) - r/8, self.width/2.0 + r,
									 (self.height * 2.5 / 4.0) + r/8, text = "3 Octave C Major Scale")

		self.backButton = Button(self.width - 200,self.height / 8.0 - 25, self.width - 100,self.height / 8.0 + 25, text = "Back")

	def onMouse(self,event):
		xClick = event.x

		if (xClick >= self.song1.x0 and xClick <= self.song1.x1 and 
			event.y >= self.song1.y0 and event.y <= self.song1.y1):
			self.presetFile = 1

		if (xClick >= self.song2.x0 and xClick <= self.song2.x1 and 
			event.y >= self.song2.y0 and event.y <= self.song2.y1):
			self.presetFile = 2

		if (xClick >= self.song3.x0 and xClick <= self.song3.x1 and 
			event.y >= self.song3.y0 and event.y <= self.song3.y1):
			self.presetFile = 3 

		if (xClick >= self.backButton.x0 and xClick <= self.backButton.x1 and 
			event.y >= self.backButton.y0 and event.y <= self.backButton.y1):
			self.home = True 

	def onKey(self,event):
		pass
	def onQuit(self):
		pass
	def onStep(self):
		pass
	def onMouseMove(self,event):
		pass
	def onDraw(self,canvas):

		canvas.create_image(550,350, image = self.homepage)
		canvas.create_text(self.width / 2.0, self.height / 8.0, text = "Presets", fill = "white",
			font = "Arial 40 bold")
		self.song1.draw(canvas)
		self.song2.draw(canvas)
		self.song3.draw(canvas)
		self.backButton.draw(canvas)
		
class Demo(eventBasedAnimation.Animation):
	def onInit(self):
		self.aboutText = self.windowTitle = "Cello Composer!"
		self.filename = ""
		self.page = Home(self.width, self.height)

	def onDraw(self,canvas):
		self.page.onDraw(canvas)

	def onKey(self,event):
		self.page.onKey(event)

	def onStep(self):
		self.page.onStep()

	def onQuit(self):
		self.page.onQuit()

	def onMouse(self,event):
		self.page.onMouse(event)

		if self.page.go == True:
			self.filename = self.page.newFile
			self.page = Reader(self.width,self.height,self.filename)
		self.timerDelay = self.page.timerDelay

		if self.page.restart == True:
			self.page = Reader(self.width, self.height, self.filename)
			self.page.restart = False 

		if self.page.composition == True:
			self.page = User(self.width, self.height)

		if self.page.preset == True:
			self.page = Presets(self.width,self.height)
		
		if self.page.presetFile == 1:
			bach = 'bwv1007-01.xml'  
			self.page = Reader(self.width,self.height,bach)
		if self.page.presetFile == 2:
			bach3 = 'bwv1007-03.xml' 
			self.page = Reader(self.width, self.height, bach3)
		if self.page.presetFile == 3:
			c = "c_major.xml"
			self.page = Reader(self.width, self.height, c)

		if self.page.instructionsVal == True:
			self.page = Instructions(self.width, self.height)

		if self.page.home == True:
			simpleAudio.stopSound()
			self.page.home = False 
			self.page = Home(self.width, self.height)
	def onMouseMove(self,event):
		self.page.onMouseMove(event)

Demo(width = 1100, height = 700, timerDelay = 500).run()

