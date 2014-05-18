import spyral
import PlayerSelectionScene
SIZE = (1200,900)
class Tutorial(spyral.Scene):
	def __init__(self, *args, **kwargs):
			spyral.Scene.__init__(self, SIZE)
			self.imageList = ["game/images/TutorialImages/Monsters.png","game/images/TutorialImages/Gems.png","game/images/TutorialImages/Chests.png","game/images/TutorialImages/Store.png","game/images/TutorialImages/StartGame.png"]
                        self.image = spyral.Image(filename=("game/images/TutorialImages/Start.png"))
			self.image.scale((1200,900))
			self.background = self.image
                        self.image_index=0
			spyral.event.register("input.keyboard.down.q", spyral.director.pop)
			spyral.event.register("input.keyboard.down.s", self.startGame)
                        spyral.event.register("input.keyboard.down.right", self.setNextImage)
			spyral.event.register("input.keyboard.down.s", self.startGame)

                                                  
        def setNextImage(self):
                if (self.image_index < len(self.imageList)):
                        self.image = spyral.Image(filename=(self.imageList[self.image_index]))
                        self.image.scale((1200,900))
                        self.background = self.image
                        self.image_index += 1   
                                                  
	def startGame(self):
		spyral.director.replace(PlayerSelectionScene.PlayerSelectionSceneMain())

		
