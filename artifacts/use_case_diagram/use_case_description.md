# Use Case Description

**Use Case:** Moving the character in the game

**Actors:** Dog, Player(initiator)

**Description:** 
1. When no keys are pressed the idle animation for the dog is displayed.
2. Player presses the left, right, or up arrow keys on thier computer.
3. The dog walking animation plays to the left if the left key if pressed and right if the right key is pressed.
4. The dog jumping animation plays if the up arrow key is pressed.
5. The dog moves across the map in the direction of the key the player pressed down.

**Cross Ref:** 

Functional Requirements: Moving the character around;
* FR1. The game shall allow the player to control the dog character using the left or right arrow keys to navigate different environments.
* FR2	The user shall be able to move the character around a 2d map.
* FR3	The dog shall move left or right when the player presses the left or right key.
* FR4	A walk animation shall be displayed as the dog is moved with the arrow keys.
* FR5	The dog shall switch based on the direction the user is making the dog go.
* FR6	The game shall allow the character to jump when the user pushes the up key.
* FR7	A jump animation shall be displayed as the dog jumps.
* FR8	An idle animation shall be displayed when the dog is not moving.

**Use Cases:** The player must have started the game. 

**Use Case:** Interaction in the game

**Actors:** Dog, Player(initiator), NPCS, Enemies

**Description:** 
1. Player moves dog with arrow keys.
2. Dog collides with floating objects, and the objects dissapear.
3. If the dog collides with all objects and collides with NPC, then the NPC changes the world or game map or displays a message.
4. If the dog does not collide with all objects and collides with NPC, then the NPC displays a message.
5. If the dog collides with enemies, then the dog's position is set back to the starting postion at the beginnign of the map.
6. The enemies move left and right across the map.
7. The NPCS display and idle animation in one spot in the map.

**Cross Ref:**
Functional Requirements: Interactive objects in the game.
* FR13	The game shall allow the picked-up items to be stored.
* FR14	The dog shall overcome enemies at each level.
* FR15	The enemies shall make the level restart when the dog runs into them.

Nonfunctional Requirements: NPCS to guide the user.
* NFR13	The NPC shall dictate if the character can move on to the next world.
* NFR14	The NPC shall have an idle animation.
* NFR15	The NPC shall show a message when the user runs into it.

**Use Cases:**
* The player must have started the game.
* The player must have used the arrow keys to move the dog.

