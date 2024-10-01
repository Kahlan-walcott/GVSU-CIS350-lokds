# is utils
import pygame
import os
# the place where all the images are in
IMAGE_TRACK = 'artifacts/images/'


def insert_img(track):
    """converts the image in pygame and makes it more efficient for rendering"""
    image = pygame.image.load(IMAGE_TRACK + track).convert()
    image.set_colorkey((0, 0, 0))
    return image


def insert_imgs(track):
    """will take a path and give you all the images in that path."""
    picts = []
    # use sorted because Linux machines organize the files differently
    for picn in sorted(os.listdir(IMAGE_TRACK + track)):
        picts.append(insert_img(track + '/' + picn))
    return picts


class Liveliness:

    """
    Controls the movement of character and anything that moves.
    """

    def __init__(self, pics, pic_duration=5, circle=True):
        self.picts = pics
        self.circle = circle
        self.pic_duration = pic_duration
        # the 2 below are specific to individual animations
        self.finished = False
        # frame of animation (where we are in the animation)
        self.scene = 0  

    def duplicate(self):
        """making a copy of its self (getting the same list of images) the images don't take extra memory because they
        are looking at the same thing"""
        return Liveliness(self.picts, self.pic_duration, self.circle)

    def version(self):
        """forces the scene to loop around when it reaches the end."""
        if self.circle:
            self.scene = (self.scene + 1) % (self.pic_duration * len(self.picts))
        else:
            self.scene = min(self.scene + 1, self.pic_duration * len(self.picts) - 1)
            if self.scene >= self.pic_duration * len(self.picts) - 1:
                self.finished = True

    def image(self):
        """get the current image of the animation (not giving it a surface to render to)"""
        return self.picts[int(self.scene / self.pic_duration)]


