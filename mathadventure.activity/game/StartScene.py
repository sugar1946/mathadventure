import spyral
import PlayerSelectionScene
import Tutorial
from spyral import Sprite, Animation, easing

SIZE = (1200,900)
WIDTH = 1200
HEIGHT = 900
class StartScene(spyral.Scene):
    def __init__(self, *args, **kwargs):
            spyral.Scene.__init__(self, SIZE)
            image = spyral.Image(filename="game/sceneImages/bg.png")
            image.scale((1200,900))
            self.background = image

            self.logo = Logo(self,"1")
            ani = Animation('y', easing.Linear(-200, 200), 2)
            self.logo.animate(ani)

            self.start = Logo(self, "2")
            self.tut = Logo(self,"3")

            self.arrow = Selector(self)

            spyral.event.register("input.keyboard.down.q", spyral.director.pop)
            spyral.event.register("input.keyboard.down.return", self.arrow.select)
            spyral.event.register("input.keyboard.down.up", self.arrow.up)
            spyral.event.register("input.keyboard.down.down", self.arrow.down)
            spyral.event.register("Logo.y.animation.end", self.arrow.set)
            

class Logo(spyral.Sprite):
    def __init__(self,scene,pick):
        spyral.Sprite.__init__(self, scene)

        if (pick == "1"):
            self.image = spyral.Image(filename="game/sceneImages/Title.png")
            self.anchor = "center"
            self.x = WIDTH/2
            self.y = 200
        elif (pick == "2"):
            self.image = spyral.Image(filename="game/sceneImages/startgame.png")
            self.anchor = "center"
            self.x = WIDTH/2 - 7
            self.y = HEIGHT - 317
        elif (pick == "3"):
            self.image = spyral.Image(filename="game/sceneImages/Tut.png")
            self.anchor = "center"
            self.x = WIDTH/2 - 7
            self.y = HEIGHT - 230

class Selector(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(filename="game/sceneImages/arrow.png")
        self.pick = "none"

    def set(self):
        self.anchor = "center"
        self.x = 395
        self.y = HEIGHT - 317
        self.pick = "up"

    def up(self):
        self.y = HEIGHT - 317
        self.pick = "up"

    def down(self):
        self.y = HEIGHT - 230
        self.pick = "down"

    def select(self):
        if (self.pick == "up"):
            self.startGame()
        elif (self.pick == "down"):
            self.openTutorial()

    def startGame(self):
        spyral.director.replace(PlayerSelectionScene.PlayerSelectionSceneMain())

    def openTutorial(self):
        spyral.director.replace(Tutorial.Tutorial())