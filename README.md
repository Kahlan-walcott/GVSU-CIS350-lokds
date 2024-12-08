# lokds

In this adventure game, players guide a resurrected dog through two distinct levels of mystical forests, each filled with unique challenges. The first forest is haunted by ghosts, while the second is plagued by sea monsters. The dog must collect specific artifacts in each level to progress, with the ability to jump, fly, and move back and forth between areas to retrieve missed items. Once all the required artifacts are collected, the dog can advance to the second level, and ultimately, after overcoming the challenges of the sea monster-infested forest, return home to its owner. The game blends exploration, puzzle-solving, and platforming to create a deeply emotional and dynamic journey.

## Team Members and Roles

* [Olivia Foster](https://github.com/Olivia-Codes/CIS350-HW2-Foster.git) (Scrum leader + Lead Developer)
* [Kahlan Walcott](https://github.com/Kahlan-walcott/CIS350-HW2-Walcott) (QA engineer + Developer)
* [Lasya Priya Vemalla](https://github.com/vemallal/CIS350-HW2-Vemalla) (QA engineer + Documentation Lead)
* [Sanidhya Didagur](https://github.com/sdidagur1/CIS350-HW2-DIDAGUR.git) (Sound Designer + Developer)
* [Delaney Kelley](https://github.com/kelleyde/CIS350-HW2-Kelley.git) (Graphics Designer + Developer)

## Prerequisites
You should have some knowledge of Python and the command line.
## Run Instructions
If you wish to use the command line find your computer of choice below and follow the instructions.

The commands you need to run will be in this $\textsf{\color{#DC143C}color}$.

The commands that have a website in them will be in a <code>code block</code>.
## Linux users
Wherever you see **system** below refer to this:

If you are using Ubuntu: type in $\textsf{\color{#DC143C}apt}$

If you are using Fedora: type in $\textsf{\color{#DC143C}dnf}$

If you are using CentOS: type in $\textsf{\color{#DC143C}yum}$
### Setting it up
#### Check your Python version:
1. Run the command $\textsf{\color{#DC143C}python3 --version}$
    1. If it is 3.7.7 or higher you are good and can move on to the next step.     
    2. If you don't have Python you need to install it. If you have instructions on your screen follow those. If not type in $\textsf{\color{#DC143C}sudo}$ **system** $\textsf{\color{#DC143C}install python3.13}$
    3. If you have an older version you have to upgrade it. You can type $\textsf{\color{#DC143C}sudo}$ **system** $\textsf{\color{#DC143C}upgrade python3}$. Since you upgraded Python you are also going to upgrade pip. You can type $\textsf{\color{#DC143C}sudo}$ **system** $\textsf{\color{#DC143C}upgrade python3-pip}$.
#### Check your PIP version: (allows you to install python packages)
2. Run the command $\textsf{\color{#DC143C}pip3 --version}$
   1. If you have it then you can move on to the next step. 
   2. If you don't have it type in $\textsf{\color{#DC143C}sudo}$ **system** $\textsf{\color{#DC143C}install python3-pip}$.
#### Install Pygame: (this is what we are using to run our game)
3. Now type in $\textsf{\color{#DC143C}python3}$ (with no commands behind it) and then type $\textsf{\color{#DC143C}import pygame}$.
    1. If the message 'Hello from the ...' then you are good and can run our game. You can move on to running it.
	2. If the message dosen't show up then you need to install it. To do that first type  $\textsf{\color{#DC143C}exit()}$ to stop python. Then type $\textsf{\color{#DC143C}pip3 install pygame-ce}$ to install Pygame.
    3. Once it is downloaded type $\textsf{\color{#DC143C}python3}$ to start the python interpreter. Then type $\textsf{\color{#DC143C}import pygame}$ if it shows "Hello from the pygame ..." then you can run our game.
### Running it
1. If you just typed $\textsf{\color{#DC143C}import pygame}$, type $\textsf{\color{#DC143C}exit()}$
1. Stay on this page, in the command line type $\textsf{\color{#DC143C}python3 src/Maingame.py}$
2. Now you can play our game. Have fun! (Use the left and right arrow keys to move left or right. Use the up arrow key to jump. Use the ESC key to restart the game from anywhere or exit the game from the home page. Use your mouse to click the start button or the exit button on the home page.)
## Mac users
### Setting it up
#### Check your Python version:
1. Run the command $\textsf{\color{#DC143C}python3 --version}$
   1. If there was an error, or it is not found you need to download it. To do this you can go to the official Python website and download the version for Mac https://www.python.org/downloads/. You can also do this by downloading homebrew https://brew.sh/ this website will give you more information about it, but I will give you the command to download it. The command to download is <code>/bin/bash -c "$(curl -fsSL ht<span>tps://</span>raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code>. Once it's downloaded you need to type $\textsf{\color{#DC143C}brew install python}$ to get Python.
   2. Type $\textsf{\color{#DC143C}python3 --version}$ again to confirm that it has been downloaded correctly.
#### Check your PIP version: (allows you to install Python packages)
2. Run the command $\textsf{\color{#DC143C}pip3 --version}$
   1. If you just downloaded Python it should show up, and you don't have to do anything else in this step.
   2. If it doesn't work first type $\textsf{\color{#DC143C}pip --version}$. If it shows up use $\textsf{\color{#DC143C}pip}$ wherever you see $\textsf{\color{#DC143C}pip3}$ in the following steps.
   3. If there is still an error you need to download it. To do this type <code>curl ht<span>tps://</span>bootstrap.pypa.io/get-pip.py -o get-pip.py</code>. Once it downloads type $\textsf{\color{#DC143C}python3 get-pip.py}$. Once that is done retype $\textsf{\color{#DC143C}pip3 --version}$.
#### Install Pygame: (this is what we are using to run our game)
3. Install Pygame
   1. Type $\textsf{\color{#DC143C}pip3 install pygame --break-system-packages}$ to install Pygame.
   2. Once it is downloaded type $\textsf{\color{#DC143C}python3}$ to start the Python interpreter. Then type $\textsf{\color{#DC143C}import pygame}$ if it shows "Hello from the pygame ..." then you can run our game.
### Running it
1. If you just typed $\textsf{\color{#DC143C}import pygame}$, type $\textsf{\color{#DC143C}exit()}$.
2. On this page, in the command line type $\textsf{\color{#DC143C}python3 src/Maingame.py}$.
3. Now you can play our game. Have fun! (Use the left and right arrow keys to move left or right. Use the up arrow key to jump. Use the ESC key to restart the game from anywhere or exit the game from the home page. Use your mouse to click the start button or the exit button on the home page.)
## Windows users
### Setting it up (Command Prompt or Windows PowerShell)
Note: There can be different Python commands so try all of them, they are $\textsf{\color{#DC143C}python}$, $\textsf{\color{#DC143C}python3}$, and $\textsf{\color{#DC143C}py}$. Wherever you see $\textsf{\color{#DC143C}py}$ replace it with the Python command that works for your computer. If $\textsf{\color{#DC143C}py}$ works then you can just copy what we have.
#### Check your Python version:
1. Run the command $\textsf{\color{#DC143C}py --version}$
   1. If it says it was not found try the other Python commands. If none of them work try downloading Python. To do this go to the official page for Python on Windows https://www.python.org/downloads/. Then click the yellow button this should be the most recent version. Once it is done uploading open the file and install it to your computer. Once it is done you can close the window and go back to the command prompt.
   2. If it shows the version make sure it is 3.7 or higher. If it is your good and can move on. If not go to the link above and install the latest version of Python.
#### Check your PIP version: (allows you to install Python packages)
2. Run the command $\textsf{\color{#DC143C}pip --version}$
   1. If it gives an error keep going because it might not recognize $\textsf{\color{#DC143C}pip}$ as a command because it is not in the PATH.
#### Install Pygame: (what we are using to run our game)
3. Install Pygame
   1. Type $\textsf{\color{#DC143C}py -m pip install pygame-ce}$ it should say that it is downloading.
   2. Then type $\textsf{\color{#DC143C}py}$ (with no commands behind it) The Python interpreter should show up. Now you can type $\textsf{\color{#DC143C}import pygame}$ if it shows "Hello from the pygame ..." then you can run our game.
### Running it
1. If you just typed $\textsf{\color{#DC143C}import pygame}$, type  $\textsf{\color{#DC143C}exit()}$.
2. Stay on this page, in the Command Prompt or Windows PowerShell type $\textsf{\color{#DC143C}py src/Maingame.py}$.
3. Now you can play our game. Have fun! (Use the left and right arrow keys to move left or right. Use the up arrow key to jump. Use the ESC key to restart the game from anywhere or exit the game from the home page. Use your mouse to click the start button or the exit button on the home page.)

