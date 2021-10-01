import pygame
from aircraft_sprites import *


pygame.init()
class AircraftGame(object):
    """Aircraft Main Game"""

    def __init__(self):
        print("Loading Game...")

        self.screen = pygame.display.set_mode((480, 700))

        self.clock = pygame.time.Clock()

        self.__create_sprites()

        # timer event for enemy
        pygame.init()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


    def __create_sprites(self):

        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # create enemy group
        self.enemy_group = pygame.sprite.Group()
        # create hero group
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("Game Start...")

        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

            pass

    def __event_handler(self):
        for event in pygame.event.get():

            # if quit game
            if event.type == pygame.QUIT:
                AircraftGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
            #    print("Enemy Coming...")
                # create enemy sprite
                enemy = Enemy()
                # add sprite to group
                self.enemy_group.add(enemy)
            elif event.type ==HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
              #  print("moving right...")

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 1 bullet collide enemy
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2 enemy collide hero
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 3 if enemies have content
        if len(enemies) > 0:

            # hero died
            self.hero.kill()

            #end game
            AircraftGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("Game Over")

        pygame.quit()
        exit()


if __name__ == '__main__':

    game = AircraftGame()

    game.start_game()