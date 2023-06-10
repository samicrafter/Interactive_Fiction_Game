import pygame
import textwrap
from pygame import mixer

WIDTH = 800
HEIGHT = 620
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init()

WINDOW_COLOR = (71, 70, 82)
LINE_COLOR = (255, 255, 255)
OUTLINE_COLOR = (0, 0, 0)
# OPTION_COLOR = (24, 25, 28)
OPTION_COLOR = (255, 255, 255)
OPTION_BACKGROUND_COLOR = (71, 70, 82)
DOT = (50, 38, 212)
HIGHLIGHT_COLOR = (178, 176, 209)
INVENTORY_ITEMS_COLOR = (0, 0, 0)
# CREME = (255, 253, 208)
CREME = (145, 140, 126)
box_color = (232, 200, 58)
END_COLOR = (0, 0, 0)


class Scene:
    def __init__(self, description, options, next_scene_variables, next_scene_map, image, image_xy, dialogue=None):
        self.description = description
        self.options = options
        self.next_scene_variables = next_scene_variables
        self.next_scene_map = next_scene_map
        self.image = image
        self.image_xy = image_xy
        self.dialogue = dialogue
        self.selected_option = 0
        self.display_dialogue = False

    def draw(self):

        # pygame.font.
        description_font = pygame.font.Font(None, 28)
        option_font = pygame.font.Font(None, 24)
        dialogue_font = pygame.font.SysFont("Georgia", 20)

        window.fill(WINDOW_COLOR)
        window.blit(self.image, self.image_xy)

        # rectangle for dialogue box
        box_out_color = (17, 17, 18)
        box_color = (232, 200, 58)
        box_y = 450

        box_out = pygame.Rect(300, box_y - 5, 485, 165)
        pygame.draw.rect(window, box_out_color, box_out)
        box_rect = pygame.Rect(305, box_y, 475, 155)
        pygame.draw.rect(window, box_color, box_rect)

        description_lines = textwrap.wrap(self.description, 72)
        y = 50
        for line in description_lines:
            description_text = description_font.render(line, True, LINE_COLOR)
            description_rect = description_text.get_rect(left=50, top=y)
            window.blit(description_text, description_rect)
            y += 30

        option_y = HEIGHT - 170
        for i, option in enumerate(self.options):  # enumerate done
            option_text = option_font.render(option, True, OPTION_COLOR)
            option_rect = option_text.get_rect(left=50, top=option_y)

            if self.display_dialogue and i < len(self.dialogue) and self.dialogue[i] is not None:
                if i == self.selected_option:
                    pygame.draw.rect(window, CREME, option_rect, 100)
                window.blit(option_text, option_rect)

            else:  # Draw a highlight around the selected option
                if i == self.selected_option:
                    pygame.draw.rect(window, CREME, option_rect, 100)
                window.blit(option_text, option_rect)

            option_y += 28

        text = 'DIALOG BOX'  # for inventory box
        font = pygame.font.Font(None, 30)
        text_render = font.render(text, True, (33, 38, 46))
        text_x = 312
        text_y = box_y + 5
        window.blit(text_render, (text_x, text_y))

        if self.display_dialogue and self.selected_option < len(self.dialogue):
            dialogue_lines = textwrap.wrap(self.dialogue[self.selected_option], 49)
            dialogue_y = box_y + 25
            for line in dialogue_lines:
                dialogue_text = dialogue_font.render(line, True, (33, 38, 46))
                dialogue_rect = dialogue_text.get_rect(left=312, top=dialogue_y)
                window.blit(dialogue_text, dialogue_rect)
                dialogue_y += 20

    def update_selection(self, direction):
        self.selected_option += direction
        if self.selected_option < 0:
            self.selected_option = len(self.options) - 1
        elif self.selected_option >= len(self.options):
            self.selected_option = 0


class Accuse:
    def __init__(self, options, next_scene_variables, next_scene_map, image, image_xy, dialogue):
        # self.description = description
        self.options = options
        self.next_scene_variables = next_scene_variables
        self.next_scene_map = next_scene_map
        self.image = image
        self.image_xy = image_xy
        self.selected_option = 0
        self.dialogue = dialogue

    def draw(self):
        # description_font = pygame.font.Font(None, 28)
        option_font = pygame.font.Font(None, 24)
        window.fill(WINDOW_COLOR)
        window.blit(self.image, self.image_xy)

        text = 'Whom will you Accuse?'  # for inventory box
        font = pygame.font.Font(None, 30)
        text_render = font.render(text, True, (250, 250, 250))  # (33,38,46)
        text_x = 250
        text_y = 105
        window.blit(text_render, (text_x, text_y))

        option_y = HEIGHT - 370
        for i, option in enumerate(self.options):  # enumerate done
            option_text = option_font.render(option, True, OPTION_COLOR)
            option_rect = option_text.get_rect(left=280, top=option_y)

            # Draw a highlight around the selected option
            if i == self.selected_option:
                pygame.draw.rect(window, CREME, option_rect, 100)
            window.blit(option_text, option_rect)

            option_y += 28

    def update_selection(self, direction):
        self.selected_option += direction
        if self.selected_option < 0:
            self.selected_option = len(self.options) - 1
        elif self.selected_option >= len(self.options):
            self.selected_option = 0


class GameEnd:
    def __init__(self, text, options, image, image_xy, dialogue, sound):
        self.text = text
        self.options = options
        self.image = image
        self.image_xy = image_xy
        self.dialogue = dialogue
        self.selected_option = 0
        self.sound = sound

    def draw(self):
        # Set up fonts
        option_font = pygame.font.Font(None, 27)
        end_font = pygame.font.SysFont("Georgia", 20)

        # Set up background color

        window.fill(INVENTORY_ITEMS_COLOR)
        window.blit(self.image, (0, 0))

        end = 'GAME END - Case Summary'  # for inventory box
        font = pygame.font.Font(None, 30)
        text_render = font.render(end, True, (250, 250, 250))  # (33,38,46)
        text_x = 50
        text_y = 50
        window.blit(text_render, (text_x, text_y))

        end_lines = textwrap.wrap(self.text, 78)
        y = 80
        for line in end_lines:
            end_text = end_font.render(line, True, (250, 250, 250))
            end_rect = end_text.get_rect(left=50, top=y)
            window.blit(end_text, end_rect)
            y += 24

        option_y = HEIGHT - 70
        for i, option in enumerate(self.options):  # enumerate done
            option_text = option_font.render(option, True, (250, 250, 250))  # OPTION_COLOR
            option_rect = option_text.get_rect(left=380, top=option_y)

            # Draw a highlight around the selected option
            if i == self.selected_option:
                pygame.draw.rect(window, CREME, option_rect, 100)
            window.blit(option_text, option_rect)

            option_y += 28

        self.sound.play()

    def update_selection(self, direction):
        self.selected_option += direction
        if self.selected_option < 0:
            self.selected_option = len(self.options) - 1
        elif self.selected_option >= len(self.options):
            self.selected_option = 0


Sam_end = GameEnd(
    "Sam is not the culprit",
    ["Restart", "  Quit  "],
    pygame.image.load(
        "Game_Pics/1237768.jpg"),
    (0, 0),
    [None, None],
    pygame.mixer.Sound("music/Mission Failed Sound Effect (mp3cut.net).mp3"))

Luke_end = GameEnd(
    "Luke is not the culprit",
    ["Restart", "  Quit  "],
    pygame.image.load(
        "Game_Pics/1237768.jpg"),
    (0, 0),
    [None, None],
    pygame.mixer.Sound("music/Mission Failed Sound Effect (mp3cut.net).mp3"))

Wolf_end = GameEnd(
    "Wolf is not the culprit",
    ["Restart", "  Quit  "],
    pygame.image.load(
        "Game_Pics/1237768.jpg"),
    (0, 0),
    [None, None],
    pygame.mixer.Sound("music/Mission Failed Sound Effect (mp3cut.net).mp3")
)

Peter_end = GameEnd(
    "The murderer was Peter Jespers, who wanted revenge for being put out of work by the victim.                       "
    "                                                 Industrialist Matthew Killian was drugged and thrown from the top"
    " of a moving train by his former employee, "
    "Peter Jespers! Put out of work by the mechanization of Killian's factory, Peter found employment as a humble "
    "train steward. However, one evening Peter realized that Killian was in his very train (prior to this journey "
    "Peter had never seen Killian, but now recognized him from a recent newspaper article). Peter, knowing that "
    "frequent passenger Vivian often swindled wealthy fellow passengers, waited until she lured Killian to her "
    "compartment. He cunningly arranged for her to be called away by means of an anonymous note. Peter then used his "
    "considerable strength to lift the drugged magnate and drag him to the top of the train, whence he threw him to "
    "his death at midnight! Killian's rival, Angus Wolf, had hoped to get Killian so inebriated as to prevent him "
    "from participating in a business meeting on the following day, but Wolf himself fell afoul of the drugged brandy "
    "and slept through the entire episode! As for Peter the murderer... perhaps he meted out justice, in turn he will "
    "not meet justice himself! – Henry Raymond ",
    ["Restart", "  Quit  "],
    pygame.image.load(
        "Game_Pics/1237768.jpg"),
    (0, 0),
    [None, None],
    pygame.mixer.Sound("music/Assassin's Creed Flag Sound Effect 1 of 2.mp3"))

Vivian_end = GameEnd(
    "Vivian is not the culprit",
    ["Restart", "  Quit  "],
    pygame.image.load(
        "Game_Pics/1237768.jpg"),
    (0, 0),
    [None, None],
    pygame.mixer.Sound("music/Mission Failed Sound Effect (mp3cut.net).mp3")
)

Ryan_end = GameEnd(
    "Ryan is not the culprit",
    ["Restart", "  Quit  "],
    pygame.image.load(
        "Game_Pics/1237768.jpg"),
    (0, 0),
    [None, None],
    pygame.mixer.Sound("music/Mission Failed Sound Effect (mp3cut.net).mp3")
)
scene_accuse = Accuse(["Ryan", "Vivian", "Peter", "Mr.wolf", "Luke",
                       "Sam", "Return"],
                      ["Ryan", "Vivian", "Peter", "Wolf", "Luke", "Sam", "Go back"],
                      {
                          "Ryan": Ryan_end,
                          "Vivian": Vivian_end,
                          "Peter": Peter_end,
                          "Wolf": Wolf_end,
                          "Luke": Luke_end,
                          "Sam": Sam_end,
                          "Go back": None
                      },
                      pygame.image.load(
                          "Game_Pics/1237768.jpg"),
                      (0, 0),
                      [None, None, None, None, None, None, None])

# sleeper2
Vivian = Scene("As you enter the room, you are met with a striking figure, exuding both elegance and an aura of "
               "intrigue. Vivian's appearance is captivating, with a mane of cascading dark curls that frame her "
               "face. Her piercing eyes, a shade of deep emerald, hold a hint of guardedness, as if she has a secret "
               "hidden beneath her composed demeanor. Her flawless porcelain skin enhances her beauty, lending an air "
               "of enigma to her presence. Dressed in a tailored evening gown, Vivian exudes timeless style. The "
               "fabric clings to her slender figure, accentuating her grace and poise. Subtle jewelry adorns Vivian's "
               "wrists and neck, adding a touch of understated glamour.",
               ['Enquire about last evening', 'Enquire about killian',
                'Enquire about a letter from sis', "Go back"],
               [99, 99, 99, "Go back"],
               {
                   "Go back": None
               },
               pygame.image.load(
                   "Game_Pics/train_scene.jpg"),
               (0, 0),
               ["Vivian :Nothing unusual at all! I had a drink with some gents and then retired to my sleeper",
                "Vivian :The rich fella? I did talk with him. Very charming, but a single woman has to be careful, "
                "you know. Did something happen to him?",
                "Vivian :Oh, all right. I flirt with rich blokes and the barman slips 'em a mickey. I take 'em back "
                "to my sleeper and they nod off,before I have to do anything shameful.They wake up thinkin' they had "
                "a night o' fun and hand me a few quid. That's what happened with Mr. Killian, but he was gone when I "
                "come back from looking for the man who left the note.",
                None])
roof_scene3 = Scene("The gustling air blows onto your face as you climb up the roof of the train. Unfortunatley, "
                    "you seem to find no clue up here",
                    ["Get Down"],
                    ["Go back"],
                    {
                        "Go back": None
                    },
                    pygame.image.load(
                        "Game_Pics/olivier-carignan-victoriastation-extfront.jpg"),
                    (-300, 20),
                    [None])
# sleeper_2
sleeper_2 = Scene("The walls of Sleeper 2 are adorned with plush velvet drapes in deep hues, creating an atmosphere "
                  "of warmth and elegance. The gentle flicker of gas lamps casts a soft glow, adding to the ambiance "
                  "of comfort and tranquility. The polished wood paneling, intricately carved with delicate patterns, "
                  "exudes a sense of timeless craftsmanship. The compartment features two comfortably-sized berths, "
                  "each adorned with luxurious bedding. The linens are crisp and meticulously arranged, "
                  "inviting weary travelers to rest and rejuvenate. Soft pillows and plush blankets provide a cocoon "
                  "of comfort",
                  ["Inspect the roof", 'Look at the handbag', 'Talk to the lady',
                   'a note on floor', "Go back"],
                  ["Roof", 99, "Vivian", 99, "Go back"],
                  {
                      "Roof": roof_scene3,
                      "Vivian": Vivian,
                      "Go back": None
                  },
                  pygame.image.load(
                      "Game_Pics/train_scene.jpg"),
                  (0, 0),
                  [None,
                   'Contains a letter: '"How goes it. Viv? Hook any more fish? It's a lovely caper you've got going- "
                   "need to find me a bonny ''scheme'' like that. Let's have a glass next time you're in Soho, Luv! -Your"
                   "sis", None,
                   'Note – A handwritten note: "Come to the restaurant carriage quickly."', None])

Vivian.next_scene_map["Go back"] = sleeper_2
roof_scene3.next_scene_map["Go back"] = sleeper_2


def handle_Note_Vivian_selection(option):
    if option == 3:
        if 'Talk about the note' not in Vivian.options:
            Vivian.options.insert(-1, 'Talk about the note')
            Vivian.next_scene_variables.insert(-1, 99)
            Vivian.dialogue.insert(-1,
                                   "Vivian :Someone slipped a note under my sleeper door a few minutes before "
                                   "midnight. It said I should come to the dining car. I went, but only Ryan and "
                                   "Wolf's man were there and they were both drunk."
                                   )


# sleeper 1
Sam = Scene("The detective now goes to interrogate sam, valet of Mr Wolf",
            ['Enquire about last evening', 'Enquire about midnight', "Enquire about Killian",
             "Enquire about Mr.Wolf", "Go back"],
            [99, 99, 99, 99, "Go back"],
            {
                "Go back": None
            },
            pygame.image.load(
                "Game_Pics/0e424d4e4efcd61c0bdaca53f729eb0f.jpg"),
            (0, 0),
            ["Sam :Mr. Wolf had a few with Mr. Killian. Then the young lady invited herself over to "
             "have a glass with 'em.",
             "Sam :Mr. Wolf became terribly tired even though he'd only had one drink. He toddled off to "
             "bed well before midnight. I stayed in the dining car for a few drinks with the barman.",
             "Sam :Mr. Wolf bought him drink after drink. Then they got angry. But the young lady come "
             "over and it's obvious that Mr. Killian was interested in a rendez-vous, like. Around about "
             "eleven-thirty, Killian and her left together.",
             "Sam : I been Mr. Wolf's valet for goin' on several years. He's frail and needs a man like me "
             "to help him about.", None])

Wolf = Scene(
    "There's wealthy Industrailist. Then the detective comes back on the floor ,he enters sleeper 1.There the detective interrogates  Angus "
    "wolf",
    ['Talk about the last evening', 'Enquire about killian', 'Talk about midnight', 'Continue investigating'],
    [99, 99, 99, "Go back"],
    {
        "Go back": None
    },
    pygame.image.load(
        "Game_Pics/582d97769e68354dd6d4ddd2371a662c.jpg"),
    (0, 0),
    ["Mr Wolf :I had drinks in the dining car with killian.We had business dealings in the past."
     "It was a pleasant surprise to discover him on this train .I suppose there were some disagreements,"
     " but there always are when a great deal of money is involved.",
     " Mr Wolf:I suppose there were some disagreements, "
     "but there always are when a great deal of money is involved.",
     " Mr Wolf :I felt unusually tired and came back here to get some sleep.",
     None])


def handle_Vivian_Wolf_selection(option):
    if option == 2:
        if "Enquire about Vivian" not in Wolf.options:
            Wolf.options.insert(-1, "Enquire about Vivian")
            Wolf.next_scene_variables.insert(-1, 99)
            Wolf.dialogue.insert(-1,
                                 "Angus Wolf:You mean the young lady? She and Killian hit it off famously. Embarrassing, "
                                 "really.")


roof_scene2 = Scene("There's nothing here on the roof",
                    ["Get Down"],
                    ["Go back"],
                    {
                        "Go back": None
                    },
                    pygame.image.load(
                        "Game_Pics/olivier-carignan-victoriastation-extfront.jpg"),
                    (-300, 20),
                    [None])
# sleeper_1
sleeper_1 = Scene("The detective continues his investigation, There's wealthy Industrailist ",
                  ['He finds an Item', 'He finds a letter', "Talk to Wolf", "Inspect the roof", 'Talk to Sam',
                   "Go back"],
                  [99, 99, "Wolf", "Roof", "Sam", "Go back"],
                  {
                      "Wolf": Wolf,
                      "Roof": roof_scene2,
                      "Sam": Sam,
                      "Go back": None
                  },
                  pygame.image.load(
                      "Game_Pics/0e424d4e4efcd61c0bdaca53f729eb0f.jpg"),
                  (0, 0),
                  ['A small, ivory-plated derringer. Chamber for two bullets, but one is missing.',
                   '"Killian will be on the 616 train to Cardiff to sign the papers. You must prevent him from '
                   'signing them at all costs or we shall be ruined!"',
                   None, None, None, None])


def handle_Valet_Wolf_selection(option):
    if option == 4:
        if 'Enquire about the valet' not in Wolf.options:
            Wolf.options.insert(-1, 'Enquire about the valet')
            Wolf.next_scene_variables.insert(-1, 99)
            Wolf.dialogue.insert(-1,
                                 "Angus Wolf: Sam? He's a trusted valet. He's terrifically strong,which makes him useful in many situations.")


Sam.next_scene_map["Go back"] = sleeper_1
Wolf.next_scene_map["Go back"] = sleeper_1
roof_scene2.next_scene_map["Go back"] = sleeper_1

# scene at passenger carriage
Luke = Scene(
    "Luke, the fair and youthful passenger carriage attendant, exudes charm with a well-groomed beard that adds "
    "maturity to his visage. His bright eyes and fair complexion instantly put people at ease. Dressed in a "
    "smart and polished train staff uniform, including a stylish cap, Luke takes pride in his role and "
    "presents himself with professionalism and authenticity.",
    ['Talk about last evening', 'Enquire about Killian', 'Talk about midnight', "Go back"],
    [99, 99, 99, "Go back"],
    {
        "Go back": None
    },
    pygame.image.load(
        "Game_Pics/582d97769e68354dd6d4ddd2371a662c.jpg"),
    (0, 0),
    ["Luke : Odd thing was, some noises on the roof woke me up briefly. You say someone was "
     "thrown from up there? You'd have to be a  very strong fellow to drag someone up onto the roof! ",
     "Luke : Killian was on this train ? Gor, I used to work at his foundry. I never even seen "
     "him. None a' us Workers ever looked what he looked like.",
     "Luke : Vivian had another of her dupes in her compartment by then. After that,"
     " I remember people going  past me from time to time, but I was half-asleep.",
     None])


def handle_Vivian_Luke_selection(option):
    if option == 2:
        if "Ask about Vivian" not in Luke.options:
            Luke.options.insert(-1, "Ask about Vivian")
            Luke.next_scene_variables.insert(-1, 99)
            Luke.dialogue.insert(-1,
                                 "That one! Clever little minx. She and the barman got a little scam goin'. I think "
                                 "everyone on staff knows about it.")


def handle_Peter_Luke_selection(option):
    if option == 2:
        if "Enquire about Peter" not in Luke.options:
            Luke.options.insert(-1, "Enquire about Peter")
            Luke.next_scene_variables.insert(-1, 99)
            Luke.dialogue.insert(-1,
                                 "Luke : Oh, Peter worked with me at the foundry. He's a very strong bloke. I got me "
                                 "arm mangled in one of the damned machines they put in. Then Killian sacked the "
                                 "whole crew. Peter, he helped me get hired as train staff.", )


roof_scene = Scene("The detective then climbs on the roof of the moving train and finds a shoe which matches the "
                   "victim's shoe, and there were some shoe prints.",
                   ["Get Down"],
                   ["Go back"],
                   {
                       "Go back": None
                   },
                   pygame.image.load(
                       "Game_Pics/olivier-carignan-victoriastation-extfront.jpg"),
                   (-300, 20),
                   [None])

passenger_carriage = Scene('The detective comes to the passenger carriage',
                           ["Talk to Luke", "Inspect the roof", "Go back"],
                           ["Luke", "Roof", "Go back"],
                           {
                               "Luke": Luke,
                               "Roof": roof_scene,
                               "Go back": None
                           },
                           pygame.image.load(
                               "Game_Pics/582d97769e68354dd6d4ddd2371a662c.jpg"),
                           (0, 0),
                           [None, None, None])
Luke.next_scene_map["Go back"] = passenger_carriage
roof_scene.next_scene_map["Go back"] = passenger_carriage

# Restaurant
Peter = Scene("He looks like peter, he's the restaurant carriage steward in the train",
              ["Ask about last evening", "Ask about Killian", "About midnight", "Go back"],
              [99, 99, 99, "Go back"],
              {
                  "Go back": None
              },
              pygame.image.load(
                  "Game_Pics/5e81d58221c02.jpg"),
              (0, 0),
              ["It was a typical evening. As far as I knew, nothing unusual happened until you came aboard with "
               "this story of a murder.",
               "Just another wealthy passenger. They're all pretty much the same.",
               "I was tidying up the passenger car. Around midnight, Vivian ran through—she thought someone was "
               "looking for her.",
               None])
Ryan = Scene("The detective goes to meet the next suspect ,ryan,the bartender",
             ['Talk to Ryan about the last evening', 'Go back'],
             [99, "Go back"],
             {
                 "Go back": None
             },
             pygame.image.load(
                 "Game_Pics/5e81d58221c02.jpg"),
             (0, 0),
             ["Nothing unusual. Couple of passengers came in and had a sort of business meeting."
              " One of 'em was buying a lot of drinks for the other, and then they started to argue."
              " But Vivian went over and joshed them out of it",
              None])

restaurant_carriage = Scene('You enter the restaurant carriage, The carriage is tastefully adorned with rich mahogany '
                            'panels, intricately carved with ornate patterns that evoke a sense of opulence. Soft, '
                            'ambient lighting emanates from elegant chandeliers suspended from the ceiling, '
                            'casting a warm glow over the surroundings. The tables are meticulously set with crisp '
                            'white linens, polished silverware, and delicate porcelain china, ready to accommodate '
                            'discerning diners. Plush, upholstered seats line the carriage, providing both comfort '
                            'and a touch of luxury. You see a bartender an ',
                            ["Read the newspaper lying on dining table", "Read a pamphlet at another table",
                             "Talk to Peter", "Talk to Ryan", "Look at item", "Go back"],
                            [99, 99, "Peter", "Ryan", 99, "Go back"],
                            {
                                "Peter": Peter,
                                "Ryan": Ryan,
                                "Go back": None
                            },
                            pygame.image.load(
                                "Game_Pics/5e81d58221c02.jpg"),
                            (0, 0),
                            ["An article about Matthew Killian's efforts to close an enormous business deal in Wales."
                             "It notes that Killian is well known for replacing workers with machinery."
                             "There is a likeness of Killian in the paper which matches the victim.",
                             "Down with the Industrialists! Down with the Monarchy! Revolution is the only way!",
                             None, None,
                             "Sleeping pills – A small box of sleeping pills. It is half-empty.                      "
                             "                  I believe I should reinterrogate a suspect", None])

Peter.next_scene_map["Go back"] = restaurant_carriage
Ryan.next_scene_map["Go back"] = restaurant_carriage


def handle_Peter_Ryan_selection(option):
    if option == 2:
        if "Enquire about Peter" not in Ryan.options:
            Ryan.options.insert(-1, "Enquire about Peter")
            Ryan.next_scene_variables.insert(-1, 99)
            Ryan.dialogue.insert(-1,
                                 "Peter? Nice bloke. Came here after being sacked from a foundry a few months ago. I'll"
                                 " tell you, he looked white as a ghost after he served the businessmen.")


def handle_pills_Ryan_selection(option):
    if option == 4:
        if "Ask about the pills" not in Ryan.options:
            Ryan.options.insert(-1, "Ask about the pills")
            Ryan.next_scene_variables.insert(-1, 99)
            Ryan.dialogue.insert(-1,
                                 "Oh, er - well, it's a noisy train. Plenty of passengers have trouble getting to "
                                 "sleep, So i keep a sedative here behind the bar .yeah?")


def handle_Vivian_Peter_selection(option):
    if option == 2:
        if "Who is Vivian?" not in Peter.options:
            Peter.options.insert(-1, "Who is Vivian?")
            Peter.next_scene_variables.insert(-1, 99)
            Peter.dialogue.insert(-1,
                                  "She rides the train often. She's very friendly with the other passengers.")


def handle_Vivian_Ryan_selection(option):
    if option == 0:
        if "Ask about Vivian" not in Ryan.options:
            Ryan.options.insert(-1, "Ask about Vivian")
            Ryan.next_scene_variables.insert(-1, 99)
            Ryan.dialogue.insert(-1,
                                 "She's a frequent passenger, that one. Hangs about with the wealthier sort. Likes "
                                 "to 'entertain' 'em, if you take my meanin'.")


def handle_Scheme_Ryan_selection(option):
    if option == 1:
        if "Ask about Scheme" not in Ryan.options:
            Ryan.options.insert(-1, "Ask about Scheme")
            Ryan.next_scene_variables.insert(-1, 99)
            Ryan.dialogue.insert(-1,
                                 "Yeah, I help Vivian fleece the dupes. I slipped a pill in the wine for the table. "
                                 "Both gents got sleepy, but Vivian picked the richest one.")


mid_train = Scene("You come back to the mid part of the train looking for more clues",
                  ["Go to Restaurant carriage", "Passenger carriage", "Sleeper 1", "Sleeper 2", "Accuse"],
                  ["Restaurant", "Passenger", "Sleeper_1", "Sleeper_2", "Accuse"],
                  {
                      "Restaurant": restaurant_carriage,
                      "Passenger": passenger_carriage,
                      "Sleeper_1": sleeper_1,
                      "Sleeper_2": sleeper_2,
                      "Accuse": scene_accuse
                  },
                  pygame.image.load(
                      "Game_Pics/train_scene.jpg"),
                  (0, 0),
                  [None, None, None, None])

scene_accuse.next_scene_map["Go back"] = mid_train
restaurant_carriage.next_scene_map["Go back"] = mid_train
passenger_carriage.next_scene_map["Go back"] = mid_train
sleeper_1.next_scene_map["Go back"] = mid_train
sleeper_2.next_scene_map["Go back"] = mid_train

train_scene = Scene("As you board the waiting train, a gust of warm air welcomed him, carrying with it a mingling "
                    "scent of polished wood, leather, and coal smoke. The interior exuded an air of faded grandeur, "
                    "a reflection of Victorian opulence on wheels. Mahogany panels adorned the walls, intricately "
                    "carved with delicate patterns. The windows, adorned with velvet curtains, allowed slivers of "
                    "pale daylight to filter into the carriage, casting a soft glow on the plush, deep-red velvet "
                    "seats.",
                    ["Go to Restaurant carriage", "Passenger carriage", "Sleeper 1", "Sleeper 2"],
                    ["Restaurant", "Passenger", "Sleeper_1", "Sleeper_2"],
                    {
                        "Restaurant": restaurant_carriage,
                        "Passenger": passenger_carriage,
                        "Sleeper_1": sleeper_1,
                        "Sleeper_2": sleeper_2,
                    },
                    pygame.image.load(
                        "Game_Pics/train_scene.jpg"),
                    (0, 0),
                    [None, None, None, None])

train_stop = Scene("You immediately pull the emergency lever and stop the train and hurriedly rush back to the station",
                   ["Board Train 549", 'Ask the train master', 'Board Train 616'],
                   ["wrong_scene1", 99, "next_scene"],
                   {
                       "wrong_scene1": None,
                       "next_scene": train_scene
                   },
                   pygame.image.load(r"Game_Pics/Train_station.png"),
                   (0, 30),
                   [None,
                    "Trainmaster: The midnight train, It's Train 616. You better hurry. It's leaving right now",
                    None])

end_game1 = GameEnd("After a few hours of travel, the train eventually arrived at the next station. Feeling a mixture "
                    "of relief and anticipation, you prepare to disembark. As the train slowed to a halt, "
                    "you step onto the platform, greeted by the bustling atmosphere of the station. Unfortunately for "
                    "you, the train you were supposed to get on departed long ago. You wait for it the next day, "
                    "but the train was cleaned and all the clues had been erased. In this city shrouded in crime, "
                    "yet another mystery remains unsolved. ",
                    ["Restart", "  Quit  "],
                    pygame.image.load(
                        "Game_Pics/1237768.jpg"),
                    (0, 0),
                    [None, None],
                    pygame.mixer.Sound("music/Mission Failed Sound Effect (mp3cut.net).mp3")
                    )

wrong_scene1 = Scene("You enter the train. But wait, the train's powerful locomotives pulled a long line of wagons, "
                     "loaded with towering mounds of coal. The air was thick with the earthy scent of coal and the "
                     "sound of clattering wheels echoed through the surroundings. It was a scene that embodied the "
                     "relentless energy and progress of the industrial era.",
                     ["Investigate the train", "Go the driver", "Get out of the train"],
                     [99, 99, "end_game1"],
                     {
                         "end_game1": end_game1
                     },
                     pygame.image.load(r"Game_Pics/bruno-morin-blacktrain.jpg"),
                     (0, 0),
                     ["Amidst the coal train, alongside the towering mounds of coal, the wagons bore witness to a "
                      "myriad of other products and materials. Maybe this is a cargo and good train.",
                      "You make your way towards the engine block. As you approach, you could see the driver's "
                      "weathered face, etched with lines that spoke of years of experience on the rails. He informs "
                      "you that this is train 549 You"
                      "understand this is not the train you were supposed to get on.",
                      None])
train_stop.next_scene_map["wrong_scene1"] = wrong_scene1

wrong_scene2 = Scene("Stepping onto the passenger train, you find yourself engulfed in a sea of "
                     "bustling humanity. The carriage was abuzz with a vibrant energy, a symphony of voices and "
                     "laughter intermingling with the rhythmic sound of the train's movement. Every seat was "
                     "occupied, and people stood shoulder to shoulder."
                     "coal train 613.",
                     ["Enquire the Train inspector", "Wait for the next station", "Stop the Train"],
                     [99, "next station", "Stop train"],
                     {
                         "next station": end_game1,
                         "Stop train": train_stop
                     },
                     pygame.image.load(r"Game_Pics/bruno-morin-blacktrain.jpg"),
                     (0, 0),
                     ["The train inspector informs you that this is train 616 and nothing such as murders happen on "
                      "this train. Since it is a passenger train, it is always crowded with people.", None, None])

# scene where dectective reaches the train station
initial_scene3 = Scene("With the pocket watch securely in his possession, You knew that he held a vital clue - a key "
                       "to unraveling the enigma that had brought darkness to the bridge that night."
                       "Determined to uncover the truth, he stepped into the murky underbelly of Victorian London - a "
                       "world teeming with corruption, deceit, and the desperation of those driven to the edge."
                       'You quickly compose yourself and take a horse cart and make your way towards the victoria '
                       'station to investigate about the '
                       "train. With a determined stride, you enter the bustling station, filled with the sounds of "
                       "whistles, steam, and the excited chatter of passengers.",
                       ['Board Train 549', 'Board Train 613', 'Ask the train master', 'Board Train 616'],
                       ["wrong_scene1", "wrong_scene2", 99, "next_scene"],
                       {
                           "wrong_scene1": wrong_scene1,
                           "wrong_scene2": wrong_scene2,
                           "next_scene": train_scene
                       },
                       pygame.image.load(r"Game_Pics/Train_station.png"),
                       (0, 0),
                       [None, None,
                        "Trainmaster: The midnight train, It's Train 616. You better hurry. It's leaving right now",
                        None])

initial_scene = Scene("At the scene, you find a man standing at a tree nearby the riverbank, maybe he was the tramp who"
                      " found the body. The gas lamps cast long shadows as you venture forth, your footsteps "
                      "echoing through the labyrinthine streets. You would navigate the treacherous web of suspects, "
                      "witnesses, and hidden motives, seeking justice in a city where the line between law and chaos "
                      "blurred. Where do ya want to go?",
                      ["Examine the body", "Look under the rail bridge", "Walk near the Riverbank",
                       "Investigate above the bridge", "Interrogate the man nearby"],
                      [99, 99, 99, 99, "next_scene"],
                      {
                          "next_scene": None,
                      },
                      pygame.image.load(
                          r"Game_Pics/murder.jpg"),
                      (-430, 0),
                      ["A lifeless Male body dressed in the attire of a "
                       "wealthy businessman, lay motionless. He is wearing only one shoe. The man has sustained "
                       "multiple fractures indicating a fall from a great height which suggests a sudden and violent "
                       "event. There are no identifying documents.",
                       "You find a Coat. Carefully handling the coat, you observe the fine fabric, noting the "
                       "attention to detail and the undeniable mark of wealth. Matthew Killian - a name that now held a"
                       " weighty significance. A rich man's coat with a name sewed in the lining: Matthew Killian.",
                       "As you walk along the riverbanks for further examination, your eyes shifted to the damp mud "
                       "revealing drag marks etched upon its surface. Your instincts sharpened. The struggle or "
                       "hurried movement indicated that something significant had transpired in this very spot.",
                       "You find a Pocket watch - A broken, silver watch. The hands have stopped just after midnight. "
                       "You wonder if someone could tell you more about this.",
                       None]
                      )  # for the last option it has take to next scene

initial_scene2 = Scene("You approached the tramp cautiously, your instinct guiding you.      "
                       '"Excuse me, sir,"' "You begin, your voice firm yet respectful."
                       "Did you stumble upon this unfortunate sight?"
                       "The tramp shifted his gaze, meeting the detective's eyes. His voice carried a tremor of "
                       "unease as he responded, Aye, stumbled across it, I did. Was just minding my own business",
                       ["Ask about the body", "Interrogate his shelter",
                        "Go back"],
                       [99, 99, "Go back"],
                       {
                           "Go back": initial_scene
                       },
                       pygame.image.load(
                           r"Game_Pics/assassins_creed_syndicate_london_art-2.png"),
                       (0, 0),
                       ["Vagrant: I heard a splash an' right quick pulled this bloke out a' the shallows. Dead as a "
                        "mackerel.",
                        "Vagrant: I live there, now. If you can call it livin'. I lost my job, didn't I? No need for "
                        'the likes of me when the machine can do the work.                      "Looks like we need '
                        'to look for more clues" ',
                        None]
                       )

initial_scene.next_scene_map["next_scene"] = initial_scene2


def handle_Coat_Tramp_selection(option):
    if option == 0:
        if "Talk about the coat" not in initial_scene2.options:
            initial_scene2.options.insert(-1, "Talk about the coat")
            initial_scene2.next_scene_variables.insert(-1, 99)
            initial_scene2.dialogue.insert(-1,
                                           "Vagrant: A nice, warm coat like that on a dead man, what do you expect? I "
                                           "snatched it before somebody else come along to nick it.")


def handle_Watch_Tramp_selection(option):
    if option == 3:
        if "What about Midnight train" not in initial_scene2.options:
            initial_scene2.options.insert(-1, "What about Midnight train")
            initial_scene2.next_scene_variables.insert(-1, 89)
            initial_scene2.dialogue.insert(-1,
                                           "Vagrant: The midnight train? That must be the 616. Stops in the station "
                                           "down the road. If you hurry, it might still be there.")


def handle_Station_selection(option):
    if option == 89:
        if "Go to the train station" not in initial_scene2.options:
            initial_scene2.options.insert(-1, "Go to the train station")
            initial_scene2.next_scene_variables.insert(-1, "next_scene")
            initial_scene2.next_scene_map["next_scene"] = initial_scene3
            initial_scene2.dialogue.insert(-1,
                                           None)
