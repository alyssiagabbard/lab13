#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="Up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.button1 = Button(self.myContainer1)
       	    self.button1.configure(text="Left", background="blue")
       	    self.button1.grid(row=0, column=1)
       	    self.button1.bind("<Button-1>", self.button1Clicked)
       	    
       	    self.button2 = Button(self.myContainer1)
       	    self.button2.configure(text="Right", background="orange")
       	    self.button2.grid(row=0, column=2)
       	    self.button2.bind("<Button-1>", self.button2Clicked)
       	    
       	    self.button3 = Button(self.myContainer1)
       	    self.button3.configure(text="Down", background="red")
       	    self.button3.grid(row=1, column=3)
       	    self.button3.bind("<Button-1>", self.button3Clicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	def button1Clicked(self, event):
            global drawpad
            global player
            drawpad.move(player,-20,0)
            
        def button2Clicked(self, event):
            global player
            global drawpad
            drawpad.move(player,20,0)
            
        def button3Clicked(self,event):
            global player
            global drawpad
            drawpad.move(player,0,-20)	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
		
app = MyApp(root)
root.mainloop()