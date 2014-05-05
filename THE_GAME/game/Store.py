import spyral
import random
import math
import Item
import Board

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
FONT_PATH = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
ITEM_BOUGHT_LIST = []

class ItemSprite(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename=img)
		self.x = x
		self.y = y

class ItemText(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y


class Store(spyral.Scene):
	def __init__(self,character):
		spyral.Scene.__init__(self, SIZE)
		self.background = spyral.Image(size=SIZE).fill((255,255,255))
		spyral.event.register("system.quit", spyral.director.pop)
		spyral.event.register("input.keyboard.down.q", self.closeStore)
		spyral.event.register("input.keyboard.down.a", self.buyHealth)#buy health
		spyral.event.register("input.keyboard.down.b", self.buyGem)#buy gem
		spyral.event.register("input.keyboard.down.c", self.buyChest)#buy gem
		spyral.event.register("input.keyboard.down.e", self.buySprite1)#buy sprite1
		self.shopFont = spyral.Font(FONT_PATH,24,(0,0,0))#font used for header
		self.itemFont = spyral.Font(FONT_PATH,14,(0,0,0))#font used for prices
		row_val = [(HEIGHT/4.5),(HEIGHT/2),(HEIGHT/1.286)]
		column_val = [0,(WIDTH/4),(WIDTH/2),(WIDTH/1.34)]
		itemSelection = ["a)","b)","c)","d)","e)","f)","g)","h)","i)","j)","k)","l)"]
		itemPrice = ["500"]
		itemSelectionIndex = 0
		self.player = character

		for row_value in row_val:
			for column_value in column_val:
				itemString = self.itemFont.render(itemSelection[itemSelectionIndex])
				itemSelectionIndex += 1
				itemSelectionText = ItemText(self,itemString,(column_value + 10),row_value)
				itemImg = ItemSprite(self,"game/store/gem.bmp",(column_value + 70),row_value)
				itemPriceImg = self.itemFont.render("Price: " + itemPrice[0])
				itemPriceImgText = ItemText(self,itemPriceImg,(column_value + 70),(row_value + 80))
				itemDescription = self.itemFont.render("This is a temp value")
				itemSelectionDescription = ItemText(self,itemDescription,(column_value + 70),(row_value + 110))
				
	def closeStore(self):
		self.player.vel = 100
		self.sceneReturn.setCharacter(self.player,self.player.ani_array)
		spyral.director.pop()			
				
	def buyHealth(self):
		#need to check if if player has enough points
		self.player.health = 150

	def buyGem(self):
		self.sceneReturn.addGem()

	def buyChest(self):
		self.sceneReturn.addChest()

	def buySprite1(self):
		self.player.ani_array = ["game/images/Animations/linkanimationdown.txt","game/images/Animations/stop2.bmp","game/images/Animations/leftanimation.txt","game/images/Animations/stop2l.bmp",'','','','']
		

	def setSceneReturn(self,scene):
		self.sceneReturn = scene
