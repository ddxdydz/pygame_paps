import pygame

from basic.tools.create_error_surface import create_error_surface
from basic.tools.loading.loading_files import load_image
from basic.tools.screen_placement.ExternalMargins import ExternalMargins
from basic.tools.screen_placement.get_drawing_center_coordinates import get_drawing_center_coordinates


class ItemsPanel:
    def __init__(self):
        self.items_dict = dict()  # {obj_code: {"count": count}, ...}
        self.loaded_items_icons = dict()  # {obj_code: {"image": image}, ...}

        self.item_cell_size = 100, 100
        self.space, self.down_padding = 10, 10
        self.item_icons_size_coefficient = 0.6

        self.text_item_placement = ExternalMargins(0, -0.03)
        self.text_size = int(0.2 * self.item_cell_size[0])

        self.error_surface = create_error_surface(*self.get_icon_size(), color="green")

    def get_icon_size(self):
        cell_width, cell_height = self.item_cell_size
        return (cell_width * self.item_icons_size_coefficient,
                cell_height * self.item_icons_size_coefficient)

    def load_items_icons(self, images_library, img_type="base"):
        self.loaded_items_icons.clear()
        for code in images_library.keys():
            if img_type in images_library[code]["paths"].keys():
                path = images_library[code]["paths"][img_type]
                self.loaded_items_icons[code] = dict()
                self.loaded_items_icons[code]["image"] = load_image(path, self.get_icon_size(), True)

    def get_item_icon(self, code):
        if code in self.loaded_items_icons.keys():
            return self.loaded_items_icons[code]["image"]
        print(f"ItemPanel Warning: Image code is not founded. Code: '{code}'")
        return self.error_surface

    def add_item(self, obj_code):
        if obj_code in self.items_dict.keys():
            self.items_dict[obj_code]["count"] += 1
        else:
            self.items_dict[obj_code] = dict()
            self.items_dict[obj_code]["count"] = 1

    def delete_item(self, obj_code):
        if obj_code in self.items_dict.keys():
            if self.items_dict[obj_code]["count"] > 0:
                self.items_dict[obj_code]["count"] -= 1
                if self.items_dict[obj_code]["count"] == 0:
                    self.items_dict.pop(obj_code)

    def get_item_surface(self, code):
        item_surface = pygame.Surface(self.item_cell_size).convert_alpha()
        item_surface.fill("purple")
        item_surface.set_colorkey("purple")

        pygame.draw.rect(
            item_surface, pygame.Color(35, 7, 52), ((0, 0), self.item_cell_size),
            border_radius=int(self.item_cell_size[0] * 0.3) + 1
        )

        pygame.draw.rect(
            item_surface, "black", ((0, 0), self.item_cell_size),
            border_radius=int(self.item_cell_size[0] * 0.3) + 1,
            width=int(self.item_cell_size[0] * 0.025) + 1
        )

        item_icon = self.get_item_icon(code)
        item_surface.blit(item_icon, get_drawing_center_coordinates(item_surface, item_icon))

        text_font = pygame.font.Font(None, self.text_size)
        text = text_font.render(str(self.items_dict[code]["count"]), True, "white")
        item_surface.blit(text, self.text_item_placement.get_drawing_coordinates(item_surface, text))

        return item_surface

    def draw_items_list_panel(self, screen):
        if not self.items_dict.keys():  # need more than 0
            return

        item_surfaces = [self.get_item_surface(code) for code in self.items_dict.keys()]
        items_count = len(item_surfaces)
        total_width = items_count * (item_surfaces[0].get_width()) + (items_count - 1) * self.space

        current_x = (screen.get_width() - total_width) / 2
        for item_surface in item_surfaces:
            screen.blit(item_surface, (current_x, screen.get_height() - self.down_padding - item_surface.get_height()))
            current_x += item_surfaces[0].get_width() + self.space
