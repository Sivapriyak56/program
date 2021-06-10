from PIL import ImageGrab
import numpy
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_s = datetime.datetime.now().strftime('%d/%m/%y %M-%S')
print(time_s)
file_name = f'{time_s}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
cap_video = cv2.VideoWriter(file_name.mp4, fourcc, 20.0, (width, height))


while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = numpy.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('recoder', img_final)
    cap_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break



