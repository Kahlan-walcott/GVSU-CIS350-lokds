import pygame
import json


AUTOMATIC_TILES = {
    tuple(sorted([(1, 0), (0, 1)])): 0,
    tuple(sorted([(1, 0), (0, 1), (-1, 0)])): 1,
    tuple(sorted([(-1, 0), (0, 1)])): 2,
    tuple(sorted([(-1, 0), (0, -1), (0, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1)])): 4,
    tuple(sorted([(-1, 0), (0, -1), (1, 0)])): 5,
    tuple(sorted([(1, 0), (0, -1)])): 6,
    tuple(sorted([(1, 0), (0, -1), (0, 1)])): 7,
    tuple(sorted([(1, 0), (-1, 0), (0, 1), (0, -1)])): 8,
}

NEARBY_COUNTERACT = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
BOUNCEOFF_TILES = {'grass', 'stone'}
# specify which tiles are auto tiles
AUTOMATIC_VARIETY = {'grass', 'stone'}


class Map:

    """
    manipulates the json file for the map.
    """

    def __init__(self, maingame, brick_bigness=16):
        self.main = maingame
        self.brick_bigness = brick_bigness
        self.map = {}
        self.isolated_islands = []

    def removal(self, match, remain=False):
        """removes a brick if it was one of the ones we were looking for"""
        pair = []
        """found one of the matches that we were looking for so we are going to remove it"""
        for brick in self.isolated_islands.copy():
            if (brick['type'], brick['variant']) in match:
                pair.append(brick.copy())
                if not remain:
                    self.isolated_islands.remove(brick)
        """deleting the brick in the map"""
        for place in self.map:
            brick = self.map[place]
            if (brick['type'], brick['variant']) in match:
                pair.append(brick.copy())
                # changing the position for the tile that we are referencing because we want it to be in pixels
                pair[-1]['pos'] = pair[-1]['pos'].copy()
                # converting (x-axis)
                pair[-1]['pos'][0] *= self.brick_bigness
                # y axis
                pair[-1]['pos'][1] *= self.brick_bigness
                if not remain:
                    del self.map[place]
        return pair

    def brick_surrounding(self, position):
        """for collisions with tiles"""
        bricks = []
        brick_place = (int(position[0] // self.brick_bigness), int(position[1] // self.brick_bigness))
        """generate all the tiles around the brick location"""
        for counteract in NEARBY_COUNTERACT:
            examine_place = str(brick_place[0] + counteract[0]) + ";" + str(brick_place[1] + counteract[1])
            if examine_place in self.map:
                bricks.append(self.map[examine_place])
        return bricks

    def store(self, track):
        """creates the tile map"""
        file = open(track, 'w')
        json.dump({'tilemap': self.map, 'tile_size': self.brick_bigness, 'offgrid': self.isolated_islands}, file)
        file.close()

    def putin(self, track):
        """loads the map into the game"""
        file = open(track, 'r')
        detailed_map = json.load(file)
        file.close()

        self.map = detailed_map['tilemap']
        self.brick_bigness = detailed_map['tile_size']
        self.isolated_islands = detailed_map['offgrid']

    def firm_examine(self, position):
        """for when we encounter one of the solid tiles."""
        brick_place = str(int(position[0] // self.brick_bigness)) + ';' + str(int(position[1] // self.brick_bigness))
        if brick_place in self.map:
            if self.map[brick_place]['type'] in BOUNCEOFF_TILES:
                return self.map[brick_place]

    def physrectangle_surrounding(self, position):
        """putting pysics on the tiles specified"""
        rectangles = []
        for brick in self.brick_surrounding(position):
            if brick['type'] in BOUNCEOFF_TILES:
                rectangles.append(pygame.Rect(brick['pos'][0] * self.brick_bigness, brick['pos'][1] * self.brick_bigness, self.brick_bigness, self.brick_bigness))
        return rectangles

    def automatic_bricks(self):
        """figures out which tiles would be best to place around the placed tiles"""
        for place in self.map:
            brick = self.map[place]
            nearby = set()
            """changes the tile based on the neighbors"""
            for transfer in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                examine_place = str(brick['pos'][0] + transfer[0]) + ';' + str(brick['pos'][1] + transfer[1])
                if examine_place in self.map:
                    if self.map[examine_place]['type'] == brick['type']:
                        nearby.add(transfer)
            nearby = tuple(sorted(nearby))
            if (brick['type'] in AUTOMATIC_VARIETY) and (nearby in AUTOMATIC_TILES):
                brick['variant'] = AUTOMATIC_TILES[nearby]

    def translate(self, surface, counteract=(0, 0)):
        """put the brick on a surface that can be off the original screen"""
        for brick in self.isolated_islands:
            surface.blit(self.main.assets[brick['type']][brick['variant']], (brick['pos'][0] - counteract[0], brick['pos'][1] - counteract[1]))

        """find the vertical (top left) placement of the other tiles"""
        for x in range(counteract[0] // self.brick_bigness, (counteract[0] + surface.get_width()) // self.brick_bigness + 1):
            """find the horizontal placement of the other tiles around it"""""
            for y in range(counteract[1] // self.brick_bigness, (counteract[1] + surface.get_height()) // self.brick_bigness + 1):
                place = str(x) + ';' + str(y)
                if place in self.map:
                    brick = self.map[place]
                    surface.blit(self.main.assets[brick['type']][brick['variant']], (brick['pos'][0] * self.brick_bigness - counteract[0], brick['pos'][1] * self.brick_bigness - counteract[1]))

