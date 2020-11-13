# Random-Laugh-Track
Play a random laugh track on a random moment on the Raspberry pi.<br>
The audio can be played through the 3.5mm jack or be transmitted over FM.

<h1>Usage</h1>

1. python3 is needed, installed on most devices by default.

2. Clone the Random-Laugh-Track repository.

```
git clone https://github.com/woutcorijn/Random-Laugh-Track
```

3. Audio playback.

For playing sound through the 3.5mm jack you need OMXPlayer.

```
sudo apt-get install omxplayer
```

For transmitting the FM Signal you need the fm_transmitter github repo by Marcin Kondej (markondej).
<br>
https://github.com/markondej/fm_transmitter
<br><br>
clone the fm_transmitter repository in the Random-Laugh-Track folder.
```
cd Random-Laugh-Track
git clone https://github.com/markondej/fm_transmitter
```
Next follow the install steps in "How to use it" on the fm_transmitter repository.<br>
(make sure you have a jumperwire on GPIO4 that acts as an antenna).<br>
https://github.com/markondej/fm_transmitter

4. Run the script.<br>

Run the shell script in the Random-Laugh-Track folder.<br>
(For transmitting FM you need root access).

```
./Random-Laugh-Track.sh
```
or (When FM transmitting is used)
```
sudo ./Random-Laugh-Track.sh
```

<h2>Configuration</h2>
In the config.txt file you can change the settings.

```
nano config.txt
```
(or any other text editor).

Default config file:

```
[config]
#jack = Audio output thru 3.5mm jack.
#fm = Transmit audio over FM.
output = fm

#If the output is set to FM set here the frequency in MHz.
#The GPIO4 pin is used to transmit the signal.
frequency = 102.1

#Settings for when the laugh track occures.
#minimum_seconds = the shortest time the laugh track could occures.
#maximum_seconds = the longest time the laugh track could occures.
minimum_seconds = 1
maximum_seconds = 30
```
