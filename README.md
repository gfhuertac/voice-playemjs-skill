## Voice Playemjs
A skill to control an instance of playemjs running headless

## Description
There are some music providers that require a ui to work, making them hard to control from audio-only controllers such as mycroft, unless you connect to a third party proxy. this skill tries to solve this.

in order to do that, we leverage playemjs, a js player for online sources such as youtube, vimeo, deezer, and using a headless browser (firefox) and xvfb (if available), we launch an instance of the player and are able to control it using voice commands.

this is a proof of concept and we hope that it can help others to achieve similar stuff.

## Examples
 - "Play queen on deezer"
 - "Play inxs on youtube"
 - "Play next"
 - "Play previous"
 - "Stop"
 - "Pause"
 - "Resume"
 - "Set volume to 50"


## Credits
Gonzalo Huerta-Cánepa


