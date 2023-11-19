import pygame
import random
import time
import sys
import colours_table

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Color Flashing Screen")

# Function to generate a random color
def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

def rgb_to_hex(rgb):
    return "{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# Main loop
clock = pygame.time.Clock()
change_color_interval = 5  # in seconds
next_color_change_time = time.time() + change_color_interval
font = pygame.font.Font("Consolas.ttf", 36)
font2 = pygame.font.Font("Consolas.ttf", 18)
cc = 1
font3 = pygame.font.Font("Consolas.ttf", 24)

col = random_color()
screen.fill(col)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if it's time to change the color
    current_time = time.time()
    if current_time >= next_color_change_time:
        col = random_color()
        screen.fill(col)
        next_color_change_time = current_time + change_color_interval
        cc += 1


    pygame.display.flip()
    if col[0] + col[1] + col[2] > 650:
        text = font.render(colours_table.color_name(rgb_to_hex(col))[0], True, (0, 0, 0))
    else:
        text = font.render(colours_table.color_name(rgb_to_hex(col))[0], True, (255, 255, 255))
    screen.blit(text, (20, 20))
    offset_bottom = text.get_height() + 5
    if col[0] + col[1] + col[2] > 650:
        text2 = font2.render(colours_table.color_name(rgb_to_hex(col))[1], True, (0, 0, 0))
    else:
        text2 = font2.render(colours_table.color_name(rgb_to_hex(col))[1], True, (255, 255, 255))
    screen.blit(text2, (20, 20 + offset_bottom))
    if col[0] + col[1] + col[2] > 650:
        text3 = font3.render("Color #" + str(cc), True, (0, 0, 0))
    else:
        text3 = font3.render("Color #" + str(cc), True, (255, 255, 255))
    screen.blit(text3, (width - 20 - text3.get_width(), 20))
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pygame.quit()
sys.exit()

