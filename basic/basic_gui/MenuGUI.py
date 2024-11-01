import pygame
import pygame_gui

from basic.basic_gui.FullScreenMessanger import FullScreenMessanger
from basic.general_settings import IMAGE_PATHS, DEFAULT_WINDOW_SIZE
from basic.tools.get_surface_size_by_screen_proportions import get_surface_size_by_screen_proportions
from basic.tools.loading.loading_files import load_image
from basic.tools.screen_placement.get_drawing_center_coordinates import get_drawing_center_coordinates


class MenuGUI:
    def __init__(self):
        self.manager = pygame_gui.UIManager(DEFAULT_WINDOW_SIZE)
        self.buttons = {
            "start": pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((0, 0), (0, 0)),
                text='ИГРАТЬ',
                manager=self.manager
            ),
            "rules": pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((0, 0), (0, 0)),
                text='ПРАВИЛА',
                manager=self.manager
            ),
            "quit": pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((0, 0), (0, 0)),
                text='ВЫХОД',
                manager=self.manager
            )
        }

        # Buttons list game_process_visualization parameters
        self.width_button_percent, self.height_button_percent = 25, 15
        self.space_between_percent = 5
        self.left_padding_percent, self.upper_padding_percent = 8, 23

        self.menu_background = load_image(IMAGE_PATHS["menu_background"])

        self.main_menu_messanger = FullScreenMessanger()
        self.main_menu_messanger.background_screen_color = pygame.Color(20, 20, 20)
        self.main_menu_messanger.default_visible = 255

    def show_rules(self, screen, rules, rules_text_font_size_coefficient=None):
        if rules_text_font_size_coefficient is not None:
            self.main_menu_messanger.main_text_font_size_coefficient = rules_text_font_size_coefficient
        self.main_menu_messanger.show_message(screen, rules)

    def recalculate_buttons(self, background_draw_coordinates, background_draw_size):
        background_x, background_y = background_draw_coordinates
        background_width, background_height = background_draw_size

        one_percent_width, one_percent_height = background_width / 100, background_height / 100
        left_padding = self.left_padding_percent * one_percent_width
        upper_padding = self.upper_padding_percent * one_percent_height
        space_size = self.space_between_percent * one_percent_height
        button_width = self.width_button_percent * one_percent_width
        button_height = self.height_button_percent * one_percent_height

        button_index = 0
        for button_key in self.buttons.keys():
            new_button_x = background_x + left_padding
            new_button_y = background_y + upper_padding + button_index * (space_size + button_height)
            self.buttons[button_key].set_position((new_button_x, new_button_y))
            self.buttons[button_key].set_dimensions((button_width, button_height))
            button_index += 1

    def update(self, fps: int):
        self.manager.update(fps)

    def draw_ui(self, screen):
        screen.fill("blue")
        resized_menu_background = pygame.transform.scale(
            self.menu_background,
            get_surface_size_by_screen_proportions(self.menu_background.get_size(), screen.get_size())
        )
        draw_coordinates = get_drawing_center_coordinates(screen, resized_menu_background)
        screen.blit(resized_menu_background, draw_coordinates)

        self.recalculate_buttons(draw_coordinates, resized_menu_background.get_size())

        self.manager.set_window_resolution(screen.get_size())
        self.manager.draw_ui(screen)
