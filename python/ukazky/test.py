import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

    clock.tick(60)

pygame.quit()


# odpoved = int(input("Zadej číslo:"))

# for i in range(odpoved + 1):
#     if i < 13:
#         print(i)

#     elif i > 13:
#         print(i)

# while True:
#     print(i)