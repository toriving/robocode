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

    def sensors(self):  #NECESARY FOR THE GAME
        """Tick each frame to have datas about the game"""

        pos = self.getPosition() #return the center of the bot
        x = pos.x() #get the x coordinate
        y = pos.y() #get the y coordinate

        angle = self.getGunHeading() #Returns the direction that the robot's gun is facing
        angle = self.getHeading() #Returns the direction that the robot is facing
        angle = self.getRadarHeading() #Returns the direction that the robot's radar is facing
        list = self.getEnemiesLeft() #return a list of the enemies alive in the battle
        for robot in list:
            id = robot["id"]
            name = robot["name"]
            # each element of the list is a dictionnary with the bot's id and the bot's name

    def onHitWall(self):
        self.reset() #To reset the run fonction to the begining (auomatically called on hitWall, and robotHit event)
        self.pause(100)
        self.move(-100)
        self.rPrint('ouch! a wall !')
        self.setRadarField("large") #Change the radar field form