import pygame

from basic.general_game_logic.collision_system.lines_collision.CollisionLines import CollisionLines
from basic.general_game_logic.scene_folder.SceneDebug import SceneDebug
from basic.tools.loading.load_borders import load_line_border, point_on_screen_to_px
from scenes.scene2.game_objects.Player import Player
from scenes.scene2.general.scene_settings import OBJECTS_VISUALISATION, MAP_SIZE_IN_PX
from scenes.scene2.map.Map import Map


class Scene2draw(SceneDebug):
    def __init__(self, screen, audio_manager):
        super().__init__(screen, audio_manager)
        self.game_visualizer.load_base_scaling_images(OBJECTS_VISUALISATION)
        self.scaling_step = 20
        self.switch_show_debug_info()

        self.map = Map()

        self.player = Player((self.map.width // 4, self.map.height // 2),
                             OBJECTS_VISUALISATION["player"]["size"], self)
        # self.player.add_hard_objects(self.map.walls)
        self.player.set_moving_borders(self.map.border)

        self.camera = self.game_visualizer.camera
        self.camera.fix_camera_on_object(self.player)

        self.input_points = []

    def process_event(self, event: pygame.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x_px, y_px = point_on_screen_to_px(pos, self.game_visualizer, self.map.size, MAP_SIZE_IN_PX)
            self.input_points.append(f"{x_px},{y_px};")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if len(self.input_points):
                    self.input_points.pop(-1)
            elif event.key == pygame.K_x:
                print("".join(self.input_points))

        if len(self.input_points) > 1:
            self.map.border = CollisionLines(load_line_border(
                "".join(self.input_points), self.map.size, MAP_SIZE_IN_PX))
            self.player.set_moving_borders(self.map.border)
        else:
            self.map.border = CollisionLines([])
            self.player.set_moving_borders(self.map.border)

        self.process_debug_event(event)

    def update(self):
        self.player.update()
        if not self.get_game_visualizer().camera.is_free:
            self.player.process_controller()
        self.game_visualizer.update()
        self.scene_gui_manager.update()

    def draw(self):
        self.game_visualizer.refresh_screen()

        self.map.draw(self.game_visualizer)
        self.player.draw(self.game_visualizer)

        if self.show_debug_info:
            self.draw_debug_info()
        if self.show_grid:
            self.draw_grid()

        self.scene_gui_manager.draw()

    def draw_debug_info(self):
        self.map.draw_collisions(self.game_visualizer)
        self.player.draw_collision(self.game_visualizer)
