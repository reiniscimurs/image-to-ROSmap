# image-to-ROSmap
Python code for creating a ROS map out of a hand drawn .png image. It is possible to manually set or measure the pixel resolution in the image directly.
Originally inspired by the code in [https://www.youtube.com/watch?v=ySlU5CIXUKE]. Changed, and updated to work with python 3.6.

To run the code, open a terminal in the file directory and execute the following:

    python3 makemap.py

Following arguments can be given:

    --resolution -Manually set pixel resolution
    --measure    -Weather to measure the pixel resolution in image
    --originx    -Set x origin
    --originy    -Set y origin
    --occupied   -Occupied pixel threshold
    --free       -Free pixel threshold
    
Example where pixel resolution is measured manually and setting argument values:

    python3 makemap.py --measure --originx -1 --originy -1 --occupied 0.3 --free 0.1
  
The original (masterfully) hand-drawn map:
<p align="left">
    <img width=70% src="https://github.com/reiniscimurs/image-to-ROSmap/blob/main/RosMap/map.png">
</p>

Visualization of the map in Rviz:
<p align="left">
    <img width=50% src="https://github.com/reiniscimurs/image-to-ROSmap/blob/main/RosMap/Rvizmap.png">
</p>

To visualize the obtained map in Rviz, make sure the map_server is installed from:
* [Navigation Package](https://github.com/ros-planning/navigation)

Publish the map on the map server (replace "ROSmap" with the name of the obtained map):

    rosrun map_server map_server ROSmap.yaml
    
Visualize in Rviz by adding a map and setting the /map topic
