import os, time

os.system('cls')

filenames = ["menu1.txt","menu2.txt","menu3.txt"]


def animateur(filenames,delay = 1,repeat = 10):
    frames = []
    for name in filenames:
        with open(name,"r",encoding="utf8") as f:
            frames.append(f.readlines())

    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system('cls')

animateur(filenames,delay = 0.5,repeat = 10)
