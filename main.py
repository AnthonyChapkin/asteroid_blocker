import pygame

from sys import exit

from classes import Planet, Moon, Asteroid


def game_loop():

    pygame.init()

    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Asteroid Blocker')
    window_icon = pygame.image.load('assets/graphics/asteroids/asteroid_1.png')
    pygame.display.set_icon(window_icon)

    clock = pygame.time.Clock()
    start_time = 0
    score = 0
    asteroid_spawn_time = 1
    asteroid_timer = 0

    game_active = False

    font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

    background_surf = pygame.image.load('assets/graphics/space.png').convert_alpha()

    planet_group = pygame.sprite.GroupSingle()
    planet_group.add(Planet())

    moon_group = pygame.sprite.GroupSingle()
    moon_group.add(Moon())

    asteroid_group = pygame.sprite.Group()

    while True:

        for event in pygame.event.get():

            if event.type is pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_active:
                game_active = True
                start_time = pygame.time.get_ticks() // 1000

        if game_active:
            if asteroid_timer >= asteroid_spawn_time:
                asteroid_timer = 0
                asteroid_spawn_time -= 0.005
                asteroid_group.add(Asteroid())
            else:
                asteroid_timer += 0.01

            screen.blit(background_surf, (0, 0))

            current_time = int(pygame.time.get_ticks() / 1000) - start_time
            score_surf = font.render(f'Score: {current_time}', False, 'White')
            score_rect = score_surf.get_rect(center=(500, 30))
            screen.blit(score_surf, score_rect)
            score = current_time

            planet_group.draw(screen)

            moon_group.update()
            moon_group.draw(screen)

            asteroid_group.update()
            asteroid_group.draw(screen)

            if pygame.sprite.groupcollide(asteroid_group, planet_group, False, False):
                game_active = False

            collided_sprites = pygame.sprite.groupcollide(asteroid_group, moon_group, False, False)
            if collided_sprites:
                for asteroid in collided_sprites:
                    asteroid: Asteroid
                    asteroid.bounce_off()

        else:
            asteroid_group.empty()

            tittle_surf = font.render('Asteroid Blocker', False, 'Grey')
            tittle_rect = tittle_surf.get_rect(center=(500, 300))

            game_message = font.render('Click to start', False, 'White')
            game_message_rect = game_message.get_rect(center=(500, 400))

            score_surf = font.render(f'Your score: {score}', False, (111, 196, 169))
            score_rect = score_surf.get_rect(center=(500, 400))

            screen.fill((0, 0, 0))
            screen.blit(tittle_surf, tittle_rect)

            if score > 0:
                screen.blit(score_surf, score_rect)
            else:
                screen.blit(game_message, game_message_rect)

        pygame.display.update()
        clock.tick(100)


if __name__ == "__main__":
    game_loop()
