from basic.general_settings import FPS


class Stamina:
    def __init__(self):
        self.max_stamina = 100
        self.current_stamina = 100
        self.decrease_speed = 20  # per second
        self.increase_speed = 10  # per second
        self.zero_increase_delay = 2  # sec
        self.current_increase_delay = 0
        self.decrease_prohibition = False

    def set_parameters(
            self, stamina: float, max_stamina: float,
            decrease_speed: float = 20, increase_speed: float = 10, zero_increase_delay: float = 2):
        if stamina < 0:
            raise Exception("GameDynamicObject Error: set stamina < 0")
        if max_stamina < 0:
            raise Exception("GameDynamicObject Error: set max_stamina < 0")
        if decrease_speed < 0:
            raise Exception("GameDynamicObject Error: set decrease_speed < 0")
        if increase_speed < 0:
            raise Exception("GameDynamicObject Error: set increase_speed < 0")
        if zero_increase_delay < 0:
            raise Exception("GameDynamicObject Error: set zero_increase_delay < 0")
        self.current_stamina = stamina
        self.max_stamina = max_stamina
        self.decrease_speed = decrease_speed
        self.increase_speed = increase_speed
        self.zero_increase_delay = zero_increase_delay

    def switch_decrease_prohibition(self):
        self.decrease_prohibition = not self.decrease_prohibition

    def decrease(self):
        if self.decrease_prohibition:
            return
        self.current_stamina -= self.decrease_speed / FPS
        if self.current_stamina < 0:
            self.current_stamina = 0
            self.current_increase_delay = self.zero_increase_delay

    def update(self):
        self.current_increase_delay -= 1 / FPS
        if self.current_increase_delay < 0:
            self.current_increase_delay = 0
            self.current_stamina += self.increase_speed / FPS
            if self.current_stamina > self.max_stamina:
                self.current_stamina = self.max_stamina
