#animated banner program 
#by Xiaosheng Wu 11/05/2015
#modified from the website   UsingPython.com/programs
import os
import time

# the width of the play 
###
WIDTH = 79
#
# the message we wish to print 
message = "WilsonWu".upper()
# the printed banner version of the message
# this is a 7-line diaplay, stored as 7 strings
# initially, these are empty
printedMessage = [ "", "", "","","","","" ]
# a dictionary mapping letters to their 7-lines banner display 
# each letter in the dictionary maps to 7 strings, one for each line of the display
characters= {" " : [  " ",
					  " ",
				      " ",
				      " ",
				      " ",
				      " ",
	                  " " ],

		   "W" : [ "*          * ",
				   "*          * ",
				   " *         * ",
				   " *    *    * ",
				   " *   * *  *  ",
				   "  * *   * *  ",
				   "   *     *   " ],

			"U": [ "       ",
                   "       ",
                   "       ",
                   " *   * ",
                   " *   * ",
                   " *   * ",
                   " ***** " ],
			
		   "I" : [ "     ",
				   " *** ",
				   " *** ",
				   "  *  ",
				   "  *  ",
				   "  *  ",
				   "  *  " ],
		   
		   "L" : [ "  **  ",
				   "  **  ",
				   "  **  ",
				   "  **  ",
				   "  **  ",
				   "  **  ",
				   "  **  " ],

		 "S" : [   "        ",
				   "        ",
				   "  ****  ",
				   "  *     ",
				   "  ****  ",
				   "     *  ",
				   "  ****  " ],
		   "O" : [ "       ",
                   "       ",
                   " ***** ",
                   " *   * ",
                   " *   * ",
                   " *   * ",
                   " ***** " ],
		    "N" : ["       ",
                   "       ",
                   " ***** ",
                   " *   * ",
                   " *   * ",
                   " *   * ",
                   " *   * " ]    # finally done.......
		   }
# build up the printed banner. the 1st row of the display is
# created for each character in the message, followed by the second line...
#build up the printed banner. to do this, the 1st row of the
#display is created for each character in the message, followed by
#the second line
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

#the offset is how far to the right we want to print the message.
#initially, we want to print the message just off the display.
offset = WIDTH
while True:
    os.system("cls")
    #print each line of the message, including the offset.
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    #move the message a little to the left.
    offset -=1
    #if the entire message has moved 'through' the display then
    #start again from the right hand side.
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    #take out or change this line to speed up / slow down the display
    time.sleep(0.05)

