from .color import Color
from typing import Callable
import jelka_validator.datawriter as dw
import time

class Jelka:
    def __init__(self, n : int, frame_rate : int, color : Color):
        self.n = n
        self.color = color
        self.lights = [color for _ in range(n)]
        self.dw = dw.DataWriter()
        self.frame = 0
        self.frame_rate = frame_rate
    
    def set_light(self, i : int, color : Color):
        self.lights[i] = color

    def write_lights(self):
        writable = [light.to_write() for light in self.lights]
        self.dw.write_frame(writable)

    def run(self, callback : Callable[['Jelka'], None]= None):
        t = 0.0
        dt = 1.0 / self.frame_rate
        current_time = time.perf_counter()

        while True:
            if callback is not None:
                callback(self)
            else : break
            self.write_lights() 
        
            new_time = time.perf_counter()
            frame_time = new_time - current_time
            current_time = new_time
            self.frame += 1

            if frame_time <= dt:
                time.sleep(dt - frame_time)
                print(f"FPS: 60")
            else: 
                #print(f"Frame rate is too slow: {frame_time}/ {dt}")
                print(f"FPS: {int(1.0 / frame_time)}")


