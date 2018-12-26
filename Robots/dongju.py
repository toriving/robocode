#! /usr/bin/python
# -*- coding: utf-8 -*-

from robot import Robot  # Import a base Robot


class Dongju(Robot):  # Create a Robot

    def init(self):  # NECESARY FOR THE GAME   To initialyse your robot


        # Set the bot color in RGB
        self.setColor(255, 255, 255)
        self.setGunColor(255, 255, 255)
        self.setRadarColor(255, 255, 255)
        self.setBulletsColor(255, 255, 255)

        # get the map size

        self.radarVisible(True)  # show the radarField
        self.init = True
        self.seige = False
        self.setRadarField("thin")
        self.lockRadar("gun")
        self.size = self.getMapSize()  # get the map size
        self.map_x = self.size.width()
        self.map_y = self.size.height()

    def run(self):  # NECESARY FOR THE GAME  main loop to command the bot
        x, y = self.position()
        if self.init:
            self.initial_move()
            self.init = False
        if (self.map_x - 100 < x and y < 100) or (x < 100 and self.map_y - 100 < y) or (x < 100 and y < 100) or (self.map_x - 100 < x and self. map_y - 100 < y) or self.seige:
            self.gunTurn(90)

        # self.seige = True

    def position(self):
        pos = self.getPosition()
        x = pos.x()
        y = pos.y()
        return x, y

    def initial_move(self):
        x, y = self.position()
        if y < self.map_y / 2:
            if x < self.map_x/2:
                self.turn(180)
                self.gunTurn(180)
                self.stop()
                self.move(int(y) - 35)
                self.stop()
                self.turn(-90)
                self.gunTurn(90)
                self.stop()
                self.move(int(x - 35))
                self.stop()
            else:
                self.turn(180)
                self.gunTurn(180)
                self.stop()
                self.move(int(y) - 35)
                self.stop()
                self.turn(90)
                self.gunTurn(90)
                self.stop()
                self.move(int(self.map_x - x - 35))
                self.stop()
        else:
            if x < self.map_x / 2:
                self.move(int(self.map_y - y - 35))
                self.stop()
                self.turn(90)
                self.gunTurn(90)
                self.stop()
                self.move(int(x - 35))
                self.stop()
            else:
                self.move(int(self.map_y - y - 35))
                self.stop()
                self.turn(-90)
                self.gunTurn(-90)
                self.stop()
                self.move(int(self.map_x - x - 35))
                self.stop()

    def sensors(self):  # NECESARY FOR THE GAME
        """Tick each frame to have datas about the game"""
        pass
    def onHitByRobot(self, robotId, robotName):
        # self.reset()
        self.seige = True
        self.rPrint("damn a bot collided me!")

    def onHitWall(self):
        self.reset()  # To reset the run fonction to the begining (auomatically called on hitWall, and robotHit event)
        self.pause(100)
        self.move(-100)
        self.rPrint('ouch! a wall !')
        self.move(100)

    def onRobotHit(self, robotId, robotName):  # when My bot hit another
        self.rPrint('collision with:' + str(
            robotName))  # Print information in the robotMenu (click on the righ panel to see it)

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):  # NECESARY FOR THE GAME
        """ When i'm hit by a bullet"""
        self.rPrint("hit by " + str(bulletBotName) + "with power:" + str(bulletPower))

    def onBulletHit(self, botId, bulletId):  # NECESARY FOR THE GAME
        """when my bullet hit a bot"""
        self.rPrint("fire done on " + str(botId))

    def onBulletMiss(self, bulletId):  # NECESARY FOR THE GAME
        """when my bullet hit a wall"""
        self.rPrint("the bullet " + str(bulletId) + " fail")
        # self.pause(10) #wait 10 frames

    def onRobotDeath(self):  # NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint("damn I'm Dead")

    def onTargetSpotted(self, botId, botName, botPos):  # NECESARY FOR THE GAME
        "when the bot see another one"
        x, y = self.position()
        if (self.map_x - 100 < x and y < 100) or (x < 100 and self.map_y - 100 < y) or (x < 100 and y < 100) or (self.map_x - 100 < x and self. map_y - 100 < y):
            self.gunTurn(2)
            self.fire(2)
        elif self.seige:
            self.gunTurn(2)
            self.fire(2)
