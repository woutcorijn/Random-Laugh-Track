import os
import subprocess
import time
import random
import configparser

configparser = configparser.RawConfigParser()
configparser.read("config.txt")

#config
f = open('config.txt', 'r')
print(f.read())

class config:
	output = configparser.get("config", "output")
	minimum_seconds = int(configparser.get("config", "minimum_seconds"))
	maximum_seconds = int(configparser.get("config", "maximum_seconds"))
	frequency = configparser.get("config", "frequency")

Tracks = []

for x in range(12):
	Tracks.append(x + 1)

while True:

	Random_Track = random.randint(0, 11)
	Random_Sleep = random.randint(config.minimum_seconds, config.maximum_seconds)

	if  config.output == "jack":
		pass
		#subprocess.run(["omxplayer", "Tracks/" + str(Tracks[Random_Track]) + ".wav"])

	elif config.output == "fm":
		pass
		 #subprocess.run(["./fm_transmitter", "-f", config.output,  "Tracks/" + str(Tracks[Random_Track]) + ".wav"])

	else:
		print("Config.txt not correct configured")
		break

	print("Tracks/" + str(Tracks[Random_Track]) + ".wav")

	time.sleep(Random_Sleep)
