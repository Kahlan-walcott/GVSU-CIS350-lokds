# Overview

The purpose of this document is to establish the framework behind the development of A Dog's Journey. This framework 
will be organized through functional and non-functional requirements.

# Software Requirements

The functional requirements will establish the product's explicitly specified basic facilities. The non-functional 
requirements will establish the quality constraints that must be satisfied.

## Functional Requirements

### Moving the character around 

| ID  |                                                             Requirement                                                             | 
|:---:|:-----------------------------------------------------------------------------------------------------------------------------------:| 
| FR1 | The game shall allow the player to control the dog character using the left or right arrow keys to navigate different environments. | 
| FR2 |                                    The user shall be able to move the character around a 2d map.                                    | 
| FR3 |                           The dog shall move left or right when the player presses the left or right key.                           | 
| FR4 |                            A walk animation shall be displayed as the dog is moved with the arrow keys.                             |
| FR5 |                            The dog shall switch based on the direction the user is making the dog go.                               |
| FR6 |                             The game shall allow the character to jump when the user pushes the up key.                             |
| FR7 |                                        A jump animation shall be displayed as the dog jumps.                                        |
| FR8 |                                   An idle animation shall be displayed when the dog is not moving.                                  |


### Interactive objects in the game

|  ID  |                                     Requirement                                     | 
|:----:|:-----------------------------------------------------------------------------------:|
| FR9  |             The game shall present collectible objects for the player.              | 
| FR10 | The player shall be presented with objects to avoid influencing the dog's journey.  | 
| FR11 |       The game shall have collectible artifacts spread throughout the world.        | 
| FR12 |                    The artifact shall be meaningful to the dog.                     | 
| FR13 |               The game shall allow the picked-up items to be stored.                |
| FR14 |                    The dog shall overcome enemies at each level.                    |
| FR15 |        The enemies shall restart the level when the dog runs into them.             |

### The map visuals

|  ID  |                            Requirement                             | 
|:----:|:------------------------------------------------------------------:|
| FR16 | The game shall load in pixel tiles that look like stones or water. | 
| FR17 |                     The tiles shall be 16X16.                      | 
| FR18 |  The map shall have solid tiles the dog can't pass through.        | 
| FR19 |             The solid tiles shall be grass and stone.              | 
| FR20 |                The non-solid tiles shall be water.                 | 
| FR21 |        The map shall consist of on-grid and off-grid tiles.        | 
| FR22 |     The map shall consist of decor such as trees and flowers.      | 


## Non-Functional Requirements

### Music and sound effects 

|  ID  |                                                     Requirement                                                      | 
|:----:|:--------------------------------------------------------------------------------------------------------------------:| 
| NFR1 | The user shall be able to hear background music and sound effects that match what is visually happening in the game. | 
| NFR2 |                 The game shall play sound effects for specific actions such as jumping and falling.                  |
| NFR3 |                  The background music shall be turned down to not overpower the sound effects.                       |
| NFR4 |                    The sound effects shall only play when the specific action is being preformed.                    |
| NFR5 |                                    The background music shall continuously play.                                     |
| NFR6 |                             The background music shall restart when the level restarts.                              |

### A starting and ending screen

|  ID   |                                                    Requirement                                                    | 
|:-----:|:-----------------------------------------------------------------------------------------------------------------:| 
| NFR7  |                     The game shall have an exit button that users can click.                                      | 
| NFR8  |                               The title screen shall reflect the game's storyline.                                |
| NFR9  |                The title screen shall have a button that the users can click on to start the game.                |
| NFR10 |                      The user shall see a congratulatory screen when they complete the game.                      | 
| NFR11 | The congratulatory screen shall only display when all the artifacts have been collected and the dog reached home. |
| NFR12 |                            The congratulation screen shall take up the entire screen.                             |

### NPCs to guide the user

|  ID   |                              Requirement                              | 
|:-----:|:---------------------------------------------------------------------:| 
| NFR13 | The NPC shall dictate if the character can move on to the next world. | 
| NFR14 |                 The NPC shall have an idle animation.                 |
| NFR15 |       The NPC shall show a message when the user runs into it.        |
| NFR16 | The message shall tell the user if they missed any artifacts.         | 
| NFR17 |     The NPC shall be different based on the world the dog is in.      |
| NFR18 |   The message shall be different based on the world the dog is in.    |

# Software Artifacts

This section provides quick access to all the resources we developed for our game. 

### Diagrams
* [use case diagram](../artifacts/diagrams/use_case_diagram/UseCaseDiagram.pdf)
* [class diagram](../artifacts/diagrams/Class_Diagram.pdf)
* [sequence diagram]
* [Gantt chart]

### Jira Board
* [Jira Board](https://lokds.atlassian.net/jira/software/projects/SCRUM/boards/1)

### Resources the game pulls
#### Music
* [jump sound](../artifacts/jump-sound.mp3)
* [background music](../artifacts/backgroundmusic.mp3)
* [falling sound](../artifacts/artifacts_falling.mp3)
#### Background images
* [first background](../artifacts/images/background.jpg)
* [second background](../artifacts/images/forest-background.png)
#### Artifacts
* [first bone](../artifacts/images/artifacts/0.png)
* [second bone](../artifacts/images/artifacts/1.png)
* [third bone](../artifacts/images/artifacts/2.png)
* [fourth bone](../artifacts/images/artifacts/3.png)
#### Entities
* [first NPC tomato idle](../artifacts/images/entities/NPC/tomato)
* [second NPC chipmunk idle](../artifacts/images/entities/NPC/Chipmunk)
* [first enemy ghost down](../artifacts/images/entities/ghost/down)
* [first enemy ghost left](../artifacts/images/entities/ghost/left)
* [first enemy ghost right](./artifacts/images/entities/ghost/right)
* [first enemy ghost up](../artifacts/images/entities/ghost/up)
* [second enemy sea monster](../artifacts/images/entities/seaMonster/0.png)
* [dog](../artifacts/images/entities/player/player.png)
* [dog idle](../artifacts/images/entities/player/idle)
* [dog jump](../artifacts/images/entities/player/jump)
* [dog run](../artifacts/images/entities/player/run)
* [dog starting image](../artifacts/images/entities/player/thing/00.png)
#### Leaf
* [leaf](../artifacts/images/float/0.png)
#### Tiles
* [decor](../artifacts/images/tiles/decor)
* [grass](../artifacts/images/tiles/grass)
* [larger decor](../artifacts/images/tiles/large_decor)
* [stone](../artifacts/images/tiles/stone/0.png)
* [water](../artifacts/images/tiles/water)

