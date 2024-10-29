from basic.basic_gui.gui_elements.DisappearingMessage import DisappearingMessage
from basic.basic_gui.gui_elements.TimerBar import TimerBar
from basic.general_game_logic.scene_folder.GuiManagerScene import GuiManagerScene
from scenes.scene1.general.scene_settings import GAME_GUI_IMAGES, OBJECTS_VISUALISATION
from scenes.scene1.scene_gui.gui_elements.HealthBar import HealthBar
from scenes.scene1.scene_gui.gui_elements.ItemsPanel import ItemsPanel
from scenes.scene1.scene_gui.gui_elements.StaminaBar import StaminaBar


class GuiManagerScene1(GuiManagerScene):
    def __init__(self, screen, show_gui=True):
        super().__init__(screen, show_gui)
        self.messanger = DisappearingMessage()
        self.timer = TimerBar()
        self.health_bar = HealthBar(GAME_GUI_IMAGES["health_bar"]["paths"]["base"])
        self.stamina_bar = StaminaBar(GAME_GUI_IMAGES["stamina_bar"]["paths"]["base"])
        self.items_panel = ItemsPanel()
        self.items_panel.load_items_icons(OBJECTS_VISUALISATION)

    def show_message(self, message: str):
        self.messanger.show_message(message)

    def set_scale_coefficient(self, scale_coefficient):
        pass

    def update(self):
        self.timer.update()
        self.messanger.update()

    def draw(self):
        if self.show_gui:
            self.health_bar.draw_health_bar(self.get_screen())
            self.stamina_bar.draw_stamina_bar(self.get_screen())
            self.items_panel.draw_items_list_panel(self.get_screen())
            self.messanger.draw(self.get_screen(), 20, 30)
