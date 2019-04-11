def newScene():
	scene = []
	return scene

def addChar(scene, char):
	scene.append(char)
	return scene

def removeChar(scene, char):
	scene.remove(char)
	return scene

def charExist(scene, char):
	if char in scene:	
		return True
	else:
		return False