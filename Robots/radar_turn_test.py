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
        
        
        self.radarTurn(90) #to turn the radar (negative values turn counter-clockwise)
        self.stop()
        """
        the stop command is used to make moving sequences: here the robot will turn the radar 90° and next, fire
        """

        self.fire(3) # To Fire (power between 1 and 10)
