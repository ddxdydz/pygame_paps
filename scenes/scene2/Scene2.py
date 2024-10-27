import pygame

from basic.general_game_logic.scene_folder.Scene import Scene
from scenes.scene2.general.rules import RULES
from scenes.scene2.game_objects.Player import Player
from scenes.scene2.general.scene_settings import OBJECTS_VISUALISATION
from scenes.scene2.map.Map import Map


class Scene2(Scene):
    def __init__(self, screen, audio_manager):
        super().__init__(screen, audio_manager)
        self.display_manager.load_images(OBJECTS_VISUALISATION)
        self.show_collisions = False

        self.map = Map()

        self.player = Player((6, 10), OBJECTS_VISUALISATION["player"]["size"])
        self.player.add_hard_objects(self.map.walls)

        self.camera.fix_camera_on_object(self.player)

    def get_rules(self):
        return RULES

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                if self.camera.is_free:
                    self.camera.fix_camera_on_object(self.player)
                    self.player.enable_updating = True
                else:
                    self.camera.enable_free_observing_mod()
                    self.player.enable_updating = False
            elif event.key == pygame.K_p:
                self.show_collisions = not self.show_collisions
            elif event.key == pygame.K_i:
                self.player.set_collision_mode(not self.player.is_no_collision_mode())
            elif event.key == pygame.K_t:
                self.gaming_gui_manager.switch_timer()
            elif event.key == pygame.K_y:
                self.player.infinity_stamina = not self.player.infinity_stamina
            elif event.key == pygame.K_u:
                self.player.infinity_health = not self.player.infinity_health
            elif event.key == pygame.K_j:
                self.player.current_health = -1
            elif event.key == pygame.K_m:
                self.gaming_gui_manager.show_message("Test MESSAGE")

    def draw(self, screen):
        self.get_screen().fill((60, 94, 106))
        self.display_manager.update_screen(screen)
        self.camera.update()

        self.player.update()

        self.map.draw(self.display_manager)
        if self.show_collisions:
            self.player.draw_collision(self.display_manager)
            self.map.draw_collisions(self.display_manager)

        self.player.draw(self.display_manager)
