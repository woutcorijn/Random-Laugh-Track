import os
import subprocess
import time
import random
import configparser

configparser = configparser.RawConfigParser() 
configparser.read("config.txt")
print(configparser.get("config", "output"))

Tracks = []

for x in range(12):
	Tracks.append(x + 1)

while True:

	Random_Track = random.randint(0, 11)
	Random_Sleep = random.randint(1, 20)

	if configparser.get("config", "output") == "fm":
		pass

	elif configparser.get("config", "output") == "jack":
		subprocess.run(["omxplayer", "Tracks/" + str(Tracks[Random_Track]) + ".wav"])

	else:
		print("Config file not correct")
		break

	print("Tracks/" + str(Tracks[Random_Track]) + ".wav")

	time.sleep(Random_Sleep)
