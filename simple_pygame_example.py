"""first pygame test"""

# https://www.geeksforgeeks.org/how-to-make-a-pygame-window/

# import the pygame module
import pygame
import random
import imageio

# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((300, 300))

# Set the caption of the screen
pygame.display.set_caption("TestPygameRecording")

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# Define the initial position and velocity of the circle
circle_pos = [150, 150]
circle_radius = 15
circle_velocity = [random.randint(-5, 5), random.randint(-5, 5)]

# List to store frames
frames = []

# Game loop for 100 frames
for _ in range(100):
    # Fill the background colour to the screen
    screen.fill(background_colour)

    # Update the circle's position
    circle_pos[0] += circle_velocity[0]
    circle_pos[1] += circle_velocity[1]

    # Check for collision with the window boundaries and reverse direction if needed
    if circle_pos[0] - circle_radius < 0 or circle_pos[0] + circle_radius > 300:
        circle_velocity[0] = -circle_velocity[0]
    if circle_pos[1] - circle_radius < 0 or circle_pos[1] + circle_radius > 300:
        circle_velocity[1] = -circle_velocity[1]

    # Draw the circle on the screen
    pygame.draw.circle(screen, (0, 0, 255), circle_pos, circle_radius)

    # Update the display
    pygame.display.flip()

    # Save the current frame
    frame = pygame.surfarray.array3d(screen)
    frames.append(frame)

# Quit Pygame
pygame.quit()

# Save frames as a video
imageio.mimsave('output_video.mp4', frames, fps=30)
