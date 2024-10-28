import pygame

from basic.general_settings import FPS
from basic.general_settings import ONE_GGUI_TICK_TO_PX
from basic.general_game_logic.game_visualization.game_process_visualization.support.ImageLoader import ImageLoader


class GameGuiManager(ImageLoader):
    def __init__(self):
        super().__init__()

        self.show_timer = False
        self.show_gui = True

        self.list_of_items = dict()  # {obj_code: {"count": count}, ...}
        self.health_bar_fill_level = 0.5
        self.stamina_bar_fill_level = 0.5
        self.current_timer_value = 0

        self.time_message_showing = 3  # sec
        self.decrease_alpha_time = 2
        self.current_time_message_showing = 0
        self.message = ''

    def show_message(self, message):
        self.current_time_message_showing = self.time_message_showing
        self.message = message

    def add_item(self, obj_code):
        if obj_code in self.list_of_items.keys():
            self.list_of_items[obj_code]["count"] += 1
        else:
            self.list_of_items[obj_code] = dict()
            self.list_of_items[obj_code]["count"] = 1

    def delete_item(self, obj_code):
        if obj_code in self.list_of_items.keys():
            if self.list_of_items[obj_code]["count"] > 0:
                self.list_of_items[obj_code]["count"] -= 1
                if self.list_of_items[obj_code]["count"] == 0:
                    self.list_of_items.pop(obj_code)

    def update_health_bar(self, current_value, max_value):
        self.health_bar_fill_level = current_value / max_value

    def update_stamina_bar(self, current_value, max_value):
        self.stamina_bar_fill_level = current_value / max_value

    def update_timer(self):
        self.current_timer_value += 1 / FPS

    def switch_timer(self):
        self.show_timer = not self.show_timer

    def get_timer_value(self):
        return round(self.current_timer_value, 1)

    def update(self):
        self.current_time_message_showing -= 1 / FPS
        if self.current_time_message_showing < 0:
            self.current_time_message_showing = 0
        self.update_timer()

    def switch_show_gui(self):
        self.show_gui = not self.show_gui

    def get_item_surface(self, obj_code):
        size = width, height = 1 * ONE_GGUI_TICK_TO_PX, 1 * ONE_GGUI_TICK_TO_PX  # px
        item_surface = pygame.Surface(size).convert_alpha()
        item_surface.fill("purple")
        item_surface.set_colorkey("purple")

        pygame.draw.rect(
            item_surface, pygame.Color(35, 7, 52), ((0, 0), size),
            border_radius=int(0.25 * ONE_GGUI_TICK_TO_PX) + 1
        )

        pygame.draw.rect(
            item_surface, "black", ((0, 0), size),
            border_radius=int(0.25 * ONE_GGUI_TICK_TO_PX) + 1, width=int(0.03 * ONE_GGUI_TICK_TO_PX) + 1
        )

        item_image = self.get_image(obj_code, "base")
        item_surface.blit(item_image, ((width - item_image.get_width()) // 2, (height - item_image.get_height()) // 2))

        text_font = pygame.font.Font(None, int(0.2 * ONE_GGUI_TICK_TO_PX))
        text = text_font.render(str(self.list_of_items[obj_code]["count"]), True, "white")
        text_down_padding = 0.08 * ONE_GGUI_TICK_TO_PX
        text_width, text_height = text.get_size()
        item_surface.blit(text, ((width - text_width) / 2, height - text_down_padding - text_height))

        return item_surface

    def draw_items_list_panel(self, screen):
        if not self.list_of_items.keys():  # need more than 0
            return

        down_padding = 0.2 * ONE_GGUI_TICK_TO_PX
        margin_between = 0.2 * ONE_GGUI_TICK_TO_PX

        item_surfaces = []
        for obj_code, info in self.list_of_items.items():
            item_surfaces.append(self.get_item_surface(obj_code))

        items_count = len(item_surfaces)
        total_width = items_count * (item_surfaces[0].get_width()) + (items_count - 1) * margin_between

        current_x = (screen.get_width() - total_width) / 2
        for item_surface in item_surfaces:
            screen.blit(item_surface, (current_x, screen.get_height() - down_padding - item_surface.get_height()))
            current_x += item_surfaces[0].get_width() + margin_between

    def draw_timer_panel(self, screen):
        left_padding = 0.2 * ONE_GGUI_TICK_TO_PX
        upper_padding = 0.2 * ONE_GGUI_TICK_TO_PX
        text_font = pygame.font.Font(None, int(0.5 * ONE_GGUI_TICK_TO_PX))
        text = text_font.render(f"{self.get_timer_value()} sec", True, "white")
        text.set_alpha(200)
        screen.blit(text, (left_padding, upper_padding))

    def draw_health_bar(self, screen):
        right_padding = 0.3 * ONE_GGUI_TICK_TO_PX
        upper_padding = 0.3 * ONE_GGUI_TICK_TO_PX
        left_filling_padding = 0.2 * ONE_GGUI_TICK_TO_PX
        upper_filling_padding = 0.17 * ONE_GGUI_TICK_TO_PX
        filling_height = 0.2 * ONE_GGUI_TICK_TO_PX
        max_filling_weight = 2 * ONE_GGUI_TICK_TO_PX
        img = self.get_image("health_bar", "base")

        bar_panel = pygame.Surface(img.get_size())
        bar_panel.fill("pink")
        colorkey = bar_panel.get_at((0, 0))
        bar_panel.set_colorkey(colorkey)
        pygame.draw.rect(
            bar_panel, "red",
            ((left_filling_padding, upper_filling_padding),
             (max_filling_weight * self.health_bar_fill_level, filling_height))
        )
        bar_panel.blit(img)
        screen.blit(bar_panel, (screen.get_width() - bar_panel.get_width() - right_padding, upper_padding))

    def draw_stamina_bar(self, screen):
        right_padding = 0.3 * ONE_GGUI_TICK_TO_PX
        upper_padding = 1 * ONE_GGUI_TICK_TO_PX
        left_filling_padding = 0.2 * ONE_GGUI_TICK_TO_PX
        upper_filling_padding = 0.14 * ONE_GGUI_TICK_TO_PX
        filling_height = 0.2 * ONE_GGUI_TICK_TO_PX
        max_filling_weight = 2.2 * ONE_GGUI_TICK_TO_PX
        img = self.get_image("stamina_bar", "base")

        bar_panel = pygame.Surface(img.get_size())
        bar_panel.fill("pink")
        colorkey = bar_panel.get_at((0, 0))
        bar_panel.set_colorkey(colorkey)
        pygame.draw.rect(
            bar_panel, (255, 170, 11),
            ((left_filling_padding, upper_filling_padding),
             (max_filling_weight * self.stamina_bar_fill_level, filling_height))
        )
        bar_panel.blit(img)
        screen.blit(bar_panel, (screen.get_width() - bar_panel.get_width() - right_padding, upper_padding))

    def draw_message(self, screen):
        if self.current_time_message_showing == 0:
            return
        left_padding = 0.2 * ONE_GGUI_TICK_TO_PX
        upper_padding = 0.6 * ONE_GGUI_TICK_TO_PX
        text_font = pygame.font.Font(None, int(0.3 * ONE_GGUI_TICK_TO_PX))
        text = text_font.render(f"{self.message}", True, "white")
        if self.current_time_message_showing - self.decrease_alpha_time < 0:
            delta = self.time_message_showing - self.decrease_alpha_time
            text.set_alpha(int(255 * (self.current_time_message_showing / delta)))
        screen.blit(text, (left_padding, upper_padding))

    def draw(self, screen):
        if self.show_gui:
            if self.show_timer:
                self.draw_timer_panel(screen)
            self.draw_items_list_panel(screen)
            self.draw_health_bar(screen)
            self.draw_stamina_bar(screen)
            self.draw_message(screen)
