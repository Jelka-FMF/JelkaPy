from jelkpy.jelka import Jelka,Color

def init(jelka : Jelka):
    None

def callback(jelka: Jelka):
    None

def main():
    jelka = Jelka(300, 60)
    jelka.run(callback,init)

main()