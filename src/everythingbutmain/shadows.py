import random


class Shadow:

    """
    loading in background clouds. and making them move.
    """

    def __init__(self, position, pic, pace, deep):
        self.position = list(position)
        self.pict = pic
        # how fast it goes
        self.pace = pace
        # how deep it is in the sky
        self.deep = deep

    def version(self):
        """the speed that the cloud is going."""
        self.position[0] += self.pace

    def translate(self, surface, counteract=(0, 0)):
        """puts the cloud on a surface and causes it to move slower then everything else"""
        translate_position = (self.position[0] - counteract[0] * self.deep, self.position[1] * self.deep)
        surface.blit(self.pict, (translate_position[0] % (surface.get_width() + self.pict.get_width()) - self.pict.get_width(), translate_position[1] % (surface.get_height() + self.pict.get_height()) - self.pict.get_height()))


class Shadows:

    """
    loops a set amount of clouds
    """

    def __init__(self, cloudy, tally=16):
        self.cloudy_day = []
        
        """sorting all the clouds key determines how you sort things (sort them by depth) will help with speed 
        layering"""
        for i in range(tally):
            self.cloudy_day.append(Shadow((random.random() * 99999, random.random() * 99999), random.choice(cloudy), random.random() * 0.05 + 0.05, random.random() * 0.6 + 0.2))
        self.cloudy_day.sort(key=lambda x: x.depth)

    def version(self):
        """updates the cloud"""
        for shadow in self.cloudy_day:
            shadow.version()

    def translate(self, surface, counteract=(0, 0)):
        """puts the cloud on a surface and makes sure that the clouds are not on top of each other"""
        for shadow in self.cloudy_day:
            shadow.translate(surface, counteract=counteract)

