import pygame
import story
import sys
import textwrap
from pygame import mixer

# Set up the game window
WIDTH = 800
HEIGHT = 620
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Text-based Game")

# Initialize Pygame
pygame.init()

# Define colors
CREME = (255, 253, 208)
WINDOW_COLOR = (150, 163, 151)
LINE_COLOR = (30, 33, 30)
DOT = (50, 38, 212)
INVENTORY_ITEMS_COLOR = (0, 0, 0)
PROLOGUE_COLOR = (0, 0, 0)

sound1 = pygame.mixer.Sound("music/Minecraft Menu Button Sound Effect Sounffex (mp3cut.net)(1).mp3")


# Create a class for the menu
class Menu:
    def __init__(self):
        self.options = ["Start Game", "Quit"]
        self.selected_option = 0
        self.image = pygame.image.load("Game_Pics/1237768.jpg")

        pygame.mixer.music.load("music/Private Investigator.mp3")
        pygame.mixer.music.play(-1)

    def draw(self):
        # Set up fonts
        title_font = pygame.font.Font(None, 60)
        option_font = pygame.font.Font(None, 36)

        # Set up background color
        window.fill(WINDOW_COLOR)
        window.blit(self.image, (0, 0))

        # Draw the title
        title_text = title_font.render("Murder on the Train", True, WINDOW_COLOR)
        title_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 200))
        window.blit(title_text, title_rect)

        # Draw the options
        for i, option in enumerate(self.options):
            option_text = option_font.render(option, True, WINDOW_COLOR)
            option_rect = option_text.get_rect(center=(WIDTH / 2, HEIGHT / 1.43 + i * 50))

            # Draw a highlight around the selected option
            if i == self.selected_option:
                pygame.draw.rect(window, CREME, option_rect, 100)

            window.blit(option_text, option_rect)

    def update_selection(self, direction):
        self.selected_option += direction
        if self.selected_option < 0:
            self.selected_option = len(self.options) - 1
        elif self.selected_option >= len(self.options):
            self.selected_option = 0


class Prologue:
    def __init__(self, text, image, enter):
        self.text = text
        self.image = image
        self.enter = enter

    def draw(self):
        # Set up fonts
        enter_font = pygame.font.Font(None, 27)
        prologue_font = pygame.font.SysFont("Georgia", 20)

        # Set up background color

        window.fill(INVENTORY_ITEMS_COLOR)
        window.blit(self.image, (-300, 0))

        # Draw the prologue text
        enter_text = enter_font.render(self.enter, True, PROLOGUE_COLOR)
        enter_rect = enter_text.get_rect(left=500, top=560)
        pygame.draw.rect(window, CREME, enter_rect, 10)
        window.blit(enter_text, enter_rect)

        text = 'PROLOGUE'  # for prologue
        font = pygame.font.Font(None, 30)
        text_render = font.render(text, True, (33, 38, 46))
        text_x = 50
        text_y = 50
        window.blit(text_render, (text_x, text_y))

        prologue_lines = textwrap.wrap(self.text, 78)
        y = 80
        for line in prologue_lines:
            prologue_text = prologue_font.render(line, True, (0, 0, 0))
            prologue_rect = prologue_text.get_rect(left=50, top=y)
            window.blit(prologue_text, prologue_rect)
            y += 24


# idea -- write the bottom text in the same colour as menu options color


class Player:
    def __init__(self):
        pass

    def draw(self):
        pass


# Create an instance of the menu
menu = Menu()

prologue1 = Prologue("London, 1868, A city cloaked in a fog of coal smoke and secrets, where gas lamps "
                     "flickered, casting eerie shadows on cobblestone streets. As you make your way along a dimly lit"
                     " road, the sound of your boots echoed against the damp stones and the surrounding buildings,"
                     " blending with the distant sound of traffic and muffled conversations. The thick mist embraced"
                     " the city, veiling its mysteries, but your trained eye could discern the subtle signs"
                     "of trouble. And trouble, it seemed, awaited you just ahead. As you were thinking, you encounter a"
                     " chap working at the road. The chap screams:                                       "
                     "                                Hey! Someone help! Some tramp found something down there!",
                     pygame.image.load(
                         r"C:Game_Pics/600965.jpg"),
                     "press 'Enter' to continue.")
prologue2 = Prologue("Looks like foul play! You rush to the scene. In the dimly lit streets of the city, "
                    "shadows danced along the crumbling "
                    "facades of buildings. The air was thick with a palpable tension, as if the very atmosphere held "
                    "secrets that were itching to be unraveled. It was a city that had seen its fair share of crimes, "
                    "a breeding ground for both the desperate and the cunning. You instantly walk down the road "
                    "under to the arches of an ancient bridge.      There, lying on the ground, was a lifeless body - a "
                    "gentleman whose face bore the pallor of death and whose finely tailored clothing contrasted "
                    "starkly with the squalor of the surroundings. The mist draped him like a mourning shroud, "
                    "while the flickering light of a gas lamp cast an eerie glow upon his still form.",
                    pygame.image.load(
                        r"Game_Pics/assassins_creed_syndicate_london_art-7.png"),
                    "press 'Enter' to start story.")

# Flag to control whether the menu is active
menu_active = True
prologue2_active = True
prologue1_active = True
# accuse_active = False

# Create an instance of the current scene
current_scene = story.initial_scene

# Create an instance of the player
player = Player()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            sound1.play()
            if menu_active or prologue2_active:
                if menu_active:

                    if event.key == pygame.K_UP:
                        menu.update_selection(-1)
                    elif event.key == pygame.K_DOWN:
                        menu.update_selection(1)
                    elif event.key == pygame.K_RETURN:
                        if menu.selected_option == 0:
                            menu_active = False
                            pygame.mixer.music.stop()
                            # Load the music files
                            music_files = [
                                "music/AC Syndicate OST Austin Wintory - London Is Waiting.mp3",
                                "music/AC Syndicate OST Austin Wintory - Danza alla Daggers.mp3",
                                "music/FASTEST-2021-09-06_-_Solving_The_Crime_-_David_Fesliyan.mp3",
                                "music/2018-07-22_-_The_Unsolved_Murder_-_David_Fesliyan.mp3",
                                "music/Fastest-Version-2021-10-23_-_Sneaky_Action_-_David_Fesliyan.mp3"
                            ]
                            # Load the first music file
                            pygame.mixer.music.load(music_files[0])
                            # Queue the remaining music files
                            for file in music_files[1:]:
                                pygame.mixer.music.queue(file)
                            # Play the music
                            pygame.mixer.music.play()

                        elif menu.selected_option == 1:
                            pygame.quit()
                            sys.exit()

                elif prologue2_active:
                    if event.key == pygame.K_RETURN:
                        if prologue1_active:
                            prologue1_active = False
                            game_active = True
                        else:
                            prologue2_active = False
                            prologue1_active = True

                    elif event.key == pygame.K_ESCAPE:
                        menu_active = True
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("music/Private Investigator.mp3")
                        pygame.mixer.music.play()

            else:
                if event.key == pygame.K_ESCAPE:
                    menu_active = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music/Private Investigator.mp3")
                    pygame.mixer.music.play()

                if event.key == pygame.K_UP:
                    current_scene.update_selection(-1)
                    current_scene.display_dialogue = False
                elif event.key == pygame.K_DOWN:
                    current_scene.update_selection(1)
                    current_scene.display_dialogue = False
                elif event.key == pygame.K_RETURN:
                    # If dialogue is not being displayed
                    if current_scene.options[current_scene.selected_option] == "Accuse":
                        current_scene = story.scene_accuse
                        if current_scene.options[current_scene.selected_option] == "Go back":
                            current_scene = story.mid_train

                    elif current_scene.options[current_scene.selected_option] == "Restart":
                        prologue2_active = True
                        current_scene = story.initial_scene
                    elif current_scene.options[current_scene.selected_option] == "Quit":
                        pygame.quit()
                        sys.exit()

                    elif current_scene.dialogue[current_scene.selected_option] is None:
                        next_scene_variable = current_scene.next_scene_variables[current_scene.selected_option]
                        if next_scene_variable is not None:
                            next_scene = current_scene.next_scene_map.get(next_scene_variable)
                            if next_scene:
                                current_scene = next_scene

                        if current_scene == story.restaurant_carriage:
                            story.handle_Peter_Ryan_selection(current_scene.selected_option)
                            story.handle_Peter_Luke_selection(current_scene.selected_option)
                        if current_scene == story.sleeper_2:
                            story.handle_Vivian_Ryan_selection(current_scene.selected_option)
                            story.handle_Vivian_Luke_selection(current_scene.selected_option)
                            story.handle_Vivian_Wolf_selection(current_scene.selected_option)
                        if current_scene == story.sleeper_1:
                            story.handle_Valet_Wolf_selection(current_scene.selected_option)



                    else:
                        current_scene.display_dialogue = True  # Set display_dialogue to True

                        if current_scene == story.initial_scene:
                            story.handle_Coat_Tramp_selection(current_scene.selected_option)
                            story.handle_Watch_Tramp_selection(current_scene.selected_option)
                        if current_scene == story.initial_scene2:
                            story.handle_Station_selection(current_scene.next_scene_variables[current_scene.selected_option])

                        if current_scene == story.restaurant_carriage:
                            story.handle_pills_Ryan_selection(current_scene.selected_option)
                        if current_scene == story.Peter:
                            story.handle_Vivian_Peter_selection(current_scene.selected_option)
                        if current_scene == story.Ryan:
                            story.handle_Vivian_Ryan_selection(current_scene.selected_option)

                        if current_scene == story.sleeper_2:
                            story.handle_Scheme_Ryan_selection(current_scene.selected_option)
                            story.handle_Note_Vivian_selection(current_scene.selected_option)




    # Draw the current scene and player
    if menu_active:
        menu.draw()
    elif prologue2_active:
        prologue2.draw()
        if prologue1_active:
            prologue1.draw()

    else:
        current_scene.draw()
        player.draw()

    # Update the display
    pygame.display.update()
    # clock.tick(60)

