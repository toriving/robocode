#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot #Import a base Robot


class Demo(Robot): #Create a Robot
    
    def init(self):# NECESARY FOR THE GAME   To initialyse your robot
        
        
        #Set the bot color in RGB
        self.setColor(0, 200, 100)
        self.setGunColor(200, 200, 0)
        self.setRadarColor(255, 60, 0)
        self.setBulletsColor(0, 200, 100)
        
        #get the map size
        size = self.getMapSize() #get the map size
        self.radarVisible(True) # show the radarField
        
    
    def run(self): #NECESARY FOR THE GAME  main loop to command the bot
        
        
        self.move(100) # for moving (negative values go back)
        self.stop()
        """
        the stop command is used to make moving sequences: here the robot will move 100 pixel and next, fire
        """

        self.fire(3) # To Fire (bullet between 1 and 10)
