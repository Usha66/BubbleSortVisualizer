import pygame
import random
import time

pygame.font.init()

# Set window dimensions and title
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort Visualizer for Puppies")

# Initialize colors
BLACK = (0, 0, 0)
DARK_BLUE = (51, 102, 153)
DARK_PURPLE = (102, 51, 153)
DARK_PINK = (153, 51, 102)
GOLD = (255, 215, 0)
WHITE = (255, 255, 255)

# Load puppy image
puppy_img_path = "C:\\Users\\usha\\OneDrive\\Desktop\\pup.jpeg"  # Specify the file path to your puppy image
puppy_img = pygame.image.load(puppy_img_path).convert_alpha()

# Scale down the puppy image
puppy_width, puppy_height = 80, 80  # Specify the desired width and height
puppy_img = pygame.transform.scale(puppy_img, (puppy_width, puppy_height))

# Initialize font
font = pygame.font.SysFont(None, 30)
font_small = pygame.font.SysFont(None, 20)

# Initialize array and color array
array_length = 150
array = [random.randint(50, 400) for _ in range(array_length)]  # Adjusted range for better visualization
array_colors = [DARK_BLUE] * array_length

# Initialize start time
start_time = time.time()

def draw():
    screen.fill(BLACK)

    # Draw instructions
    text_start_sort = font.render("Press ENTER to start sorting", True, GOLD)
    text_generate_array = font.render("Press R to generate new array", True, GOLD)
    text_time = font_small.render(f"Running Time (sec): {int(time.time() - start_time)}", True, GOLD)
    screen.blit(text_start_sort, (20, 20))
    screen.blit(text_generate_array, (20, 50))
    screen.blit(text_time, (screen_width - 200, 20))

    # Draw puppies representing array elements
    for i in range(array_length):
        puppy_scaled_height = array[i]  # Scale puppy height based on array value
        screen.blit(puppy_img, (50 + i * (puppy_width + 2), screen_height - puppy_scaled_height - puppy_height))
        # Display array element value next to puppy image
        text_value = font_small.render(str(array[i]), True, WHITE)
        screen.blit(text_value, (50 + i * (puppy_width + 2), screen_height - puppy_scaled_height - puppy_height - 20))

    pygame.display.update()

def bubble_sort_generator(arr):
    """ A generator that performs bubble sort step by step """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr  # Yield after every swap

def generate_array():
    global array, array_colors, start_time, sorting_generator
    array = [random.randint(50, 400) for _ in range(array_length)]  # Adjusted range for better visualization
    array_colors = [DARK_BLUE] * array_length
    start_time = time.time()
    sorting_generator = None  # Reset the sorting generator
    draw()

# Initialize sorting generator
sorting_generator = None
generate_array()

running = True
sorting = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generate_array()
                sorting = False
            if event.key == pygame.K_RETURN and not sorting:
                sorting = True
                sorting_generator = bubble_sort_generator(array)  # Initialize sorting generator

    # Handle sorting and drawing
    if sorting and sorting_generator is not None:
        try:
            next(sorting_generator)  # Perform the next step in bubble sort
            draw()
            pygame.time.delay(20)  # Delay to visualize each step
        except StopIteration:
            sorting = False  # Sorting finished

pygame.quit()
