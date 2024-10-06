class Fragment:
    
    """
    Makes fragments like leafs move or fall.
    """
    
    def __init__(self, maingame, player_variety, position, quickness=None, structure=0):
        if quickness is None:
            quickness = [0, 0]
        self.main = maingame
        self.variety = player_variety
        self.position = list(position)
        self.quickness = quickness
        self.movement = self.main.assets['particles/' + player_variety].copy()
        self.movement.structure = structure

    def version(self):
        """updates the velocity and animation and it kills the animation."""
        dead = False
        if self.movement.finished:
            dead = True

        self.position[0] += self.quickness[0]
        self.position[1] += self.quickness[1]

        self.movement.version()

        return dead

    def translate(self, surface, counteract=(0, 0)):
        """Puts a picture on the surface."""
        pict = self.movement.image()
        # x and y
        surface.blit(pict, (self.position[0] - counteract[0] - pict.get_width() // 2, self.position[1] - counteract[1] - pict.get_height() // 2))

