# Overview
The purpose of this document is to present the framework behind the development of 'A Dog's Journey Home'. This framework will be constructed through specified functional and requirements for our game, which are the functions our game needs to work. It also describes the non-functional requierments, which are the functions we would like to add to improve the user’s experience.

# Functional Requirements
1. Moving the character around with the arrow keys.
   1. R1: The game shall allow the player to control the dog character using the left or right arrow keys to navigate different environments.
   2. R2 The user shall be able to move the character around a 2d map.
   3. R3: The dog shall move left or right when the player presses the left or right key and a walk animation shall be displayed.
2. Saving the users progress in the game.
   1. R1: The user’s session shall be saved and stored, so they can leave the game without losing their progress.
   2. R2: The game map shall be saved as a .json file created and exported from Tiled.
3. Allowing the user to end the game and having an ending to the game.
   1. R1: The GUI shall display a congratulations message when the user completes the final objective of the game and reaches the allotted dog’s home location.
   2. R2: The user shall be able to quit the game whenever they want to.
4. Picking up objects in the game.
   1. R1: The game shall present interactive objects, such as food and obstacles, that the player can collect or avoid to influence the dog's journey.
   2. R2: The game shall have collectible artifacts spread throughout the world.
   3. R3: An item shall be stored for use later when a player uses the pickup key on that item.
5. The user can talk with NPCs
   1. R1: Text box dialog shall be displayed when the player interacts with a npc.
6. The character needs to move.
   1. R1: The game shall allow the character to walk or run left or right.
   2. R2: The game shall allow the character to jump when the user pushes the up key.
7. Keeping the items the character picks up.
   1. R1: The game shall allow the picked up items to be stored.
8. The map needs to consist of tiles
   1. R1: The game shall load in pixel tiles that look like stones or water.
9. The character needs to be animated.
   1. R1: The character shall change based on the movements.

# Non-Functional Requirements
1. Playing music and sound effects thought out the game.
   1. R1: The user shall be able to hear background music and sound effects that match what is visually happening in the game.
   2. R2: The game shall provide background music and sound effects with volume control options to enhance player immersion while respecting player preferences.
   3. R3: The game shall be original in music and design, so as not to infringe on copyright laws.
2. The game needs to be easily understandable for the user.
   1. R1: The game’s user interface shall be intuitive and simple, allowing new players to understand controls and objectives within the first five minutes of gameplay.
   2. R2: The game shall be easily playable to non-technical people. That is to say, users should not have to download additional software or go through various confusing steps to play the game on their PC.
3. The user can customize the dog.
   1. R1: The user shall be able to customize the characters (Eg: changing color, outfits, etc.)
4. Make the visuals appealing.
   1. R1: The GUI shall be visually appealing with no lags in gameplay. 
5. The storyline needs to be engaging.
   1. R1: The game shall have an engaging storyline and built-in tasks that motivate and excite users to play. 
6. The game needs to run smoothly.
   1. R1: The user shall be able to smoothly transition to a different level once they have completed the level they were on.
   2. R2: The game should run smoothly without lagging.
7. The game needs to load fast.
   1. R1: The game shall load in under 10 seconds to provide quick access to the game or levels.
8. The game needs to work on all screens.
   1. R1: The game shall be able to load on any type of screen.
9. The game needs multiple moving objects
   1. R1: The game shall be able to have multiple moving objects on screen at the same time.
10. The NPCs can give and take objects.
	1. R1: The character shall be able to give and receive objects from the NPC.
