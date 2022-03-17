# Catfeeder
This is a tutorial to build your own automatic catfeeder using raspberry pi, some 3D printing, a camera, and a continuous servo motor!

# Materials
- Raspberry Pi
- Raspberry Pi Camera
- 6 Wires
- A Continuous 360 Degress Servo Motor
- A Computer
- A 3D Printer and Filaments

# Guide
1. Download all the files in the Github Repo to your computer
2. Save all the .STL files in a separate folder.
3. Save motiondetect-2.py somewhere you can access it.
# Part 1 - Program
4. Open motiondetect-2.py using an IDE of your choice, or simply with notepad.
5. Take out your Raspberry Pi, motor, and camera, and connect them like so:
![Wiring connection](IMG_20220317_154805.jpg)
If in doubt, check the card that comes with your Raspberry Pi. The motor should be connected to PIN 18.
5. Use the white wire to connect the Pi to your computer.
6. Open windows powershell and connect the Pi using SSH. The command should be ssh pi@yourpiname.local, the default password is raspberry.
7. Open a new document called catfeeder by typing sudo nano catfeeder.py
8. Copy the code from motiondetect-2.py, then go back to windows powershell and press right click. This should paste the code into the powershell.
9. Press ctrl + x to leave the file. Press enter, then y, then enter again.
10. Install the dependencies necessary by typing:
  - sudo apt-get install libgtkmm-3.0-1
  - sudo apt-get install libnotify4
  - sudo apt-get update
  - sudo apt-get install python3-pip
  - sudo pip3 install imutils
  - sudo pip3 install opencv-python
12. Ensure that the camera is facing a still background.
13. Test run the program by typing python3 catfeeder.py
14. After the terminal prints "Meow", try to make the camera observe a moving object. When it does, the motor should turn 520 degrees.
15. Congrats, you've finished the programming part of this project.
