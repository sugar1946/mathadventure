import spyral
import Main

def main():
	spyral.director.init(size=(0, 0), max_ups=30, max_fps=30, fullscreen=False, caption='The Game')
	spyral.director.push(Main.Main())
	spyral.director.push(Board.Board())
	#spyral.event.register("input.keyboard.down.r", spyral.director.push(self.scene2))
	#self.sene2 = spyral.Scene.__init__(self,SIZE2)
