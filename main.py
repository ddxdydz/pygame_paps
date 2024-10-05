import sys
import pygame
import pygame_gui

from basic.local_constants import WINDOW_SIZE, FPS
from basic.local_constants import IMAGE_PATHS
from basic.loading_files import load_image
from basic.MenuGUI import MenuGUI
from scenes.SceneLoader import SceneLoader
from basic.AudioManager import AudioManager


def main():
    menu_gui = MenuGUI()
    audio_manager = AudioManager()
    audio_manager.load_menu_music()
    scene_loader = SceneLoader(audio_manager)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get().copy():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == menu_gui.start_button:
                    audio_manager.load_game_music()
                    scene_loader.load(screen)
                    audio_manager.load_menu_music()
                elif event.ui_element == menu_gui.rules_button:
                    menu_gui.show_rules(screen)
                elif event.ui_element == menu_gui.quit_button:
                    running = False
            audio_manager.process_event(event)
            menu_gui.manager.process_events(event)

        menu_gui.manager.update(FPS)
        screen.blit(menu_gui.menu_background, (0, 0))
        menu_gui.manager.draw_ui(screen)

        audio_manager.update(FPS)
        audio_manager.draw_ui(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("TestGame")
    pygame.display.set_icon(load_image(IMAGE_PATHS["icon"]))
    screen = pygame.display.set_mode(WINDOW_SIZE)
    main()
