import sys,os

current_dir = os.path.dirname(os.path.abspath(__file__))
relative_top_directory = "../src/"  
absolute_top_directory = os.path.join(current_dir, relative_top_directory)
norm_path = os.path.normpath(absolute_top_directory)


print("HERE")
print(norm_path)
sys.stdout.flush()
sys.path.append(norm_path)

from src.jelkpy.sphere import Sphere
print("Hello world")
