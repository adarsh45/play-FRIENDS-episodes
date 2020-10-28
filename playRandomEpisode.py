import os
import random

# get all folder names from base folder first
seasonFolders = []
for (dirPath, dirName, fileNames) in os.walk("."):
	seasonFolders.extend(dirName)
	break

# choose any random season folder from list
randomFolderName = random.choice(seasonFolders)
print(randomFolderName)

# get all files inside that random folder chosen
files = []
for (dirPath, dirName, fileNames) in os.walk(randomFolderName):
	files.extend(fileNames)
	break

# similarly get any random episode from that files list
randomFileName = random.choice(files)
print(randomFileName)

# prepare a full absolute path to pass to startfile() func
fullEpisodePath = os.path.abspath(randomFolderName+"/"+ randomFileName)

print(fullEpisodePath)

# finally open that randomly chosen episode video file
os.startfile(fullEpisodePath)