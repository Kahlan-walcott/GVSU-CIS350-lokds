import sys  # Import the sys module to handle system-specific parameters and functions
import json  # Import the json module for reading and writing JSON data
import pygame  # Import the pygame library for creating games
import os  # Import the os module for interacting with the operating system
from Sprites import Avatar, AnimationSequence  # Import the Avatar and AnimationSequence 

# Base path for image files
BASE_IMAGE_DIR = 'data/images/'


# Function to load a single image
def load_picture(file):

    picture = pygame.image.load(BASE_IMAGE_DIR + file).convert()  # Load the image and convert it for faster blitting
    picture.set_colorkey((0, 0, 0))  # Set the color key for transparency (black in this case)

    return picture  # Return the loaded image


# Function to load multiple images from a specified directory
def load_pictures(file):
    pictures = []  # Initialize an empty list to store images
    png_filesNjpg_Files = [f for f in os.listdir(BASE_IMAGE_DIR + file) if f.endswith('.png') or f.endswith('.jpg')]

        # Iterate through sorted list of image filenames in the directory
    for img_name in sorted(png_filesNjpg_Files):
        pictures.append(load_picture(file + '/' + img_name))  # Load each image and add it to the list
    # Handle errors related to Pygame image loading
         # Load a default image if an error occurs
        if os.path.exists(BASE_IMAGE_DIR + file):  # Check if the path exists
            print(f"File exists: {BASE_IMAGE_DIR + file}")  # Print a message indicating the existence of the path
    return pictures  # Return the list of loaded images

 

# List of offsets for neighboring tiles
ADJACENT_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

# Set of tile types that have physics properties
PHYSICS_TILES = {'grass', 'stone'}


# Main game class
class Adventure:
    def __init__(self):
        pygame.init()  # Initialize Pygame

        pygame.display.set_caption('Dog\'s Journey Home')  # Set the title of the game window
        self.tile_dimension = 16  # Set the size of each tile
        self.tile_layout = {}  # Initialize an empty dictionary for the tile layout
        self.exterior_tiles = []  # Initialize a list for tiles that are not on the grid
        self.window = pygame.display.set_mode((640, 480))  # Create the main game window
        self.render_surface = pygame.Surface((295, 230))  # Create a surface for rendering the game
        self.character_type = 'avatar'  # Set the type of the player
        self.timer = pygame.time.Clock()  # Create a clock object to manage the frame rate

        self.movement_status = [False, False]  # List to track movement input (left/right)

        # Load assets for various types of game entities
        self.resources = {
            'decor': load_pictures('tiles/decor'),
            'grass': load_pictures('tiles/grass'),
            'large_decor': load_pictures('tiles/large_decor'),
            'stone': load_pictures('tiles/stone'),
            'player': load_picture('entities/player/player.png'),
            'background': load_picture('background.png'),
            'clouds': load_pictures('clouds'),
            'water': load_pictures('tiles/water'),
            'player/idle': AnimationSequence(load_pictures('entities/player/idle'), 6),  # Idle animation for the player
            'player/thing': AnimationSequence(load_pictures('entities/player/thing')),
            'player/run': AnimationSequence(load_pictures('entities/player/run'), 4),  # Run animation for the player
            'player/jump': AnimationSequence(load_pictures('entities/player/jump')),  # Jump animation for the player
            'player/slide': AnimationSequence(load_pictures('entities/player/slide')),  # Slide animation for the player
            'player/wall_slide': AnimationSequence(load_pictures('entities/player/wall_slide')),
            # Wall slide animation for the player
        }


        self.load_game('level1.json')  # Load the initial game level from a JSON file

        self.scroll_offset = [0, 0]  # Initialize scrolling offsets for the view
        self.avatar = Avatar(self, 'player', (50, 50), (10, 10))  # Create a player instance at a given position and size
        self.current_animation = self.resources['player/idle'].duplicate()  # Copy the idle animation for the player
        self.current_action = 'idle'  # Set the initial action to 'idle'

    # Function to get tiles surrounding a given position
    def surrounding_tiles(self, position):
        tiles = []  # Initialize an empty list to store neighboring tiles
        tile_position = (int(position[0] // self.tile_dimension), int(position[1] // self.tile_dimension))  # Calculate the tile's grid location
        for offset in ADJACENT_OFFSETS:  # Iterate through neighbor offsets
            check_position = str(tile_position[0] + offset[0]) + ';' + str(
                tile_position[1] + offset[1])  # Check the location of each neighboring tile
            if check_position in self.tile_layout:  # If the tile exists in the tile layout
                tiles.append(self.tile_layout[check_position])  # Add it to the list of neighboring tiles
        return tiles  # Return the list of neighboring tiles

    # Function to save the current game state to a JSON file
    def save_game(self, file):
        f = open(file, 'w')  # Open a file for writing
        json.dump({'tile_layout': self.tile_layout, 'tile_dimension': self.tile_dimension, 'exterior_tiles': self.exterior_tiles},
                  f)  # Write the game state to the file
        f.close()  # Close the file

    # Function to load the game state from a JSON file
    def load_game(self, file):
        f = open(file, 'r')  # Open a file for reading
        level_data = json.load(f)  # Load the JSON data from the file
        f.close()  # Close the file

        # Update the game's tile layout, tile size, and exterior tiles based on the loaded data
        self.tile_layout = level_data['tilemap']
        self.tile_dimension = level_data['tile_size']
        self.exterior_tiles = level_data['offgrid']

    # Function to get physics rectangles around a given position
    def physics_rectangles(self, position):

        rectangles = []  # Initialize an empty list to store physics rectangles
        for tile in self.surrounding_tiles(position):  # Get the surrounding tiles
            if tile['type'] in PHYSICS_TILES:  # Check if the tile has physics properties
                rectangles.append(
                    pygame.Rect(tile['pos'][0] * self.tile_dimension, tile['pos'][1] * self.tile_dimension, self.tile_dimension,
                                self.tile_dimension)  # Create a rectangle for the tile and add it to the list
                )
        return rectangles  # Return the list of physics rectangles

    # Function to render the game on a given surface with an offset
    def render(self, surface, offset=(0, 0)):
        for tile in self.exterior_tiles:  # Render off-grid tiles
            surface.blit(self.resources[tile['type']][tile['variant']],
                         (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))  # Draw each tile

        # Iterate through the visible tile grid
        for x in range(offset[0] // self.tile_dimension, (offset[0] + surface.get_width()) // self.tile_dimension + 1):
            for y in range(offset[1] // self.tile_dimension, (offset[1] + surface.get_height()) // self.tile_dimension + 1):
                location = str(x) + ';' + str(y)  # Get the location key for the tile
                if location in self.tile_layout:  # If the tile exists in the tile layout
                    tile = self.tile_layout[location]  # Retrieve the tile data
                    surface.blit(self.resources[tile['type']][tile['variant']], (
                        tile['pos'][0] * self.tile_dimension - offset[0],
                        tile['pos'][1] * self.tile_dimension - offset[1]))  # Draw the tile on the surface

    # Function to run the main game loop
    def run(self):
        while True:  # Infinite loop for the game
            self.render_surface.blit(self.resources['background'], (0, 0))  # Draw the background on the display surface
           # Print the avatar's current position

            # Check if the avatar has fallen below a certain threshold
            if self.avatar.position[1] >= 1000:
                Adventure().run()  # If so, create a new Adventure instance and run it

            # Update scrolling offsets based on avatar position
            self.scroll_offset[0] += (self.avatar.rect().centerx - self.render_surface.get_width() / 2 - self.scroll_offset[0]) / 30
            self.scroll_offset[1] += (self.avatar.rect().centery - self.render_surface.get_height() / 2 - self.scroll_offset[1]) / 30
            render_scroll = (int(self.scroll_offset[0]), int(self.scroll_offset[1]))  # Convert scroll offsets to integers

            self.render(self.render_surface, offset=render_scroll)  # Render the game with the current offsets

            # Update the avatar's position and handle movement
            self.avatar.update_avatar(self.tile_layout, (self.movement_status[1] - self.movement_status[0], 0))
            self.avatar.render(self.render_surface, offset=render_scroll)  # Render the avatar on the display surface

            # Handle Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If the window is closed
                    pygame.quit()  # Quit Pygame
                    sys.exit()  # Exit the program
                if event.type == pygame.KEYDOWN:  # If a key is pressed
                    if event.key == pygame.K_LEFT:  # If the left arrow key is pressed
                        self.movement_status[0] = True  # Set left movement to True
                    if event.key == pygame.K_RIGHT:  # If the right arrow key is pressed
                        self.movement_status[1] = True  # Set right movement to True
                    if event.key == pygame.K_UP:  # If the up arrow key is pressed
                        self.avatar.avatar_velocity[1] = -2  # Set the avatar's upward velocity
                if event.type == pygame.KEYUP:  # If a key is released
                    if event.key == pygame.K_LEFT:  # If the left arrow key is released
                        self.movement_status[0] = False  # Set left movement to False
                    if event.key == pygame.K_RIGHT:  # If the right arrow key is released
                        self.movement_status[1] = False  # Set right movement to False

            # Scale the render surface to match the screen size and update the display
            self.window.blit(pygame.transform.scale(self.render_surface, self.window.get_size()), (0, 0))
            pygame.display.update()  # Update the full display surface to the screen
            self.timer.tick(60)  # Cap the frame rate at 60 FPS


# Start the game by creating an Adventure instance and calling its run method
Adventure().run()
