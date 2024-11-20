from .color import Color
from typing import Callable
import jelka_validator.datawriter as dw
import time

class Jelka:
    def __init__(self, n : int, frame_rate : int, color : Color = Color(0,0,0), file : str = "lucke3d.csv"):
        self.n = n
        self.color = color
        self.lights = [color for _ in range(n)]
        self.dw = dw.DataWriter()
        self.frame = 0
        self.frame_rate = frame_rate
        self.positions_raw = dict()
        self.positions_normalized = dict()
        self.start_time = time.perf_counter()
        self.cur_time = 0
        for i in range(n): self.positions_raw[i] = (0,0,0)

        with open(file) as f:
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                i, x, y, z = line.split(",")
                self.positions_raw[int(i)] = (float(x), float(y), float(z))
        
        self.normalize_positions(0,1)

    def normalize_positions(self, l : int = 0, r : int = 1):
        min_x = min([pos[0] for pos in self.positions_raw.values()])
        max_x = max([pos[0] for pos in self.positions_raw.values()]) + 0.01 # to avoid division by zero
        min_y = min([pos[1] for pos in self.positions_raw.values()])
        max_y = max([pos[1] for pos in self.positions_raw.values()]) + 0.01
        min_z = min([pos[2] for pos in self.positions_raw.values()])
        max_z = max([pos[2] for pos in self.positions_raw.values()]) + 0.01
        print("here")
        for i, pos in self.positions_raw.items():
            x = (pos[0] - min_x) / (max_x - min_x) * (r - l) + l
            y = (pos[1] - min_y) / (max_y - min_y) * (r - l) + l
            z = (pos[2] - min_z) / (max_z - min_z) * (r - l) + l
            self.positions_normalized[i] = (x, y, z)


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
            self.cur_time = time.perf_counter() - self.start_time
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


