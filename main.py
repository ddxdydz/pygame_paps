import sys
import pygame
import pygame_gui
from pygame import RESIZABLE

from basic.general_settings import DEFAULT_WINDOW_SIZE, FPS
from basic.general_settings import IMAGE_PATHS, AUDIO_PATHS
from basic.tools.loading_files import load_image
from basic.general_visualization.general_gui.MenuGUI import MenuGUI
from basic.general_game_logic.scene_folder.SceneLoader import SceneLoader
from basic.audio.AudioManager import AudioManager
from scenes.scene1.Scene1 import Scene1


def main():
    menu_gui = MenuGUI()
    audio_manager = AudioManager()
    audio_manager.load_audio_data(AUDIO_PATHS)
    audio_manager.load_music("menu")

    scene_loader = SceneLoader(audio_manager)
    scene = Scene1

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get().copy():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == menu_gui.buttons["start"]:
                    audio_manager.load_music("game")
                    scene_loader.load(scene(screen, audio_manager))
                    audio_manager.load_music("menu")
                elif event.ui_element == menu_gui.buttons["rules"]:
                    menu_gui.show_rules(screen, scene.rules)
                elif event.ui_element == menu_gui.buttons["quit"]:
                    running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 13:  # Enter
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_ALT:
                        pygame.display.toggle_fullscreen()
                        pygame.display.set_icon(load_image(IMAGE_PATHS["icon"]))

            audio_manager.process_event(event)
            menu_gui.manager.process_events(event)

        menu_gui.update(FPS)
        menu_gui.draw_ui(screen)

        audio_manager.update(FPS)
        audio_manager.draw_ui(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("TestGame")
    pygame.display.set_icon(load_image(IMAGE_PATHS["icon"]))
    screen = pygame.display.set_mode(DEFAULT_WINDOW_SIZE, RESIZABLE)
    main()
