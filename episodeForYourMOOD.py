import os
import random

# data
dict_moods = {1: "Feeling HAPPY", 2: "Want to LAUGH out loud", 3: "Feeling ROMANTIC", 4:"Just want to CRY", 5:"Want to SMILE"}

dict_happy = {
	1: "S01:E10 The One with the Monkey",
	2: "S02:E11 The One with the Lesbian Wedding",
	3: "S03:E09 The One with the Football",
	4: "S05:E13 The One with Joey's Bag",
	5: "S06:E07 The One Where Phoebe Runs",
	6: "S07:E07 The One with Ross's Library Book",
	7: "S08:E06 The One with the Halloween Party",
	8: "S09:E04 The One with the Sharks",
	9: "S10:E04 The One with the Cake",
	}

dict_laugh = {
	1: "S01:E07 The One with the Blackout",
	2: "S01:E13 The One with the Boobies",
	3: "S02:E23 The One with the Chicken Pox",
	4: "S03:E02 The One where No One's Ready",
	5: "S03:E08 The One with the Giant Poking Device",
	6: "S04:E08 The One with the Chandler in a Box",
	7: "S04:E20 The One with All the Wedding Dresses",
	8: "S05:E11 The One with All the Resolutions",
	9: "S05:E14 The One Where Everybody Finds Out",
	10: "S06:E08 The One with Ross's Teeth",
	11: "S06:E09 The One where Ross got High",
	12: "S06:E17 The One With Unagi",
	13: "S07:E06 The One with the Nap Partners",
	14: "S08:E15 The One with the Birthing Video",
	15: "S09:E07 The One with Ross's Inappropriate Song",
	16: "S10:E02 The One where Ross is Fine",
	17: "S10:E03 The One with Ross's Tan",
	}

dict_rom = {
	1: "S02:E07 The One Where Ross Finds Out",
	2: "S02:E14 The One with the Prom Video",
	3: "S02:E15 The One Where Ross and Rachel...You Know",
	4: "S03:E13 The One Where Monica And Richard Are Just Friends",
	5: "S06:E25 The One with the Proposal, Part 2",
	6: "S09:E19 The One with Rachel's Dream",
	7: "S10:E12 The One with Phoebe's Wedding",
	8: "S10:E18 The Last One, Part 2"
	}

dict_cry = {
	1: "S03:E16 The One With The Morning After",
	2: "S05:E03 The One with the Triplets",
	3: "S06:E24 The One with the Proposal, Part 1",
	4: "S06:E25 The One with the Proposal, Part 2",
	5: "S09:E21 The One with the Fertility Test",
	6: "S10:E08 The One with the Late Thanksgiving",
	7: "S10:E17 The Last One, Part 1",
	8: "S10:E18 The Last One, Part 2",
	}

dict_smile = {
	1: "S02:E07 The One With The Embryos",
	1: "S02:E19 The One With The Prom Video",
	3: "S05:E19 The One where Everybody Finds Out",
	4: "S07:E22 The One with the Chandler's Dad"
	}

dict_data = {1: dict_happy, 2: dict_laugh, 3: dict_rom, 4: dict_cry, 5: dict_smile}

# methods
def playEpisode(episodeStr):
	# get folder name of provided season number
	season = int(episodeStr[1:3])
	episode = int(episodeStr[5:7])

	seasonFolders = []
	for (dirPath, dirName, fileNames) in os.walk("."):
		seasonFolders.extend(dirName)
		break
	seasonFolder = seasonFolders[int(season)-1]

	# get file name inside folder with provided episode number
	files = []
	for (dirPath, dirName, fileNames) in os.walk(seasonFolder):
		files.extend(fileNames)
		break
	episodeFile = files[int(episode) - 1]

	# prepare a full absolute path to pass to startfile() func
	fullEpisodePath = os.path.abspath(seasonFolder+"/"+ episodeFile)

	print("We are playing: "+ fullEpisodePath)
	os.startfile(fullEpisodePath)


# actual runtime code
print("\nEnter your choice of mood and I will play suitable episode for you...\n")

for key, value in dict_moods.items():
	print(key , ":", value)

yourMood = int(input("\nNow enter your mood choice: "))

dict_preferred_mood = dict_data[yourMood]

print("\nPress...\n")
print("1 : If you want to see full list of available episodes and choose your own\n")
print("2 : If you don't want too much Stress, I will play random episode according to Your Mood...\n")

exactOrRandom = int(input("Enter your choice: "))

if exactOrRandom == 1:
	# show full list of available episodes
	for key, value in dict_preferred_mood.items():
		print(key,":", value)

	choice = int(input("\nEnter choice for episode you want to play: "))
	playEpisode(dict_preferred_mood[choice])

else:
	# play epiode randomly from given mood
	randomEpisode = random.choice(list(dict_preferred_mood.values()))
	playEpisode(randomEpisode)