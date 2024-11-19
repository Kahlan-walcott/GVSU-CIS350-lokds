# lokds

In this adventure game, players guide a resurrected dog through two distinct levels of mystical forests, each filled with unique challenges. The first forest is haunted by ghosts, while the second is plagued by sea monsters. The dog must collect specific artifacts in each level to progress, with the ability to jump, fly, and move back and forth between areas to retrieve missed items. Once all the required artifacts are collected, the dog can advance to the second level, and ultimately, after overcoming the challenges of the sea monster-infested forest, return home to its owner. The game blends exploration, puzzle-solving, and platforming to create a deeply emotional and dynamic journey.

## Team Members and Roles

* [Olivia Foster](https://github.com/Olivia-Codes/CIS350-HW2-Foster.git) (Scrum leader)
* [Kahlan Walcott](https://github.com/Kahlan-walcott/CIS350-HW2-Walcott) (Quality assurance engineer)
* [Lasya Priya Vemalla](https://github.com/vemallal/CIS350-HW2-Vemalla)
* [Sanidhya Didagur](https://github.com/sdidagur1/CIS350-HW2-DIDAGUR.git)
* [Delaney Kelley](https://github.com/kelleyde/CIS350-HW2-Kelley.git)

## Prerequisites

## Run Instructions
If you wish to use the command line find your computer of choice below and follow the instructions.

## Linux users
Wherever you see **system** below refer to this:

If you are using Ubuntu: type in *apt*

If you are using Fedora: type in *dnf*

If you are using CentOS: type in *yum*
### Setting it up
#### Check your python version:
1. Run the command <font color="red">*python3 --version*</font>
    1. If it is 3.7.7 or higher you are good and can move on to the next step.     
    2. If you don't have Python you need to install it. If you have instructions on your screen follow those. If not type in <font color="red">*sudo* **system** *install python3.13*</font>
    3. If you have an older version you have to upgrade it. You can type <font color="red">*sudo* **system** *upgrade python3*</font>. Since you upgraded Python you are also going to upgrade pip. You can type <font color="red">*sudo*  **system** *upgrade python3-pip*</font>.
#### Check your PIP version: (allows you to install python packages)
2. Run the command *pip3 --version*
   1. If you just downloaded Python it should show up, and you don't have to do anything else in this step.
   2. If it doesn't work first type *pip --version*. if it shows up use *pip* where ever you see *pip3* in the following steps.
   3. If there is still an error you need to download it. To do this type *curl ht<span>tps://</span>bootstrap.pypa.io/get-pip.py -o get-pip.py*. Once it downloads type *python3 get-pip.py*. Once that is done retype *pip3 --version*
#### Install Pygame: (this is what we are using to run our game)
3. Install Pygame
    1. Type *pip3 install pygame-ce* to install Pygame.
    2. Once it is downloaded type *python3* to start the pythong interpreter. Then type *import pygame* if it shows "Hello from the pygame ..." then you can run our game.
### Running it
1. Stay on this page, in the command line type *python3 src/Maingame.py*
2. Now you can play our game. Have fun!
## Mac users
### Setting it up
#### Check your Python version:
1. Run the command *python3 --version*
   1. If there was an error, or it is not found you need to download it. To do this you can go to the official Python website and download the version for mack https://www.python.org/downloads/. You can also do this by downloading homebrew https://brew.sh/ this website will give you more information about it, but I will give to the command to download it. The command to download is */bin/bash -c "$(curl -fsSL ht<span>tps://</span>raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"*. Once it is downloaded you need to type *brew install python* to get Python.
   2. Type *python3 --version* again to confirm that it has been downloaded correctly.
#### Check your PIP version: (allows you to install python packages)
2. Run the command *pip3 --version*
   1. If you just downloaded Python it should show up, and you don't have to do anything else in this step.
   2. If it doesn't work first type *pip --version*. If it shows up use *pip* wherever you see *pip3* in the following steps.
   3. If there is still an error you need to download it. To do this type *curl ht<span>tps://</span>bootstrap.pypa.io/get-pip.py -o get-pip.py*. Once it downloads type *python3 get-pip.py*. Once that is done retype *pip3 --version*
#### Install Pygame: (this is what we are using to run our game)
3. Install Pygame
   1. Type *pip3 install pygame --break-system-packages* to install pygame.
   2. Once it is downloaded type *python3* to start the python interpreter. Then type *import pygame* if it shows "Hello from the pygame ..." then you can run our game.
### Running it
1. On this page, in the command line type *python3 src/Maingame.py*
2. Now you can play our game. Have fun!
## Windows users
### Setting it up (command prompt)
Note: There can be different Python commands so try all of them, they are *python*, *python3*, and *py*. Wherever you see *py* replace it with the python command that works for your computer. If *py* works then you can just copy what we have.
1. Run the command *py --version*
   1. If it says it was not found try the other Python commands. If none of them work try downloading Python. To do this go to the official page for Python on Windows https://www.python.org/downloads/. Then click the yellow button this should be the most recent version. Once it is done uploading open the file and install it to your computer. Once it is done you can close the window and go back to the command prompt.
   2. If it shows the version make sure it is 3.7 or higher. If it is your good and can move on. If not go to the link above and install the latest version of Python.
#### Check your PIP version: (allows you to install Python packages)
2. Run the command *pip --version*
   1. If it gives an error keep going because it might not recognize *pip* as a command because it is not in the PATH.
#### Install pygame: (what we are using to run our game)
3. Install Pygame
   1. Type *py -m pip install pygame-ce* it should say that it is downloading.
   2. Then type *py* (with no commands behind it) The Python interpreter should show up. now you can type *import pygame* and the Pygame version will be shown. Then you can start downloading our game and it should run.
### Running it
1. Stay on this page, in command prompt type *py src/Maingame.py*
2. Now you can play our game. Have fun!

