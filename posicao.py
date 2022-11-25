import os
import cv2
import pytesseract
import pyautogui as bot
import time
import re
import string
import csv

time.sleep(10)
x, y = bot.position()
#bot.click(126, 1293)
#print ("Posicao atual do mouse:")
#print ("x = "+str(x)+" y = "+str(y))
#
contador = 1

print ("Posicao atual do mouse:")
print ("x = "+str(x)+" y = "+str(y))