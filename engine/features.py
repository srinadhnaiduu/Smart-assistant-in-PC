import os
from playsound import playsound
import eel




#Playing assistant 

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)




