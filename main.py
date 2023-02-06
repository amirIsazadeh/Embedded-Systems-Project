import logging
import threading
import time

temperature = 0
humidity = 0


def temperature_and_humidity():
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def find_light():
    pass

def weather_api():
    pass

def sound():
    pass

def face_detector():
    pass

def hand_detector():
    pass


while True:
    temperature, humidity = temperature_and_humidity()
    light = find_light()
    weather = weather_api()
    sound_command = sound()
    face = face_detector()
    hand = hand_detector()
    
