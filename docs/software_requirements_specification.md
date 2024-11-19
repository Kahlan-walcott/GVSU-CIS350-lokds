# Overview
The purpose of this document is to establish the framework behind the development of ‘A Dog's Journey'. This framework will be constructed through functional and non-functional requirements. The functional requirements will establish the product's explicitly specified basic facilities. The non-functional requirements will establish the quality constraints that must be satisfied. 

# Functional Requirements
1. Moving the character around with the arrow keys.
   1. R1: The game shall allow the player to control the dog character using the left, right, and up arrow keys to navigate different environments.
   2. R2 The user shall be able to move the character around a 2d map.
   3. R3: The dog shall move left or right when the player presses the left or right key and a walk animation shall be displayed.
2. Saving the users progress in the game.
   1. R1: The user’s session shall be saved and stored, so they can leave the game without losing their progress.
   2. R2: The game map shall be saved as a .json file.
3. Allowing the user to exit the game or win the game.
   1. R1: The GUI shall display a congratulations message when the user completes the final objective of the game and reaches the allotted dog’s home location.
   2. R2: The user shall be able to quit the game whenever they want to.
4. Picking up objects in the game.
   1. R1: The game shall present interactive objects, such as food and artifacts, that the player can collect that will influence the dog's journey back home.
   2. R2: The game shall have collectible artifacts spread throughout the world.
   3. R3: An item shall be stored for use later when a player uses the pickup key on that item.
5. The user can talk with NPCs
   1. R1: Text box dialog shall be displayed when the player interacts with an npc.
6. The character needs to move.
   1. R1: The game shall allow the character to walk or run left or right.
   2. R2: The game shall allow the character to jump when the user pushes the up key.
7. Keeping the items the character picks up.
   1. R1: The game shall allow the picked up items to be stored.
8. The map needs to consist of tiles
   1. R1: The game shall load in pixel tiles that look like stone or water.
   2. R2: The tiles shall match the "place" that the character is at.
9. The character needs to be animated.
   1. R1: The character shall change based on the movements.
10. Giving collected artifacts
	1. R1: The character shall be able to give the stored items/artifacts to the NPCs if asked to pass through the "gate".
11. The character will move to the next level(one step close to home)
	1. R1: The character shall be allowed to "fall into" the next level as it gives the artifact asked by the NPC.
12. The atmosphere needs to be meaningful
    1. R1: The artifacts shall be meaningful to the current level the dog is on.
    2. R2: The background shall reflect the progression of the story.
13. The game needs to have enemies
    1. R1: The character shall overcome an enemy in each level.  
    2. R2: The enemies shall kill the dog.
    3. R3: The enemies shall move left to right.
14. The enemies need to make sense in the game
    1. R1: The enemies shall reflect the current wold the dog is in.
15. The game needs multiple changing worlds
    1. R1: The worlds shall be challenging. 
    2. R2: The worlds shall fit into the story line.   

# Non-Functional Requirements
1. Playing music and sound effects throughout the game.
   1. R1: The user shall be able to hear background music and sound effects that match what is visually happening in the game.
   2. R2: The game shall provide background music and sound effects with volume control options to enhance player immersion while respecting player preferences.
   3. R3: The game shall be original in music and design, so as not to infringe on copyright laws.
2. The game needs to be easily understandable for the user.
   1. R1: The game’s user interface shall be intuitive and simple, allowing new players to understand controls and objectives within the first five minutes of gameplay.
   2. R2: The game shall be easily playable to non-technical people. That is to say, users should not have to download additional software or go through various confusing steps to play the game on their PC.
3. Make the visuals appealing.
   1. R1: The GUI shall be visually appealing with no lags in gameplay. 
4. The storyline needs to be engaging.
   1. R1: The game shall have an engaging storyline and built-in tasks that motivate and excite users to play. 
5. The game needs to run smoothly.
   1. R1: The user shall be able to smoothly transition to a different level once they have completed the level they were on.
   2. R2: The game should run smoothly without lagging.
6. The game needs to load fast.
   1. R1: The game shall load in under 10 seconds to provide quick access to the game or levels.
7. The game needs multiple moving objects
   1. R1: The game shall be able to have multiple moving objects on screen at the same time.
8. The NPCs can give and take objects.
	1. R1: The character shall be able to give and receive objects from the NPC.
9. Character visual appearance.
	1. R1: The character shall get bigger as it picks up food along the journey.
10. The character needs to fly
    1. R1: The dog shall have wings, so he can fly. 
11. The character can push objects around
    1. R1: The dog shall be able to push crates around.
12. The trees need to have leaves falling
    1. R1: The trees shall have animated leaves that constantly fall.
13. The wolds need to be different lengths
    1. R1: The worlds shall range in length.
14. The game needs a title screen 
	1. R1: The game shall have a title screen telling the user hpw to play the game.
    2. R2: The title screen shall reflect the game's storyline.
15. The game needs a congratulation screen
    1. R1: The user shall see a congratulation screen when they compleat the game. 
