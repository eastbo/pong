import pygame
import sys
from Settings import settings
from Draw import draw
from Players import players

class Pong:
    """A class to manage overall settings within the game"""
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.draw = draw()
        self.players = players()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("Pong")
        self.left_player_y = int(self.settings.HEIGHT/2)
        self.right_player_y = int(self.settings.HEIGHT/2)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.l_change = 0
        self.r_change = 0

    def run_game(self):
        """Run the game"""
        while True:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == self.draw.left_player_keys[0]:
                        self.l_change = -10
                    if event.key == self.draw.left_player_keys[1]:
                        self.l_change = 10
                    if event.key == self.draw.right_player_keys[0]:
                        self.r_change = -10
                    if event.key == self.draw.right_player_keys[1]:
                        self.r_change = 10

            self.left_player_y, self.right_player_y = self.players.move_players(self.left_player_y, self.right_player_y, self.l_change, self.r_change)

            self.screen.fill(self.settings.bg_col)

            ###Draw items here###
            self.draw.left_player(self.screen, self.left_player_y)
            self.draw.right_player(self.screen, self.right_player_y)
            #####################

            pygame.display.flip()


if __name__ == '__main__':
    p = Pong()
    p.run_game()
