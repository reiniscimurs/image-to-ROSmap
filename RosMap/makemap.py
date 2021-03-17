import cv2
import math
import os.path
from args import d_args


def measure(event, x, y, flags, param):
    global mx, my
    if event == cv2.EVENT_LBUTTONDOWN and len(mx) < 2:
        print(f'Point added at coordinate: {x, y}')
        mx.append(x)
        my.append(y)

        if len(mx) > 1:
            print("What is the distance in meters between the 2 points?")
            deltapx = float(input())
            dpx = math.sqrt((mx[1] - mx[0]) ** 2 + (my[1] - my[0]) ** 2)
            global resolution
            resolution = deltapx / dpx
            print(f'Calculated pixel resolution is: {resolution} meters')
            print(f'Press any key on the image or close it to continue')


print("Name of the .png image to turn into a ROS map:")
file_name = input()
image = cv2.imread(file_name)

resolution = d_args.resolution

mx = []
my = []

if d_args.measure:
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image)
    print("Click on two points in the image")
    cv2.setMouseCallback('image', measure)

    esc = 0
    while (esc == 0):
        cv2.imshow('image', image)
        esc = cv2.waitKey() & 0xFF

    cv2.destroyAllWindows()

print("Name of the ROS map?")
mapName = input()

mapLocation = ''
completeFileNameMap = os.path.join(mapLocation, mapName + ".pgm")
completeFileNameYaml = os.path.join(mapLocation, mapName + ".yaml")
yaml = open(completeFileNameYaml, "w")
cv2.imwrite(completeFileNameMap, image)

yaml.write("image: " + mapName + ".pgm\n")
yaml.write("resolution: " + str(resolution) + "\n")
yaml.write("origin: [" + str(d_args.originx) + "," + str(d_args.originy) + ", 0.000000]\n")
yaml.write("negate: 0\noccupied_thresh: " + str(d_args.occupied) +"\nfree_thresh: " + str(d_args.free))
yaml.close()
