import spyral
import random
import math

class StoreForm(spyral.Form):
	def setButtomImage(self,item):
		image_up: item
		image_up_hovered: item
		image_up_focused: item
		image_down: item
		image_down_hovered: item
		image_down_focused: item
		nine_slice: True
	#answer_input = spyral.widgets.TextInput(100, "")
	store_button = spyral.widgets.Button("Item")
	whichButton = 1


class Store(spyral.Scene):


	def __init__(self, character):
        spyral.Scene.__init__(self, SIZE)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
		button_row = [3]
		for row_value in button_row:
			temp = StoreForm(self)
			temp.store_button.x = row_value
			temp.store_button.y = column_value
			temp.setButtonImage("game/store/gem.bmp")
        #spyral.event.register('director.update', self.update)
	
	def setScene
