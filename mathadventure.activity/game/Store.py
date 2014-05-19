import spyral
import random
import math
import Item
import Board

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
FONT_PATH = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

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

class PurchaseText(spyral.Sprite):
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
		spyral.event.register("input.keyboard.down.x", self.closeStore)
		spyral.event.register('director.update', self.update)
		self.message = ''
		spyral.event.register("input.keyboard.down.a", self.buyHealth)#buy health
		spyral.event.register("input.keyboard.down.b", self.buyGem)#buy gem
		spyral.event.register("input.keyboard.down.c", self.buyChest)#buy gem
		spyral.event.register("input.keyboard.down.d", self.buyKey)#buy key
		spyral.event.register("input.keyboard.down.e", self.buySprite1)#buy sprite1
		spyral.event.register("input.keyboard.down.f", self.buySprite2)#buy sprite2
		spyral.event.register("input.keyboard.down.g", self.buySprite3)#buy sprite3
		spyral.event.register("input.keyboard.down.h", self.buySprite4)#buy sprite4
		spyral.event.register("input.keyboard.down.i", self.buySprite5)#buy sprite5
		spyral.event.register("input.keyboard.down.j", self.buySprite6)#buy sprite6
		spyral.event.register("input.keyboard.down.k", self.buySprite7)#buy sprite7
		self.playerScoreFont = spyral.Font(FONT_PATH,18,(0,255,0))#font used for header
		self.shopFont = spyral.Font(FONT_PATH,24,(0,0,0))#font used for header
		self.itemFont = spyral.Font(FONT_PATH,14,(0,0,0))#font used for prices
		self.purchaseFont = spyral.Font(FONT_PATH,18,(255,0,0))#font used for purchase status
		self.storeHeaderFont = spyral.Font(FONT_PATH,80,(0,0,0))#font used for purchase status
		storeHeaderImg = self.storeHeaderFont.render("STORE")
		itemSelectionText = ItemText(self,storeHeaderImg,(WIDTH/3),(20))
		self.storeQuitFont = spyral.Font(FONT_PATH,18,(0,0,0))#font used for purchase status
		storeInstImg1 = self.storeQuitFont.render("Press the key next to")
		storeInstImg2 = self.storeQuitFont.render("the item to purchase it.")
		storeInstImg3 = self.storeQuitFont.render("Press x to exit the store")
		itemInstText1 = ItemText(self,storeInstImg1,20,20)
		itemInstText2 = ItemText(self,storeInstImg2,20,50)
		itemInstText3 = ItemText(self,storeInstImg3,20,80)
		self.purchaseMessage = ''
		row_val = [(HEIGHT/4.5),(HEIGHT/2),(HEIGHT/1.286)]
		column_val = [0,(WIDTH/4),(WIDTH/2),(WIDTH/1.34)]
		itemSelection = ["a)","b)","c)","d)","e)","f)","g)","h)","i)","j)","k)"]
		itemPrice = ["10","20","20","200","Free","Free","120","120","120","120","120"]
		itemImageArray = self.setItemImgArray("game/store/imgFile.txt")
		itemDescrip = self.setItemImgArray("game/store/itemText.txt")
		itemSelectionIndex = 0
		self.player = character
		self.playerScoreImage = self.playerScoreFont.render("Available Points to Spend: "+str(self.player.totalScore))
		self.scoreImg = ItemText(self,self.playerScoreImage,20, 100)

		for row_value in row_val:
			for column_value in column_val:
				if(itemSelectionIndex < 11):	
					itemString = self.itemFont.render(itemSelection[itemSelectionIndex])
					itemSelectionText = ItemText(self,itemString,(column_value + 10),row_value)
					itemImg = ItemSprite(self,itemImageArray[itemSelectionIndex],(column_value + 70),row_value)
					itemPriceImg = self.itemFont.render("Price: " + itemPrice[itemSelectionIndex])
					itemPriceImgText = ItemText(self,itemPriceImg,(column_value + 90),(row_value + 140))
					itemDescription = self.itemFont.render(itemDescrip[itemSelectionIndex])
					itemSelectionDescription = ItemText(self,itemDescription,(column_value + 70),(row_value + 180))
					itemSelectionIndex += 1

	def setItemImgArray(self,animationPath):
		data=[]                               # will hold the lines of the file
		with open(animationPath,'rU') as fin:
			for line in fin:                  # for each line of the file
				line=line.strip()             # remove CR/LF
				if line:                      # skip blank lines
					data.append(line)
		return data

	def update(self,delta):
		if(self.message != ''):
			if(self.purchaseMessage == ''):
				img = self.purchaseFont.render(self.message)
				self.purchaseMessage = PurchaseText(self,img,(WIDTH/1.34),50)
				self.message = ''
			else:
				self.purchaseMessage.kill()
				img = self.purchaseFont.render(self.message)
				self.purchaseMessage = PurchaseText(self,img,(WIDTH/1.34),50)
				self.message = ''
		self.playerScoreImage = self.playerScoreFont.render("Available Points to Spend: "+str(self.player.totalScore))
		self.scoreImg.kill()
		self.scoreImg = ItemText(self,self.playerScoreImage,20, 100)
						
	def closeStore(self):
		#self.sceneReturn.setCharacter(self.player,self.player.ani_array)
		self.player.initialize(self.sceneReturn,self.player.ani_array)
		spyral.director.pop()
		self.sceneReturn.defreezeMonster()
	
	def points(self):
		self.player.totalScore = 1200
		self.player.keys = 3				
				
	def buyHealth(self):
		#need to check if if player has enough points
		if(self.player.totalScore >= 10):
			self.player.health = 150
			self.player.totalScore -= 10
			self.message = "Health was replenished!"

		else:
			self.message = "You don't have a enough points!"

	def buyGem(self):
		if(self.player.totalScore >= 20):
			self.sceneReturn.addGem()
			self.player.totalScore -= 20
			self.message = "A Gem was added to the Map!"
		else:
			self.message = "You don't have a enough points!"

	def buyChest(self):
		if(self.player.totalScore >= 20):
			self.sceneReturn.addChest()
			self.player.totalScore -= 20
			self.message = "A Chest was added to the Map!"
		else:
			self.message = "You don't have a enough points!"

	def buyKey(self):
		if(self.player.totalScore >= 200):
			self.player.keys = self.player.keys + 1
			self.player.totalScore -= 200
			self.message = "A Key was added to your Invetory!"
		else:
			self.message = "You don't have a enough points!"
			
			

	def buySprite1(self):
		self.player.ani_array = ["game/images/Animations/Boy/rightanimation.txt","game/images/Animations/Boy/leftanimation.txt","game/images/Animations/Boy/upanimation.txt","game/images/Animations/Boy/downanimation.txt"]
		self.player.setStopImage(self.player.ani_array)
		self.player.setImage("game/images/Animations/Boy/1.png")
		self.message = "You changed your character!"

	def buySprite2(self):
		self.player.ani_array = ["game/images/Animations/Girl/rightanimation.txt","game/images/Animations/Girl/leftanimation.txt","game/images/Animations/Girl/upanimation.txt","game/images/Animations/Girl/downanimation.txt"]
		self.player.setStopImage(self.player.ani_array)
		self.player.setImage("game/images/Animations/Girl/1.png")
		self.message = "You changed your character!"	

	def buySprite3(self):
		if(self.player.totalScore >= 120):
			self.player.ani_array = ["game/images/Animations/Cape/rightanimation.txt","game/images/Animations/Cape/leftanimation.txt","game/images/Animations/Cape/upanimation.txt","game/images/Animations/Cape/downanimation.txt"]
			self.player.setStopImage(self.player.ani_array)
			self.player.setImage("game/images/Animations/Cape/1.png")
			self.player.totalScore -= 120
			self.message = "You changed your character!"
		else:
			self.message = "You don't have enough points!"

	def buySprite4(self):
		if(self.player.totalScore >= 120):
			self.player.ani_array = ["game/images/Animations/Bald/rightanimation.txt","game/images/Animations/Bald/leftanimation.txt","game/images/Animations/Bald/upanimation.txt","game/images/Animations/Bald/downanimation.txt"]
			self.player.setStopImage(self.player.ani_array)
			self.player.setImage("game/images/Animations/Bald/1.png")
			self.player.totalScore -= 120
			self.message = "You changed your character!"
		else:
			self.message = "You don't have enough points!"

	def buySprite5(self):
		if(self.player.totalScore >= 120):
			self.player.ani_array = ["game/images/Animations/Princess/rightanimation.txt","game/images/Animations/Princess/leftanimation.txt","game/images/Animations/Princess/upanimation.txt","game/images/Animations/Princess/downanimation.txt"]
			self.player.setStopImage(self.player.ani_array)
			self.player.setImage("game/images/Animations/Princess/1.png")
			self.player.totalScore -= 120
			self.message = "You changed your character!"
		else:
			self.message = "You don't have enough points!"

	def buySprite6(self):
		if(self.player.totalScore >= 120):
			self.player.ani_array = ["game/images/Animations/Ninja/rightanimation.txt","game/images/Animations/Ninja/leftanimation.txt","game/images/Animations/Ninja/upanimation.txt","game/images/Animations/Ninja/downanimation.txt"]
			self.player.setStopImage(self.player.ani_array)
			self.player.setImage("game/images/Animations/Ninja/1.png")
			self.player.totalScore -= 120
			self.message = "You changed your character!"
		else:
			self.message = "You don't have enough points!"

	def buySprite7(self):
		if(self.player.totalScore >= 120):
			self.player.ani_array = ["game/images/Animations/Stache/rightanimation.txt","game/images/Animations/Stache/leftanimation.txt","game/images/Animations/Stache/upanimation.txt","game/images/Animations/Stache/downanimation.txt"]
			self.player.setStopImage(self.player.ani_array)
			self.player.setImage("game/images/Animations/Stache/1.png")
			self.player.totalScore -= 120
			self.message = "You changed your character!"
		else:
			self.message = "You don't have enough points!"
		

	def setSceneReturn(self,scene):
		self.sceneReturn = scene
		

