import pygame
import pygame_gui

from basic.general_settings import IMAGE_PATHS
from basic.general_settings import WINDOW_SIZE
from basic.general_visualization.general_gui.Messanger import Messanger
from basic.tools.get_center_drawing_coordinates import get_center_drawing_coordinates
from basic.tools.loading_files import load_image


class MenuGUI:
    def __init__(self):
        self.manager = pygame_gui.UIManager(WINDOW_SIZE)
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 200), (300, 100)),
            text='ИГРАТЬ',
            manager=self.manager
        )
        self.rules_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 350), (300, 100)),
            text='ПРАВИЛА',
            manager=self.manager
        )
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 500), (300, 100)),
            text='ВЫХОД',
            manager=self.manager
        )

        self.menu_background = load_image(IMAGE_PATHS["menu_background"])

        self.main_menu_messanger = Messanger()
        self.main_menu_messanger.background_screen_color = pygame.Color(20, 20, 20, 255)

    def show_rules(self, screen, rules):
        self.main_menu_messanger.show_message(screen, rules)

    def update(self, fps: int):
        self.manager.update(fps)

    def draw_ui(self, screen):
        screen.fill("blue")
        screen_width, screen_height = screen.get_size()

        background_width, background_height = self.menu_background.get_size()
        if screen_width < screen_height:
            background_width = int(background_width * background_height / screen_height)
            background_height = screen_height
        else:
            background_width = screen_width
            background_height = int(background_height * background_width / screen_width)

        resized_menu_background = pygame.transform.scale(self.menu_background, (background_width, background_height))
        screen.blit(resized_menu_background, get_center_drawing_coordinates(screen, resized_menu_background))
        self.manager.draw_ui(screen)
